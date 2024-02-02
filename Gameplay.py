import random
def gameplay():
    user = input("what's your choice? 'r' for rock,'p' for paper 's' for scissors:")
    computer = random.choice(["r","p","s"])

    if user == computer:
        return 'It\'s a tie'

    if winner(user,computer):
        return 'You won!'

    return 'you lost!'

def winner(player,opponent):
    if (player == 'r' and opponent == 'p') or (player == 'p' and opponent == 's')\
            or ( player == 's' and opponent == 'r'):
        return True
    return False

print(gameplay())









