import random


def apocalypse():
    num_of_families = random.randint(1000000, 10000000)
    population = 0
    for i in range(num_of_families):
        its_a_boy = True
        while its_a_boy:
            prop_boy_or_girl = random.uniform(0, 1)
            population += 1
            if prop_boy_or_girl > .5: #means it's a girl
                break
    num_of_girls = num_of_families
    ratio = num_of_girls/(population-num_of_girls)
    return ratio

print(apocalypse())

