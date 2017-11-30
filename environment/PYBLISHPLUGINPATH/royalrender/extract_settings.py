import pyblish.api as api


class TGBVFXEnvironmentRoyalRenderExtractSettingsNuke(api.InstancePlugin):
    """Add studio submission settings.

    Offset to fetch Nuke job.
    """

    order = api.ExtractorOrder + 0.1
    label = "Royal Render TGBVFX"
    families = ["royalrender"]
    hosts = ["nuke", "nukeassist"]
    targets = ["process.royalrender"]

    def process(self, instance):
        import os

        for job in instance.data["royalrenderJobs"]:
            if job["Software"] != "Nuke":
                continue

            # SubmitterParameter
            submit_params = job.get("SubmitterParameter", [])
            submit_params.append("SeqDivMINComp=1~5")
            submit_params.append("SeqDivMAXComp=1~40")
            submit_params.append("DefaultClientGroup=1~NODES_2D")
            submit_params.append(
                "CompanyProjectName=0~{0}".format(
                    os.environ["PROJECT_PATH"].split(os.sep)[-1]
                )
            )
            job["SubmitterParameter"] = submit_params
