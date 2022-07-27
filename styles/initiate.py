import matplotlib.pyplot as plt
from matplotlib import rcParams
import os
import matplotlib

here=os.path.abspath(__file__).replace("initiate.py","")

plt.style.use(os.path.join(here, 'unhcrpyplotstyle.mplstyle'))

#override the harsh RGB colors
newc = dict(
        blue='#0072BC',
        white= '#FFFFFF',
        black= '#000000',
        yellow= '#FAEB00',
        grey= '#666666',
        navy= '#18375F',
        green= '#00B398',
        red= '#EF4A60',
        lightblue= '#DCE9FF',
        mediumblue= '#8EBEFF',
        darkblue= '#044F85',
        lightgrey= '#E6E6E6',
        mediumgrey= '#CCCCCC',
        darkgrey= '#222222',
        lightyellow= '#FFF9CB',
        mediumyellow= '#FFF483',
        darkyellow= '#E1CC0D',
)

for key in newc.keys():
    matplotlib.colors.ColorConverter.colors[key] = newc[key]