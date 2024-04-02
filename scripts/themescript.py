import ujson

def themegrabber(themesettings):
    theme = "resources/moonlight/"
    if themesettings["Moonlight"] == True:
        theme = "resources/moonlight/"
    elif themesettings["Seaside"] == True:
        theme = "resources/seaside/"
    elif themesettings["ClassicClangen"] == True:
        theme = "resources/clangenclassic/"
    return theme
