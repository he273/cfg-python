import random
import requests


possible_stats = ['poke_id', 'height', 'weight']
used_cards = []
player_score = 0
comp_score = 0


# chooses a random number and gets this pokemon from the API
def get_pokemon():

    while True:
        poke_id = random.randint(1, 151)
        if poke_id in used_cards:
            continue
        else:
            used_cards.append(poke_id)
            break

    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(poke_id)
    response = requests.get(url)
    data = response.json()

    stats = {'name': data['name'],
             'poke_id': data['id'],
             'height': data['height'],
             'weight': data['weight']}

    return stats


# gets the player to input which stat they want to use
def player_select_stat():

    while True:
        stat_choice = input('\nPlease choose poke_id, height or weight: ')

        if stat_choice in possible_stats:
            print('You have chosen to use {}'.format(stat_choice))
            return stat_choice

        else:
            print('invalid input')
            continue


# randomly selects a stat to use
def comp_select_stat():

    stat_choice = random.choice(possible_stats)
    print('\nComputer has chosen to use {}'.format(stat_choice))
    return stat_choice


# carries out a whole round - gets pokemon for the player, prints it, the player chooses a stat if it's the first round
# or if they won the last round, random stat used if the player lost the previous round, gets pokemon for computer and
# shows it to the player, stats compared and scores updated
def play_round(player_chooses):

    global player_score, comp_score

    player_stats = get_pokemon()
    print('\nYour pokemon:')
    print("\n".join("{}\t{}".format(k, v) for k, v in player_stats.items()))

    if player_chooses is True:
        chosen_stat = player_select_stat()
    else:
        chosen_stat = comp_select_stat()

    computer_stats = get_pokemon()
    print('\nComputer\'s pokemon:')
    print("\n".join("{}\t{}".format(k, v) for k, v in computer_stats.items()))

    player_value = player_stats[chosen_stat]
    computer_value = computer_stats[chosen_stat]

    if player_value > computer_value:
        print('\nYou win!')
        player_chooses = True
        player_score += 1

    elif player_value == computer_value:
        print('\nIt\'s a draw')

    elif player_value < computer_value:
        print('\nYou lose :(')
        player_chooses = False
        comp_score += 1

    else:
        print('\nerror')

    return player_chooses


# lets the player choose how many rounds to play, then runs that many rounds updating the player on their score and
# publishing a final score at the end
def main():
    while True:
        try:
            rounds = int(input('Welcome to pokemon top trumps how many rounds would you like to play? '))
        except ValueError:
            print('please enter a positive number')
            continue
        if rounds < 0:
            print('please enter a positive number')
            continue
        elif rounds > 75:
            print('not enough cards for this many rounds (max 75)')
            continue
        else:
            break
    player_chooses = True
    while rounds > 0:
        player_chooses = play_round(player_chooses)
        rounds -= 1
        print('Scores:   You {}     Computer {}'.format(player_score, comp_score))
        print('Rounds left: {}'.format(rounds))
    print('\nGame over.')
    print('Final scores:  You {}   Computer {}'.format(player_score, comp_score))
    if player_score > comp_score:
        print('You win overall')
    elif player_score < comp_score:
        print('Computer wins overall')
    else:
        print('It is a draw overall')


# carries out the program
main()
