from random import randint
import random
import time

def main():
    # welcome message
    print("Bonjour, quelle table de multiplication voulez-vous réviser ?")
    # type the number

    while True:
        number_choise = input("Choisissez un nombre entre 0 et 10 - ")
        try:
            val = int(number_choise)
            print("Vous avez choisi le numero " + number_choise)
            break
        except ValueError:
            print("No.. input is not a number. It's a string, please start the program again")


    # get random table number
    table_list = list(range(11))
    random.shuffle(table_list)

    longest_time = 0

    # score
    score = 0

    for i in table_list:
        # start time
        start_time = time.time()

        print(number_choise,"*", i, "=")
        multiplication_answer = int(number_choise) * int(i)
        type_answer = input()

        try:
            if int(type_answer) == int(multiplication_answer):
                print('Bravo !')
                score += 1
            else:
                print("Il y a une erreur ! La réponse c'est " + str(multiplication_answer))
        except:
            print("Il y a une erreur ! La réponse c'est " + str(multiplication_answer))

        #end time
        end_time = time.time()
        #time difference
        time_diff = end_time - start_time
        if time_diff > longest_time:
            longest_time = time_diff

    print("Vous avez fini ! Votre score c'est " + str(score) + ".")

    print("Le temps le plus long pour répondre a été " + str(longest_time) + ".")

main()
