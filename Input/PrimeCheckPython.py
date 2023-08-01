def primeTest (num):
    num = int(num)
    if num > 1:
        for i in range (2,num):
            if (num % i) ==0:
                isPrime = "{0} is not a prime number.".format(num)
                break
            else:
                isPrime = "{0} is a prime number.".format(num)
    else:
        isPrime = "{0} is not a prime number.".format(num)
        
    return isPrime
