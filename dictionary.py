# Cristina Rosace
from InquirerPy import inquirer
from time import sleep
from random import random
from clint.textui import progress
import pyfiglet
from colorama import Fore, Back, Style
from pyboxen import boxen

class Dictionary:
    def __init__(self):
        self.word = "hello"
        self.part_of_speech = "\x1B[3mnoun\x1B[0m"
        self.definition = "an expression of greeting"
        self.welcome()

    def welcome(self):
        print("")
        title_art = pyfiglet.figlet_format("Dictionary", font="roman")
        print(title_art)
        print("** Welcome to the Dictionary tool created by Cristina Rosace")
        print("** Use this tool to explore the English language!")
        print("** Use your arrow keys to get started")
        print("")

        action = self.main_menu_actions()
    
    def main_menu_actions(self):
        action = inquirer.select(
            message="Select an Action:",
            choices = ["Get random word", "Search word", "Exit"],
        ).execute()
        self.main_menu_selections(action)

    def main_menu_selections(self, action):
        if action == "Search word":
            self.search_word()
        elif action == "Get random word":
            self.progress_bar("Getting random word...")
            self.word = "pony"
            self.definition = "a small glass adequate to hold a single swallow of whiskey"
            self.word_definition()
        else:
            pass

    def progress_bar(self, action):
        print("")
        print(Fore.GREEN, action)
        for i in progress.bar(range(10)):
            sleep(random() * .1)
        print(Style.RESET_ALL)       
        return


    def search_word(self):
        self.word = inquirer.text(message="Enter a word:").execute()
        self.progress_bar("Getting word...")
        self.word_definition()
    
    def word_definition(self):
        print(Fore.BLUE + self.word + Style.RESET_ALL)
        print("| " + Style.DIM +  self.part_of_speech + Style.RESET_ALL)
        print("| " + self.definition)
        print("")
        self.definition_check()

    def definition_check(self):
        action = inquirer.select(
            message="Is this the definition you're looking for?",
            choices = ["Yes", "No"]
        ).execute()
        if action == "Yes":
            choices = ["Example", "Synonyms", "Antonyms", "Pronunciation", "New search", "Exit"]
        else:
            choices = ["Different definition", "New search", "Exit"]
        self.word_info_actions(action, choices)


    def word_info_actions(self, action, choices):
        print("")
        if action == "Yes":
            while True:
                action = inquirer.select(
                    message="Select an Action:",
                    choices = choices          
                ).execute()
                self.word_info_selection(action, choices)
                   
        else:
            while True:
                action = inquirer.select(
                    message="Select an Action:",
                    choices = choices
                ).execute()
                self.word_info_selection(action, choices)


    
    def word_info_selection(self, action, choices):
        if action == "Example":
            self.progress_bar("Getting example...")
            self.example(choices)
        elif action == "Synonyms":
            self.progress_bar("Getting synonyms...")
            self.synonyms(choices)
        elif action == "Antonyms":
            self.progress_bar("Getting antonyms...")
            self.antonyms(choices)
        elif action == "Pronunciation":
            self.progress_bar("Getting pronunciation...")
            self.pronunciation(choices)
        elif action == "Different definition":
            self.progress_bar("Getting another definition...")
            self.word_definition()
        elif action == "New search":
            print("")
            self.main_menu_actions()
        elif action == "Exit":
            self.goodbye()



    def example(self, choices):
        print("")
        example = "Every morning they exchanged polite hellos"
        print(Fore.BLUE + self.word + Style.RESET_ALL)
        print("| " + Style.DIM +  "example" + Style.RESET_ALL)
        print("| " + example)
        print("")
        choices.remove("Example")
        return
    
    def synonyms(self, choices):
        print("")
        synonyms = ["hi", "how-do-you-do", "howdy", "hullo"]
        print(Fore.BLUE + self.word + Style.RESET_ALL)
        print("| " + Style.DIM +  "synonyms" + Style.RESET_ALL)
        print("| ", end="")
        print(*synonyms, sep=", ")
        print("")
        choices.remove("Synonyms")
        return
    
    def antonyms(self, choices):
        print("")
        antonyms = ["adios", "au revoir", "goodbye"]
        print(Fore.BLUE + self.word + Style.RESET_ALL)
        print("| " + Style.DIM +  "antonyms" + Style.RESET_ALL)
        print("| ", end="")
        print(*antonyms, sep=", ")
        print("")
        choices.remove("Antonyms")
        return
    
    def pronunciation(self, choices):
        print("")
        pronuncation = "hɛ'loʊ"
        print(Fore.BLUE + self.word + Style.RESET_ALL)
        print("| " + Style.DIM +  "pronunciation" + Style.RESET_ALL)
        print("| " + pronuncation)
        print("")
        choices.remove("Pronunciation")
        return      
    

    def goodbye(self):
        exit_art = pyfiglet.figlet_format("Goodbye", font="roman")
        print(exit_art)
        exit()






        

if __name__ == "__main__":
    Dictionary()