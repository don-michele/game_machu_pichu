#!/usr/bin/python3

import random

def choose_number_of_players():

	valid_entry_list = ['2','3','4']
	print("This game is played between 2 and 4 players!")
	print()
	players_nr = input("Type the number of players: ")
	isCorrectNumber = False
	while(isCorrectNumber == False):
		if (players_nr not in valid_entry_list):
			print()
			print("Too few/many players or not valid number!")
			print()
			print("The game must be played by 2-4 players!")
			print()
			players_nr = input("Type the number of players: ")
		else:
					isCorrectNumber = True
	print()
	print("The game will have " + str(players_nr) + " players!")
	print()
	print("Chosen number:", players_nr)
	return players_nr

def create_deck():

	deck = { 'A♥':('A', '♥', 14), 'A♠':('A', '♠', 14), 'A♦':('A', '♦', 14), 'A♣':('A', '♣', 14),
			 'K♥':('K', '♥', 13), 'K♠':('K', '♠', 13), 'K♦':('K', '♦', 13), 'K♣':('K', '♣', 13),
			 'Q♥':('Q', '♥', 12), 'Q♠':('Q', '♠', 12), 'Q♦':('Q', '♦', 12), 'Q♣':('Q', '♣', 12),
			 'J♥':('J', '♥', 11), 'J♠':('J', '♠', 11), 'J♦':('J', '♦', 11), 'J♣':('J', '♣', 11),
			 '10♥':('10', '♥', 10), '10♠':('10', '♠', 10), '10♦':('10', '♦', 10), '10♣':('10', '♣', 10) }

	return deck

def get_card_info():

	pachet = create_deck()
	print("Pachet initial:", pachet)
	carte = random.choice(list(pachet.keys()))
	print("Carte:", carte)
	caracteristici = pachet[carte]
	print("Tipul caracteristici:", type(caracteristici))
	nume = caracteristici[0]
	print("Nume:", nume)
	semn = caracteristici[1]
	print("Semn:", semn)
	valoare = caracteristici[2]
	print("Valoare:", valoare)
	print("Caracteristici ale cartii alese:", caracteristici)
	pachet.pop(carte)
	print("Pachet final:", pachet)

def first_card_split(players_nr):

	initial_hand = []
	initial_card_nr = 5
	players_nr = int(players_nr)

	for i in range(players_nr):
		initial_hand.append([])
	
	card_pack = create_deck()

	for item in range(initial_card_nr):
		for player in range(players_nr):
			card = random.choice(list(card_pack.keys()))
			initial_hand[player].append(card)
			card_pack.pop(card)

	for player in range(players_nr):
		print("Player " + str(player+1) + " cards:", initial_hand[player])

	print("Cards left in deck:", card_pack)
	#return initial_hand, card_pack
		

def main():

	players_nr = choose_number_of_players()
	first_card_split(players_nr)

main()

#get_card_info()

#choose_number_of_players()
