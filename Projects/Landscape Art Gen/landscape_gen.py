import os
import random
from PIL import Image, ImageDraw
import bisect
from colourlovers import clapi
import argparse


parser = argparse.ArgumentParser(description = "2D Landscape Generator")
parser.add_argument("-t", "--theme", type = str, help = "theme for color palette")
args = parser.parse_args()



#midpoint vertical displacement

def midpoint_displacement(start, end, roughness, vertical_displacement=None, num_of_iterations = 16):
    
    """
    returns list of points = [[x_0, y_0], [x_1, y_1],... [x_n, y_n]
    """

    if vertical_displacement is None:
        
        vertical_displacement = (start[1] + end[1]) / 2
        
        #points list is kept sorted from small to big x-value
        
    points = [start, end]
    iteration = 1
    
    while iteration <= num_of_iterations:
        
        #create copy of the state at the beginning of iteration
        #to iterate over original sequence
        
        points_tup = tuple(points)
        
        for i in range(len(points_tup) - 1):
            #calculate x and y midpoints
            
            midpoint = list(map(lambda x: (points_tup[i][x] + points_tup[i + 1][x]) /2, [0, 1]))
            
            #insert displaced midpoint in the current list of points
            bisect.insort(points, midpoint)
            
            #bisect inserts an element in a list so that its order is preserved
            
            #reduce displacement range
            vertical_displacement *= 2 ** (-roughness)
            
            #update iterations
            
            iteration += 1
    return points


def draw_layers(layers, width, height, colour_palette_keyword):
    
    """
    Compute points that conform each of the layers in the landscape
    """
    colour_dict = None
    
    if colour_palette_keyword:
        cl = clapi.ColourLovers()
        palettes = cl.search_palettes(
            request = "top", keywords = colour_palette_keyword, numResults = 15)
        
        palette = palettes[random.choice(range(len(palettes)))]
        
        colour_dict = {
            str(iter): palette.hex_to_rgb()[iter] for iter in range(len(palette.colors))
        }
       
    if colour_dict is None or len(colour_dict.keys()) < len(layers):
        colour_dict = {
            "0": (195, 157, 224),
            "1": (158, 98, 204),
            "2": (130, 79, 138),
            "3": (68, 28, 99),
            "4": (49, 7, 82),
            "5": (23, 3, 38),
            "6": (240, 203, 163)
        }
    else:
        #len(colour_dict) >= # of layers +1 (background color)
        
        if len(colour_dict) < len(layers) +1:
            raise ValueError("Num of colors should be bigger than the num of layers")
            
            
    #create image
    
    landscape = Image.new(
        "RGBA", (width, height), colour_dict[str(len(colour_dict) - 1)])
    landscape_draw = ImageDraw.Draw(landscape)
    
    #draw ellipse
    
    landscape_draw.ellipse((50, 25, 100, 75), fill = (255, 255, 255, 255))
    
    #sample y values of all x in img
    
    final_layers = []
    
    for layer in layers:
        sampled_layer = []
        
        for i in range(len(layer) - 1):
            sampled_layer += [layer[i]]
            
            #if x difference is greater than 1
            
            if layer[i+1][0] - layer[i][0] > 1:
                
                #linearly sample y values in the range x_[i+1] - x_[i]
                #obtain equation of straight ling (y=mx+b) that connects 2 points
                
                m = float(layer[i+1][1] - layer[i][1]) / (layer[i+1][0] - layer[i][0])
                b = layer[i][1] - m * layer[i][0]
                r = lambda x: m * x + b #straight line
                
                for j in range(int(layer[i][0] + 1), int(layer[i + 1][0])):
                    
                    sampled_layer += [[j, r(j)]]
                    
        final_layers += [sampled_layer]
        
    final_layers_enum = enumerate(final_layers)
    
    for final_layer in final_layers_enum:
        
        #traverse all x values in layer
        
        for x in range(len(final_layer[1]) - 1):
            
            #for each x value draw a line from its y value to the bottom
            
            landscape_draw.line(
                (
                    final_layer[1][x][0],
                    height - final_layer[1][x][1],
                    final_layer[1][x][0],
                    height
                ),
                colour_dict[str(final_layer[0])]
            )
    return landscape


def load():
    
    width = 1000 
    height = 500
    
    layer_1 = midpoint_displacement([180, 0], [width, 150], 1.4, 20, 12)
    layer_2 = midpoint_displacement([0, 170], [width, 90], 1.2, 30, 12)
    layer_3 = midpoint_displacement([0, 250], [width, 200], 1, 120, 9)
    layer_4 = midpoint_displacement([0, 300], [width, 250], 0.9, 260, 8)
    
    colour_theme = None
    
    if args.theme:
        
        colour_theme = args.theme
        
    landscape = draw_layers(
        [layer_4, layer_3, layer_2, layer_1], width, height, colour_theme
    )
    
    landscape.save(os.getcwd() + "/generated_imgs/landscape8.png")
    
    
if __name__ == "__main__":
    load()

 
        
        

