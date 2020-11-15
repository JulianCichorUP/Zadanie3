word='slowo'
guess=''
for i in range(5):
    guess=input("Zgadnij slowo: ")
    if guess!=word:
        print("Odpowiedz nieprawidlowa.")
    else:
        print("Odpowiedz prawidlowa.")
        break