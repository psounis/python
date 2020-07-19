def factory_power(power):
    def nth_power(number):
        return number ** power

    return nth_power


square = factory_power(2)
print(square(4))

cube = factory_power(3)
print(cube(4))