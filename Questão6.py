primos = []
num = 2
while True:
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primos.append(num)
    if len(primos) == 100:
        break
    num += 1
print(primos)
