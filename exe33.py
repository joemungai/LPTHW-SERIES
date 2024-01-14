def even_numbers(header,step):
    numbers = []
    while int(header) < 10:
        print(f"At the top i is {header}")
        numbers.append(header)
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {numbers[0]}")
        header += step

even_numbers(2,1)
