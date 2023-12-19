#!/usr/bin/python3

import request



def main():
    print("Trivia questions. Ready?")
    print("How many questions do you want")
    amount = input(">>>")
    
    print("How difficult do you want the questions? easy, medium or hard")
    difficulty = input(">>>")

    print(amount, difficulty)
    
if __name__ == "__main__":
    main()
