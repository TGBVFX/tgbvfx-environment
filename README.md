# tgbvfx-environment



To get started with the pipeline, execute ```\\10.11.0.184\171000_TGB_Library\pipeline\startup.bat```. This will install the pipeline on your machine. The initial installation may take a little while.

Once the installation is finished, you should be presented with the Ftrack-connect application.

![capture](https://user-images.githubusercontent.com/1860085/28813336-3290973e-7699-11e7-896f-4037f0e04cea.PNG)

Please log into Ftrack at https://tgb.ftrackapp.com. Once logged in input "https://tgb.ftrackapp.com" into the ftrack-connect application and sign in. Now you are ready to launch your applications.

## Application launch

To launch any application you'll need to get a list of the available actions. You can reach the action in multiple ways:

- Right-click menu on an entity > ```Actions```

![capture](https://user-images.githubusercontent.com/1860085/28925020-ed958690-7863-11e7-8884-9cceb3acabf6.PNG)
- From the **Actions** button in the side of the task.

![capture](https://user-images.githubusercontent.com/1860085/28925075-123bd224-7864-11e7-9573-82e1b1fb6c29.PNG)

- From the **Actions** button on the task in ```My Tasks```

![capture](https://user-images.githubusercontent.com/1860085/28925215-814e4c78-7864-11e7-83ab-5fc0f3651b98.PNG)

You can now choose an application to launch from the available actions.

![capture](https://user-images.githubusercontent.com/1860085/28924918-95c234d6-7863-11e7-9048-4598668f38c0.PNG)

## NukeStudio

To publish from NukeStudio you'll first have to create the project in Ftrack.

Go to ```Projects > Create new project```, enter the name and specify the ```Workflow``` as "VFX".

Once created go to the project's info by selecting the project in the hierarchy and go to ```Info```. Here specify the ```Disk``` as **Root**, and the ```Project folder```. The **Root** disk refers to the storage IP ```\\10.11.0.184``` and the ```Project folder``` refers to the folder at the **Root** disk, so with a ```Project folder``` of **171001_ftrack** will give you a project path **\\\10.11.0.184\171001_ftrack**.

Its recommended to having an "Editing" task directly under the project, so you project overview should look something like this:

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
 - It does not matter where the project root is set to, or how your folder structure is setup so you can just put your Nuke scripts and transcodes directly in the preset.

 ![capture](https://user-images.githubusercontent.com/1860085/28813768-033234f0-769b-11e7-9ace-0550f4a3677b.PNG)

- Choose "Pyblish" in the drop-down menu for "Render with:".
- You will be presented with the Pyblish interface where you'll find a list of the exports under the "trackItem.task" family section.

Once you have exported a Nuke script, you won't be able to overwrite it again by default. If you want to overwrite the Nuke scripts, you can enable the plugin ```TGBVFX Overwrite Nuke Scripts```.
**NOTE: Overwriting can cause loss of work, so be proceed with caution**
