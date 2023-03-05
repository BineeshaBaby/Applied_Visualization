# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 01:48:27 2023

@author: BINEESHA BABY - 22023287
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Read the inflation data from the Excel file into a pandas DataFrame
inflation_df = pd.read_excel("D:/inflation and consumer prices.xls", skiprows=3)

# Read the unemployment data from the Excel file into a pandas DataFrame
unemployment_df = pd.read_excel("D:/unemployment India.xls", skiprows=3)

# Read the labour force participation data from the Excel file into a pandas DataFrame
labour_force_df = pd.read_excel("D:/labour force participation.xls", skiprows=3)

# Print the DataFrame to the console
print(inflation_df)

# Sort the inflation DataFrame in descending order based on the inflation rate in 2021
sorted_inflation_df = inflation_df.sort_values(by="2021", ascending=False)

# Define a function to generate a visualization graph using the specified parameters
def visualize_data(x_values, y_values, x_label, y_label, title, kind, legend=None):
    """
    Plot a visualization graph using the specified parameters.

    Parameters:
    x_values (list or array): The values for the x-axis.
    y_values (list or array): The values for the y-axis.
    x_label (str): The label for the x-axis.
    y_label (str): The label for the y-axis.
    title (str): The title of the graph.
    kind (str): The type of plot to generate (bar or multiple_line).
    legend (list or None): The legend labels for the plot (only for kind='multiple_line').

    Returns:
    None
    """
    if kind == "multiple_line":
        # Create a figure and axis object
        fig, ax = plt.subplots()

        # Plot each line with a linewidth of 2
        for y, label in zip(y_values, legend):
            ax.plot(x_values, y, label=label, linewidth=3)

        # Add a legend and labels
        ax.legend()
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title, fontweight="bold")

        # Display the plot
        plt.show()


# Call the visualize_data function to plot a multiple line graph of the top 5 countries with highest inflation rates
visualize_data(
    x_values=sorted_inflation_df["Country Name"].head(5),
    y_values=[sorted_inflation_df["2021"].head(5), sorted_inflation_df["2020"].head(5), sorted_inflation_df["2019"].head(5)],
    x_label="Country Name",
    y_label="Inflation Rate",
    title="Top 5 Countries with Highest Inflation Rates (2019-2021)",
    kind="multiple_line",
    legend=["2021", "2020", "2019"]
)


def plot_stacked_bar(data, x_col, y_cols, x_label, y_label, title):
    """
    Plot a stacked bar chart using the specified parameters.

    Parameters:
    data (pd.DataFrame): The data to plot.
    x_col (str): The column name to use for the x-axis.
    y_cols (list): The column names to use for the y-axis.
    x_label (str): The label for the x-axis.
    y_label (str): The label for the y-axis.
    title (str): The title of the graph.

    Returns:
    None
    """
    # Set the index to the x column
    data.set_index(x_col, inplace=True)

    # Transpose the data to make it easier to plot
    data_transposed = data[y_cols].T

    # Create the stacked bar plot
    data_transposed.plot(kind='bar', stacked=True, figsize=(10,6),edgecolor='none')
    
    # Set a rounded edge for the bars
    for i, patch in enumerate(ax.patches):
        
        # Calculate the x, y, and width of each bar
        x = patch.get_x()
        y = patch.get_y()
        width = patch.get_width()
        
        # Set the rounding value
        rounding = 0.1
        
        # Set the coordinates for the rounding
        x_left = x + width*rounding
        x_right = x + width*(1-rounding)
        y_bottom = y + width*rounding
        y_top = y + patch.get_height() - width*rounding
        
        # Create a Path object for the bar with rounded edges
        bar_path = plt.Path([(x_left, y_bottom),
                            (x_right, y_bottom),
                            (x_right, y_top),
                            (x_left, y_top),
                            (x_left, y_bottom)])
       
        # Set the path for the bar
        patch.set_path(bar_path)
       
        # Set the facecolor for the bar
        patch.set_facecolor(ax.get_legend().legendHandles[i].get_facecolor())
   
    # Add labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(title, fontweight='bold')
    
    # Display the plot
    plt.show()

# Sort the data by country name
sorted_inflation = inflation_df.sort_values(by='Country Name', ascending=True)

