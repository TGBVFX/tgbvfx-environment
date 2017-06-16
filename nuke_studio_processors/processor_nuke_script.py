import os
import tempfile

import hiero.core

import ftrack_api
import ftrack_connect_nuke_studio.processor
import pyblish.util
import pyblish.api
import pyblish_ftrack


class NukeScriptPlugin(ftrack_connect_nuke_studio.processor.ProcessorPlugin):
    """Publish the Nuke Studio project"""

    def __init__(self, session, *args, **kwargs):
        """Initialise processor."""
        super(NukeScriptPlugin, self).__init__(
            *args, **kwargs
        )

        self.session = session

        self.name = "processor.nukescript"
        self.defaults = {
            'OUT': {
                'file_type': 'nk'
            }
        }

    def discover(self, event):
        """Return discover data for *event*."""
        data = {
            "defaults": self.defaults,
            "name": "NukeScript",
            "processor_name": self.name,
            "asset_name": "scene"
        }

        data["process"] = self.get_process_state(event, data)

        return data

    def launch(self, event):
        """Launch processor from *event*."""
        item = event['data']['input']['application_object']
        file_path = item.source().mediaSource().fileinfos()[0].filename()
        fps = item.sequence().framerate().toFloat()

        # Get handles.
        handles = 0

        # Get reverse, retime, first and last frame
        reverse = False
        if item.playbackSpeed() < 0:
            reverse = True

        retime = False
        if item.playbackSpeed() != 1.0:
            retime = True

        first_frame = int(item.sourceIn() + 1) - handles
        first_frame_offset = 1
        last_frame = int(item.sourceOut() + 1) + handles
        last_frame_offset = last_frame - first_frame + 1
        if reverse:
            first_frame = int(item.sourceOut() + 1)
            first_frame_offset = 1
            last_frame = int(item.sourceIn() + 1)
            last_frame_offset = last_frame - first_frame + 1

        # Get resolution
        width = item.parent().parent().format().width()
        height = item.parent().parent().format().height()

        # Creating shot nuke script
        nukeWriter = hiero.core.nuke.ScriptWriter()

        # Root node
        root_node = hiero.core.nuke.RootNode(
            first_frame_offset,
            last_frame_offset,
            fps=fps
        )
        if retime:
            last_frame = abs(int(round(
                last_frame_offset / item.playbackSpeed()
            )))
            root_node = hiero.core.nuke.RootNode(
                first_frame_offset,
                last_frame,
                fps=fps
            )
        fmt = item.parent().parent().format()
        root_node.setKnob("format", "{0} {1}".format(
            fmt.width(),
            fmt.height()
        ))
        nukeWriter.addNode(root_node)

        # Primary read node
        read_node = hiero.core.nuke.ReadNode(
            file_path,
            width=width,
            height=height,
            firstFrame=first_frame,
            lastFrame=last_frame + 1
        )
        read_node.setKnob("frame_mode", 2)
        read_node.setKnob("frame", str(first_frame - 1))
        nukeWriter.addNode(read_node)

        if reverse or retime:

            last_frame = last_frame_offset
            if retime:
                last_frame = abs(int(round(
                    last_frame_offset / item.playbackSpeed()
                )))
            retime_node = hiero.core.nuke.RetimeNode(
                first_frame_offset,
                last_frame_offset,
                first_frame_offset,
                last_frame,
                reverse=reverse
            )
            retime_node.setKnob("shutter", 0)
            retime_node.setInputNode(0, read_node)
            nukeWriter.addNode(retime_node)

        # Secondary read nodes
        seq = item.parent().parent()
        time_in = item.timelineIn()
        time_out = item.timelineOut()

        items = []
        for count in range(time_in, time_out):
            items.extend(seq.trackItemsAt(count))

        items = list(set(items))
        items.remove(item)

        last_frame = abs(int(round(last_frame_offset /
                                   item.playbackSpeed())))

        for i in items:
            src = i.source().mediaSource().fileinfos()[0].filename()
            in_frame = i.mapTimelineToSource(time_in) + 1 - handles
            out_frame = i.mapTimelineToSource(time_out) + 1 + handles
            read_node = hiero.core.nuke.ReadNode(
                src,
                width=width,
                height=height,
                firstFrame=in_frame,
                lastFrame=out_frame
            )
            nukeWriter.addNode(read_node)

            retime_node = hiero.core.nuke.RetimeNode(
                in_frame,
                out_frame,
                first_frame_offset,
                last_frame
            )
            retime_node.setKnob("shutter", 0)
            retime_node.setInputNode(0, read_node)
            nukeWriter.addNode(retime_node)

        # Get file path
        file_path = tempfile.NamedTemporaryFile(suffix='.nk').name

        # Create directories
        if not os.path.exists(os.path.dirname(file_path)):
            os.makedirs(os.path.dirname(file_path))

        # Create nuke script
        nukeWriter.writeToDisk(file_path)
        print("Writing Nuke script to: \"%s\"" % file_path)

        # Publish to Ftrack with pyblish plugins
        data = event['data'].get('input', {})

        parent = self.session.get(
            "AssetVersion", data["asset_version_id"]
        )["asset"]["parent"]

        context = pyblish.api.Context()
        context.create_instance(
            name="nukescript",
            families=["ftrack"],
            ftrackComponentsList=[
                {
                    "assettype_data": {
                        "short": "scene"
                    },
                    "asset_data": {
                        "name": parent["name"],
                        "parent": parent
                    },
                    "component_data": {
                        "name": "nuke"
                    },
                    "component_path": file_path,
                }
            ]
        )

        paths = [
            os.path.join(os.path.dirname(pyblish_ftrack.__file__), "plugins")
        ]
        plugins = pyblish.api.discover(paths=paths)
        pyblish.util.publish(context=context, plugins=plugins)

        header = "{:<10}{:<40} -> {}".format("Success", "Plug-in", "Instance")
        result = "{success:<10}{plugin.__name__:<40} -> {instance}"
        error = "{:<10}+-- EXCEPTION: {:<70}"
        record = "{:<10}+-- {level}: {message:<70}"

        results = list()
        for r in context.data["results"]:
            # Format summary
            results.append(result.format(**r))

            # Format log records
            for lr in r["records"]:
                lines = str(lr.msg).split("\n")
                msg = lines[0]
                for line in lines[1:]:
                    msg += "\t\t\t\t\t" + line
                data = record.format("", level=lr.levelname, message=msg)
                results.append(data)

            # Format exception (if any)
            if r["error"]:
                lines = str(r["error"]).split("\n")
                msg = lines[0]
                for line in lines[1:]:
                    msg += "\t\t\t\t\t" + line
                results.append(error.format("", msg))

        report = "{header}\n{line}\n{results}".format(
            header=header, results="\n".join(results), line="-" * 70
        )
        print report

        # Clean up temp nuke script
        os.remove(file_path)

    def register(self):
        """Register processor"""
        self.session.event_hub.subscribe(
            "topic=ftrack.processor.discover and "
            "data.object_type=shot",
            self.discover
        )
        self.session.event_hub.subscribe(
            "topic=ftrack.processor.launch and data.name={0}".format(
                self.name
            ),
            self.launch
        )


def register(session, **kw):
    """Register plugin. Called when used as an plugin."""
    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an old or incompatible API and
    # return without doing anything.
    if not isinstance(session, ftrack_api.session.Session):
        return

    plugin = NukeScriptPlugin(
        session
    )

    plugin.register()
