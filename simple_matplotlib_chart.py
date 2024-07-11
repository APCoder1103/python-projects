# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 14:32:11 2024

@author: Paulr
"""

# This program displays a simple line graph.
import matplotlib.pyplot as plt

def main():
    # Create lists with the X and Y coordinates of each data point.
    x_coords = [0, 1, 2, 3, 4]
    y_coords = [0, 3, 30, 52, 23]

    # Build the line graph.
    plt.plot(x_coords, y_coords)

    # Display the line graph.
    plt.show()

# Call the main function.
if __name__ == '__main__':
    main()

