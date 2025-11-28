import random
import os
import sys

FILE_NAME = "numbers.txt"
MIN_VAL = -sys.maxsize
MAX_VAL = sys.maxsize

def generate_random_number(floating_point=False):
    existing_numbers = get_existing_numbers()
    while True:
        if floating_point:
            number = round(random.uniform(MIN_VAL, MAX_VAL), 2)
        else:
            number = random.randint(MIN_VAL, MAX_VAL)

        if number not in existing_numbers:
            return number

def get_existing_numbers():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            return [int(line.strip()) for line in f.readlines()]
    return []

def add_number_to_file(number):
    numbers = get_existing_numbers()
    numbers.append(number)
    numbers.sort()  # Sort numerically

    with open(FILE_NAME, 'w') as f:
        for num in numbers:
            f.write(f"{num}\n")

def all_values_generated(floating_point=False):
    if floating_point:
        return len(get_existing_numbers()) >= (MAX_VAL - MIN_VAL) * 100
    else:
        return len(get_existing_numbers()) == (MAX_VAL - MIN_VAL + 1)

if __name__ == "__main__":
    number = generate_random_number()
    add_number_to_file(number)
    print(f"Number {number} is a number that exists in the computer.")

    if all_values_generated():
        print("All available values have been generated.")
