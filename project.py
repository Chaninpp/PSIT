import pygal                                                       # First import pygal
from pygal.style import Style
from pygal.style import DefaultStyle
from pygal.style import NeonStyle
from math import cos
xy_chart = pygal.XY()
xy_chart.title = 'XY Cosinus'
#xy_chart.add('x = cos(y)', [(cos(x / 10.), x / 10.) for x in range(-50, 50, 5)])
#xy_chart.add('y = cos(x)', [(x / 10., cos(x / 10.)) for x in range(-50, 50, 5)])
xy_chart.add('xy',  [(10, 10), (10, 50), (90, 50), (90, 10), (10, 10)])
xy_chart.add('pq',  [(70, 20), (70, 70), (130,70), (130, 20), (70, 20)])
xy_chart.render_to_file('bar_chart.svg')                        # Save the svg to a file