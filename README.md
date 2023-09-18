# unhcrpyplotstyle

[![PyPI version](https://badge.fury.io/py/unhcrpyplotstyle.svg)](https://badge.fury.io/py/unhcrpyplotstyle)

The `unhcrpyplotstyle` package provides Matplotlib styles following the [UNHCR Data Visualization Guidelines](https://www.unhcr.org/brand/wp-content/uploads/sites/89/2021/11/UNHCR_Data_Visualization_Guidelines.pdf), ensuring that charts are professional and brand-compliant. The purpose of this package is to simplify and expedite the chart creation process using Matplotlib custom stylesheets.

## Getting started
The easiest way to install the `unhcrpyplotstyle` package is by using pip:

```bash
# to install the latest PyPI release
pip install unhcrpyplotstyle

# to install the latest Github commit
pip install git+https://github.com/leichen88/unhcrpyplotstyle
```

The pip installation will automatically download and store all Matplotlib custom style files (*.mplstyle) in the appropriate local directory on your computer.

## Use the styles
`unhcrpyplotstyle` is the base style of this package. It provides basic styles for chart elements such as color, font, font size, and position. To use the base style, you can simply call it from your local style directory after importing the `Matplotlib` library.

```python
import matplotlib.pyplot as plt
plt.style.use('unhcrpyplotstyle')
```

Once the base style is applied, you can add a specific style related to the type of chart you want to create by combining two styles together:

```python
import matplotlib.pyplot as plt
plt.style.use('unhcrpyplotstyle','column')
```

In this case, the 'column' style will add some parameters to the base style 'unhcrpyplotstyle' to align all chart element styles with a standard UNHCR-style column chart.

You can find the full list of styles based on chart types below:
- `area`
- `bar`
- `bubble`
- `column`
- `connected_scatterplot`
- `donut`
- `dotplot`
- `heatmap`
- `histogram`
- `line`
- `linecolumn`
- `lollipop`
- `map`
- `pie`
- `population_pyramid`
- `scatterplot`
- `slope`
- `streamgraph`
- `treemap`

## Example
The chart with `unhcrpyplotstyle` + `column` styles:

<img src="https://raw.githubusercontent.com/leichen88/unhcrpyplotstyle/main/example/python_column_chart-1.svg" width="500">

_Find code example for column chart [here](https://dataviz.unhcr.org/tools/python/python_column_chart.html)._


The chart with `unhcrpyplotstyle` + `bar` styles:

<img src="https://raw.githubusercontent.com/leichen88/unhcrpyplotstyle/main/example/python_bar_chart-1.svg" width="500">

_Find code example for bar chart [here](https://dataviz.unhcr.org/tools/python/python_bar_chart.html)._


The chart with `unhcrpyplotstyle` + `line` styles:

<img src="https://raw.githubusercontent.com/leichen88/unhcrpyplotstyle/main/example/python_line_chart-1.svg" width="500">

_Find code example for line chart [here](https://dataviz.unhcr.org/tools/python/python_line_chart.html)._


The chart with `unhcrpyplotstyle` + `scatterplot` styles:

<img src="https://raw.githubusercontent.com/leichen88/unhcrpyplotstyle/main/example/python_scatterplot-1.svg" width="500">

_Find code example for scatterplot [here](https://dataviz.unhcr.org/tools/python/python_scatterplot.html)._

