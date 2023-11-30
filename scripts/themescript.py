import ujson
from .housekeeping.datadir import get_save_dir

savefolder = get_save_dir()
def themegrabber():
    theme = "resources/moonlight/"
    try:
        with open('saves/settings.json', 'r') as f:
            themesettings = ujson.load(f)
    except:
        try:
            with open(savefolder + '/saves/settings.json', 'r') as f:
                themesettings = ujson.load(f)
        except:
            themesettings = {"Moonlight": True}
    if themesettings["Moonlight"] == True:
        theme = "resources/moonlight/"
    elif themesettings["Seaside"] == True:
        theme = "resources/seaside/"
    elif themesettings["ClassicClangen"] == True:
        theme = "resources/clangenclassic/"
    return theme
