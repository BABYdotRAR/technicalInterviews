#write a recursive and iterative block to retrieve the N number in the fibonnacci sequence

fibonacci = [0, 1] #dp array to store the calculated fibonnacci series, it starts with the first two elements


def fibonacci_recursive_dp(n):
    already_calculated = len(fibonacci) >= n
    if already_calculated:
        return fibonacci[n-1] #if we already stored the value for n in the fibo array, return it
    #otherwise we calculated and stored it
    fibonacci.append(fibonacci_recursive_dp(n-2) + fibonacci_recursive_dp(n-1))
    return fibonacci[n-1]


def fibonacci_iterative(n):
    second_last = 0
    last = 1
    current = 0
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(3, n+1):
        current = second_last + last
        second_last = last
        last = current
    return current
        
print(fibonacci_recursive_dp(3))
print(fibonacci_iterative(3))