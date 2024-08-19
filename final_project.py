import random 

def tas_kagit_makas_ECEM_AVCI():

    rules = """
    Rock, Paper, Scissors Game Rules:

    1. How to Play:
    - In Rock, Paper, Scissors, two players (one human, one computer) face each other.
    - Each player takes turns choosing rock, paper, or scissors.
    - Rock beats scissors, scissors beats paper, and paper beats rock.

    2. Game Rounds:
    - The game will be played for a minimum of 3 rounds.
    - In each round, a player can win, the computer can win, or it can be a draw.
    - In case of a draw, the score will not change, and a new round will be played.
    - The game is won by the player who wins two rounds.

    3. After the Game:
    - After determining the winner, both players will be asked if they want to play again.
    - If both players agree, the game will restart.
    - If either player declines, the game will end.

    """
    print(rules)

    options = ['rock','paper', 'scissors']
   
    games_played = 0 #games have rounds this will increase after we have a winner
    rounds_played = 0 #each game has multiple rounds
    
    #wins are in counted per GAME won by either of the players 
    computer_wins = 0
    player_wins = 0

    while True:
        rounds_won_player = 0
        rounds_won_computer = 0
        while True:
            #get computer to randomly choose a move
            computer_move = random.choice(options)

            #get a valid input from the user 
            while True:
                player_move = input ('Choose your move from: [rock, paper, scissors]\n').strip().lower()
                #check if the input is valid
                if player_move in options:
                    break
                else:
                    player_move = input ('That is an invalid move. Choose your move from:', options)

            #check if there is a draw
            if player_move == computer_move:
                print('It is a draw')


            if player_move == 'rock':

                if computer_move == 'paper':
                    rounds_won_computer += 1
                    rounds_played += 1
                    print('You lost this round :( \n Player:', rounds_won_player,'\n Computer:', rounds_won_computer)
                
                elif computer_move == 'scissors':
                    rounds_won_player += 1
                    rounds_played += 1
                    print('You won this round :) \n Player:', rounds_won_player,'\n Computer:', rounds_won_computer)

            if player_move == 'paper':

                if computer_move == 'scissors':
                    rounds_won_computer += 1
                    rounds_played += 1
                    print('You lost this round :( \n Player:', rounds_won_player,'\n Computer:', rounds_won_computer)
                
                elif computer_move == 'rock':
                    rounds_won_player += 1
                    rounds_played += 1
                    print('You won this round :) \n Player:', rounds_won_player,'\n Computer:', rounds_won_computer)


            if player_move == 'scissors':

                if computer_move == 'rock':
                    rounds_won_computer += 1
                    rounds_played += 1
                    print('You lost this round :( \n Player:', rounds_won_player,'\n Computer:', rounds_won_computer)
                
                elif computer_move == 'paper':
                    rounds_won_player += 1
                    rounds_played += 1
                    print('You won this round :) \n Player:', rounds_won_player,'\n Computer:', rounds_won_computer)
            

            if rounds_won_computer == 2:
                computer_wins += 1
                games_played += 1
                print('You lost, maybe next time :) \n General score is: \n Player:', player_wins, '\n Computer:', computer_wins,'\n Total games played:', games_played,'\n Total rounds played:',rounds_played)
                break # exit the loop if computer won 2 rouns
            
            if rounds_won_player == 2:
                player_wins += 1
                games_played += 1
                print('You won, congradulations !!! \n General score is: \n Player:', player_wins, '\n Computer:', computer_wins,'\n Total games played:', games_played,'\n Total rounds played:',rounds_played )
                break # exit the loop if player won 2 rounds
    

        #this will ask the user if they want to continue and will continue till it gets a valid input
        while True:
            continue_input = input("Do you want to try again? (yes/no): ").strip().lower()
            if continue_input in ['yes', 'no']:
                break
            else:
                continue_input = input('You entered a wrong answer please put in yes or no options.\n Do you want to try again (yes/no)').strip().lower()


        computer_continue = random.randint(1,2)

        if continue_input == 'yes':
            computer_continue = random.randint(1,2)
            if computer_continue == 1:
                print('You both want to play again. YEEEY!')
            else:
                print('Sorry, computer had a hard day, she does not want to play again, maybe next time :)')
                break
        else:
            print('Thanks for playing, see you next time :)')
            break
