import random
def game(name):
    print("Well, ",name," I am thinking of a number between 1 and 20.")
    print("Take a guess.")
    w_num = random.randint(1,20)
    tmp = None
    count = 0
    while 1:
        tmp = int(input())
        if tmp>w_num:
            print("Your guess is too large.")
        elif tmp<w_num:
            print("Your guess is too low.")
        else:
            print("Good job,", name+"!", "You guessed my number in", count ,"guesses!")
            return 
        count+=1
        print("Take a guess")

if __name__ == "__main__":
    print("Hello! What is your name?")
    name = input()
    game(name)