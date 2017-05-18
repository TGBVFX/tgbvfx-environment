import pyblish.api
import pymel.core as pc


class TGBMayaCollectSwitchRenderlayer(pyblish.api.ContextPlugin):

    order = pyblish.api.CollectorOrder
    label = "Switch renderlayer"
    hosts = ["maya"]

    def process(self, context):

        self.log.info("Switching to master renderlayer.")

        layer = pc.PyNode("defaultRenderLayer")
        layer.setCurrent()
