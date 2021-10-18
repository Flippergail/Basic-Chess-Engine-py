# importing packages
from main import eval_moves
import pygame as pyg

WIDTH = HEIGHT = 512
DIMENSION = 8
SO_SIZE = HEIGHT // DIMENSION
MAX_FPS = 15
IMAGES = {}

def loadImages():
    IM