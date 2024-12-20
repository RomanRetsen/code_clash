from itertools import groupby
import operator

data = sorted('Taras Grugorovish Shevchenko'.replace(' ', ''))
grouped_data = groupby(data)
convert_data = [(key, len(list(value))) for key, value in grouped_data] # must convert _grouper into list
print(convert_data)
for key, value in sorted(convert_data, key=lambda x:x[1], reverse=True):
    print(key, value, end='\t')
print()
print(list(groupby(data)))
