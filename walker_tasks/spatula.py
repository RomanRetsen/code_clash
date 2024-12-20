'''
Try a spatula
def pancake_scramble(text):
Analogous to lipping a stack of pancakes by sticking a spatula inside the stack and lipping over the
stack of pancakes resting on top of that spatula, a pancake lip of order k performed for the text
string reverses the pre ix of irst k characters and keeps the rest of the string as it were. For
example, the pancake lip of order 2 performed on the string 'ilkka' would produce the string
'likka'. The pancake lip of order 3 performed on the same string would produce 'klika'.
A pancake scramble, as de ined in the excellent Wolfram Challenges programming problems site,
consists of the sequence of pancake lips of order 2, 3, ... , n performed in this exact sequence for the
given n-character text string. For example, the pancake scramble done to the string 'ilkka'
would step through the intermediate results 'likka', 'kilka', 'klika' and 'akilk'. This
function should compute the pancake scramble of its parameter text string.
text Expected result
'hello world' 'drwolhel ol'
'ilkka' 'akilk'
'pancake' 'eanpack'
'abcdefghijklmnopqrstuvwxyz' 'zxvtrpnljhfdbacegikmoqsuwy'
'this is the best of the
enterprising rear' 're nsrrteetf sbets ithsi h
eto h nepiigra'
For those of you who are interested in this sort of stuff, the follow-up question "How many times
you need to pancake scramble the given string to get back the original string?" is also educational,
especially once the strings get so long that the answer needs to be computed analytically (note that
the answer depends only on the length of the string but not the content, as long as all characters are
distnct) instead of actually performing these scrambles until the original string appears. A more
famous problem of pancake sorting asks for the shortest series of pancake lips to sort the given list.
'''
def pancake_scramble(text):
    the_list = list(text)
    for i in range(2, len(text) + 1):
        start_temp = list(reversed(the_list[:i]))
        end_temp = the_list[i:]
        the_list.clear()
        the_list = start_temp + end_temp
    return "".join(the_list)

print(pancake_scramble(input()))