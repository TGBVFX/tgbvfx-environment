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
            cls_instance = ValidatePluginNodes()
            nodes_to_select.extend(
                cls_instance.get_upstream_plugin_nodes(
                    instance[0], instance.data["class_prefixes"]
                )
            )

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


class ValidatePluginNodes(pyblish.api.InstancePlugin):
    """Superclass for validating plugins nodes."""

    order = pyblish.api.ValidatorOrder
    families = ["royalrender"]
    hosts = ["nuke", "nukeassist"]
    targets = ["process.royalrender"]
    actions = [TGBVFXSelectPluginNodes]
    optional = True

    def get_upstream_plugin_nodes(self, node, class_prefixes):
        nodes = []

        dependencies = []

        # Dirty hack to circumvent max recursion issue in Nuke.
        try:
            dependencies = self.recurse_dependencies(node)
        except RuntimeError as e:
            if e.message == "maximum recursion depth exceeded":
                self.log.warning(e.message)
            else:
                raise

        for node in dependencies:
            for prefix in class_prefixes:
                if node.Class().startswith(prefix):
                    nodes.append(node)

        return nodes

    def recurse_dependencies(self, node):
        dependencies = []
        dependency_nodes = node.dependencies()
        dependencies.extend(dependency_nodes)
        for dependant in dependency_nodes:
            dependencies.extend(self.recurse_dependencies(dependant))

        return dependencies


class TGBVFXValidateMochaNodes(ValidatePluginNodes):
    """Validate that there are no Mocha nodes upstream."""

    label = "Mocha Nodes"

    def process(self, instance):
        class_prefixes = [
            "OFXcom.borisfx.ofx.mochapro", "OFXcom.borisfx.ofx.mochavr"
        ]
        instance.data["class_prefixes"] = class_prefixes
        nodes = self.get_upstream_plugin_nodes(
            instance[0], class_prefixes
        )

        msg = (
            "Mocha nodes found in upstream. RoyalRender does not support these"
            " nodes."
        )
        assert not nodes, msg


class TGBVFXValidateNeatVideoNodes(ValidatePluginNodes):
    """Validate that there are no Neat Video nodes upstream."""

    label = "Neat Video Nodes"

    def process(self, instance):
        class_prefixes = ["OFXcom.absoft.neatvideo"]
        nodes = self.get_upstream_plugin_nodes(
            instance[0], class_prefixes
        )
        instance.data["class_prefixes"] = class_prefixes
        active_nodes = False
        for node in nodes:
            if not node["disable"].getValue():
                active_nodes = True

        msg = (
            "Neat Video nodes found in upstream. RoyalRender does not support "
            "these nodes."
        )
        assert not active_nodes, msg
