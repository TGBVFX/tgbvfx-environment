import pymel.core as pc
import maya.mel as mm


def tgbvfxSetRenderer():

    # Load plugin if available
    try:
        pc.loadPlugin("vrayformaya.mll", quiet=True)
    except:
        return

    print "tgbvfx-environment: Setting Vray as renderer."
    render_globals = pc.PyNode("defaultRenderGlobals")
    render_globals.currentRenderer.set("vray")
    mm.eval("vrayCreateVRaySettingsNode")


pc.evalDeferred("tgbvfxSetRenderer()")
