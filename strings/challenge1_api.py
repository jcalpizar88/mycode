#!/usr/bin/python3

import pprint
import requests
from random import randint

base_url= "https://opentdb.com/api.php?"


def main():

    print("Trivia questions. Ready?")
    print("How many questions do you want")
    amount = input(">>>")

    print("How difficult do you want the questions? easy, medium or hard")
    difficulty = input(">>>")

    trivia = requests.get(base_url + f"amount={amount}&difficulty={difficulty}").json()

#for q in trivia[result]:
    question = trivia.get('results')[randint(0, int(amount)-1)]["question"]
    print(question)
    answer = trivia.get('correct_answer')[randint(0, int(amount)-1)]["correct_answer"]
    print(answer)

   # response = trivia.get



if __name__ == "__main__":
    main()
