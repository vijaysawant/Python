"""
input = 4
1
1 2
1 2 3
1 2 3 4
1 2 3
1 2
1
"""
def printPattern(col):
    for i in range(0,col):
        for j in range(0,i+1):
            print(f"{j+1} ",end="")
        print("")
    col -= 1
    for i in range(0,col):
        for k in range(i,col):
            print(f"{k-i+1} ",end="")
        print("")

if __name__ == "__main__":
    # col = eval(input("Enter colomn length: "))
    printPattern(4)
"""
    for i in range(0,4):
        for j in range(0,i+1):
            print(f"{j+1} ",end="")
        print("")
    for i in range(0,4):
        for k in range(i,4):
            print(f"{k-i+1} ",end="")
        print("")
"""