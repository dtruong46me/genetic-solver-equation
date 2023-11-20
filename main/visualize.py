
import matplotlib.pyplot as plt
import pylab
import os
import sys
from pathlib import Path

path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, path)

class Visualize:

    @staticmethod
    def plot_result(x_result, y_result):
        title_font = {'fontname': 'Consolas', 'size': 9, 'color': '#035B96'}
        tick_font = {'fontname': 'Consolas', 'size': 8, 'color': '#035B96'}
        
        save_path = r"assets/viz/"
        os.makedirs(save_path, exist_ok=True)

        width, height = 369, 276
        dpi = 100

        # Plot for x
        plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)

        plt.plot([i for i in range(1, len(x_result) + 1)], x_result)
        plt.title('The values of \'x\' in each generation', title_font)

        plt.xticks(**tick_font)
        plt.yticks(**tick_font)
        plt.savefig(os.path.join(save_path, 'x.png'))


        # Plot for y
        plt.figure(figsize=(width/dpi, height/dpi), dpi=dpi)

        plt.plot([i for i in range(1, len(x_result) + 1)], y_result)
        plt.title('The values of \'y\' in each generation', title_font)

        plt.xticks(**tick_font)
        plt.yticks(**tick_font)
        plt.savefig(os.path.join(save_path, 'y.png'), bbox_inches='tight', pad_inches=0.1)