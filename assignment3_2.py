while True:
    try:
        n = int(input("n: "))
        break
    except ValueError:
        print("invalid integer")
    
def recursion(list,n,current = ""):
    if n == 0:
        print(current)
        return

    for i in list:
        recursion(list,n - 1,current + i)
        



list = ["a","b","c"]
recursion(list,n)

