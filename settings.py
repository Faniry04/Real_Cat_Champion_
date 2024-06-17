from pygame.math import *

#différents  paramaètres pour la taille de l'écran d'affichage
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
#Taille de chauqe Tile de la map tiled
TILE_SIZE = 64

#dictionnaire pour l'ordre d'affichage de chaque sprite
LAYERS = {
	'water': 0,
	'ground': 1,
	'forest grass':2,
	'outside decorations': 3,
	'fence': 5,
	'main': 6,
	'building': 7,
	'dialogue' : 8,
	'screen' : 9,
	'combat_cat': 10,
	'text' : 11,
	'victory_screen' : 12,
	'win_text' : 13
}
