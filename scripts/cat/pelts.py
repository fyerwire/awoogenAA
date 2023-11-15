from random import choice
from scripts.cat.sprites import sprites
import random
from re import sub
from scripts.game_structure.game_essentials import game


    

class Pelt():
    
    sprites_names = {
        "SingleColour": 'single',
        'TwoColour': 'single',
        'Tabby': 'tabby',
        'Marbled': 'marbled',
        'Rosette': 'rosette',
        'Smoke': 'smoke',
        'Ticked': 'ticked',
        'Speckled': 'speckled',
        'Bengal': 'bengal',
        'Mackerel': 'mackerel',
        'Classic': 'classic',
        'Sokoke': 'sokoke',
        'Agouti': 'agouti',
        'Singlestripe': 'singlestripe',
        'Arctic': 'arctic',
        'Colorpoint': 'colorpoint',
        'Graywolf': 'graywolf',
        'Mexican': 'mexican',
        'Ophelia': 'ophelia',
        'Runic': 'runic',
        'Semisolid': 'semisolid',
        'Smokey': 'smokey',
        'Stormy': 'stormy',
        'Timber': 'timber',
        'Vibrant': 'vibrant',
        'Winter': 'winter',
        'Brindle': 'brindle',
        'Husky': 'husky',
        'Points': 'points',
        'Sable': 'sable',
        'Shepherd': 'shepherd',
        'Solid': 'solid',
        'Tortie': None,
        'Calico': None,
    }
    
    # ATTRIBUTES, including non-pelt related
    pelt_colours = [
        'SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM', 'PEARL', 'MIST', 'ASH', 'STEEL',
		'BLACK', 'CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER', 'BRASS', 'SILVER',
		'ONYX', 'SUNSTONE', 'MOONSTONE', 'COCOA', 'SPRUCE', 'ISABELLA',
                        'SUNNY', 'LUNA'
    ]
    pelt_c_no_white = [
        'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE'
    ]
    pelt_c_no_bw = [
        'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE'
    ]

    tortiepatterns = ['CAPE', 'DIPPED', 'HEARTBREAKER', 'INKSPILL', 'MINIMAL', 'PHANTOM',
		'PUDDLES', 'REDTAIL', 'SHADOWSTEP', 'SPLIT', 'SPLOTCH', 'WATERFALL']
    tortiebases = ["Graywolf", "Ophelia", "Runic", "Timber", "Sable", "Shepherd", 
		"Arctic", "Winter", "Husky", "Mexican", "Stormy", "Vibrant", "Colorpoint", "Smokey", 
		"Points", "Semisolid", "Solid"]

    pelt_length = ["short", "medium", "long"]
    eye_colours = ['DAYLIGHT', 'ICE', 'NAVY', 'RAIN', 'SAPPHIRE', 'SEAFOAM', 'SKY', 'STORM', 'TEAL', 
				'ALMOND', 'BEAR', 'CASHEW', 'HAZEL', 'LATTE', 'SPARROW', 'BLACK', 'GULL', 
				'SILVER', 'SMOKE', 'WHITE', 'EMERALD', 'FERN', 'FOREST', 'LEAF', 'LIME', 
				'MINT', 'HARVEST', 'PEACH', 'PUMPKIN', 'TANGELO', 'TWILIGHT', 'AMETHYST',
                                                'DAWN', 'DUSK', 'LILAC', 'MIDNIGHT', 'VIOLET', 'BUBBLEGUM', 'PINK', 'ROUGE',
                                                'RUBY', 'SCARLET', 'AMBER', 'LEMON', 'PALE', 'SUNBEAM', 'SUNLIGHT', 'WHEAT']
    yellow_eyes = ['AMBER', 'LEMON', 'PALE', 'SUNBEAM', 'SUNLIGHT', 'WHEAT']
    orange_eyes = ['HARVEST', 'PEACH', 'PUMPKIN', 'TANGELO', 'TWILIGHT']
    green_eyes = ['EMERALD', 'FERN', 'FOREST', 'LEAF', 'LIME', 'MINT']
    gray_eyes = ['BLACK', 'GULL', 'SILVER', 'SMOKE', 'WHITE']
    brown_eyes = ['ALMOND', 'BEAR', 'CASHEW', 'HAZEL', 'LATTE', 'SPARROW']
    blue_eyes = ['DAYLIGHT', 'ICE', 'NAVY', 'RAIN', 'SAPPHIRE', 'SEAFOAM', 'SKY', 'STORM', 'TEAL']
    purple_eyes = ['AMETHYST', 'DAWN', 'DUSK', 'LILAC', 'MIDNIGHT', 'VIOLET']
    red_eyes = ['BUBBLEGUM', 'PINK', 'ROUGE', 'RUBY', 'SCARLET']
    # scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
    # bite scars by @wood pank on discord
    scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
            "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
            "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH", "GIN"]
    scars2 = ["BRIGHTHEART", "BURNBELLY", "BURNTAIL", "LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
    scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT",
            "FROSTSOCK", "BLIND"]
    scars4 = []

    # make sure to add plural and singular forms of new accs to acc_display.json so that they will display nicely
    plant_accessories = ["BLUEBELLS", "BLUE BERRIES", "CATMINT", "DRY HERBS", "FORGET ME NOTS", "HERBS", 
		"HOLLY", "JUNIPER", "LAUREL", "LAVENDER", "MAPLE LEAF", "MAPLE SEED", "NETTLE", "OAK LEAVES", 
		"PETALS", "POPPY", "RYE STALK", "BLACK EYED SUSANS", "GOLD HERBS", "IVY", "MARIGOLD", 
		"PURPLE PETALS", "ROSE", "SAKURA", "SUNFLOWER", "WHITE ROSE"]
    wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS", 
		"CROW FEATHERS", "DOVE FEATHERS"]
    collars = [
        "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
        "BLACK", "SPIKES", "WHITE", "PINK", "PURPLE", "MULTI", "INDIGO", "BELLBLACK", "BELLBLUE", 
		"BELLCRIMSON", "BELLCYAN", "BELLGREEN", "BELLINDIGO", "BELLLIME", "BELLMULTI", "BELLPINK", 
		"BELLPURPLE", "BELLRAINBOW", "BELLRED", "BELLSPIKES", "BELLWHITE", "BELLYELLOW", 
		"BOWBLACK", "BOWBLUE", "BOWCRIMSON", "BOWCYAN", "BOWGREEN", "BOWINDIGO", "BOWLIME", 
		"BOWMULTI", "BOWPINK", "BOWPURPLE", "BOWRAINBOW", "BOWRED", "BOWSPIKES", "BOWWHITE", "BOWYELLOW", 
		"NYLONBLACK", "NYLONBLUE", "NYLONCRIMSON", "NYLONCYAN", "NYLONGREEN", "NYLONINDIGO", "NYLONLIME", 
		"NYLONMULTI", "NYLONPINK", "NYLONPURPLE", "NYLONRAINBOW", "NYLONRED", "NYLONSPIKES", "NYLONWHITE", 
		"NYLONYELLOW",
		"PASTELNYLONBLACK", "PASTELNYLONBLUE", "PASTELNYLONCRIMSON", "PASTELNYLONCYAN", "PASTELNYLONGREEN", 
		"PASTELNYLONINDIGO", "PASTELNYLONLIME", "PASTELNYLONMULTI", "PASTELNYLONPINK", "PASTELNYLONPURPLE", 
		"PASTELNYLONRAINBOW", "PASTELNYLONRED", "PASTELNYLONSPIKES", "PASTELNYLONWHITE", "PASTELNYLONYELLOW"
    ]
    radiocollars = [
		"RADIOBLACK", "RADIOBLUE", "RADIOCRIMSON", "RADIOCYAN", "RADIOGREEN", 
		"RADIOINDIGO", "RADIOLIME", "RADIOMULTI", "RADIOPINK", "RADIOPURPLE", 
		"RADIORAINBOW", "RADIORED", "RADIOSPIKES", "RADIOWHITE", "RADIOYELLOW"
	]
    harnesses = [
		"HARNESSBLACK", "HARNESSBLUE", "HARNESSCRIMSON", "HARNESSCYAN", "HARNESSGREEN", 
		"HARNESSINDIGO", "HARNESSLIME", "HARNESSMULTI", "HARNESSPINK", "HARNESSPURPLE", 
		"HARNESSRAINBOW", "HARNESSRED", "HARNESSSPIKES", "HARNESSWHITE", "HARNESSYELLOW"
	]
    bandanas = [
		"BANDANABLACK", "BANDANABLUE", "BANDANACRIMSON", "BANDANACYAN", "BANDANAGREEN", 
		"BANDANAINDIGO", "BANDANALIME", "BANDANAMULTI", "BANDANAPINK", "BANDANAPURPLE", 
		"BANDANARAINBOW", "BANDANARED", "BANDANASPIKES", "BANDANAWHITE", "BANDANAYELLOW", 
		"PLAIDBANDANABLACK", "PLAIDBANDANABLUE", "PLAIDBANDANACRIMSON", "PLAIDBANDANACYAN", "PLAIDBANDANAGREEN", 
		"PLAIDBANDANAINDIGO", "PLAIDBANDANALIME", "PLAIDBANDANAMULTI", "PLAIDBANDANAPINK", "PLAIDBANDANAPURPLE", 
		"PLAIDBANDANARAINBOW", "PLAIDBANDANARED", "PLAIDBANDANASPIKES", "PLAIDBANDANAWHITE", "PLAIDBANDANAYELLOW"
	]
    every_acc_list = [plant_accessories, wild_accessories, collars, radiocollars, harnesses, bandanas]
    standardpelts = ["Graywolf", "Ophelia", "Runic", "Timber", "Sable", "Shepherd"]
    northpelts = ["Arctic", "Winter", "Husky"]
    southpelts = ["Mexican", "Stormy", "Vibrant"]
    darkpelts = ["Colorpoint", "Smokey", "Points"]
    specialpelts = ["Semisolid", "Solid", "Brindle"]
    torties = ["Tortie", "Calico"]
    pelt_categories = [standardpelts, northpelts, southpelts, darkpelts, specialpelts, torties]

    # SPRITE NAMES
    single_colours = [
        'WHITE', 'PALEGREY', 'SILVER', 'GREY', 'DARKGREY', 'GHOST', 'BLACK', 'CREAM', 'PALEGINGER',
        'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA', 'LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN',
        'CHOCOLATE'
    ]
    #ginger_colours = ['CREAM', 'PALEGINGER', 'GOLDEN', 'GINGER', 'DARKGINGER', 'SIENNA']
    #black_colours = ['GREY', 'DARKGREY', 'GHOST', 'BLACK']
    #white_colours = ['WHITE', 'PALEGREY', 'SILVER']
    #brown_colours = ['LIGHTBROWN', 'LILAC', 'BROWN', 'GOLDEN-BROWN', 'DARKBROWN', 'CHOCOLATE']
    #colour_categories = [ginger_colours, black_colours, white_colours, brown_colours]
    yellow_colors = ['HONEY', 'FLAXEN', 'CREAM', 'PEARL', 'GOLD', 'BRASS', 'SUNSTONE', 'SUNNY']
    gray_colors = ['MIST', 'ASH', 'STEEL', 'SILVER', 'MOONSTONE']
    black_colors = ['BLACK', 'ONYX', 'LUNA']
    red_colors = ['SPICE', 'GINGER', 'COPPER']
    dilute_colors = ['CHOCOLATE', 'COCOA', 'BLUE', 'SPRUCE', 'LILAC', 'ISABELLA']
    colour_categories = [yellow_colors, gray_colors, black_colors, red_colors, dilute_colors]
    eye_sprites = ['DAYLIGHT', 'ICE', 'NAVY', 'RAIN', 'SAPPHIRE', 'SEAFOAM', 'SKY', 'STORM', 'TEAL', 
				'ALMOND', 'BEAR', 'CASHEW', 'HAZEL', 'LATTE', 'SPARROW', 'BLACK', 'GULL', 
				'SILVER', 'SMOKE', 'WHITE', 'EMERALD', 'FERN', 'FOREST', 'LEAF', 'LIME', 
				'MINT', 'HARVEST', 'PEACH', 'PUMPKIN', 'TANGELO', 'TWILIGHT', 'AMETHYST',
                                                'DAWN', 'DUSK', 'LILAC', 'MIDNIGHT', 'VIOLET', 'BUBBLEGUM', 'PINK', 'ROUGE',
                                                'RUBY', 'SCARLET', 'AMBER', 'LEMON', 'PALE', 'SUNBEAM', 'SUNLIGHT', 'WHEAT']
    low_white = ['FLASH', 'HIGHLIGHTS', 'JACKAL', 'LOCKET', 'SNOWFLAKE', 'SOCKS', 'SPLIT', 
				'STRIPE', 'TOES', 'TRIM', 'WOLFTICKING', 'BACKLEG', 'BEE',
                                                'DAPPLES', 'POINTED', 'SPECKLES']
    mid_white = ['BLAZE', 'BLOTCH', 'HALF', 'HEART',  'IRISH', 'MOONRISE', 'MUNSTERLANDER', 
				'SPITZ', 'STAR', 'SUMMERFOX', 'TICKING', 'URAJIRO',
                                                 'DIAMOND', 'HOUND', 'KING']
    high_white = ['BLUETICK', 'EXTREMEPIEBALD', 'LIGHTDALMATIAN', 'PIEBALD', 'TAIL', 'WHITE',
                                                  'HEAVYDALMATIAN', 'HEELER']
					
    mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                    'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO','PEBBLESHINE', 'BOOTS', 'COW', 'COWTWO', 'LOVEBUG',
                    'SHOOTINGSTAR', 'EYESPOT', 'PEBBLE', 'TAILTWO', 'BUDDY', 'KROPKA']
    point_markings = ['COLOURPOINT', 'RAGDOLL', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']
    vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'KARPATI', 'POWDER', 'BLEACHED', 'SMOKEY']
    white_sprites = [low_white, mid_white, high_white]
    skin_sprites = ['BLACK', 'BLUE', 'BUTTERFLY', 'DUDLEY', 'DUDLEYBLUE', 'DUDLEYLIVER', 'GRAY', 'ISABELLA', 'LIVER', 'MOCHA', 'PINK', 'SNOWNOSE', 'SPECKLED']
    skin_list = []
    """Holds all appearence information for a cat. """
    def __init__(self,
                 name:str="Solid",
                 species:str="Wolf",
                 species_mix:list=["W", "W", "C", "C", "D", "D"],
                 length:str="short",
                 colour:str="WHITE",
                 white_patches:str=None,
                 eye_color:str="BLUE",
                 eye_colour2:str=None,
                 tortiebase:str=None,
                 tortiecolour:str=None,
                 pattern:str=None,
                 tortiepattern:str=None,
                 vitiligo:str=None,
                 points:str=None,
                 accessory:str=None,
                 paralyzed:bool=False,
                 opacity:int=100,
                 scars:list=None,
                 tint:str="none",
                 skin:str="BLACK",
                 white_patches_tint:str="none",
                 kitten_sprite:int=None,
                 adol_sprite:int=None,
                 adult_sprite:int=None,
                 senior_sprite:int=None,
                 para_adult_sprite:int=None,
                 reverse:bool=False,
                 ) -> None:
        self.name = name
        self.species = species
        self.species_mix = species_mix
        self.colour = colour
        self.white_patches = white_patches
        self.eye_colour = eye_color
        self.eye_colour2 = eye_colour2
        self.tortiebase = tortiebase
        self.pattern = pattern
        self.tortiepattern = tortiepattern
        self.tortiecolour = tortiecolour
        self.vitiligo = vitiligo
        self.length=length
        self.points = points
        self.accessory = accessory
        self.paralyzed = paralyzed
        self.opacity = opacity
        self.scars = scars if isinstance(scars, list) else []
        self.tint = tint
        self.white_patches_tint = white_patches_tint
        self.cat_sprites =  {
            "kitten": kitten_sprite if kitten_sprite is not None else 0,
            "adolescent": adol_sprite if adol_sprite is not None else 0,
            "young adult": adult_sprite if adult_sprite is not None else 0,
            "adult": adult_sprite if adult_sprite is not None else 0,
            "senior adult": adult_sprite if adult_sprite is not None else 0,
            "senior": senior_sprite if senior_sprite is not None else 0,
            "para_adult": para_adult_sprite if para_adult_sprite is not None else 0,
        }        
        self.cat_sprites['newborn'] = 20
        self.cat_sprites['para_young'] = 17
        self.cat_sprites["sick_adult"] = 18
        self.cat_sprites["sick_young"] = 19
        
        self.reverse = reverse
        self.skin = skin

    @staticmethod
    def generate_new_pelt(gender:str, parents:tuple=(), age:str="adult"):
        new_pelt = Pelt()
        
        pelt_white = new_pelt.init_pattern_color(parents, gender)
        new_pelt.init_white_patches(pelt_white, parents)
        new_pelt.init_sprite()
        new_pelt.init_scars(age)
        new_pelt.init_accessories(age)
        new_pelt.init_eyes(parents)
        new_pelt.init_pattern()
        new_pelt.init_tint()
        
        return new_pelt
    
    def check_and_convert(self, convert_dict):
        """Checks for old-type properties for the apperence-related properties
        that are stored in Pelt, and converts them. To be run when loading a cat in. """
        
        #First, convert from some old names that may be in white_patches. 
        if self.white_patches == 'POINTMARK':
            self.white_patches = "SEALPOINT"
        elif self.white_patches == 'PANTS2':
            self.white_patches = 'PANTSTWO'
        elif self.white_patches == 'ANY2':
            self.white_patches = 'ANYTWO'
        elif self.white_patches == "VITILIGO2":
            self.white_patches = "VITILIGOTWO"
            
        if self.vitiligo == "VITILIGO2":
            self.vitiligo = "VITILIGOTWO"
        
        # Move white_patches that should be in vit or points. 
        if self.white_patches in Pelt.vit:
            self.vitiligo = self.white_patches
            self.white_patches = None
        elif self.white_patches in Pelt.point_markings:
            self.points = self.white_patches
            self.white_patches = None

        
        if self.tortiepattern and "tortie" in self.tortiepattern:
            self.tortiepattern = sub("tortie", "", self.tortiepattern.lower())
            if self.tortiepattern == "solid":
                self.tortiepattern = "single"
                
        if self.white_patches in convert_dict["old_creamy_patches"]:
            self.white_patches = convert_dict["old_creamy_patches"][self.white_patches]
            self.white_patches_tint = "darkcream"
        elif self.white_patches in ['SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']:
            self.white_patches_tint = "none"
        
        # Eye Color Convert Stuff
        if self.eye_colour == "BLUE2":
            self.eye_colour = "COBALT"
        if self.eye_colour2 == "BLUE2":
            self.eye_colour2 = "COBALT"
            
        if self.eye_colour in ["BLUEYELLOW", "BLUEGREEN"]:
            if self.eye_colour == "BLUEYELLOW":
                self.eye_colour2 = "YELLOW"
            elif self.eye_colour == "BLUEGREEN":
                self.eye_colour2 = "GREEN"
            self.eye_colour = "BLUE"
        
        if self.cat_sprites['senior'] not in [12, 13, 14]:
            if self.cat_sprites['senior'] == 3:
                self.cat_sprites['senior'] = 12
            elif self.cat_sprites['senior'] == 4:
                self.cat_sprites['senior'] = 13
            elif self.cat_sprites['senior'] == 5:
                self.cat_sprites['senior'] = 14
        
        if self.pattern in convert_dict["old_tortie_patches"]:
            old_pattern = self.pattern
            self.pattern = convert_dict["old_tortie_patches"][old_pattern][1]
            
            # If the pattern is old, there is also a change the base color is stored in
            # tortiecolour, and that may be different from the pelt color (main for torties
            # generated before the "ginger-on-ginger" update. If it was generated after that update,
            # tortiecolour and pelt_colour will be the same. Therefore, lets also re-set the pelt color
            self.colour = self.tortiecolour
            self.tortiecolour = convert_dict["old_tortie_patches"][old_pattern][0]
            
        if self.pattern == "MINIMAL1":
            self.pattern = "MINIMALONE"
        elif self.pattern == "MINIMAL2":
            self.pattern = "MINIMALTWO"
        elif self.pattern == "MINIMAL3":
            self.pattern = "MINIMALTHREE"
        elif self.pattern == "MINIMAL4":
            self.pattern = "MINIMALFOUR"
		
       # FIX FOR PARALYZED - Kori
	    # changed in utility!
       # SCAR BASED POSE CHANGER - Kori
                # figuring this out later
        
    def init_eyes(self, parents):
        eye_groups = [Pelt.yellow_eyes, Pelt.orange_eyes, Pelt.green_eyes, Pelt.gray_eyes, Pelt.brown_eyes, Pelt.blue_eyes, Pelt.purple_eyes, Pelt.red_eyes]
        if not parents:
            self.eye_colour = random.choice(random.choices(eye_groups, weights=(90, 70, 50, 30, 20, 10, 5, 2), k=1)[0])
        else:
            par_eye_colors = []
            color_base_p = ''
            for p in parents:
                par_eye_colors.append(p.pelt.eye_colour)
            if len(par_eye_colors) <= 1:
                if par_eye_colors[0] == None:
                    color_base_p = par_eye_colors[1]
                else:
                    color_base_p = par_eye_colors[0]
            else:
                color_base_p = random.choice(par_eye_colors)
            if color_base_p in Pelt.yellow_eyes:
                self.eye_colour = random.choice(random.choices(eye_groups, weights=(40, 25, 15, 2, 10, 2, 1, 5), k=1)[0])
            elif color_base_p in Pelt.orange_eyes:
                self.eye_colour = random.choice(random.choices(eye_groups, weights=(25, 40, 2, 1, 15, 1, 1, 15), k=1)[0])
            elif color_base_p in Pelt.green_eyes:
                self.eye_colour = random.choice(random.choices(eye_groups, weights=(10, 3, 40, 10, 25, 10, 1, 1), k=1)[0])
            elif color_base_p in Pelt.gray_eyes:
                self.eye_colour = random.choice(random.choices(eye_groups, weights=(1, 1, 2, 40, 15, 30, 10, 1), k=1)[0])
            elif color_base_p in Pelt.brown_eyes:
                self.eye_colour = random.choice(random.choices(eye_groups, weights=(10, 10, 30, 6, 40, 2, 1, 1), k=1)[0])
            elif color_base_p in Pelt.blue_eyes:
                self.eye_colour = random.choice(random.choices(eye_groups, weights=(4, 4, 10, 30, 1, 40, 10, 1), k=1)[0])
            elif color_base_p in Pelt.purple_eyes:
                self.eye_colour = random.choice(random.choices(eye_groups, weights=(1, 1, 1, 20, 2, 30, 40, 5), k=1)[0])
            else:
                #red eyes
                self.eye_colour = random.choice(random.choices(eye_groups, weights=(10, 20, 1, 5, 2, 2, 20, 40), k=1)[0])
            
        
        #White patches must be initalized before eye color. 
        num = game.config["cat_generation"]["base_heterochromia"]
        if self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'WHITE']:
            num = num - 90
        if self.white_patches == 'FULLWHITE' or self.colour == 'WHITE':
            num -= 10
        for _par in parents:
            if _par.pelt.eye_colour2:
                num -= 10
        
        if num < 0:
            num = 1
            
        if not random.randint(0, num):
            if self.eye_colour in Pelt.yellow_eyes:
                eye_choice = choice([Pelt.green_eyes, Pelt.brown_eyes, Pelt.blue_eyes, Pelt.purple_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.orange_eyes:
                eye_choice = choice([Pelt.green_eyes, Pelt.brown_eyes, Pelt.blue_eyes, Pelt.red_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.green_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.orange_eyes, Pelt.gray_eyes, Pelt.brown_eyes, Pelt.blue_eyes, Pelt.purple_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.gray_eyes:
                eye_choice = choice([Pelt.green_eyes, Pelt.brown_eyes, Pelt.blue_eyes, Pelt.purple_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.brown_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.orange_eyes, Pelt.green_eyes, Pelt.gray_eyes, Pelt.blue_eyes, Pelt.purple_eyes, Pelt.red_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.blue_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.orange_eyes, Pelt.green_eyes, Pelt.gray_eyes, Pelt.brown_eyes, Pelt.purple_eyes, Pelt.red_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.purple_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.orange_eyes, Pelt.green_eyes, Pelt.gray_eyes, Pelt.brown_eyes, Pelt.blue_eyes, Pelt.red_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.red_eyes:
                eye_choice = choice([Pelt.green_eyes, Pelt.gray_eyes, Pelt.brown_eyes, Pelt.blue_eyes, Pelt.purple_eyes])
                self.eye_colour2 = choice(eye_choice)

    def pattern_color_inheritance(self, parents: tuple=(), gender="female"):
        # setting parent pelt categories
        #We are using a set, since we don't need this to be ordered, and sets deal with removing duplicates.
        par_peltlength = set()
        par_peltcolours = set()
        par_peltnames = set()
        par_pelts = []
        par_white = []
        par_species_mix = [[], []]
        temp_parent = [["W", "W", "W", "W", "W", "W"], ["C", "C", "C", "C", "C", "C"], ["D", "D", "D", "D", "D", "D"], ["W", "C", "W", "C", "W", "W"], ["W", "W", "W", "W", "W", "W"]]
        x = 0
        for p in parents:
            if p:
                # Gather pelt color.
                par_peltcolours.add(p.pelt.colour)

                # Gather pelt length
                par_peltlength.add(p.pelt.length)

                # Gather pelt name
                if p.pelt.name in Pelt.torties:
                    par_peltnames.add(p.pelt.tortiebase.capitalize())
                else:
                    par_peltnames.add(p.pelt.name)

                # Gather exact pelts, for direct inheritance.
                par_pelts.append(p.pelt)

                # Gather if they have white in their pelt.
                par_white.append(p.pelt.white)
                
                # Species information
                par_species_mix[x] = p.pelt.species_mix
            else:
                # If order for white patches to work correctly, we also want to randomly generate a "pelt_white"
                # for each "None" parent (missing or unknown parent)
                par_white.append(bool(random.getrandbits(1)))

                # Append None
                # Gather pelt color.
                par_peltcolours.add(None)
                par_peltlength.add(None)
                par_peltnames.add(None)
                par_species_mix[x] = random.choice(temp_parent)
            x += 1
		# HYBRIDIZATION - Kori
		# Determines numbers for hybrids and sets the hybrid status. part of pelts
		# just for simplicity, as I'm modifying this file a lot
		# I am new to coding so lots of if/else statements sorry!
        if len(par_species_mix[0]) != 6 or len(par_species_mix[1]) != 6:
            if len(par_species_mix[0]) != 6 and len(par_species_mix[1]) != 6:
                par_species_mix[0] = random.choice(temp_parent)
                par_species_mix[1] = random.choice(temp_parent)
            elif len(par_species_mix[0]) !=6:
                par_species_mix[0] = random.choice(temp_parent)
            elif len(par_species_mix[1]) != 6:
                par_species_mix[1] = random.choice(temp_parent)
        chosen_species_mix = ["", "", "", "", "", ""]
        chosen_species = "Wolf"
        y = 0
        z = 1
        for i in range(0, 3):
            p1 = [par_species_mix[0][y], par_species_mix[0][z]]
            p2 = [par_species_mix[1][y], par_species_mix[1][z]]
            chosen_species_mix[y] = random.choice(p1)
            chosen_species_mix[z] = random.choice(p2)
            y += 2
            z += 2
        if "C" not in chosen_species_mix and "D" not in chosen_species_mix:
            chosen_species = "Wolf"
        elif "D" not in chosen_species_mix and "W" not in chosen_species_mix:
            chosen_species = "Coyote"
        else:
            wolf = chosen_species_mix.count("W")
            yote = chosen_species_mix.count("C")
            dog = chosen_species_mix.count("D")
            if wolf == 5 and yote == 1 or wolf == 4 and yote == 2 or wolf == 3 and yote == 3 or yote == 4 and wolf == 2 or yote == 5 and wolf == 1:
                chosen_species = "Coywolf"
            elif wolf == 5 and dog == 1 or wolf == 4 and dog == 2 or wolf == 3 and dog == 3 or dog == 4 and wolf == 2 or dog == 5 and wolf == 1:
                chosen_species = "Wolfdog"
            elif wolf == 5 or wolf == 4 or wolf == 3:
                chosen_species = "Wolf Hybrid"
            elif yote == 5 and dog == 1 or yote == 4 and dog == 2 or yote == 3 and dog == 3 or dog == 4 and wolf == 2 or dog == 5 and wolf == 1:
                chosen_species = "Coydog"
            elif yote == 5 or yote == 4 or yote == 3:
                chosen_species = "Coyote Hybrid"
            else:
                chosen_species = "Hybrid"
        self.species_mix = chosen_species_mix
        self.species = chosen_species
        
        # If this list is empty, something went wrong.
        if not par_peltcolours:
            print("Warning - no parents: pelt randomized")
            return self.randomize_pattern_color(gender)

        # There is a 1/10 chance for kits to have the exact same pelt as one of their parents
        if not random.randint(0, game.config["cat_generation"]["direct_inheritance"]):  # 1/10 chance
            selected = choice(par_pelts)
            self.name = selected.name
            self.length = selected.length
            self.colour = selected.colour
            self.tortiebase = selected.tortiebase
            return selected.white

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT
        # ------------------------------------------------------------------------------------------------------------#

        # Determine pelt.
        weights = [0, 0, 0, 0, 0]  #Weights for each pelt group. It goes: (tabbies, spotted, plain, exotic)
        #standardpelts, northpelts, southpelts, darkpelts, specialpelts
        for p_ in par_peltnames:
            if p_ in Pelt.standardpelts:
                add_weight = (50, 25, 10, 10, 5)
            elif p_ in Pelt.northpelts:
                add_weight = (20, 50, 5, 5, 20)
            elif p_ in Pelt.southpelts:
                add_weight = (10, 5, 50, 25, 10)
            elif p_ in Pelt.darkpelts:
                add_weight = (10, 5, 20, 50, 15)
            elif p_ in Pelt.specialpelts:
                add_weight = (10, 30, 5, 5, 50)
            elif p_ is None:  # If there is at least one unknown parent, a None will be added to the set.
                add_weight = (35, 25, 20, 10, 10)
            else:
                add_weight = (0, 0, 0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weight[x]

        #A quick check to make sure all the weights aren't 0
        if all([x == 0 for x in weights]):
            weights = [1, 1, 1, 1, 1]

        # Now, choose the pelt category and pelt. The extra 0 is for the tortie pelts,
        chosen_pelt = ""
        temp_chosen_pelt = random.choices(Pelt.pelt_categories, weights=weights + [0], k = 1)
        if "Graywolf" in temp_chosen_pelt[0]:
            chosen_pelt = random.choices(Pelt.standardpelts, weights=(60, 40, 40, 40, 20, 20), k = 1)[0]
        elif "Arctic" in temp_chosen_pelt[0]:
            chosen_pelt = random.choices (Pelt.northpelts, weights=(65, 65, 20), k = 1)[0]
        elif "Mexican" in temp_chosen_pelt[0]:
            chosen_pelt = random.choices(Pelt.southpelts, weights=(50, 50, 50), k = 1)[0]
        elif "Colorpoint" in temp_chosen_pelt[0]:
            chosen_pelt = random.choices(Pelt.darkpelts, weights=(50, 70, 15), k = 1)[0]
        elif "Semisolid" in temp_chosen_pelt[0]:
            chosen_pelt = random.choices(Pelt.specialpelts, weights=(70, 20, 10), k = 1)[0]
        else:
            print('Hi you borked the inheritance for pelts')

        # Tortie chance
        tortie_chance_f = game.config["cat_generation"]["base_female_tortie"]  # There is a default chance for female tortie
        tortie_chance_m = game.config["cat_generation"]["base_male_tortie"]
        for p_ in par_pelts:
            if p_.name in Pelt.torties:
                tortie_chance_f = int(tortie_chance_f / 2)
                tortie_chance_m = tortie_chance_m - 1
                break

        # Determine tortie:
        if gender == "female":
            torbie = random.getrandbits(tortie_chance_f) == 1
        else:
            torbie = random.getrandbits(tortie_chance_m) == 1

        chosen_tortie_base = None
        if torbie:
            # If it is tortie, the chosen pelt above becomes the base pelt.
            chosen_tortie_base = chosen_pelt
            if chosen_tortie_base in ["Semisolid", "Solid"]:
                chosen_tortie_base = "Solid"
            chosen_tortie_base = chosen_tortie_base.lower()
            chosen_pelt = random.choice(Pelt.torties)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT COLOUR
        # ------------------------------------------------------------------------------------------------------------#
        # Weights for each colour group. It goes: (ginger_colours, black_colours, white_colours, brown_colours)
        # yellow_colors, gray_colors, black_colors, red_colors, dilute_colors
        weights = [0, 0, 0, 0, 0]
        for p_ in par_peltcolours:
            if p_ in Pelt.yellow_colors:
                add_weight = (55, 10, 10, 20, 5)
            elif p_ in Pelt.gray_colors:
                add_weight = (10, 40, 25, 5, 20)
            elif p_ in Pelt.black_colors:
                add_weight = (5, 30, 40, 5, 20)
            elif p_ in Pelt.red_colors:
                add_weight = (30, 5, 5, 55, 5)
            elif p_ in Pelt.dilute_colors:
                add_weight = (10, 25, 20, 10, 35)
            elif p_ is None:
                add_weight = (35, 25, 20, 15, 5)
            else:
                add_weight = (0, 0, 0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weight[x]

            # A quick check to make sure all the weights aren't 0
            if all([x == 0 for x in weights]):
                weights = [1, 1, 1, 1, 1]
        
        chosen_pelt_color = ""
        temp_chosen_pelt_color = random.choices(Pelt.colour_categories, weights=weights, k=1)
        if "HONEY" in temp_chosen_pelt_color[0]:
            chosen_pelt_color = random.choices(Pelt.yellow_colors, weights=(50, 50, 50, 50, 15, 15, 15, 25), k=1)[0]
        elif "MIST" in temp_chosen_pelt_color[0]:
            chosen_pelt_color = random.choices(Pelt.gray_colors, weights=(70, 70, 70, 20, 20), k=1)[0]
        elif "BLACK" in temp_chosen_pelt_color[0]:
            chosen_pelt_color = random.choices(Pelt.black_colors, weights=(90, 10, 20), k=1)[0]
        elif "SPICE" in temp_chosen_pelt_color[0]:
            chosen_pelt_color = random.choices(Pelt.red_colors, weights=(80, 80, 20), k=1)[0]
        elif "CHOCOLATE" in temp_chosen_pelt_color[0]:
            chosen_pelt_color = random.choices(Pelt.dilute_colors, weights=(70, 40, 70, 40, 20, 10), k=1)[0]
        else:
            print('color inheritance is borked')
        # ------------------------------------------------------------------------------------------------------------#
        #   PELT LENGTH
        # ------------------------------------------------------------------------------------------------------------#

        weights = [0, 0, 0]  # Weights for each length. It goes (short, medium, long)
        for p_ in par_peltlength:
            if p_ == "short":
                add_weight = (50, 10, 2)
            elif p_ == "medium":
                add_weight = (25, 50, 25)
            elif p_ == "long":
                add_weight = (2, 10, 50)
            elif p_ is None:
                add_weight = (10, 10, 10)
            else:
                add_weight = (0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weight[x]

        # A quick check to make sure all the weights aren't 0
        if all([x == 0 for x in weights]):
            weights = [1, 1, 1]

        chosen_pelt_length = random.choices(Pelt.pelt_length, weights=weights, k=1)[0]

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT WHITE
        # ------------------------------------------------------------------------------------------------------------#

        # There is 94 percentage points that can be added by
        # parents having white. If we have more than two, this
        # will keep that the same.
        percentage_add_per_parent = int(94 / len(par_white))
        chance = 3
        for p_ in par_white:
            if p_:
                chance += percentage_add_per_parent

        chosen_white = random.randint(1, 100) <= chance

        # Adjustments to pelt chosen based on if the pelt has white in it or not.
        if chosen_pelt in ["TwoColour", "SingleColour"]:
            if chosen_white:
                chosen_pelt = "TwoColour"
            else:
                chosen_pelt = "SingleColour"
        elif chosen_pelt == "Calico":
            if not chosen_white:
                chosen_pelt = "Tortie"

        # SET THE PELT
        self.name = chosen_pelt
        self.colour = chosen_pelt_color
        self.length = chosen_pelt_length
        self.tortiebase = chosen_tortie_base   # This will be none if the cat isn't a tortie.
        return chosen_white

    def randomize_pattern_color(self, gender):
        # ------------------------------------------------------------------------------------------------------------#
        #   PELT
        # ------------------------------------------------------------------------------------------------------------#

        # Determine pelt.
        chosen_pelt = ""
        temp_chosen_pelt = random.choices(Pelt.pelt_categories, weights=(35, 25, 20, 15, 5, 0), k = 1)
        if "Graywolf" in temp_chosen_pelt[0]:
            chosen_pelt = random.choices(Pelt.standardpelts, weights=(60, 40, 40, 40, 20, 20), k = 1)[0]
        elif "Arctic" in temp_chosen_pelt[0]:
            chosen_pelt = random.choices (Pelt.northpelts, weights=(70, 70, 20), k = 1)[0]
        elif "Mexican" in temp_chosen_pelt[0]:
            chosen_pelt = random.choices(Pelt.southpelts, weights=(50, 50, 50), k = 1)[0]
        elif "Colorpoint" in temp_chosen_pelt[0]:
            chosen_pelt = random.choices(Pelt.darkpelts, weights=(50, 70, 20), k = 1)[0]
        elif "Semisolid" in temp_chosen_pelt[0]:
            chosen_pelt = random.choices(Pelt.specialpelts, weights=(70, 20, 10), k = 1)[0]
        else:
            print('Hi you borked the randomized pelts')

        # Tortie chance
        # There is a default chance for female tortie, slightly increased for completely random generation.
        tortie_chance_f = game.config["cat_generation"]["base_female_tortie"] - 1
        tortie_chance_m = game.config["cat_generation"]["base_male_tortie"]
        if gender == "female":
            torbie = random.getrandbits(tortie_chance_f) == 1
        else:
            torbie = random.getrandbits(tortie_chance_m) == 1

        chosen_tortie_base = None
        if torbie:
            # If it is tortie, the chosen pelt above becomes the base pelt.
            chosen_tortie_base = chosen_pelt
            if chosen_tortie_base in ["TwoColour", "SingleColour"]:
                chosen_tortie_base = "Single"
            chosen_tortie_base = chosen_tortie_base.lower()
            chosen_pelt = random.choice(Pelt.torties)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT COLOUR
        # ------------------------------------------------------------------------------------------------------------#

        chosen_pelt_color = ""
        temp_chosen_pelt_color = random.choices(Pelt.colour_categories, weights=(35, 25, 20, 15, 5), k=1)
        if "HONEY" in temp_chosen_pelt_color[0]:
            chosen_pelt_color = random.choices(Pelt.yellow_colors, weights=(50, 50, 50, 50, 10, 10, 10, 25), k=1)[0]
        elif "MIST" in temp_chosen_pelt_color[0]:
            chosen_pelt_color = random.choices(Pelt.gray_colors, weights=(70, 70, 70, 10, 10), k=1)[0]
        elif "BLACK" in temp_chosen_pelt_color[0]:
            chosen_pelt_color = random.choices(Pelt.black_colors, weights=(90, 10, 20), k=1)[0]
        elif "SPICE" in temp_chosen_pelt_color[0]:
            chosen_pelt_color = random.choices(Pelt.red_colors, weights=(80, 80, 20), k=1)[0]
        elif "CHOCOLATE" in temp_chosen_pelt_color[0]:
            chosen_pelt_color = random.choices(Pelt.dilute_colors, weights=(70, 40, 70, 40, 20, 10), k=1)[0]
        else:
            print('color randomization is borked')

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT LENGTH
        # ------------------------------------------------------------------------------------------------------------#


        chosen_pelt_length = random.choice(Pelt.pelt_length)

		# SPECIES
        chosen_species_mix = ["", "", "", "", "", ""]
        chosen_species = ""
        poss_genes = ["W", "C", "D"]
        quick_genes = [["W", "W", "W", "W", "W", "W"], ["C", "C", "C", "C", "C", "C"]]
        x = 0
        species_grabber = random.randint(0, 10)
        if species_grabber <= 2:
            chosen_species_mix = random.choices(quick_genes, weights=(100, 20), k=1)[0]
        else:
            for i in range(0, 6):
                chosen_species_mix[x] = random.choices(poss_genes, weights=(400, 40, 10), k=1)[0]
                x += 1
        if "C" not in chosen_species_mix and "D" not in chosen_species_mix:
            chosen_species = "Wolf"
        elif "D" not in chosen_species_mix and "W" not in chosen_species_mix:
            chosen_species = "Coyote"
        else:
            wolf = chosen_species_mix.count("W")
            yote = chosen_species_mix.count("C")
            dog = chosen_species_mix.count("D")
            if wolf == 5 and yote == 1 or wolf == 4 and yote == 2 or wolf == 3 and yote == 3 or yote == 4 and wolf == 2 or yote == 5 and wolf == 1:
                chosen_species = "Coywolf"
            elif wolf == 5 and dog == 1 or wolf == 4 and dog == 2 or wolf == 3 and dog == 3 or dog == 4 and wolf == 2 or dog == 5 and wolf == 1:
                chosen_species = "Wolfdog"
            elif wolf == 5 or wolf == 4 or wolf == 3:
                chosen_species = "Wolf Hybrid"
            elif yote == 5 and dog == 1 or yote == 4 and dog == 2 or yote == 3 and dog == 3 or dog == 4 and wolf == 2 or dog == 5 and wolf == 1:
                chosen_species = "Coydog"
            elif yote == 5 or yote == 4 or yote == 3:
                chosen_species = "Coyote Hybrid"
            else:
                chosen_species = "Hybrid"
				
        # ------------------------------------------------------------------------------------------------------------#
        #   PELT WHITE
        # ------------------------------------------------------------------------------------------------------------#


        chosen_white = random.randint(1, 100) <= 40

        # Adjustments to pelt chosen based on if the pelt has white in it or not.
        if chosen_pelt in ["TwoColour", "SingleColour"]:
            if chosen_white:
                chosen_pelt = "TwoColour"
            else:
                chosen_pelt = "SingleColour"
        elif chosen_pelt == "Calico":
            if not chosen_white:
                chosen_pelt = "Tortie"

        self.name = chosen_pelt
        self.colour = chosen_pelt_color
        self.length = chosen_pelt_length
        self.tortiebase = chosen_tortie_base   # This will be none if the cat isn't a tortie.
        self.species_mix = chosen_species_mix
        self.species = chosen_species
        return chosen_white

    def init_pattern_color(self, parents, gender) -> bool:
        """Inits self.name, self.colour, self.length, 
            self.tortiebase and determines if the cat 
            will have white patche or not. 
            Return TRUE is the cat should have white patches, 
            false is not. """
        
        if parents:
            #If the cat has parents, use inheritance to decide pelt.
            chosen_white = self.pattern_color_inheritance(parents, gender)
        else:
            chosen_white = self.randomize_pattern_color(gender)
        
        return chosen_white

    def init_sprite(self):
        self.cat_sprites = {
            'newborn': 20,
            'kitten': random.randint(0, 2),
            'adolescent': random.randint(3, 5),
            'senior': random.randint(12, 14),
            'sick_young': 19,
            'sick_adult': 18
        }
        self.reverse = choice([True, False])
        # skin chances
        temp_dilute_list = ['CHOCOLATE', 'COCOA', 'BLUE', 'SPRUCE', 'LILAC', 'ISABELLA']
        skin_sprites = Pelt.skin_sprites.copy()
        low_white = Pelt.low_white.copy()
        mid_white = Pelt.mid_white.copy()
        high_white = Pelt.high_white.copy()
        if self.white_patches == None and self.colour not in temp_dilute_list and self.tortiepattern == None:
            skin_list = [skin_sprites[0], skin_sprites[11]]
            self.skin = random.choices(skin_list, weights=(90, 10), k=1)[0]
        elif self.colour in temp_dilute_list:
            if self.colour == "CHOCOLATE" or self.colour == 'COCOA':
                if self.white_patches == None and self.tortiepattern == None:
                    skin_list = [skin_sprites[8], skin_sprites[9]]
                    self.skin = random.choices(skin_list, weights=(60, 40), k=1)[0]
                else:
                    skin_list = [skin_sprites[8], skin_sprites[9], skin_sprites[5], skin_sprites[10]]
                    self.skin = random.choices(skin_list, weights=(10, 20, 40, 30), k=1)[0]
            elif self.colour == "BLUE" or self.colour == 'SPRUCE':
                if self.white_patches == None and self.tortiepattern == None:
                    skin_list = [skin_sprites[1], skin_sprites[6]]
                    self.skin = random.choices(skin_list, weights=(60, 40), k=1)[0]
                else:
                    #Lilac and Isabella
                    skin_list = [skin_sprites[1], skin_sprites[6], skin_sprites[4], skin_sprites[10]]
                    self.skin = random.choices(skin_list, weights=(30, 20, 40, 10), k=1)[0]
            else:
                if self.white_patches == None and self.tortiepattern == None:
                    skin_list = [skin_sprites[7], skin_sprites[10]]
                    self.skin = random.choices(skin_list, weights=(80, 20), k=1)[0]
                else:
                    self.skin = skin_sprites[10]
        elif self.white_patches != None:
            if self.tortiepattern != None:
                if self.white_patches not in high_white:
                    skin_list = [skin_sprites[0], skin_sprites[2], skin_sprites[3], skin_sprites[11], skin_sprites[12]]
                    self.skin = random.choices(skin_list, weights=(10, 30, 15, 15, 30), k=1)[0]
                else:
                    self.skin = skin_sprites[10]
            elif self.white_patches not in low_white:
                skin_list = [skin_sprites[0], skin_sprites[2], skin_sprites[3], skin_sprites[10], skin_sprites[11], skin_sprites[12]]
                self.skin = random.choices(skin_list, weights=(20, 10, 10, 20, 20, 20), k=1)[0]
            else:
                skin_list = [skin_sprites[0], skin_sprites[3], skin_sprites[11]]
                self.skin = random.choices(skin_list, weights=(60, 20, 20), k=1)[0]
        elif self.tortiepattern != None:
            skin_list = [skin_sprites[0], skin_sprites[2], skin_sprites[3], skin_sprites[11]]
            self.skin = random.choice(skin_list)
        else:
            self.skin = choice(Pelt.skin_sprites)
                
        if self.length != 'long':
            self.cat_sprites['adult'] = random.randint(6, 11)
            self.cat_sprites['para_adult'] = 16
        else:
            self.cat_sprites['adult'] = random.randint(6, 11)
            self.cat_sprites['para_adult'] = 16
        self.cat_sprites['young adult'] = self.cat_sprites['adult']
        self.cat_sprites['senior adult'] = self.cat_sprites['adult']

    def init_scars(self, age):
        if age == "newborn":
            return
        
        if age in ['kitten', 'adolescent']:
            scar_choice = random.randint(0, 50)
        elif age in ['young adult', 'adult']:
            scar_choice = random.randint(0, 20)
        else:
            scar_choice = random.randint(0, 15)
            
        if scar_choice == 1:
            self.scars.append(choice([
                choice(Pelt.scars1),
                choice(Pelt.scars3)
            ]))

        if 'NOTAIL' in self.scars and 'HALFTAIL' in self.scars:
            self.scars.remove('HALFTAIL')

    def init_accessories(self, age):
        if age == "newborn": 
            self.accessory = None
            return
        
        acc_display_choice = random.randint(0, 80)
        if age in ['kitten', 'adolescent']:
            acc_display_choice = random.randint(0, 180)
        elif age in ['young adult', 'adult']:    
            acc_display_choice = random.randint(0, 100)
        
        if acc_display_choice in range(1, 30):
            self.accessory = choice([
                choice(Pelt.plant_accessories),
                choice(Pelt.wild_accessories)
            ])
        elif acc_display_choice in range(31, 45):
            self.accessory = choice(Pelt.radiocollars)
        elif acc_display_choice in range(46, 53):
            self.accessory = choice([
                 choice(Pelt.collars),
            	 choice(Pelt.bandanas)
            ])
        elif acc_display_choice in range(54, 60):
            self.accessory = choice(Pelt.harnesses)
        else:
            self.accessory = None

    def init_pattern(self):
        if self.name in Pelt.torties:
            if not self.tortiebase:
                self.tortiebase = choice(Pelt.tortiebases)
            if not self.pattern:
                self.pattern = choice(Pelt.tortiepatterns)

            wildcard_chance = game.config["cat_generation"]["wildcard_tortie"]
            if self.colour:
                # The "not wildcard_chance" allows users to set wildcard_tortie to 0
                # and always get wildcard torties.
                if not wildcard_chance or random.getrandbits(wildcard_chance) == 1:
                    # This is the "wildcard" chance, where you can get funky combinations.
                    # people are fans of the print message so I'm putting it back
                    print("Wildcard tortie!")

                    # Allow any pattern:
                    self.tortiepattern = choice(Pelt.tortiebases)
                    self.tortiepattern = self.tortiepattern.lower()

                    # Allow any colors that aren't the base color.
                    possible_colors = Pelt.pelt_colours.copy()
                    possible_colors.remove(self.colour)
                    self.tortiecolour = choice(possible_colors)

                else:
                    # Normal generation
                    self.tortiepattern = random.choices([self.tortiebase, 'semisolid', 'solid'], weights=[45, 30, 25], k=1)[0]

                    # Picking out tortie colors
                    if (self.colour in Pelt.black_colors):
                        self.tortiecolour = choice((Pelt.yellow_colors * 2) + Pelt.gray_colors + Pelt.red_colors + Pelt.black_colors)
                    elif self.colour in Pelt.yellow_colors:
                        self.tortiecolour = choice(Pelt.red_colors + (Pelt.black_colors * 2) + Pelt.yellow_colors)
                    elif self.colour in Pelt.gray_colors:
                        self.tortiecolour = choice(Pelt.gray_colors + Pelt.dilute_colors + Pelt.black_colors)
                    elif self.colour in Pelt.red_colors:
                        self.tortiecolour = choice(Pelt.yellow_colors + (Pelt.black_colors * 2))
                    elif self.colour in Pelt.dilute_colors:
                        if self.colour == "CHOCOLATE" or self.colour == "COCOA":
                            choc_temp = ["CHOCOLATE", "COCOA"]
                            self.tortiecolour = choice(choc_temp)
                        if self.colour == "BLUE" or self.colour == "SPRUCE":
                            blue_temp = ["BLUE", "SPRUCE"]
                            self.tortiecolour = choice(blue_temp)
                        if self.colour == "LILAC" or self.colour == "ISABELLA":
                            lilac_temp = ["LILAC", "ISABELLA"]
                            self.tortiecolour = choice(lilac_temp)
                    else:
                        self.tortiecolour = "HONEY"

            else:
                self.tortiecolour = "HONEY"
        else:
            self.tortiebase = None
            self.tortiepattern = None
            self.tortiecolour = None
            self.pattern = None

    def white_patches_inheritance(self, parents: tuple):

        par_whitepatches = set()
        par_points = []
        for p in parents:
            if p:
                if p.pelt.white_patches:
                    par_whitepatches.add(p.pelt.white_patches)
                if p.pelt.points:
                    par_points.append(p.pelt.points)

        if not parents:
            print("Error - no parents. Randomizing white patches.")
            self.randomize_white_patches()
            return

        # Direct inheritance. Will only work if at least one parent has white patches, otherwise continue on.
        if par_whitepatches and not random.randint(0, game.config["cat_generation"]["direct_inheritance"]):
            # This ensures Torties and Calicos won't get direct inheritance of incorrect white patch types
            _temp = par_whitepatches.copy()
            if self.name == "Tortie":
                for p in _temp.copy():
                    if p in Pelt.high_white + Pelt.mostly_white + ["FULLWHITE"]:
                        _temp.remove(p)
            elif self.name == "Calico":
                for p in _temp.copy():
                    if p in Pelt.low_white + Pelt.mid_white:
                        _temp.remove(p)

            # Only proceed with the direct inheritance if there are white patches that match the pelt.
            if _temp:
                self.white_patches = choice(list(_temp))

                # Direct inheritance also effect the point marking.
                if par_points and self.name != "Tortie":
                    self.points = choice(par_points)
                else:
                    self.points = None

                return

        # dealing with points
        if par_points:
            chance = 10 - len(par_points)
        else:
            chance = 40

        if self.name != "Tortie" and not (random.random() * chance):
            self.points = choice(Pelt.point_markings)
        else:
            self.points = None


        white_list = [Pelt.low_white, Pelt.mid_white, Pelt.high_white]

        weights = [0, 0, 0]  # Same order as white_list
        for p_ in par_whitepatches:
            if p_ in Pelt.low_white:
                add_weights = (45, 15, 5)
            elif p_ in Pelt.mid_white:
                add_weights = (20, 45, 15)
            elif p_ in Pelt.high_white:
                add_weights = (15, 45, 35)
            else:
                add_weights = (0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weights[x]


        # If all the weights are still 0, that means none of the parents have white patches.
        if not any(weights):
            if not all(parents):  # If any of the parents are None (unknown), use the following distribution:
                weights = [30, 10, 5]
            else:
                # Otherwise, all parents are known and don't have any white patches. Focus distribution on little_white.
                weights = [35, 5, 0]

        # Adjust weights for torties, since they can't have anything greater than mid_white:
        if self.name == "Tortie":
            weights = weights[:2] + [0, 0]
            # Another check to make sure not all the values are zero. This should never happen, but better
            # safe then sorry.
            if not any(weights):
                weights = [2, 1, 0]
        elif self.name == "Calico":
            weights = [0, 0] + weights[2:]
            # Another check to make sure not all the values are zero. This should never happen, but better
            # safe then sorry.
            if not any(weights):
                weights = [2, 1, 0]

        #kori - fix for now, weights aren't adding up correctly for whatever reason
        if len(weights) != 3:
            weights = [35, 5, 0]

        chosen_white_patches = choice(random.choices(white_list, weights=weights, k=1)[0])

        self.white_patches = chosen_white_patches
        if self.points and self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE']:
            self.points = None

    def randomize_white_patches(self):

        # Points determination. Tortie can't be pointed
        #if self.name != "Tortie" and not random.getrandbits(game.config["cat_generation"]["random_point_chance"]):
			# Cat has colorpoint!
        #    self.points = choice(Pelt.point_markings)
        #else:
        self.points = None

        # Adjust weights for torties, since they can't have anything greater than mid_white:
        if self.name == "Tortie":
            weights = (55, 0, 0)
        elif self.name == "Calico":
            weights = (15, 50, 25)
        else:
            weights = (30, 10, 5)

        white_list = [Pelt.low_white, Pelt.mid_white, Pelt.high_white]
        chosen_white_patches = choice(random.choices(white_list, weights=weights, k=1)[0])

        self.white_patches = chosen_white_patches
        if self.points and self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE']:
            self.points = None

    def init_white_patches(self, pelt_white, parents:tuple):
        # Vit can roll for anyone, not just cats who rolled to have white in their pelt. 
        #par_vit = []
        #for p in parents:
        #    if p:
        #        if p.pelt.vitiligo:
        #            par_vit.append(p.pelt.vitiligo)
        
        #vit_chance = max(game.config["cat_generation"]["vit_chance"] - len(par_vit), 0)
        #if not random.getrandbits(vit_chance):
        #    self.vitiligo = choice(Pelt.vit)

        # If the cat was rolled previously to have white patches, then determine the patch they will have
        # these functions also handle points. 
        if pelt_white:
            if parents:
                self.white_patches_inheritance(parents)
            else:
                self.randomize_white_patches()
        else:
            self.white_patches = None
            self.points = None

    def init_tint(self):
        """Sets tint for pelt and white patches"""

        # PELT TINT
        # Basic tints as possible for all colors.
        base_tints = sprites.cat_tints["possible_tints"]["basic"]
        if self.colour in sprites.cat_tints["colour_groups"]:
            color_group = sprites.cat_tints["colour_groups"].get(self.colour, "warm")
            color_tints = sprites.cat_tints["possible_tints"][color_group]
        else:
            color_tints = []
        
        if base_tints or color_tints:
            self.tint = choice(base_tints + color_tints)
        else:
            self.tint = "none"

        # WHITE PATCHES TINT
        if self.white_patches or self.points:
            #Now for white patches
            base_tints = sprites.white_patches_tints["possible_tints"]["basic"]
            if self.colour in sprites.cat_tints["colour_groups"]:
                color_group = sprites.white_patches_tints["colour_groups"].get(self.colour, "white")
                color_tints = sprites.white_patches_tints["possible_tints"][color_group]
            else:
                color_tints = []
            
            if base_tints or color_tints:
                self.white_patches_tint = choice(base_tints + color_tints)
            else:
                self.white_patches_tint = "none"    
        else:
            self.white_patches_tint = "none"

    @property
    def white(self):
        return self.white_patches or self.points
    
    @white.setter
    def white(self, val):
        print("Can't set pelt.white")
        return    

    @staticmethod
    def describe_appearance(cat, short=False):
        
        # Define look-up dictionaries
        if short:
            renamed_colors = {
                "honey": "honey",
                "flaxen": "flaxen",
                "cream": "cream",
                "pearl": "pearl",
                "gold": "golden",
                "brass": "brass",
                "sunstone": "peach",
                "mist": "gray",
                "ash": "gray",
                "steel": "gray",
                "silver": "gray",
                "moonstone": "gray",
                "black": "black",
                "onyx": "black",
                "spice": "red",
                "ginger": "ginger",
                "copper": "copper",
                "chocolate": "chocolate",
                "blue": "blue",
                "lilac": "lilac",
                "cocoa": "cocoa",
                "spruce": "blue",
                "isabella": "isabella",
                "sunny": "gold",
                "luna": "black"
            }
        else:
            renamed_colors = {
                "honey": "honey",
                "flaxen": "flaxen",
                "cream": "cream",
                "pearl": "cream",
                "gold": "golden",
                "brass": "brass",
                "sunstone": "peachy yellow",
                "mist": "misty gray",
                "ash": "ashen gray",
                "steel": "steel gray",
                "silver": "silver gray",
                "moonstone": "blue-gray",
                "black": "black",
                "onyx": "onyx black",
                "spice": "red",
                "ginger": "ginger",
                "copper": "copper",
                "chocolate": "chocolate",
                "blue": "blue",
                "lilac": "lilac",
                "cocoa": "cocoa",
                "spruce": "dark blue",
                "isabella": "isabella",
                "sunny": "bright gold",
                "luna": "silvery black"
            }

        pattern_des = {
            "Graywolf": "c_n agouti",
            "Ophelia": "c_n agouti",
            "Runic": "c_n agouti",
            "Timber": "c_n agouti",
            "Sable": "c_n sable",
            "Shepherd": "c_n saddle",
            "Arctic": "arctic c_n agouti",
            "Winter": "c_n winter agouti",
            "Husky": "c_n domino",
            "Mexican": "flashy c_n agouti",
            "Stormy": "dark c_n agouti",
            "Vibrant": "vibrant c_n agouti",
            "Colorpoint": "c_n colorpoint",
            "Smokey": "smokey c_n agouti",
            "Points": "c_n points",
            "Semisolid": "solid c_n",
            "Solid": "solid c_n"
        }

        # Start with determining the base color name. 
        color_name = str(cat.pelt.colour).lower()
        if color_name in renamed_colors:
            color_name = renamed_colors[color_name]
        
        # Replace "white" with "pale" if the cat is 
        #if cat.pelt.name not in ["SingleColour", "TwoColour", "Tortie", "Calico"] and color_name == "white":
        #    color_name = "pale"

        # Time to descibe the pattern and any additional colors. 
        if cat.pelt.name in pattern_des:
            if cat.pelt.name != "Points":
                color_name = pattern_des[cat.pelt.name].replace("c_n", color_name)
            else:
                temp_color_name = ''
                if str(cat.pelt.colour).lower() == "cocoa" or str(cat.pelt.colour).lower() == "spice" or str(cat.pelt.colour).lower() == "ginger" or str(cat.pelt.colour).lower() == "copper":
                    temp_color_name = "black and red"
                elif str(cat.pelt.colour).lower() == "honey" or str(cat.pelt.colour).lower() == "flaxen":
                    temp_color_name = "black and fawn"
                elif str(cat.pelt.colour).lower() == "cream" or str(cat.pelt.colour).lower() == "pearl":
                    temp_color_name = "black and cream"
                elif str(cat.pelt.colour).lower() == "mist" or str(cat.pelt.colour).lower() == "ash" or str(cat.pelt.colour).lower() == "silver" or str(cat.pelt.colour).lower() == 'moonstone':
                    temp_color_name = "gray and silver"
                elif str(cat.pelt.colour).lower() == "steel" or str(cat.pelt.colour).lower() == "onyx":
                    temp_color_name = "black and gray"
                elif str(cat.pelt.colour).lower() == "black" or str(cat.pelt.colour).lower() == "luna":
                    temp_color_name = "solid black"
                elif str(cat.pelt.colour).lower() == "chocolate" or str(cat.pelt.colour).lower() == "blue" or str(cat.pelt.colour).lower() == "lilac":
                    temp_color_name = str(renamed_colors[color_name]) + " and cream"
                elif str(cat.pelt.colour).lower() == "spruce":
                    temp_color_name = "blue and gray"
                elif str(cat.pelt.colour).lower() == "isabella":
                    temp_color_name = "isabella and silver"
                elif str(cat.pelt.colour).lower() == "sunny":
                    temp_color_name = "gold and cream"
                elif str(cat.pelt.colour).lower() == "gold":
                    temp_color_name = "black and gold"
                elif str(cat.pelt.colour).lower() == "brass":
                    temp_color_name = "brown and cream"
                elif str(cat.pelt.colour).lower() == "sunstone":
                    temp_color_name = "peach and cream"

                if cat.pelt.colour.lower() != "black":
                    color_name = pattern_des[cat.pelt.name].replace("c_n", temp_color_name)
                else:
                    #makes sure the color name for now comes up as 'solid black' if the color is black
                    color_name = temp_color_name
        elif cat.pelt.name in Pelt.torties:
            #had to revamp this entirely, sorry about the mess!
            # Calicos and Torties need their own desciptions.
            temp_agouti_list = ["graywolf", "ophelia", "runic", "timber", "arctic", "winter", "mexican", "stormy", "vibrant", "smokey"]
            tc1 = renamed_colors[str(cat.pelt.colour).lower()]
            tc2 = renamed_colors[str(cat.pelt.tortiecolour).lower()]
            if short:
                color_name = cat.pelt.name.lower()
            else:
                #if both patterns on the tortie are the same
                
                if str(cat.pelt.tortiebase) == str(cat.pelt.tortiepattern):
                    if cat.pelt.tortiebase == "solid" or cat.pelt.tortiebase == "semisolid":
                        color_name = renamed_colors[str(cat.pelt.colour).lower()] + " and " + renamed_colors[str(cat.pelt.tortiecolour).lower()]
                    elif cat.pelt.tortiebase in temp_agouti_list:
                        color_name = tc1 + " and " + tc2  + " agouti " + cat.pelt.name.lower()
                    elif cat.pelt.tortiebase == "sable":
                        color_name = tc1 + " and " + tc2 + " sable " + cat.pelt.name.lower()
                    elif cat.pelt.tortiebase == "shepherd":
                        color_name = tc1 + " and " + tc2 + " saddle " + cat.pelt.name.lower()
                    elif cat.pelt.tortiebase == "husky":
                        color_name = tc1 + " and " + tc2 + " domino " + cat.pelt.name.lower()
                    elif cat.pelt.tortiebase == "colorpoint":
                        color_name = tc1 + " and " + tc2 + " colorpoint " + cat.pelt.name.lower()
                    else:
                        color_name = tc1 + " and " + tc2 + " pointed " + cat.pelt.name.lower()
                #if both patterns are different
                else:
                    if cat.pelt.tortiebase == "solid" or cat.pelt.tortiebase == "semisolid" or cat.pelt.tortiepattern == "solid" or cat.pelt.tortiepattern == "semisolid":
                        if cat.pelt.tortiebase == "solid" or cat.pelt.tortiebase == "semisolid":
                            if cat.pelt.tortiepattern in temp_agouti_list:
                                color_name = tc1 + " agouti and " + tc2 + " " + cat.pelt.name.lower()
                            elif cat.pelt.tortiepattern == "sable":
                                color_name = tc1 + " sable and " + tc2 + " " + cat.pelt.name.lower()
                            elif cat.pelt.tortiepattern == "shepherd":
                                color_name = tc1 + " saddle and " + tc2 + " " + cat.pelt.name.lower()
                            elif cat.pelt.tortiepattern == "husky":
                                color_name = tc1 + " domino and " + tc2 + " " + cat.pelt.name.lower()
                            elif cat.pelt.tortiepattern == "colorpoint":
                                color_name = tc1 + " colorpoint and " + tc2 + " " + cat.pelt.name.lower()
                            else:
                                color_name = tc1 + " points and " + tc2 + " " + cat.pelt.name.lower()
                        else:
                            if cat.pelt.tortiebase in temp_agouti_list:
                                color_name = tc2 + " agouti and " + tc1 + " " + cat.pelt.name.lower()
                            elif cat.pelt.tortiebase == "sable":
                                color_name = tc2 + " sable and " + tc1 + " " + cat.pelt.name.lower()
                            elif cat.pelt.tortiebase == "shepherd":
                                color_name = tc2 + " saddle and " + tc1 + " " + cat.pelt.name.lower()
                            elif cat.pelt.tortiebase == "husky":
                                color_name = tc2 + " domino and " + tc1 + " " + cat.pelt.name.lower()
                            elif cat.pelt.tortiebase == "colorpoint":
                                color_name = tc2 + " colorpoint and " + tc1 + " " + cat.pelt.name.lower()
                            else:
                                color_name = tc2 + " points and " + tc1 + " " + cat.pelt.name.lower()
                    else:
                        color_name = tc1 + " and " + tc2 + " dappled " + cat.pelt.name.lower()
            #if short:
                # If using short, don't add describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
                # If using short, don't describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
                #if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
                #    cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
                #    color_name = "mottled"
                #else:
                #    color_name = cat.pelt.name.lower()
            #else:
            #    base = cat.pelt.tortiebase.lower()
            #    if base in Pelt.tabbies + ['bengal', 'rosette', 'speckled']:
            #        base = 'tabby'
            #    else:
            #        base = ''

            #    patches_color = cat.pelt.tortiecolour.lower()
            #    if patches_color in renamed_colors:
            #        patches_color = renamed_colors[patches_color]
            #    color_name = f"{color_name}/{patches_color}"
                
            #    if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
            #        cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
            #            color_name = f"{color_name} mottled"
            #    else:
            #        color_name = f"{color_name} {cat.pelt.name.lower()}"

        if cat.pelt.white_patches:
            if cat.pelt.white_patches == "WHITE":
                # If the cat is fullwhite, discard all other information. They are just white. 
                color_name = "white"
            if cat.pelt.white_patches in Pelt.mostly_white and cat.pelt.name != "Calico":
                color_name = f"white and {color_name}"
            elif cat.pelt.name != "Calico":
                color_name = f"{color_name} and white"
        
        #if cat.pelt.points:
        #    color_name = f"{color_name} point"
        #    if "ginger point" in color_name:
        #        color_name.replace("ginger point", "flame point")

        if "white and white" in color_name:
            color_name = color_name.replace("white and white", "white")

        # Now it's time for gender
        #if cat.genderalign in ["female", "trans female"]:
        #    color_name = f"{color_name} she-cat"
        #elif cat.genderalign in ["male", "trans male"]:
        #    color_name = f"{color_name} tom"
        #else:
        #    color_name = f"{color_name} cat"

        #species instead
        color_name = str(color_name + " " + str(cat.pelt.species).lower())

        # Here is the place where we can add some additional details about the cat, for the full non-short one. 
        # These include notable missing limbs, vitiligo, long-furred-ness, and 3 or more scars. 
        if not short:
            
            scar_details = {
                "NOTAIL": "no tail", 
                "HALFTAIL": "half a tail", 
                "NOPAW": "three legs", 
                "NOLEFTEAR": "a missing ear", 
                "NORIGHTEAR": "a missing ear",
                "NOEAR": "no ears"
            }

            additional_details = []
            #if cat.pelt.vitiligo:
            #    additional_details.append("vitiligo")
            for scar in cat.pelt.scars:
                if scar in scar_details and scar_details[scar] not in additional_details:
                    additional_details.append(scar_details[scar])
            
            if len(additional_details) > 1:
                color_name = f"{color_name} with {', '.join(additional_details[:-1])} and {additional_details[-1]}"
            elif additional_details:
                color_name = f"{color_name} with {additional_details[0]}"
        
        
            if len(cat.pelt.scars) >= 3:
                color_name = f"scarred {color_name}"
            #if cat.pelt.length == "long":
            #    color_name = f"long-furred {color_name}"

        return color_name
    
    def get_sprites_name(self):
        return Pelt.sprites_names[self.name]
