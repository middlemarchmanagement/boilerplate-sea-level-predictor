import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Assign columns to variables for clarity
    x = df['Year']
    y = df['CSIRO Adjusted Sea Level']

    # Create scatter plot
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y, label='Original Data', color='blue')

    # --- Create first line of best fit (Using all data) ---
    
    # Get slope and y-intercept for the entire dataset
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(x, y)
    
    # Create an array of years for the prediction line (from min year to 2050)
    # The max_year is 2050 as requested, but the start year should be from the data's minimum year (1880)
    # to show the entire fit.
    x_pred1 = np.arange(x.min(), 2051)
    
    # Calculate the predicted sea level for each year in x_pred1
    y_pred1 = slope1 * x_pred1 + intercept1
    
    # Plot the first line of best fit
    plt.plot(x_pred1, y_pred1, 
             label=f'Fit 1880-{x.max()}', 
             color='red', 
             linestyle='--')
    
    # Prediction for 2050 (for reference, not explicitly asked to be plotted as a point)
    # prediction_2050_all_data = slope1 * 2050 + intercept1

    # --- Create second line of best fit (Using data from year 2000 onwards) ---

    # Filter data from the year 2000
    df_recent = df[df['Year'] >= 2000]
    x_recent = df_recent['Year']
    y_recent = df_recent['CSIRO Adjusted Sea Level']

    # Get slope and y-intercept for the recent data
    slope2, intercept2, r_value2, p_value2, std_err2 = linregress(x_recent, y_recent)
    
    # Create an array of years for the prediction line (from 2000 to 2050)
    x_pred2 = np.arange(2000, 2051)
    
    # Calculate the predicted sea level for each year in x_pred2
    y_pred2 = slope2 * x_pred2 + intercept2
    
    # Plot the second line of best fit
    plt.plot(x_pred2, y_pred2, 
             label=f'Fit 2000-{x.max()}', 
             color='green', 
             linestyle='-')

    # Prediction for 2050 (for reference, not explicitly asked to be plotted as a point)
    # prediction_2050_recent_data = slope2 * 2050 + intercept2

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()
    plt.grid(True, linestyle=':', alpha=0.6)
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()

if __name__ == '__main__':
    draw_plot()
