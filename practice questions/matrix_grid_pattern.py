"""
Fill in the python method such to print below output
def fetch_grid(n):
    raise NotImplemented

print(fetch_grid(5))

1 1 1 1 1
2 4 2 2 2
3 3 9 3 3
4 4 4 16 4
5 5 5 5 25

"""

class NotImplemented(Exception):
    pass

def fetch_grid(n):
    """This function will print matrix up to 5x5 as it implemented in that way"""
    try:
        if n > 5:
            print(f"value of n is {n}")
            raise NotImplemented
        for row in range(1, n+1):
            for i in range(1, n+1):
                if row == i:
                    print(row * i,end=" ")
                else:
                    print(row,end=" ")
            print("\n")
    except:
        print("logic not implemented")

if __name__ == "__main__":
    num = int(input("Enter number : "))
    fetch_grid(num)

'''
Enter number : 5
1 1 1 1 1 

2 4 2 2 2 

3 3 9 3 3 

4 4 4 16 4 

5 5 5 5 25 
'''
