import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'], index_col='date')

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) & 
    (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(15, 5))

    ax.plot(df)  # Plot the data using the index (date column)

    ax.set_title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    ax.set_xlabel('Date')
    ax.set_ylabel('Page Views')

    # Set date format on x-axis (using df.index for correct handling)
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))

    # Rotate date labels for better readability
    plt.xticks(rotation=45)

    plt.tight_layout()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = pd.DataFrame()
    df_bar['date'] = df['date']
    df_bar['year'] = df['date'].dt.year  # Add a 'year' column based on date
    df_bar['month'] = df['date'].dt.month_name()  # Add a 'month' column with month names

    # Resample data by year and month, averaging daily page views
    monthly_averages = df_bar.groupby(['date'.dt.year, 'month'])['value'].mean()

    # Unstack to create a DataFrame suitable for bar plot
    monthly_averages_unstacked = monthly_averages.unstack()

    fig, ax = plt.subplots(figsize=(10, 6))  # Create a figure and axes
    monthly_averages_unstacked.plot(kind='bar', colormap='tab20', ax=ax)  # Plot bars
    ax.set_title('Months')
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months', loc='upper left', bbox_to_anchor=(1, 1))  # Add legend with title

    # Rotate x-axis labels for better readability
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)

    fig, ax = plt.subplots()
    ax.plot(df)
    plt.show()



    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
