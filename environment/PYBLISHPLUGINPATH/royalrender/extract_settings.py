import pyblish.api as api


class TGBVFXEnvironmentRoyalRenderExtractSettingsNuke(api.InstancePlugin):
    """ Add studio submission settings. """

    order = api.ExtractorOrder
    label = "Settings"
    families = ["royalrender"]
    hosts = ["nuke"]
    targets = ["process.royalrender"]

    def process(self, instance):

        data = instance.data.get("royalrenderData", {})

        # SubmitterParameter
        submit_params = data.get("SubmitterParameter", [])
        submit_params.append("SeqDivMINComp=1~5")
        submit_params.append("SeqDivMAXComp=1~40")
        submit_params.append("DefaultClientGroup=1~NODES_OLD")
        data["SubmitterParameter"] = submit_params

        # Setting data
        instance.data["royalrenderData"] = data
