import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')

# Clean data
df = df.loc[(df['value']>=df['value'].quantile(0.025)) & (df['value']<=df['value'].quantile(0.975))]
# print(df.shape[0])


def draw_line_plot():
    # Draw line plot
    fig = df.plot.line(figsize=(15,5), color='red', legend=False)
    plt.xlabel('Date')
    plt.ylabel('Page Views')
    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')

    fig = fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = pd.DatetimeIndex(df_bar.index).year
    df_bar['month']=pd.DatetimeIndex(df_bar.index).month_name()

    plt.figure(figsize=(9,6))
    fig=sns.barplot(
        data=df_bar, x='year', y='value', hue='month'
        ,palette='bright',hue_order=['January', 'February', 'March', 'April', 'May', 
                 'June', 'July', 'August', 'September', 'October', 
                 'November', 'December'])


    # Draw bar plot
    fig.set_ylabel('Average Page Views')
    fig.set_xlabel('Years')

    sns.move_legend(fig, "upper left",borderaxespad=0,bbox_to_anchor=(0.01, 0.98))
    fig=fig.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

# def draw_box_plot():
#     # Prepare data for box plots (this part is done!)
#     df_box = df.copy()
#     df_box.reset_index(inplace=True)
#     df_box['year'] = [d.year for d in df_box.date]
#     df_box['month'] = [d.strftime('%b') for d in df_box.date]

#     # Draw box plots (using Seaborn)





#     # Save image and return fig (don't change this part)
#     fig.savefig('box_plot.png')
#     return fig
