import altair as alt
import numpy as np
import pandas as pd

from vega_datasets import data


# URL: https://altair-viz.github.io/gallery/index.html#simple-charts ###


def make_bar_chart():
    source = pd.DataFrame({
        'a': list('ABCDEFGHI'),
        'b': [28, 55, 43, 91, 81, 53, 19, 87, 52]
    })

    chart = alt.Chart(source).mark_bar().encode(
        x='a',
        y='b'
    )

    return chart


def make_heatmap():
    # make data to visualize
    # Compute x^2 + y^2 across 2D grid

    x, y = np.meshgrid(range(-5, 6), range(-5, 6))
    z = x ** 2 + y ** 2

    source = pd.DataFrame({
        'x': x.ravel(),
        'y': y.ravel(),
        'z': z.ravel()
    })

    chart = alt.Chart(source).mark_rect().encode(
        x='x:O',
        y='y:O',
        color='z:Q'
    )

    return chart


def make_hist():
    source = pd.read_json(data.movies.url)
    chart = alt.Chart(source).mark_bar().encode(
        alt.X("IMDB_Rating:Q", bin=True),
        y='count()',
    )

    return chart


def make_line():
    x = np.arange(100)
    source = pd.DataFrame({
        'x': x,
        'y': np.sin(x / 5)
    })

    chart = alt.Chart(source).mark_line().encode(
        x='x',
        y='y'
    ).interactive()

    return chart


def make_scatter_plot():
    source = data.cars()
    chart = alt.Chart(source).mark_circle(size=60).encode(
        x='Horsepower',
        y='Miles_per_Gallon',
        color='Origin',
        tooltip=['Name', 'Origin', 'Horsepower', 'Miles_per_Gallon']
    ).interactive()

    return chart


def make_stacked_area():
    source = data.iowa_electricity()

    chart = alt.Chart(source).mark_area().encode(
        x='year:T',
        y='net_generation:Q',
        color='source:N'
    )

    return chart


def make_strip_plot():
    source = data.cars()

    chart = alt.Chart(source).mark_tick().encode(
        x='Horsepower:Q',
        y='Cylinders:O'
    )

    return chart


if __name__ == '__main__':
    # chart = make_bar_chart()
    # chart = make_heatmap()
    # chart = make_hist()
    # chart = make_line()
    # chart = make_scatter_plot()
    # chart = make_stacked_area()
    chart = make_strip_plot()
    chart.show()
