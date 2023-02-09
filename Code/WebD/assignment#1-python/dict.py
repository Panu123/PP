
import json
import os

d = {}



    
while True:
    



    def where_json(file_name):
        return os.path.exists(file_name)


    if where_json('data.json'):
        with open('data.json') as outfile:
            d = json.load(outfile)
            
    word = input("Give me a word or enter to Exit ? : ")
    
    if not word: break
    if word.isdigit():
        print("numbers like 1 are same in finnish put as a word one is different please give a word or press ENTER to exit: ")
       
    if word.isalpha():
        
        
        
        if word in d:
            print(f"{word} = {d[word]}")
        else:
            defenition = input(f"word not found. Please give me defenition for {word}? If not press enter to exit : ")
            if not defenition: break
                    
            defenition.capitalize()
                
            if defenition:
                d[word] = defenition
                with open("data.json", "w") as outfile:
                    json.dump(d, outfile)

            else:
                d = {"cat": "kissa", "dog": "koira"}
                print("DISCLAIMER can not found/load data.json, opening with default dictionary  : ")
                word = input("Give me a word or enter to Exit ? : ")

                if not word: break
                        

                if word in d:
                    print(f"{word} = {d[word]}")
                else:
                    defenition = input(f"word not found. Please give me defenition for {word}? If not press enter to exit : ")
                    if not defenition: break

                  
            
                
           







