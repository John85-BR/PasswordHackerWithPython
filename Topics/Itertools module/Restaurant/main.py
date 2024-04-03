import itertools
dishes = itertools.product(main_courses, desserts, drinks)
prices = itertools.product(price_main_courses, price_desserts, price_drinks)

for i, j in zip(dishes, prices):
    if sum(j) <= 30:
        print(f"{' '.join(i)} {sum(j)}")
