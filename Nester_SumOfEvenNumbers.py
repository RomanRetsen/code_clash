random_numbers = input("Input 10 space-seperated numbers \n>>> ").split()
print(f"All random generated numbers {random_numbers[:10]}")
even_numbers_sum = sum([int(x) for x in random_numbers[:10] if int(x) % 2 == 0])
print(f"The sum of even numbers from the list only  {even_numbers_sum}")









