entry = input()
print([(x.lower(), x) if x not in ['?','!', ';', "'", ",", ".", '-'] else ("{",x) for x in entry if not x == ' '])
print(''.join([i[2] for i in sorted([(x.lower(), index, x) if x not in ['?','!', ';', "'", ",", ".", '-'] else ("{", index, x) for index, x in enumerate(entry) if not x == ' '])]))