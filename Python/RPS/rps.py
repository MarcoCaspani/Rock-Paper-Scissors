from random import random
from math import floor

markov_chain = [[0,0,0],[0,0,0],[0,0,0]]
game = 0
last_state = 0

stats = [0,0,0]

def random_game():  # returns user choice, machine choice, result
    print("User: ", end='')
    machine = floor(random() * 3)
    user = 0
    try:
        user = int(input())
    except:
        pass

    print("Machine: " + str(machine))

    result = wins(user, machine)

    print("result: \t\t\t\t\t\t" + str(result))
    return user, machine, result

def markov_game():
    global markov_chain
    global last_state
    # calculate probabilities
    p0 = markov_chain[last_state][0]
    p1 = markov_chain[last_state][1]
    p2 = markov_chain[last_state][2]
    # pick the most probable object the user will choose
    user_prediction = [p0, p1, p2].index(max([p0, p1, p2]))
    # therefore the machine choice will be
    machine = get_winning_object(user_prediction)

    # start the game
    print("User: ", end='')
    user = 0
    try:
        user = int(input())
    except:
        pass
    print("AI: " + str(machine))

    result = wins(user, machine)

    # update stats
    if result == 1:
        stats[0] += 1
    elif result == 0:
        stats[1] += 1
    elif result == -1:
        stats[2] += 1

    print("result: \t\t\t\t\t\t" + str(result))
    return user, machine, result

# returns the object that beats "object"
def get_winning_object(object):
    return (object + 1) % 3

# returns 1 if win, 0 if tie, -1 if lost
def wins(user, machine):
    result = 0
    if user == machine:             # TIE
        result = 0
    elif (machine + 1) % 3 == user:   # USER WINS
        result = 1
    else:
        result = -1                       # MACHINE WINS
    return result

def print_markov_chain():
    global markov_chain
    for row in markov_chain:
        print(row)

def print_stats(stats):
    total = sum(stats)
    if total == 0:
        total = 1
    you = floor(stats[0] / total * 100)
    tie = floor(stats[1] / total * 100)
    computer = floor(stats[2] / total * 100)

    print()
    print("You: " + str(you) + "%")
    print("Tie: " + str(tie) + "%")
    print("Computer: " + str(computer) + "%")

def main():
    global game
    global last_state
    global markov_chain
    global stats

    while True:
        # print_markov_chain()
        print_stats(stats)

        if game < 10:
            # play
            new_state, machine, result = random_game()
            # update markov chain
            markov_chain[last_state][new_state] += 1
            last_state = new_state
            # next game
            game += 1
        else:
            # play
            new_state, machine, result = markov_game()
            # update markov chain
            markov_chain[last_state][new_state] += 1
            last_state = new_state
            # next game
            game += 1
        print()
main()
