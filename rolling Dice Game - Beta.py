import random;
import time;

Numbers=['1','2','3','4','5','6'];

def Welcome():
    print('Welcome to Roll A Die.');
    print('This project was coded in Sublime Text3');
    print('This project was created by (Discord) WhyAmIThisSad?#2972.');
    UserName=input('Do you know the UserName for the game?');
    if UserName == 'RAD':
        Password=input('Correct, what is that Password?');
        if Password == 'RAD123':
            print('That was the correct Password!');
            Rules();
        else:
                print('That is the wrong Password');
    else:
        print('That is the wrong UserName');

def Rules():
    print('The computer will randomly roll a dice. (a 6 sided dice)');
    time.sleep(1);
    print('You have 2 guesses to guess the dice.');
    time.sleep(1);
    print('If you guess it right the first time you get 2 points.');
    time.sleep(1);
    print('If you guess it the second time you get 1 point.\n');
    time.sleep(1)
    Game();

def Game():
    GameWhile=0;
    Points=0;
    while GameWhile == 0:
        RandomNumber=random.randint(0,5);
        NumberNeedToGuess=(Numbers[RandomNumber]);
        print('The number has now been selected');
        time.sleep(1);
        Guess1=input('What is your first guess?');
        if Guess1 == NumberNeedToGuess:
            print('Correct! You have gained 2 points.\n');
            Points=Points+2;
        else:
            print('Incorrect! Have another go.');
            Guess2=input('What is your second guess?');
            if Guess2 == NumberNeedToGuess:
                print('Correct! You have gained 1 point\n');
                Points=Points+1;
            else:
                print('Game over!');
                print('Goodbye your final score was',Points);
                GameWhile=GameWhile+1;

Welcome();
