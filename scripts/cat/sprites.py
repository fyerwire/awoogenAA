import pygame

import ujson

from scripts.game_structure.game_essentials import game

class Sprites():
    cat_tints = {}
    white_patches_tints = {}

    def __init__(self, size=None):
        """Class that handles and hold all spritesheets. 
        Size is normall automatically determined by the size
        of the lineart. If a size is passed, it will override 
        this value. """
        self.size = None
        self.spritesheets = {}
        self.images = {}
        self.sprites = {}

        # Shared empty sprite for placeholders
        self.blank_sprite = None
        
        self.load_tints()

    def load_tints(self):
        try:
            with open("sprites/dicts/tint.json", 'r') as read_file:
                self.cat_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading Tints")

        try:
            with open("sprites/dicts/white_patches_tint.json", 'r') as read_file:
                self.white_patches_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading White Patches Tints")
            
    def spritesheet(self, a_file, name):
        """
        Add spritesheet called name from a_file.

        Parameters:
        a_file -- Path to the file to create a spritesheet from.
        name -- Name to call the new spritesheet.
        """
        self.spritesheets[name] = pygame.image.load(a_file).convert_alpha()

    def make_group(self,
                   spritesheet,
                   pos,
                   name,
                   sprites_x=3,
                   sprites_y=7):  # pos = ex. (2, 3), no single pixels
        """
        Divide sprites on a sprite-sheet into groups of sprites that are easily accessible.

        Parameters:
        spritesheet -- Name of spritesheet.
        pos -- (x,y) tuple of offsets. NOT pixel offset, but offset of other sprites.
        name -- Name of group to make.
        
        Keyword Arguments
        sprites_x -- Number of sprites horizontally (default: 3)
        sprites_y -- Number of sprites vertically (default: 3)
        """

        group_x_ofs = pos[0] * sprites_x * self.size
        group_y_ofs = pos[1] * sprites_y * self.size
        i = 0

        # splitting group into singular sprites and storing into self.sprites section
        for y in range(sprites_y):
            for x in range(sprites_x):
                try:
                    new_sprite = pygame.Surface.subsurface(
                        self.spritesheets[spritesheet],
                        group_x_ofs + x * self.size,
                        group_y_ofs + y * self.size,
                        self.size, self.size
                    )
                except ValueError:
                    # Fallback for non-existent sprites
                    if not self.blank_sprite:
                        self.blank_sprite = pygame.Surface(
                            (self.size, self.size),
                            pygame.HWSURFACE | pygame.SRCALPHA
                        )
                    new_sprite = self.blank_sprite
                self.sprites[f'{name}{i}'] = new_sprite
                i += 1

    def load_all(self):
        # get the width and height of the spritesheet
        lineart = pygame.image.load('sprites/lineart.png')
        width, height = lineart.get_size()
        del lineart # unneeded

        # if anyone changes lineart for whatever reason update this
        if isinstance(self.size, int):
            pass
        elif width / 3 == height / 7:
            self.size = width / 3
        else:
            self.size = 80 # default, what base clangen uses
            print(f"lineart.png is not 3x7, falling back to {self.size}")
            print(f"if you are a modder, please update scripts/cat/sprites.py and do a search for 'if width / 3 == height / 7:'")

        del width, height # unneeded

        for x in [
            'lineart',
            'whitepatches', 'eyes', 'eyes2', 'skin', 'scars', 'missingscars', 'specialpoints', 
			'arctic', 'colorpoint', 'graywolf', 'mexican', 'ophelia', 'runic',
			'semisolid', 'smokey', 'stormy', 'timber', 'vibrant', 'winter',
			'brindle', 'husky', 'points', 'sable', 'shepherd', 'solid', 'merle', 
            'collars', 'bellcollars', 'bowcollars', 'nyloncollars',
			'nylonpastelcollars', 'harness', 'radio', 'bandana', 'bandanaplaid',
            'shadersnewwhite', 'lineartdead', 'tortiepatchesmasks', 
            'medcatherbs', 'lineartdf', 'lightingnew', 'fademask',
            'fadestarclan', 'fadedarkforest'

        ]:
            if 'lineart' in x and game.config['fun']['april_fools']:
                self.spritesheet(f"sprites/aprilfools{x}.png", x)
            else:
                self.spritesheet(f"sprites/{x}.png", x)

        # Line art
        self.make_group('lineart', (0, 0), 'lines')
        self.make_group('shadersnewwhite', (0, 0), 'shaders')
        self.make_group('lightingnew', (0, 0), 'lighting')

        self.make_group('lineartdead', (0, 0), 'lineartdead')
        self.make_group('lineartdf', (0, 0), 'lineartdf')

        # Fading Fog
        for i in range(0, 3):
            self.make_group('fademask', (i, 0), f'fademask{i}')
            self.make_group('fadestarclan', (i, 0), f'fadestarclan{i}')
            self.make_group('fadedarkforest', (i, 0), f'fadedf{i}')

        for a, i in enumerate(
                ['ICE', 'NAVY', 'RAIN', 'SAPPHIRE', 'SEAFOAM', 'SKY', 'STORM', 'TEAL']):
            self.make_group('eyes', (a, 0), f'eyes{i}')
            self.make_group('eyes2', (a, 0), f'eyes2{i}')
        for a, i in enumerate(
                ['ALMOND', 'BEAR', 'CASHEW', 'HAZEL', 'LATTE', 'SPARROW', 'BLACK', 'GULL']):
            self.make_group('eyes', (a, 1), f'eyes{i}')
            self.make_group('eyes2', (a, 1), f'eyes2{i}')
        for a, i in enumerate(
                ['SILVER', 'SMOKE', 'WHITE', 'EMERALD', 'FERN', 'FOREST', 'LEAF', 'LIME']):
            self.make_group('eyes', (a, 2), f'eyes{i}')
            self.make_group('eyes2', (a, 2), f'eyes2{i}')
        for a, i in enumerate(
                ['MINT', 'PEACH', 'PUMPKIN', 'TANGELO', 'AMETHYST', 'LILAC', 'BUBBLEGUM', 'PINK']):
            self.make_group('eyes', (a, 3), f'eyes{i}')
            self.make_group('eyes2', (a, 3), f'eyes2{i}')
        for a, i in enumerate(
                ['ROUGE', 'SCARLET', 'AMBER', 'LEMON', 'PALE', 'SUNBEAM', 'SUNLIGHT', 'WHEAT']):
            self.make_group('eyes', (a, 4), f'eyes{i}')
            self.make_group('eyes2', (a, 4), f'eyes2{i}')
        for a, i in enumerate(
                ['HARVEST', 'VIOLET', 'RUBY', 'DAWN', 'DAYLIGHT', 'TWILIGHT', 'DUSK', 'MIDNIGHT']):
            self.make_group('eyes', (a, 5), f'eyes{i}')
            self.make_group('eyes2', (a, 5), f'eyes2{i}')

        # white patches
        for a, i in enumerate(['FLASH', 'HIGHLIGHTS', 'JACKAL', 'LOCKET', 'SNOWFLAKE', 'SOCKS', 'SPLIT', 'STRIPE', 'TOES', 'TRIM']):
            self.make_group('whitepatches', (a, 0), f'white{i}')
        for a, i in enumerate(['WOLFTICKING', 'BLAZE', 'BLOTCH', 'HALF', 'HEART', 'IRISH', 'MOONRISE', 'MUNSTERLANDER', 'SPITZ', 'STAR']):
            self.make_group('whitepatches', (a, 1), f'white{i}')
        for a, i in enumerate(['SUMMERFOX', 'TICKING', 'URAJIRO', 'BLUETICK', 'EXTREMEPIEBALD', 'LIGHTDALMATIAN', 'PIEBALD', 'TAIL', 'WHITE', 'HEAVYDALMATIAN']):
            self.make_group('whitepatches', (a, 2), f'white{i}')
        for a, i in enumerate(['BACKLEG', 'BEE', 'DAPPLES', 'POINTED', 'SPECKLES', 'DIAMOND', 'HOUND', 'KING', 'HEELER']):
            self.make_group('whitepatches', (a, 3), f'white{i}')

        # colorpoints (special points)
        for a, i in enumerate(['SEPIA', 'MINK', 'POINT', 'CLEAR']):
            self.make_group('specialpoints', (a, 0), f'specialpoint{i}')
        for a, i in enumerate(['HIMALAYAN', 'BEW', 'ALBINO']):
            self.make_group('specialpoints', (a, 1), f'specialpoint{i}')

        # merles
        for a, i in enumerate(['SOLID', 'ARCTIC', 'BRINDLE', 'COLORPOINT', 'GRAYWOLF', 'HUSKY', 'MEXICAN', 'OPHELIA', 'POINTS', 'RUNIC']):
            self.make_group('merle', (a, 0), f'darkmerle{i}')
        for a, i in enumerate(['SABLE', 'SHEPHERD', 'SMOKEY', 'STORMY', 'TIMBER', 'VIBRANT', 'WINTER']):
            self.make_group('merle', (a, 1), f'darkmerle{i}')
        for a, i in enumerate(['HUSKY', 'MEXICAN', 'OPHELIA', 'RUNIC', 'SABLE', 'SMOKEY', 'STORMY', 'TIMBER', 'VIBRANT', 'WINTER']):
            self.make_group('merle', (a, 2), f'redmerle{i}')
        self.make_group('merle', (7, 1), 'redmerleARCTIC')
        self.make_group('merle', (8, 1), 'redmerleCOLORPOINT')
        self.make_group('merle', (9, 1), 'redmerleGRAYWOLF') # these 3 help the sheet fit, but they had to be put on darkmerle's row
        for a, i in enumerate(['DARKDAPPLE', 'SHADOWSNEAK', 'STORMSONG', 'BRINDLECLOUD', 'DAPPLEPELT', 'DAYSKY', 'WILLOWLEAF', 'BRIGHTLEAF', 'SEAFUR', 'SILVERCLAW']):
            self.make_group('merle', (a, 3), f'merle{i}')
        
        # arctic
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('arctic', (a, 0), f'arctic{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('arctic', (a, 1), f'arctic{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('arctic', (a, 2), f'arctic{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('arctic', (a, 3), f'arctic{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('arctic', (a, 4), f'arctic{i}')
		# colorpoint
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('colorpoint', (a, 0), f'colorpoint{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('colorpoint', (a, 1), f'colorpoint{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('colorpoint', (a, 2), f'colorpoint{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('colorpoint', (a, 3), f'colorpoint{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('colorpoint', (a, 4), f'colorpoint{i}')
        # graywolf
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('graywolf', (a, 0), f'graywolf{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('graywolf', (a, 1), f'graywolf{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('graywolf', (a, 2), f'graywolf{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('graywolf', (a, 3), f'graywolf{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('graywolf', (a, 4), f'graywolf{i}')
		# mexican
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('mexican', (a, 0), f'mexican{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('mexican', (a, 1), f'mexican{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('mexican', (a, 2), f'mexican{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('mexican', (a, 3), f'mexican{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('mexican', (a, 4), f'mexican{i}')
		# ophelia
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('ophelia', (a, 0), f'ophelia{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('ophelia', (a, 1), f'ophelia{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('ophelia', (a, 2), f'ophelia{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('ophelia', (a, 3), f'ophelia{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('ophelia', (a, 4), f'ophelia{i}')
		# runic
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('runic', (a, 0), f'runic{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('runic', (a, 1), f'runic{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('runic', (a, 2), f'runic{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('runic', (a, 3), f'runic{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('runic', (a, 4), f'runic{i}')
		# semisolid
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('semisolid', (a, 0), f'semisolid{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('semisolid', (a, 1), f'semisolid{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('semisolid', (a, 2), f'semisolid{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('semisolid', (a, 3), f'semisolid{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('semisolid', (a, 4), f'semisolid{i}')
		# smokey
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('smokey', (a, 0), f'smokey{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('smokey', (a, 1), f'smokey{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('smokey', (a, 2), f'smokey{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('smokey', (a, 3), f'smokey{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('smokey', (a, 4), f'smokey{i}')
		# stormy
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('stormy', (a, 0), f'stormy{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('stormy', (a, 1), f'stormy{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('stormy', (a, 2), f'stormy{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('stormy', (a, 3), f'stormy{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('stormy', (a, 4), f'stormy{i}')
		# timber
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('timber', (a, 0), f'timber{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('timber', (a, 1), f'timber{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('timber', (a, 2), f'timber{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('timber', (a, 3), f'timber{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('timber', (a, 4), f'timber{i}')
		# vibrant
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('vibrant', (a, 0), f'vibrant{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('vibrant', (a, 1), f'vibrant{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('vibrant', (a, 2), f'vibrant{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('vibrant', (a, 3), f'vibrant{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('vibrant', (a, 4), f'vibrant{i}')
		# winter
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('winter', (a, 0), f'winter{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('winter', (a, 1), f'winter{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('winter', (a, 2), f'winter{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('winter', (a, 3), f'winter{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('winter', (a, 4), f'winter{i}')
		# brindle
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('brindle', (a, 0), f'brindle{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('brindle', (a, 1), f'brindle{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('brindle', (a, 2), f'brindle{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('brindle', (a, 3), f'brindle{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('brindle', (a, 4), f'brindle{i}')
		# husky
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('husky', (a, 0), f'husky{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('husky', (a, 1), f'husky{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('husky', (a, 2), f'husky{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('husky', (a, 3), f'husky{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('husky', (a, 4), f'husky{i}')
		# points
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('points', (a, 0), f'points{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('points', (a, 1), f'points{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('points', (a, 2), f'points{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('points', (a, 3), f'points{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('points', (a, 4), f'points{i}')
		# sable
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('sable', (a, 0), f'sable{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('sable', (a, 1), f'sable{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('sable', (a, 2), f'sable{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('sable', (a, 3), f'sable{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('sable', (a, 4), f'sable{i}')
		# shepherd
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('shepherd', (a, 0), f'shepherd{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('shepherd', (a, 1), f'shepherd{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('shepherd', (a, 2), f'shepherd{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('shepherd', (a, 3), f'shepherd{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('shepherd', (a, 4), f'shepherd{i}')
		# solid
        for a, i in enumerate(['SPICE', 'GINGER', 'HONEY', 'FLAXEN', 'CREAM']):
            self.make_group('solid', (a, 0), f'solid{i}')
        for a, i in enumerate(['PEARL', 'MIST', 'ASH', 'STEEL', 'BLACK']):
            self.make_group('solid', (a, 1), f'solid{i}')
        for a, i in enumerate(['CHOCOLATE', 'BLUE', 'LILAC', 'GOLD', 'COPPER']):
            self.make_group('solid', (a, 2), f'solid{i}')
        for a, i in enumerate(['BRASS', 'SILVER', 'ONYX', 'SUNSTONE', 'MOONSTONE']):
            self.make_group('solid', (a, 3), f'solid{i}')
        for a, i in enumerate(['COCOA', 'SPRUCE', 'ISABELLA', 'SUNNY', 'LUNA']):
            self.make_group('solid', (a, 4), f'solid{i}')
            
        # new new torties
        for a, i in enumerate(['CAPE', 'DIPPED', 'HEARTBREAKER', 'INKSPILL', 'MINIMAL', 'PHANTOM']):
            self.make_group('tortiepatchesmasks', (a, 0), f"tortiemask{i}")
        for a, i in enumerate(['PUDDLES', 'REDTAIL', 'SHADOWSTEP', 'SPLIT', 'SPLOTCH', 'WATERFALL']):
            self.make_group('tortiepatchesmasks', (a, 1), f"tortiemask{i}")

        # SKINS
        for a, i in enumerate(['BLACK', 'BLUE', 'BUTTERFLY', 'DUDLEY', 'DUDLEYBLUE', 'DUDLEYLIVER']):
            self.make_group('skin', (a, 0), f"skin{i}")
        for a, i in enumerate(['GRAY', 'ISABELLA', 'LIVER', 'MOCHA', 'PINK', 'SNOWNOSE']):
            self.make_group('skin', (a, 1), f"skin{i}")
        for a, i in enumerate(['SPECKLED']):
            self.make_group('skin', (a, 2), f"skin{i}")

        self.load_scars()

    def load_scars(self):
        """
        Loads scar sprites and puts them into groups.
        """
        for a, i in enumerate(
                ["BEAKLOWER", "BEAKCHEEK", "BELLY", "BLIND", "BOTHBLIND", "BRIDGE", 
                 "BRIGHTHEART", "BURNPAWS", "BURNRUMP", "BURNBELLY", "BURNTAIL", "CATBITE"]):
            self.make_group('scars', (a, 0), f'scars{i}')
        for a, i in enumerate(
                ["CHEEK", "FACE", "FROSTFACE", "FROSTMITT", "FROSTSOCK", "FROSTTAIL",
                 "HALFTAIL", "LEFTBLIND", "LEFTEAR", "LEGBITE", "MANTAIL", "MANLEG"]):
            self.make_group('scars', (a, 1), f'scars{i}')
        for a, i in enumerate(
                ["NECKBITE", "NOEAR", "NOLEFTEAR", "NOPAW", "NORIGHTEAR", "NOTAIL", "ONE", "QUILLCHUNK", "QUILLSCRATCH",
                 "RATBITE", "RIGHTBLIND", "RIGHTEAR"]):
            self.make_group('scars', (a, 2), f'scars{i}')
        for a, i in enumerate(
                ["SIDE", "SNAKE", "SNOUT", "TAILBASE", "TAILSCAR", "THREE", "THROAT", "TOETRAP", "TWO",
                 "GIN"]):
            self.make_group('scars', (a, 3), f'scars{i}')
        # missing parts
        for a, i in enumerate(
                ["BRIGHTHEART", "BURNBELLY", "BURNTAIL", "FROSTTAIL", "HALFTAIL", "LEFTEAR"]):
            self.make_group('missingscars', (a, 0), f'scarsmissing{i}')
        for a, i in enumerate(
                ["NOEAR", "NOLEFTEAR", "NOPAW", "NORIGHTEAR", "NOTAIL", "RIGHTEAR"]):
            self.make_group('missingscars', (a, 1), f'scarsmissing{i}')

        #ACCESSORIES
        for a, i in enumerate([
		"BLUE FEATHERS", "BLUEBELLS", "BLUE BERRIES", "CATMINT", "CICADA WINGS", "DRY HERBS", "FORGET ME NOTS", "HERBS", "HOLLY", "JAY FEATHERS", "JUNIPER"]):
            self.make_group('medcatherbs', (a, 0), f'natural{i}')
        for a, i in enumerate([
		"LAUREL", "LAVENDER", "MAPLE LEAF", "MAPLE SEED", "MOTH WINGS", "NETTLE", "OAK LEAVES", "PETALS", "POPPY", "RED FEATHERS", "RYE STALK"]):
            self.make_group('medcatherbs', (a, 1), f'natural{i}')
        for a, i in enumerate([
		"BLACK EYED SUSANS", "CROW FEATHERS", "DOVE FEATHERS", "GOLD HERBS", "IVY", "MARIGOLD", "PURPLE PETALS", "ROSE", "SAKURA", "SUNFLOWER", "WHITE ROSE"]):
            self.make_group('medcatherbs', (a, 2), f'natural{i}')
		
        for a, i in enumerate(["BLACK", "BLUE", "CRIMSON", "CYAN", "GREEN"]):
            self.make_group('collars', (a, 0), f'collars{i}')
        for a, i in enumerate(["INDIGO", "LIME", "MULTI", "PINK", "PURPLE"]):
            self.make_group('collars', (a, 1), f'collars{i}')
        for a, i in enumerate(["RAINBOW", "RED", "SPIKES", "WHITE", "YELLOW"]):
            self.make_group('collars', (a, 2), f'collars{i}')
			
        for a, i in enumerate(["BELLBLACK", "BELLBLUE", "BELLCRIMSON", "BELLCYAN", "BELLGREEN"]):
            self.make_group('bellcollars', (a, 0), f'collars{i}')
        for a, i in enumerate(["BELLINDIGO", "BELLLIME", "BELLMULTI", "BELLPINK", "BELLPURPLE"]):
            self.make_group('bellcollars', (a, 1), f'collars{i}')
        for a, i in enumerate(["BELLRAINBOW", "BELLRED", "BELLSPIKES", "BELLWHITE", "BELLYELLOW"]):
            self.make_group('bellcollars', (a, 2), f'collars{i}')
			
        for a, i in enumerate(["BOWBLACK", "BOWBLUE", "BOWCRIMSON", "BOWCYAN", "BOWGREEN"]):
            self.make_group('bowcollars', (a, 0), f'collars{i}')
        for a, i in enumerate(["BOWINDIGO", "BOWLIME", "BOWMULTI", "BOWPINK", "BOWPURPLE"]):
            self.make_group('bowcollars', (a, 1), f'collars{i}')
        for a, i in enumerate(["BOWRAINBOW", "BOWRED", "BOWSPIKES", "BOWWHITE", "BOWYELLOW"]):
            self.make_group('bowcollars', (a, 2), f'collars{i}')

        for a, i in enumerate(["NYLONBLACK", "NYLONBLUE", "NYLONCRIMSON", "NYLONCYAN", "NYLONGREEN"]):
            self.make_group('nyloncollars', (a, 0), f'collars{i}')
        for a, i in enumerate(["NYLONINDIGO", "NYLONLIME", "NYLONMULTI", "NYLONPINK", "NYLONPURPLE"]):
            self.make_group('nyloncollars', (a, 1), f'collars{i}')
        for a, i in enumerate(["NYLONRAINBOW", "NYLONRED", "NYLONSPIKES", "NYLONWHITE", "NYLONYELLOW"]):
            self.make_group('nyloncollars', (a, 2), f'collars{i}')
		
        for a, i in enumerate(["PASTELNYLONBLACK", "PASTELNYLONBLUE", "PASTELNYLONCRIMSON", "PASTELNYLONCYAN", "PASTELNYLONGREEN"]):
            self.make_group('nylonpastelcollars', (a, 0), f'collars{i}')
        for a, i in enumerate(["PASTELNYLONINDIGO", "PASTELNYLONLIME", "PASTELNYLONMULTI", "PASTELNYLONPINK", "PASTELNYLONPURPLE"]):
            self.make_group('nylonpastelcollars', (a, 1), f'collars{i}')
        for a, i in enumerate(["PASTELNYLONRAINBOW", "PASTELNYLONRED", "PASTELNYLONSPIKES", "PASTELNYLONWHITE", "PASTELNYLONYELLOW"]):
            self.make_group('nylonpastelcollars', (a, 2), f'collars{i}')
			
        for a, i in enumerate(["RADIOBLACK", "RADIOBLUE", "RADIOCRIMSON", "RADIOCYAN", "RADIOGREEN"]):
            self.make_group('radio', (a, 0), f'collars{i}')
        for a, i in enumerate(["RADIOINDIGO", "RADIOLIME", "RADIOMULTI", "RADIOPINK", "RADIOPURPLE"]):
            self.make_group('radio', (a, 1), f'collars{i}')
        for a, i in enumerate(["RADIORAINBOW", "RADIORED", "RADIOSPIKES", "RADIOWHITE", "RADIOYELLOW"]):
            self.make_group('radio', (a, 2), f'collars{i}')
			
        for a, i in enumerate(["HARNESSBLACK", "HARNESSBLUE", "HARNESSCRIMSON", "HARNESSCYAN", "HARNESSGREEN"]):
            self.make_group('harness', (a, 0), f'collars{i}')
        for a, i in enumerate(["HARNESSINDIGO", "HARNESSLIME", "HARNESSMULTI", "HARNESSPINK", "HARNESSPURPLE"]):
            self.make_group('harness', (a, 1), f'collars{i}')
        for a, i in enumerate(["HARNESSRAINBOW", "HARNESSRED", "HARNESSSPIKES", "HARNESSWHITE", "HARNESSYELLOW"]):
            self.make_group('harness', (a, 2), f'collars{i}')

        for a, i in enumerate(["BANDANABLACK", "BANDANABLUE", "BANDANACRIMSON", "BANDANACYAN", "BANDANAGREEN"]):
            self.make_group('bandana', (a, 0), f'collars{i}')
        for a, i in enumerate(["BANDANAINDIGO", "BANDANALIME", "BANDANAMULTI", "BANDANAPINK", "BANDANAPURPLE"]):
            self.make_group('bandana', (a, 1), f'collars{i}')
        for a, i in enumerate(["BANDANARAINBOW", "BANDANARED", "BANDANASPIKES", "BANDANAWHITE", "BANDANAYELLOW"]):
            self.make_group('bandana', (a, 2), f'collars{i}')
			
        for a, i in enumerate(["PLAIDBANDANABLACK", "PLAIDBANDANABLUE", "PLAIDBANDANACRIMSON", "PLAIDBANDANACYAN", "PLAIDBANDANAGREEN"]):
            self.make_group('bandanaplaid', (a, 0), f'collars{i}')
        for a, i in enumerate(["PLAIDBANDANAINDIGO", "PLAIDBANDANALIME", "PLAIDBANDANAMULTI", "PLAIDBANDANAPINK", "PLAIDBANDANAPURPLE"]):
            self.make_group('bandanaplaid', (a, 1), f'collars{i}')
        for a, i in enumerate(["PLAIDBANDANARAINBOW", "PLAIDBANDANARED", "PLAIDBANDANASPIKES", "PLAIDBANDANAWHITE", "PLAIDBANDANAYELLOW"]):
            self.make_group('bandanaplaid', (a, 2), f'collars{i}')

# CREATE INSTANCE 
sprites = Sprites()
