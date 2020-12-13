word = 'slowo'
for i in range(5):
    guess = input("Zgadnij slowo: ")
    if guess == word:
        print("Odpowiedz prawidlowa.")
        break
else:
    print("Odpowiedz nieprawidlowa.")
