import math

def drawing_a(w, h):
    #draw hat
    middle = (h + 1) // 2
    counter = 2
    yield "#".center(w, " ")
    for i in range(1, w, 2):
        if counter == middle:
            corrected_i = i if i + 2 <= w else i-1
            # corrected_i = i if i + 2 == w else i + 1 if i + 1 < w else i-1
            yield(("#"*(corrected_i+2)).center(w, " ") )
        else:
            corrected_i = i if i + 2 <= w else i - 1
            yield((" "*corrected_i).center(corrected_i+2, "#").center(w, " "))
        counter += 1
    #drawing legs
    legs = 0 if h - counter < 0 else h - counter
    for y in range(counter, h+1):
        if counter == middle:
            yield("#"*w)
        else:
            yield((" "*(w-2)).center(w, "#"))
        counter += 1

def drawing_b(w, h):
    middle = (h+1) // 2
    counter = 2
    yield ("#"*(w-1)).ljust(w, ' ')

    for i in range(counter, middle):
        yield (' '*(w-2)).center(w, "#")
        counter += 1

    yield ("#"*(w-1)).ljust(w, ' ')
    counter += 1

    for i in range(counter, h):
        yield (' '*(w-2)).center(w, "#")
        counter += 1

    yield ("#"*(w-1)).ljust(w, ' ')

def drawing_c(w, h):
    counter = 2
    yield ("#"*(w-1)).rjust(w, ' ')

    for i in range(counter, h):
        yield '#'.ljust(w, " ")
        counter += 1

    yield ("#"*(w-1)).rjust(w, ' ')

def drawing_d(w, h):
    counter = 2
    yield ("#"*(w-1)).ljust(w, ' ')

    for i in range(counter, h):
        yield (' '*(w-2)).center(w, "#")
        counter += 1

    yield ("#"*(w-1)).ljust(w, ' ')

def drawing_e(w, h):
    middle = (h+1) // 2
    counter = 2
    yield "#"*w

    for i in range(counter, middle):
        yield "#"
        counter += 1

    yield ("#"*(w-1)).ljust(w, ' ')
    counter += 1

    for i in range(counter, h):
        yield "#"
        counter += 1

    yield "#"*w

def drawing_f(w, h):
    middle = (h+1) // 2
    counter = 2
    yield "#"*w

    for i in range(counter, middle):
        yield "#".ljust(w, " ")
        counter += 1

    yield ("#"*(w-1)).ljust(w, " ")
    counter += 1

    for i in range(counter, h+1):
        yield "#".ljust(w, " ")
        counter += 1

def drawing_g(w, h):
    middle = (h + 1) // 2
    counter = 2
    yield ("#"*(w-1)).rjust(w, ' ')

    for i in range(counter, middle):
        yield '#'
        counter += 1

    for i in range(counter, h):
        yield (' '*(w-2)).center(w, '#')
        counter += 1

    yield ("#"*(w-1)).rjust(w, ' ')

def drawing_h(w, h):
    middle = (h + 1) // 2
    counter = 1

    for i in range(counter, middle):
        yield (" " * (w - 2)).center(w, "#")
        counter += 1

    yield "#"*w
    counter += 1

    for i in range(counter, h+1):
        yield (' '*(w-2)).center(w, '#')
        counter += 1

def drawing_i(w, h):
    middle = (h + 1) // 2
    counter = 2

    yield "#"*w

    for i in range(counter, h):
        yield '#'.center(w, ' ')
        counter += 1

    yield  "#"*w

def drawing_j(w, h):
    #draw hat
    middle = (h + 1) // 2
    counter = 1
    # tail_mark = h - ((w+1) // 2) if h / 2 > ((w+1) // 2) else h - ((w+1) // 2) + 1
    tail_mark = h - ((w + 1) // 2)
    yield "##".rjust(w, " ")

    for i in range(counter, tail_mark):
        yield "#".rjust(w, " ")
        counter += 1

    tail_width = w if w % 2 == 1 else w - 1
    for y in range(tail_width, 1, -2):
        yield (" "*(y - 2)).center(y, "#").center(w, " ")
        counter += 1

    yield "#".center(tail_width).center(w, " ")

def drawing_k(w, h):
    #draw hat
    middle = (h + 1) // 2
    counter = 1

    for i in range(1, middle):
        # print(f'w: {w}; i: {i}; counter: {counter}')
        yield (" "*(w - i - 1 if w - i > 1 else 1 )).center(w-i+1 if w - i > 1 else 3 , "#").ljust(w, "#" if counter==1 else " ")
        counter += 1

    yield ("##" if w - i <= 2 else "#" * (w-i-1))
    counter += 1

    for y in range((h+1)-counter, 0, -1):
        yield (" "*(w - y - 1 if w - y > 1 else 1 )).center(w-y+1 if w - y > 1 else 3 , "#").ljust(w, "#" if counter==h else " ")
        counter += 1


for i in drawing_k(3, 5):
    print(i)
w,h = map(int, input().split())
coding_char = {"A":drawing_a, "B":drawing_b}
entered_string = [coding_char[x](w, h) for x in input()]
print(f'entered_string ', entered_string)

printing_line = []
for _ in range(h):
    printing_line.clear()
    for i in entered_string:
        printing_line.append(next(i))
    print(' '.join(printing_line))

