import nuke

import pyblish.api


class TGBVFXSelectMochaNodes(pyblish.api.Action):

    label = "Select Mocha Nodes"
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
            cls_instance = TGBVFXValidateMochaNodes()
            nodes_to_select.extend(
                cls_instance.get_upstream_mocha_nodes(instance[0])
            )

        # Deselect all nodes.
        for node in nuke.allNodes():
            node["selected"].setValue(False)

        # Selecting nodes
        for node in nodes_to_select:
            node["selected"].setValue(True)


class TGBVFXValidateMochaNodes(pyblish.api.InstancePlugin):
    """Validate that there are no Mocha nodes upstream."""

    order = pyblish.api.ValidatorOrder
    label = "Mocha Nodes"
    families = ["royalrender"]
    hosts = ["nuke"]
    targets = ["process.royalrender"]
    actions = [TGBVFXSelectMochaNodes]
    optional = True

    def process(self, instance):
        mocha_nodes = self.get_upstream_mocha_nodes(instance[0])

        msg = (
            "Mocha nodes found in upstream. RoyalRender does not support these"
            " nodes."
        )
        assert not mocha_nodes, msg

    def get_upstream_mocha_nodes(self, node):
        mocha_nodes = []
        mocha_classes = [
            "OFXcom.borisfx.ofx.mochapro_v1", "OFXcom.borisfx.ofx.mochavr_v1"
        ]
        for node in self.recurse_dependencies(node):
            if node.Class() in mocha_classes:
                mocha_nodes.append(node)

        return mocha_nodes

    def recurse_dependencies(self, node):
        dependencies = []
        dependency_nodes = node.dependencies()
        dependencies.extend(dependency_nodes)
        for dependant in dependency_nodes:
            dependencies.extend(self.recurse_dependencies(dependant))

        return dependencies
