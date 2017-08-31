# -*- coding: utf-8 -*-
from matplotlib.font_manager import FontManager
import subprocess

fm = FontManager()
mat_fonts = set(f.name for f in fm.ttflist)

output = subprocess.check_output(
    'fc-list :lang=zh -f "%{family}\n"', shell=True)

# f = str(output,encoding='utf-8')
print(mat_fonts)
print(str(output))
print(list(f for f in str(output,encoding='utf-8').split('\n')))
zh_fonts = set(f.split(',', 0)[0] for f in str(output,encoding='utf-8').split('\n'))

available = mat_fonts & zh_fonts

print ('*' * 10)
for f in available:
    print (f)