word = input()
sol1 = word.find('f')
sol2 = word.rfind('f')
if 'f' not in word:
    print(' ')
elif sol1 == sol2:
    print(sol1)
else:
    print(sol1, sol2)