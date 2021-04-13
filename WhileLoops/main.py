"""i = 100
while i >= 0:
    if i == 0:
        print("Boom!") 
    else:
        print(i)
    i-=1
"""


for i in range(100, -1, -1):
    if i == 0:
        print("Boom!") 
    else:
        print(i)

input()