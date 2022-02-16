def test_dict(the_dict):
    the_dict[1] = 1
    print(the_dict)

the_dict = {x:y for x, y in enumerate("abc")}
print(f"pre {the_dict}")
test_dict(the_dict.items())
print(f"post {the_dict}")
