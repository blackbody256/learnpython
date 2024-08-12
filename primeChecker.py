check_prime = [26,39,51,53,57,79,85]

for num in check_prime:
    if num == 2:
        print(num,"is a prime number")
        continue
    for i in range(2,num):
        if num % i == 0:
            print(num,"is not a prime number, because it is divisible by",i)
            break
    else:
        print(num,"is a prime number")  