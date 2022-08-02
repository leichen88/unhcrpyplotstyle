# unhcrpyplotstyle
The `unhcrpyplotstyle` package provides Matplotlib styles following [UNHCR Data Visualization Guidelines](https://www.unhcr.org/brand/wp-content/uploads/sites/89/2021/11/UNHCR_Data_Visualization_Guidelines.pdf) which ensures plots are professional and brand–compliant. The porpose of this package is to ease and speed up the chart creation process using Matplotlib custom stylesheets. 

## Getting started
The easiest way to install `unhcrpyplostyle` package is by using `pip`:

```bash
# to install the lastest PyPI release
pip install unhcrpyplotstyle

# to install the latest Github commit
pip install git+https://github.com/leichen88/unhcrpyplotstyle
```

The pip installation will automatically download and store all Matplotlib custom style files (*.mplstyle) in the appropriate local directory of your computer.

## Use the styles
`unhcrpyplotstyle` is the base style of this package. It provides the basic style to the chart elements such as color, font, fontsize, and position. To use the style you can simply call it after importing `matplotlib` library.

```python
import matplotlib.pyplot as plt
plt.style.use('unhcrpyplotstyle')
```

Once the base style is used then you can add a specific style related to the type of chart that you want to use by simply combining two styles together:

```python
import matplotlib.pyplot as plt
plt.style.use('unhcrpyplotstyle','column')
```

In this case, the`column`style will add some of the parameters to the base style `unhcrpyplostyle` in order to align all styles of chart elements with a standard UNHCR style column chart.

See the full list of styles based on chart types below:
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
- `map`
- `pie`
- `population_pyramid`
- `scatterplot`
- `slope`
- `streamgraph`
- `treemap`

## Example
The charts with `unhcrpyplotstyle` + `column` styles:

<img src="https://raw.githubusercontent.com/leichen88/unhcrpyplotstyle/main/example/python_column_chart-1.svg" width="700">
Find code example for column chart [here](https://dataviz.unhcr.org/tools/python/python_column_chart.html).

<img src="https://raw.githubusercontent.com/leichen88/unhcrpyplotstyle/main/example/python_grouped_column_chart-1.svg" width="700">
Find code example for grouped column chart [here](https://dataviz.unhcr.org/tools/python/python_grouped_column_chart.html).

<img src="https://raw.githubusercontent.com/leichen88/unhcrpyplotstyle/main/example/python_stacked_column_chart-1.svg" width="700">
Find code example for stacked column chart [here](https://dataviz.unhcr.org/tools/python/python_stacked_column_chart.html).

<img src="https://raw.githubusercontent.com/leichen88/unhcrpyplotstyle/main/example/python_100perstackedcolumn-1.svg" width="700">
Find code example for 100% stacked column chart [here](https://dataviz.unhcr.org/tools/python/python_100perc_stacked_column_chart.html).


The charts with `unhcrpyplotstyle` + `bar` styles:


The charts with `unhcrpyplotstyle` + `bubble` styles:
