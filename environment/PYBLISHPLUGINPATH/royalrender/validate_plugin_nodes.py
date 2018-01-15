import nuke

import pyblish.api


class TGBVFXSelectPluginNodes(pyblish.api.Action):

    label = "Select Plugin Nodes"
    icon = "hand-o-up"
    on = "failed"

    def process(self, context, plugin):

        # Get the errored instances
        failed = []
        for result in context.data["results"]:
            if (result["error"] is not None and result["instance"] is not None
               and result["instance"] not in failed):
                failed.append(result["instance"])

        # Apply pyblish.logic to get the instances for the plug-in
        instances = pyblish.api.instances_by_plugin(failed, plugin)

        nodes_to_select = []
        for instance in instances:
            cls_instance = plugin()
            nodes_to_select.extend(cls_instance.get_plugin_nodes())

        # Deselect all nodes.
        for node in nuke.allNodes():
            node["selected"].setValue(False)

        # Selecting nodes
        for node in nodes_to_select:
            node["selected"].setValue(True)

        # Zoom to node
        xC = node.xpos() + node.screenWidth()/2
        yC = node.ypos() + node.screenHeight()/2
        nuke.zoom(3, [xC, yC])


class TGBVFXValidateMochaNodes(pyblish.api.InstancePlugin):
    """Validate that there are no Mocha nodes in the script."""

    label = "Mocha Nodes"
    order = pyblish.api.ValidatorOrder
    families = ["royalrender"]
    hosts = ["nuke", "nukeassist"]
    targets = ["process.royalrender"]
    actions = [TGBVFXSelectPluginNodes]
    optional = True

    def get_plugin_nodes(self):
        plugin_nodes = []
        class_prefixes = [
            "OFXcom.borisfx.ofx.mochapro",
            "OFXcom.borisfx.ofx.mochavr",
            "OFXcom.borisfx.ofx.mochavr_v1"
        ]
        for node in nuke.allNodes():
            if node.Class() in class_prefixes:
                plugin_nodes.append(node)

        return plugin_nodes

    def process(self, instance):
        plugin_nodes = self.get_plugin_nodes()

        msg = (
            "Mocha nodes found in the script. RoyalRender does not support "
            "these nodes: {0}".format(plugin_nodes)
        )
        assert not plugin_nodes, msg