# Select the columns to use for the plot
cols_to_plot = ['Country Name', '2021', '2020', '2019']

# Create a figure and axis object
fig, ax = plt.subplots(figsize=(10,6))

# Close the extra figure
plt.close()

# Call the visualize_stacked_bar function to plot a stacked bar chart
plot_stacked_bar(
    data=sorted_inflation_df.head(5), 
    x_col='Country Name', 
    y_cols=cols_to_plot[1:], 
    x_label='years', 
    y_label='Inflation Rate',
    title='Inflation Rates of Top 5 Countries (2019-2021)'
)


# Second Visualization with unemployment
# Define a function to generate second visualization graph using the specified parameters
def plot_unemployment(country, years, unemployment_percentage):
    """
    Plot a bar chart of the unemployment_percentage in total labour force for a given country over the years.

    Parameters:
    country (str): Name of the country.
    years (list): A list of years to plot unemployment percentage for.
    unemployment_percentage (list): A list of unemployment percentage corresponding to the years.

    Returns:
    None
    """
    # Set the figure size
    plt.figure(figsize=(8, 5))

    # Create a bar plot
    plt.bar(years, unemployment_percentage, linewidth=2, edgecolor='black')

    # Set the title and labels
    plt.title('Unemployment Percentage in Total Labour Force for {}\n'.format(country),
              y=1.05, fontdict={'fontsize': 16, 'fontweight': 'bold'})

    plt.xlabel('India (1995-2020)')
    plt.ylabel('Unemployment Percentage (%)')

    # Add a legend
    plt.legend(['Unemployment Percentage'])

    # Add the unemployment percentages as text on top of the bars
    for i, percentage in enumerate(unemployment_percentage):
        plt.text(i, percentage + 0.5, f'{percentage:.1f}%',
                 horizontalalignment='center', fontsize=10)

    # Get the spines object and set the linewidth
    spines = plt.gca().spines
    spines['top'].set_linewidth(1.5)
    spines['bottom'].set_linewidth(1.5)
    spines['left'].set_linewidth(1.5)
    spines['right'].set_linewidth(1.5)

    # Show the plot
    plt.show()


# Filter the DataFrame to keep rows where the "Country Name" column is equal to "India"
India_df = unemployment_df[unemployment_df["Country Name"] == "India"]

# Extract the years and unemployment rates
years = ['1995', '2000', '2005', '2010', '2015', '2020']
unemployment_percentage = India_df[years].values[0]

# Call the function with the specified arguments
plot_unemployment('India', years, unemployment_percentage)


# third visualization
# Define a function to generate third visualization graph using the specified parameters
def plot_top_n_countries_by_mean_lfp(labour_force_df, top_n):
    """
    Plot a pie chart of the top n countries by mean labour force participation rate.

    Parameters:
    labour_force_df (DataFrame): A DataFrame containing labour force data.
    top_n (int): The number of top countries to plot.

    Returns:
    None
    """
    # Filter the columns and compute the mean labour force participation rate for each country
    filtered_df = labour_force_df[["Country Name"] + list(labour_force_df.columns[4:])]
    mean_lfp_country = filtered_df.select_dtypes(include=np.number).mean(axis=1)

    # Sort the countries by mean labour force participation rate in descending order
    mean_lfp_country_sorted = mean_lfp_country.sort_values(ascending=False)

    # Set the index to the country names
    mean_lfp_country_sorted.index = filtered_df["Country Name"]

    # Select the top n countries with the highest mean labour force participation rates
    top_n_countries = mean_lfp_country_sorted.head(top_n)

    # Create a larger figure object
    plt.figure(figsize=(10, 6))

    # Create a pie chart with percentages and a legend
    plt.pie(top_n_countries, labels=top_n_countries.index, autopct='%1.1f%%')
    plt.legend(title='Countries', loc=(1.05, 0.5))

    # Set the title and show the chart
    plt.title("Top {} Countries by Labour Force Participation Rate".format(
        top_n), fontdict={'fontsize': 16, 'fontweight': 'bold'})
    
    plt.show()
    

# call the function with the desired DataFrame
plot_top_n_countries_by_mean_lfp(labour_force_df, 5)



























