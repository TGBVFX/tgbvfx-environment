# tgbvfx-environment

To get started with the pipeline, execute ```\\10.11.0.184\171000_TGB_Library\pipeline\startup.bat```. This will install the pipeline on your machine. The initial installation may take a little while.

Once the installation is finished, you should be presented with the Ftrack-connect application.

![capture](https://user-images.githubusercontent.com/1860085/28813336-3290973e-7699-11e7-896f-4037f0e04cea.PNG)

Please log into Ftrack at https://tgb.ftrackapp.com. Once logged in input "https://tgb.ftrackapp.com" into the ftrack-connect application and sign in. Now you are ready to launch your applications.

## NukeStudio

To publish from NukeStudio you'll first have to create the project and a task in Ftrack. Its recommended to having an "Editing" task directly under the project, so you project overview should look something like this:

![capture](https://user-images.githubusercontent.com/1860085/28670596-ba4607e0-72d9-11e7-9e02-545ac894daa6.PNG)

Now launch NukeStudio from the "editing" task.

Once you have your edit in NukeStudio ready, its time to export.

### Ftrack

If you want to export Ftrack shots you just need to select the shots to export > right-click > "Publish". A list of the Ftrack shots to export will appear under the "trackItem.ftrack.shot" family section.

If you want to export Ftrack tasks, you'll need to tag the track items. In the "Tags" window under the "pyblish-grill" > "ftrack.task" category, you'll find all the task types available. A list of the Ftrack tasks to export will appear under the "trackItem.ftrack.task" family section.

### Nuke Scripts and Transcodes

If you want to export Nuke scripts or transcodes, its the same process as normal in NukeStudio:

- Select the shots you want to export.
- Right-click > "Export...".
- Choose your exports.
 - It does not matter where the project root is set to, or how your folder structure is setup so you can just put your Nuke scripts and transcodes directory in the preset.

 ![capture](https://user-images.githubusercontent.com/1860085/28813768-033234f0-769b-11e7-9ace-0550f4a3677b.PNG)

- Choose "Pyblish" in the drop-down menu for "Render with:".
- You will be presented with the Pyblish interface where you'll find a list of the exports under the "trackItem.task" family section.

Once you have exported a Nuke script, you won't be able to overwrite it again by default. If you want to overwrite the Nuke scripts, you can enable the plugin ```TGBVFX Overwrite Nuke Scripts```.
**NOTE: Overwriting can cause loss of work, so be proceed with caution**
