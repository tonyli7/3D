from display import *
from draw import *
from parser import *
from matrix import *
import sys

screen = new_screen()
color = [ 0, 255, 0 ]
edges = new_matrix()
transform = new_matrix()
f=open("script_3d")
my_script=open("script_lol")
if len(sys.argv) == 2:
    f = open(sys.argv[1])

#parse_file( f, edges, transform, screen, color )
parse_file(my_script, edges, transform, screen, color)
f.close()
