< strong > < em >
from < / em > < / strong > random < strong > < em >
import < / em > < / strong > shuffle
# Кол-во попыток.
turns = 10

print(f"Привет, Давай сыграем в виселицу! У тебя есть {turns} попыток!")

# Список слов, которые участвуют в игре.
wordList = ["geekflare", "awesome", "python", "magic"]
# Перемешиваем список.
shuffle(wordList)
# Берем последнее слово из списка.
word = wordList.pop()

guesses = ""

# Цикл, который будет работать, пока не останется попыток или не отгаданных букв.
< strong > < em >
while < / em > < / strong > turns > 0:
    wrong = 0

    < strong > < em >
    for < / em > < / strong > char < strong > < em > in < / em > < / strong > word:
        < strong > < em > if < / em > < / strong > char < strong > < em > in < / em > < / strong > guesses:
        print(char, end=" ")
    < strong > < em > else < / em > < / strong >:
    print("_", end=" ")
    wrong += 1

print("\n")

< strong > < em > if < / em > < / strong > wrong == 0:
print("Ты выиграл! :)")

< strong > < em >
break < / em > < / strong >

< strong > < em > < / em > < / strong > print()

guess = ""
< strong > < em > if < / em > < / strong > len(guess) < 1:
guess = input("Впиши букву и нажми enter: ")[0]

< strong > < em > if < / em > < / strong > guess < strong > < em > in < / em > < / strong > guesses:
print("Эта буква уже была!")
guesses += guess

< strong > < em > if < / em > < / strong > guess < strong > < em > not in < / em > < / strong > word:
turns -= 1

print("Упс! Ошибка")
print(f"У тебя осталось {turns} попыток")

< strong > < em > if < / em > < / strong > turns == 0:
print("Ты проиграл! :(")