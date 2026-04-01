# Number 1 this is a Fizz Buzz app

# loop through numbers 1 to 100 and print them
# range is exclusive so we need to go one past the target
# range starts at 0 so we tell it to start at 1
for i in range(1,101):

    # fizzbuzz
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")

    # divisible by 3
    elif i % 3 == 0:
        print("fizz")

    # divisible by 5
    elif i % 5 == 0:
        print("buzz")

    else:
        print(i)

