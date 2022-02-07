import altair as alt
from vega_datasets import data

### Article: https://towardsdatascience.com/python-interactive-data-visualization-with-altair-b4c4664308f8

cars = data.cars()
print(cars.columns)
brush = alt.selection_interval()


# mark point with selection option
# and alter non-selected area color to lightgray
def mark_point_selection():
    chart = alt.Chart(cars).mark_point().encode(
                x='Miles_per_Gallon:Q',
                y='Horsepower:Q',
                color=alt.condition(brush,
                                    'Origin:N',
                                    alt.value('lightgray'))
            ).add_selection(
                brush
            )

    return chart


# mark bar chart according to the
# selected area in mark_point
def mark_bar_with_selection():
    chart = alt.Chart(cars).mark_bar().encode(
        y='Origin:N',
        color='Origin:N',
        x='count(Origin):Q'
    ).transform_filter(
        brush
    )

    return chart


if __name__ == '__main__':
    points = mark_point_selection()
    bars = mark_bar_with_selection()

    chart = points & bars

    chart.show()
