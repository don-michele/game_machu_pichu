#!/usr/bin/python3

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

choose_number_of_players()
