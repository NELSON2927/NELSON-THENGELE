def number_skipper():
    for num in range(1, 101):
        if num % 5 == 0 and num % 10 != 0:
            continue
        print(num)

number_skipper()