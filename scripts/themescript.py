import ujson
def themegrabber():
    theme = "resources/moonlight/"
    try:
        with open('saves/settings.json', 'r') as f:
            themesettings = ujson.load(f)
    except:
        themesettings = {"Moonlight": True}
    if themesettings["Moonlight"] == True:
        theme = "resources/moonlight/"
    elif themesettings["ClassicClangen"] == True:
        theme = "resources/clangenclassic/"
    return theme
