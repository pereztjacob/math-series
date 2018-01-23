def fibonacci(n):
    if(n <= 1):
        return n
    else:
        return(fibonacci(n-1) + fibonacci(n-2))

# n = int(input("n + ?"))
# print(fibonacci(n))

# ////////////////////////////////////////////////////////////////////////////////

def lucas(n):
    if(n <= 0):
        return 2
    elif(n == 1):
        return 1
    else:
        return(lucas(n-1) + lucas(n-2))

# n = int(input("n = ?"))
# print(lucas(n))

# ////////////////////////////////////////////////////////////////////////////////

def sum_series(n, n_one=0, n_two=1):
    if(n <= 0):
        return n_one
    elif(n == 1):
        return 1
    else:
        return(sum_series(n-1, n_one, n_two) + sum_series(n-2, n_one, n_two))

# n = int(input("n = ?"))
# print(sum_series(n, 2, 1))