import altair as alt
# alt.renderers.enable('altair_viewer')
import pandas as pd

### Article: https://towardsdatascience.com/python-interactive-data-visualization-with-altair-b4c4664308f8
### First code ###

data = pd.DataFrame({
    'col-1': list('CCCDDDEEE'),
    'col-2': [2, 7, 4, 1, 2, 6, 8, 4, 7]
})

# 3 components: Chart(data) - Chart, mark - mark_point() and encode - encode()
chart = alt.Chart(data).mark_point().encode(
    x='col-1',
    y='col-2'
).interactive()
chart.show()
