import random


def choose():
    words = ["rainbow",'computer', 'science', 'programming', 'mathematics', 'player', 'condition', 'reverse', 'water','ocean','river']
    pick = random.choice(words)
    return pick

def jumble(word):
    return "".join(random.sample(word,len(word)))

def thank(p1name, p2name, pp1, pp2):
    print(f'Thank you for playing. {p1name} your score is {pp1}. {p2name} your score is {pp2}. See you soon!!')


def play():
    p1name = input('Hi player1, Enter your name: ') #player1 name
    p2name = input('Hi player2, Enter your name: ') #player2 name
    pp1 = 0 #player1 points
    pp2= 0 #player 2 points
    turn = 0 #turn variable to choose which player to play
    chance = 0
    while True:
        #Computer task
        picked_word = choose()
        #generating ques
        ques = jumble(picked_word)
        print(ques)
        #player1's turn
        if turn % 2 ==0 :
            print(f'Hey {p1name}, its your turn ')
            ans = input("What is on my mind? ")
            if ans == picked_word:
                pp1 +=1
                print(f'Hey {p1name}, your score is {pp1}')
            else:

                while chance <3 :
                    print('Try again')
                    ans = input("What is on my mind? ")
                    chance += 1


                else:
                    print("your turn is over")

                c = int(input('press 1 to continue or 0 to leave '))
                if c==0:
                    thank(p1name,p2name,pp1,pp2)
                    break




        #player 2's turn
        else:
            print(f'Hey {p2name}, its your turn ')
            ans = input("What is on my mind? ")
            if ans == picked_word:
                pp2 += 1
                print(f'Hey {p2name}, your score is {pp2}')
            else:
                print('Better luck next time. Right word is ', picked_word)
            c = int(input('press 1 to continue or 0 to leave '))
            if c == 0:
                thank(p1name, p2name, pp1, pp2)
                break
        turn = turn +1


play()