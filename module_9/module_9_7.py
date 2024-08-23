def is_prime(func):
    def wrapper(*args, **kwargs):
        accepted = func(*args, **kwargs)

        if accepted > 1:
            for i in range(2, int(accepted ** 0.5) + 1):
                if accepted % i == 0:
                    print("Составное")
                    break
            else:
                print("Простое")
        else:
            print("Составное")

        return accepted

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)
