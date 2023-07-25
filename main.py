import random

# word list
words = ["apple", "banana", "cherry", "fig", "grape", "kiwi", "lemon"]

# choose a word from the list
word = random.choice(words)

# number of attempts
attempts = int(input("Введіть кількість спроб: "))

# word with stars
hidden_word = "*" * len(word)

while attempts > 0:
    print(hidden_word)
    guess = input("Введіть букву або слово: ")
    if guess == word:
        print("Вітаю, ви вгадали слово!")
        break
    elif len(guess) == len(word):
        print("Слово не правильне.")
        attempts -= 1
    elif len(guess) == 1:
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    hidden_word = hidden_word[:i] + guess + hidden_word[i+1:]
            if hidden_word == word:
                print("Вітаю, ви вгадали слово!")
                break
        else:
            print("Такої літери немає.")
            attempts -= 1
    else:
        print("Неправильний формат.")
    print("Кількість спроб закінчилася. Ви програли.")
