#!/usr/bin/python3

import pprint as p
import requests
from random import randint

base_url= "https://opentdb.com/api.php?"


def main():

    print("Trivia questions. Ready?")
    print("How many questions do you want")
    amount1 = input(">>>")

    print("How difficult do you want the questions? easy, medium or hard")
    difficulty1 = (input(">>>")).lower()
    

    trivia = requests.get(base_url + f"amount={amount1}&difficulty={difficulty1}").json()

    response= []
    for i in range(int(amount1)):   
        print("Question "+ str(i+1)+ ": ")
        question1 = trivia.get("results")[i]["question"]
        p.pprint(question1)
        print ("Enter your response: ")
        response= input(">>>")
        response1 = trivia.get("results")[i]["correct_answer"]
        if response == response1:
            print("CORRECT!!!")
        else:
            print("Incorrect!!! The right response is: ")
        #response1 = trivia.get("results")[i]["correct_answer"]
            p.pprint(response1)

if __name__ == "__main__":
        main()
