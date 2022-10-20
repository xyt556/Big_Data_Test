# View more python tutorials on my Youtube and Youku channel!!!

# Youtube video tutorial: https://www.youtube.com/channel/UCdyjiB5H8Pu7aDTNVXTTpcg
# Youku video tutorial: http://i.youku.com/pythontutorial
"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
from __future__ import print_function
import pandas as pd
import os
# read from
data = pd.read_csv('student.csv')
print(data)

# save to
print(os.stat('student.csv').st_size / (1024 * 1024))
data.to_pickle('student.pickle')
print(os.stat('student.pickle').st_size / (1024 * 1024))