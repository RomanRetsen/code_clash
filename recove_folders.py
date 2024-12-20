"""
Junior did a big mistake. He deleted the FileSystem of his computer.
Now he is left only with the root folder ("/").
Fortunately he has a backup.
However the backup tool is quite basic, and Junior has to re-create by hands all the folders.
Junior has the list of paths of the folders to be restored from back-up.
He wants to know how many folders must be created to achieve the full restore.

Input
Line 1: an Integer N, the number of paths of folders to be restored
N following lines: a string representing the path of a folder to be restored.
Output
Number of folders that must be created
Constraints
Each path is given in the Unix format (e.g. /usr/local/bin), and uses only alphanum characters.
Each path starts with "/" and ends with an alphanum.
Example
Input

1
/usr/bin

Output

2


----------test2

1
/usr/local/bin

3

---------test3

2
/a
/b

2

------------test4
2
/a/b
/b/a

4

------------test5

5
/a/b/c/d/e
/a/b/c/d/e/f
/a/b/c/g
/a/b/c/h
/a/b/c/m/h/a/b

12

-----------------------------------
"""
database = {}
folder_counter = 0
n = int(input())
for i in range(n):
    path = input().split("/")
    value_in = database
    for folder in path[1:]:
        if not folder in value_in.keys():
            value_in[folder] = {}
            folder_counter += 1
        value_in = value_in[folder]

print(folder_counter)


"""
#other guy's solution
n = int(input())
asd=[]
for i in range(n):
    path = input()
    print(path.split('/'), file=sys.stderr)
    s="/"
    for j in path.split('/'):
        s+=j
        if s not in asd and j != '':
            asd.append(s)

print(len(asd))
"""