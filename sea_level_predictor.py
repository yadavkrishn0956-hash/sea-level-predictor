import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np


def draw_plot():
    # Load data
    df = pd.read_csv('epa-sea-level.csv')

    # =====================
    # First regression (all data)
    # =====================
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    result = linregress(x, y)
    years_all = np.arange(1880, 2051)
    sea_level_all = result.slope * years_all + result.intercept

    # =====================
    # Second regression (year >= 2000)
    # =====================
    recent_df = df[df['Year'] >= 2000]

    x_recent = recent_df['Year']
    y_recent = recent_df['CSIRO Adjusted Sea Level']

    result_recent = linregress(x_recent, y_recent)
    years_recent = np.arange(2000, 2051)
    sea_level_recent = result_recent.slope * years_recent + result_recent.intercept

    # =====================
    # Plot
    # =====================
    plt.figure(figsize=(6, 6))
    plt.scatter(x, y)
    plt.plot(years_all, sea_level_all)
    plt.plot(years_recent, sea_level_recent)

    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    plt.savefig('sea_level_plot.png')
    plt.show()
