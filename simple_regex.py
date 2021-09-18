import re

patter_write = r'write (.*)\.'
patter_times = r'(\d*) times'
commands = input()

result_write = re.search(patter_write, commands)
result_times = re.search(patter_times, commands)
if result_times:
    times = int(result_times.group(1))
else:
    times = 1

if result_write:
    string_to_print = result_write.group(1)
    [print(string_to_print) for _ in range(times)]
else:
    print("Error")