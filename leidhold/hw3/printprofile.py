import cProfile
import re
import pstats
from pstats import SortKey
#cProfile.run('re.compile("hw2")', 'output_1000')

p = pstats.Stats('output_original')
p.strip_dirs().sort_stats(SortKey.TIME).print_stats(60)