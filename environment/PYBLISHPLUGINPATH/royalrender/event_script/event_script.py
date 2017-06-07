import os
import sys

import rr


job = rr.getJob()

# Setup environment
value = job.custom_Str("FTRACK_SERVER")
# Workaround of RR converting / to \
os.environ["FTRACK_SERVER"] = value.replace("\\", "/")
os.environ["FTRACK_APIKEY"] = job.custom_Str("FTRACK_APIKEY")
os.environ["LOGNAME"] = job.custom_Str("LOGNAME")

# Add ftrack module
path = job.custom_Str("PYTHONPATH")
print "Adding path: " + path
sys.path.append(path)

import ftrack

# Getting status
# integer mappings from
# http://www.royalrender.de/help8/index.html?modulerrJob.html#enum_rrStatus
event_mapping = {
    "None": 0,
    "FirstCheck": 20,
    "WaitForJobs": 40,
    "ScriptPreRender": 60,
    "PreviewRender": 80,
    "ScriptAfterPreview": 90,
    "WaitForApprovalMain": 100,
    "WaitForJobsAfterPreview": 110,
    "MainRender": 120,
    "ScriptPostRender": 140,
    "WaitForApprovalDone": 160,
    "ScriptFinished": 180,
    "Finished": 200
}

event_type = None
for key, value in event_mapping.iteritems():
    if value == job.status:
        event_type = key

status_mapping = {
    "None": "Processing Queued",
    "FirstCheck": "Processing Queued",
    "WaitForJobs": "Processing Queued",
    "ScriptPreRender": "Processing Queued",
    "PreviewRender": "Processing Queued",
    "ScriptAfterPreview": "Processing Queued",
    "WaitForApprovalMain": "Processing Queued",
    "WaitForJobsAfterPreview": "Processing Queued",
    "MainRender": "Processing",
    "ScriptPostRender": "Processing",
    "WaitForApprovalDone": "Processing",
    "ScriptFinished": "Processing",
    "Finished": "Processing Done"
}

status = None
for ft_status in ftrack.getTaskStatuses():
    if ft_status.getName() == status_mapping[event_type]:
        status = ft_status
        break

# Setting status
task = ftrack.Task(job.custom_Str("FTRACK_TASKID"))
task.setStatus(ft_status)
msg = "Setting \"{0}\" to \"{1}\"".format(
    task.getName(), status.getName()
)
print msg
