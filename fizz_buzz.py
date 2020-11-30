def fizz_buzz(num):
    if num % 15 == 0:
        return 'fizzbuzz'
    elif num % 3 == 0:
        return 'fizz'
    elif num % 5 == 0:
        return 'buzz'
    else:
        return str(num)


next_number = 0

while next_number < 100:
    next_number += 1
    print(fizz_buzz(next_number))
    next_number += 1
    players_answer = input("Your turn: ")
    correct_answer = fizz_buzz(next_number)
    if players_answer != correct_answer:
        print("Sorry, you lose, the correct answer was {}".format(correct_answer))
        break
else:
    print("Congrats, you reached {}".format(next_number))