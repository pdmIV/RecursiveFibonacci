# This is a recursive algorithm, meaning that the function is called within itself
def Fibonacci(n):
  if n <= 1:
    return n
  else:
    return (Fibonacci(n-1) + Fibonacci(n-2))
  
# Asks the user for the length of the sequence, then prints the result of our algo
while True:
    n_terms = int(input("Length of Fibonacci sequence: "))
    for i in range(n_terms):
        print(Fibonacci(i))