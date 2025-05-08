import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle, Circle, Wedge, Polygon
import numpy as np
from tkinter import *
from enum import Enum

from Object import ICCompositeFigure

from Forms import ICPoint2D
from Forms import ICCircle
from Forms import ICSemicircle
from Forms import ICQuadrant
from Forms import ICRectangle
from Forms import ICTriangle


class Color(Enum):
    gray = "#5e5c64"
    light_gray = "#868687"
    dark_blue = "#18304a"
    light_blue = "#0251a1"
    aqua_blue = "#033f70"
    white = "#e8e8ed"
    black = "#000000"