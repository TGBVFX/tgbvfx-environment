import nuke

import pyblish.api


class TGBVFXSelectPluginNodes(pyblish.api.Action):

    label = "Repair"
    icon = "wrench"
    on = "failed"

    def process(self, context, plugin):

        for node in nuke.allNodes("Viewer"):
            node["masking_ratio"].setValue(0)


class TGBVFXValidateMaskingRaio(pyblish.api.ContextPlugin):
    """Validates against custom masking ratio options."""

    order = pyblish.api.ValidatorOrder
    families = ["royalrender"]
    hosts = ["nuke", "nukeassist"]
    targets = ["process.royalrender"]
    actions = [TGBVFXSelectPluginNodes]
    optional = True
    label = "Masking Ratio"

    def process(self, context):

        valid_masking_ratio = True
        for node in nuke.allNodes("Viewer"):
            if node["masking_ratio"].getValue() > 6.0:
                valid_masking_ratio = False

        msg = ("RoyalRender does not support custom masking ratios.")
        assert valid_masking_ratio, msg
