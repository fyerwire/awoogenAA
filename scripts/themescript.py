import ujson
def themegrabber():
    theme = "resources/moonlight/"
    with open('saves/settings.json', 'r') as f:
        themesettings = ujson.load(f)
    if themesettings["Moonlight"] == True:
        theme = "resources/moonlight/"
    elif themesettings["ClassicClangen"] == True:
        theme = "resources/clangenclassic/"
    print(theme)
    return theme
