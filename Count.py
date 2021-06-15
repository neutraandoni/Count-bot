import time

# n = start number

n = 0

# b = the number we are constantly adding

b = 1

# e = ending number

e = 9000





while True:
    print(n)
    n = n + b
    if(n == e):
        print(n)
        time.sleep(1000)
    