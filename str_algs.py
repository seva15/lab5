def rev_str(str):
    str_new=''
    for i in range(len(str), -1, 0, -1):
        str_new += str[i]

str = 'hello, world'

for i in range(1,4):
    print(rev_str(str))