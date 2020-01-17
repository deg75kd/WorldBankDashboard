import pandas as pd
import plotly.graph_objs as go

def cleandata(dataset, keepcolumns = ['Country Name', '2014'], value_variables = ['2014']):
    """Clean world bank data for a visualizaiton dashboard

    Keeps data range of dates in keep_columns variable and data for the top 10 economies
    Reorients the columns into a year, country and value
    Saves the results to a csv file

    Args:
        dataset (str): name of the csv data file

    Returns:
        None

    """    
    df = pd.read_csv(dataset, skiprows=4)

    # Keep only the columns of interest (years and country name)
    df = df[keepcolumns]

    regionlist = ['East Asia & Pacific', 'Europe & Central Asia', 'Latin America & Caribbean', 'Middle East & North Africa', 'North America', 'South Asia', 'Sub-Saharan Africa']
    df = df[df['Country Name'].isin(regionlist)]

    # melt year columns  and convert year to date time
    df_melt = df.melt(id_vars='Country Name', value_vars = value_variables)
    df_melt.columns = ['country','year', 'variable']
    df_melt['year'] = df_melt['year'].astype('datetime64[ns]').dt.year

    # output clean csv file
    return df_melt

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

  # first chart plots internet users per 100 from 2000 to 2014
  # as a line chart
    
    graph_one = []
    keepcolumns = [str(x) for x in range(2000, 2015)]
    keepcolumns.insert(0, 'Country Name')
    years = [str(x) for x in range(2000, 2015)]
    df = cleandata('data/API_IT.NET.USER.P2_DS57_en_csv_v2_729213.csv', keepcolumns, years)
    regionlist = df['country'].unique().tolist()
    
    for region in regionlist:
      x_val = df[df['country'] == region]['year'].tolist()
      y_val =  df[df['country'] == region]['variable'].tolist()
      graph_one.append(
          go.Scatter(
          x = x_val,
          y = y_val,
          mode = 'lines',
          name = region
          )
      )

    layout_one = dict(title = 'Internet Users per 100 People, 2000 to 2014',
                xaxis = dict(title = 'Year',
                  autotick=False, tick0=2000, dtick=1),
                yaxis = dict(title = 'Internet Users per 100'),
                )

# second chart plots population for 2014 as a bar chart    
    graph_two = []
    df = cleandata('data/API_SP.POP.TOTL_DS2_en_csv_v2_713131.csv')
    df = df[df['year'] == 2014]

    graph_two.append(
      go.Bar(
      x = df['country'].tolist(),
      y = df['variable'].tolist(),
      )
    )

    layout_two = dict(title = 'Total Population in 2014',
                xaxis = dict(title = 'Region',),
                yaxis = dict(title = 'Population'),
                )


# third chart shows female youth (15-24) illiterate rate vs. female enrollment rate
    graph_three = []
    
    df_illiterate = cleandata('data/API_UIS.LPP.AG15T24_DS12_en_csv_v2_740510.csv')
    df_enrollment = cleandata('data/API_UIS.GTVP.2.GPV.F_DS12_en_csv_v2_742432.csv')
    
    df_illiterate.columns = ['country', 'year', 'illiterate']
    df_enrollment.columns = ['country', 'year', 'enrollment']

    #df_illiterate = df_illiterate.fillna(0)
    #df_enrollment = df_enrollment.fillna(0)
    df_illiterate.dropna(subset=['illiterate'], axis=0, inplace=True)
    df_enrollment.dropna(subset=['enrollment'], axis=0, inplace=True)
    
    df = df_illiterate.merge(df_enrollment, on=['country', 'year'])
    regionlist = df['country'].unique().tolist()
    indicatorlist = ['illiterate', 'enrollment']
    
    for indicator in indicatorlist:
      y_val = df[indicator].tolist()

      graph_three.append(
          go.Bar(
          name = indicator,
          x = regionlist,
          y = y_val
          )
      )

    layout_three = dict(title = 'Female Youth (15-24) Illiterate Rate vs. Female Lower Secondary Enrollment Rate (2014)',
                xaxis = dict(title = 'Region'),
                yaxis = dict(title = 'Rate'),
                barmode='group'
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))

    return figures