def create_randoms(start, stop, amount):
    import math
    import random
    random_numbers = [random.randint(start, stop) for number in range(amount)]
    return random_numbers


def get_input(input_texts):
    user_input = input(input_texts)
    return user_input


def print_message(message):
    return print(message)


def generate_texts(start, stop):
    texts = {"guess": "Enter an integer from {} to {}: ".format(start, stop),
             "low": "guess is low",
             "high": "guess is high",
             "guessed": "you guessed it!"}
    return texts


def guessing_the_number(random_numbers, texts):
    for current_number in random_numbers:
        guess = int(get_input(texts["guess"]))
        while guess != current_number:
            print_message(texts["low"]) if guess < current_number else print_message(texts["high"])
            guess = int(get_input(texts["guess"]))
        print_message(texts["guessed"])


def main():
    guessing_the_number(create_randoms(1, 99, 1), generate_texts(1, 99))
    guessing_the_number(create_randoms(1, 49, 10), generate_texts(1, 49))


if __name__ == "__main__":
    main()
