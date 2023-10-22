def c2f(celsius):
    fahrenheit = 9 * celsius / 5 + 32
    return fahrenheit


print(c2f(0), c2f(1000), c2f(-40))


def f2c(fahrenheit):
    celsius = 5 * (fahrenheit - 32)/9
    return celsius


print(c2f(f2c(20)))
