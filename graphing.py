from plotly.graph_objs import *
import pandas as pd
import plotly.offline as py
py.init_notebook_mode(connected=True)
import matplotlib.pyplot as plt
import plotly.graph_objs as go

def getMonthlyData_Years(data):
    months = pd.DataFrame(columns=["Month", "Num"])
    months["Month"] = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    months["Num"] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    yearlyMeanScore = data.groupby(["Year", "Month"])["compound_score"].agg(["mean", "count", "std"]).reset_index()
    temp = months.merge(yearlyMeanScore, how="outer", on="Month")
    dataFinal = temp.sort_values(["Year", "Num"])
    dataFinal = dataFinal[dataFinal["Year"] != 2009]
    layout = Layout({
        'title':"Monthly Sentiment Analysis by Year",
        'xaxis':{'title':'Month'},
        #xaxis also takes in a dictionary, just like layout does
        'yaxis':{'title':'Mean Compound Score'}
    })
    split_traces = [] 

    for year in dataFinal.Year.unique():
        split_traces.append(
            Scatter({
                'x':dataFinal["Month"][dataFinal.Year == year],
                'y':dataFinal["mean"][dataFinal.Year == year],
                'mode':'lines',
                'name':year
            })
        )

    split_fig = Figure(data = split_traces, layout = layout)
    py.iplot(split_fig)
    

def getGroupChart(messages, timeline):
    annualMessScore = messages.groupby(["Year"])["compound_score"].agg(["mean","std","count"]).reset_index()
    annualTimeScore = timeline.groupby(["Year"])["compound_score"].agg(["mean","std","count"]).reset_index()
    annualTimeScore["height_err"] = (2 * (annualTimeScore["std"] / (annualTimeScore["count"] ** 0.5)))
    annualMessScore["height_err"] = (2 * (annualMessScore["std"] / (annualMessScore["count"] ** 0.5)))
    trace1 = go.Bar(
            x=annualMessScore.Year,
            y=annualMessScore["mean"],
            marker=dict(
                color='#add8e6'
            ),
            name='Messages',
            error_y=dict(
                type='data',
                array=annualMessScore["height_err"],
                visible=True
            )
        )


    trace2 = go.Bar(
                x=annualTimeScore.Year,
                y=annualTimeScore["mean"],
                marker=dict(
                    color='#FFA500'
                ),
                name='Timeline',
                error_y=dict(
                    type='data',
                    array=annualTimeScore["height_err"],
                    visible=True
                )
            )
    data = [trace1, trace2]

    layout = go.Layout(
        barmode='group'
    )

    fig = go.Figure(data=data, layout=layout)
    py.iplot(fig, filename='grouped-bar')

def getDropDownChart(messages, timeline):
    x_months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    x_days = [1, 2,3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    x_years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017]

    y_year_mes = messages.groupby("Year")["compound_score"].mean()
    y_month_mes = messages.groupby("Month")["compound_score"].mean()
    y_day_mes = messages.groupby("Day")["compound_score"].mean()

    y_year_time = timeline.groupby("Year")["compound_score"].mean()
    y_month_time = timeline.groupby("Month")["compound_score"].mean()
    y_day_time = timeline.groupby("Day")["compound_score"].mean()

    trace1_messages_year = Scatter(
        x=x_years, y=y_year_mes,
        line=Line(
            color='#3b5998',
            width=3
        ),
        name='Messages-Year',
        visible=True
    )

    trace1_timeline_year = Scatter(
        x=x_years, y=y_year_time,
        line=Line(
            color='#FFA500',
            width=3
        ),
        name='Timeline-Year',
        visible=True
    )


    trace2_messages_month = Scatter(
        x=x_months, y=y_month_mes,
        line=Line(
            color='#3b5998',
            width=3
        ),
        name='Messages-Month',
        visible=False
    )

    trace2_timeline_month = Scatter(
        x=x_months, y=y_month_time,
        line=Line(
            color='#FFA500',
            width=3
        ),
        name='Timeline-Month',
        visible=False
    )

    trace3_messages_day = Scatter(
        x=x_days, y=y_day_mes,
        line=Line(
            color='#3b5998',
            width=3
        ),
        name='Messages-Day',
        visible=False
    )

    trace3_timeline_day = Scatter(
        x=x_days, y=y_day_time,
        line=Line(
            color='#FFA500',
            width=3
        ),
        name='Timeline-Day',
        visible=False
    )

    data = Data([trace1_messages_year, trace1_timeline_year, trace2_messages_month, trace2_timeline_month, trace3_messages_day, trace3_timeline_day])
    layout = Layout(
        title='Messages Sentiment Analysis',
        updatemenus=list([
            dict(
                x=-0.05,
                y=1,
                yanchor='top',
                buttons=list([
                    dict(
                        args=['visible', [True, True, False, False, False, False]],
                        label='Year',
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, True, True, False, False]],
                        label='Month',
                        method='restyle'
                    ),
                    dict(
                        args=['visible', [False, False, False, False, True, True]],
                        label='Day',
                        method='restyle'
                    )
                ]),
            )
        ]),
    )
    fig = Figure(data=data, layout=layout)
    py.iplot(fig)