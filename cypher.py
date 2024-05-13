from array import *
import tkinter as tk


alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
b = len(alphabet)
i = 0
j = 0
#user_input = str(input("Welcome to ceasar cypher encryption/decryption! \n Enter A for Encoding a word, or press B for Decoding a word: "))

word_array = []
pos = 0
found = False

def encrypt():
    user_input1 = int(input("enter the K value: "))
    user_input2 = str(input("enter the word you'd like to encode: "))
    posArray = []
    k = 0
    finalResult = []
    i = 0

    for ch in user_input2:
            word_array.append(ch)
        
    while i < len(word_array):
            j = 0
            while j < len(alphabet):
                if word_array[i] == alphabet[j]:
                    posArray.append(j)
                    break
                j += 1
            i += 1
        
    while(k < user_input1):
            k += 1
            alphabet.insert(0, alphabet[25])
            alphabet.pop(b)
    manipulatedAlphabet = alphabet
        
    i = 0 
    while i < len(posArray):
        j = 0
        while j < len(manipulatedAlphabet):
            if posArray[i] == j:
                finalResult.append(manipulatedAlphabet[j])
                i += 1 
                break
            else: 
                j += 1

    concatenatedResult = "".join(finalResult)
    print("Your encoded word is:", concatenatedResult)

def decrypt():
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    user_input3 = str(input("What is the word you'd like do decrypt: "))
    user_input4 = int(input("Enter the key you'd like to decrypt in: "))
    k = 0
    word_array = []
    manipulatedAlphabet = []
    posArray = []
    finalResult = []
    i = 0

    for ch in user_input3: #creates an array of characters based on the word given
        word_array.append(ch)
        
    while(k < user_input4): #manipulates alphabet array to shift it by k value
        k += 1
        alphabet.insert(0, alphabet[25])
        alphabet.pop(b)
    manipulatedAlphabet = alphabet

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    while i < len(word_array): # finds the position of each letter from user word in the manipulated alphabet
        j = 0
        while j < len(manipulatedAlphabet):
            if word_array[i] == manipulatedAlphabet[j]:
                posArray.append(j)
                break
            j += 1
        i += 1

    i = 0
    while i < len(posArray): #creates the final result from the original alphabet. 
        j = 0
        while j < len(alphabet):
            if posArray[i] == j:
                finalResult.append(alphabet[j])
                i += 1 
                break
            else:
                j += 1

    concatenatedResult = "".join(finalResult)
    print("Your decoded word is:", concatenatedResult)

def execute_operation():
    valid = True
    print("Welcome to the ceasar cypher!")

    while valid == True:
        main_userInput = str(input("enter 'e' for encyption, 'd' for decryption, or type 'exit' to leave the program: "))
        if main_userInput == 'e' or main_userInput == 'E':
            encrypt()
            valid = True
        elif main_userInput == 'd' or main_userInput == 'D':
            decrypt()
            valid = True
        elif main_userInput == "exit" or main_userInput == "EXIT":
            exit()
        else: 
            print("invalid input")
            valid = True

execute_operation()








            



    




    

    



