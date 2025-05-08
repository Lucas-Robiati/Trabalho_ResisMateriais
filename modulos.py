import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.patches import Rectangle, Circle, Wedge, Polygon
import numpy as np
from tkinter import *
from enum import Enum

import Forms
import Object

class Color(Enum):
    gray = "#5e5c64"
    light_gray = "#868687"
    dark_blue = "#18304a"
    light_blue = "#0251a1"
    aqua_blue = "#033f70"
    white = "#e8e8ed"
    black = "#000000"