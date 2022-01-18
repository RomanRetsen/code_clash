def sample():
    n = 0
    def func():
        print("n = ", n)

    def setn(value):
        nonlocal n
        n = value
    def getn():
        return n

    func.setn = setn
    func.getn = getn
    return func

s = sample()
s.setn(4)
s()
print(s.getn())