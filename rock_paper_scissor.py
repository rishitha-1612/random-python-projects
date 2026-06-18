import random
def func_play():
    userinput = input("enter your choice? 'r' for rock, 'p' for paper, 's' for scissor")
    user_input=userinput.lower()
    computer_input = random.choice(['r','p','s'])
    print(f"Computer chose: {computer_input}")
    if user_input == computer_input:
        return 'it is a tie'
    if func_is_win(user_input, computer_input):
        return 'you win'
    return 'you lost'
def func_is_win(var_player, var_opponent):
    if(var_player=='r' and var_opponent=='s')or(var_player=='p' and var_opponent=='r')or(var_player=='s' and var_opponent=='p'):
        return True
    return False

print(func_play())