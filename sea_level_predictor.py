import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from pandas.core.frame import DataFrame
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv("epa-sea-level.csv", float_precision='legacy')

    # Create scatter plot
    plt.scatter(x = "Year", y = "CSIRO Adjusted Sea Level", data = df)

    # Create first line of best fit
    first_line = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    year = np.arange(1880, 2051, dtype = np.dtype('f8'))
    plt.plot(year, (first_line.intercept + first_line.slope * year))
    first_line.intercept + first_line.slope * year

    # Create second line of best fit
    df = df[df["Year"] >= 2000]
    plt.scatter(x = "Year", y = "CSIRO Adjusted Sea Level", data = df)
    second_line = linregress(df["Year"], df["CSIRO Adjusted Sea Level"])
    year = np.arange(2000, 2051)
    plt.plot(year, (second_line.intercept + second_line.slope *year))

    # Add labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()