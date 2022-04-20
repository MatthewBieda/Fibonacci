def main():
    
    #Naive approach using recursion
    #Fails to solve fib(100)
    #Time complexity (2^n)
    def fib_naive(n):
        if n < 2:
            return n
        
        return fib_naive(n-1) + fib_naive(n-2)

    #Approach using dynamic programming (memoization)
    #Instantly solves fib(100)

    cache = {0: 0, 1: 1}
    def fib_memo(n):
        if n in cache: #Base Case
            return cache[n]
        #Else compute and then cache
        cache[n] = fib_memo(n-1) + fib_memo(n-2) #Recursive Case
        return cache[n]
    
    #Alt approach using dynamic programming (tabulation)
    #Less recursive overhead

    F = [0]*10001
    def fib_tab(n):
        F[n] = 0
        F[1] = 1

        for i in range(2, n+1):
            F[i] = F[i-1] + F[i-2]
        return F[n]


    def tribonacci(signature, desired_length):
    
        # if less than 1, return a blank list
        if desired_length<1:
            return []
        # if n is less than the signature, slice the signature and return a sublist
        if desired_length<len(signature):
            return signature[0:desired_length]
    
        # counter
        count = 0
    
        # copy the signature list as a starting point
        # this syntax creates a shallow copy of a list
        # this is because we don't want to create a link between these two objects
        sequence = signature[:]
    
        # increment
        while count <= desired_length:
            # add up the last 3 items
            add = sum(sequence[count:count+3])
            # append to the new list
            sequence.append(add)
            # increment counter
            count += 1
        
        # return the new list sliced to the specified integer
        return sequence[0:desired_length]

    print(tribonacci([1, 1, 1], 10))
    print(tribonacci([300, 200, 100], 0))
    print(tribonacci([1, 2, 3], 2))


if __name__ == "__main__":
    main()