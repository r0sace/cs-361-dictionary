# Cristina Rosace
from InquirerPy import inquirer
from time import sleep
from random import random
from clint.textui import progress
import pyfiglet
from colorama import Fore, Back, Style
import zmq
import requests

class Dictionary:
    def __init__(self):
        self.word = None
        self.word_details = None
        self.definition = None
        self.examples = None
        self.synonyms = None
        self.antonyms = None
        self.pronunciation = None
        self.current_result_idx = 0
        self.num_definitions = None
        self.part_of_speech = None

        self.headers =  {
        "X-RapidAPI-Key": "x",
	    "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com"
        }
        
        self.welcome()

    def welcome(self):
        print("")
        title_art = pyfiglet.figlet_format("Dictionary", font="roman")
        print(title_art)
        print(Fore.GREEN + "** Welcome to the Dictionary tool created by Cristina Rosace" + Style.RESET_ALL)
        print("")
        print("** Use this tool to explore the English language!")
        print("** Simply view definitions or get detailed information about words.")
        print("** Use your" + Fore.MAGENTA + " arrow keys " + Style.RESET_ALL + "to get started!")
        print("")
        Style.RESET_ALL

        action = self.main_menu_actions()
    
    def main_menu_actions(self):
        action = inquirer.select(
            message="Select an action:",
            choices = ["Search word", "Get random word", "Exit"],
        ).execute()
        self.main_menu_selections(action)

    def main_menu_selections(self, action):
        if action == "Search word":
            self.search_word()
        elif action == "Get random word":
            self.get_random_word()
        else:
            pass

    def progress_bar(self, action):
        print("")
        print(Fore.GREEN, action)
        for i in progress.bar(range(10)):
            sleep(random() * .1)
        print(Style.RESET_ALL)       
        return
    
    def client(self):
        context = zmq.Context()

        socket = context.socket(zmq.REQ)
        socket.connect("tcp://localhost:5555")
        socket.send(b'Fetch random word')

        message = socket.recv()
        decoded_message = message.decode()
        return(f'{decoded_message}')


    def get_random_word(self):
        self.progress_bar("Getting random word...")
        self.current_result_idx = 0
        self.word = str(self.client())
        self.get_random_word_details()


    def get_random_word_details(self):
        url = "https://wordsapiv1.p.rapidapi.com/words/" + self.word
        response = requests.request("GET", url, headers=self.headers)
        word_details = response.json()
    
        self.word_details = word_details["results"]
        self.num_definitions = len(self.word_details) - 1
        self.pronunciation = word_details["pronunciation"]
        self.get_definition()

    def get_searched_word_details(self):
        url = "https://wordsapiv1.p.rapidapi.com/words/" + self.word
        response = requests.request("GET", url, headers=self.headers)
        word_details = response.json()

        if "success" in word_details:
            print(Fore.RED + 'Error: "' + self.word +  '" not found in the dictionary. \n' + Style.RESET_ALL)
            self.main_menu_actions()
        
        self.word_details = word_details["results"]
        self.num_definitions = len(self.word_details) - 1

        self.pronunciation = word_details["pronunciation"]

        if self.num_definitions < 0:
            print(Fore.RED + 'Error: "' + self.word +  '" not found in the dictionary. \n' + Style.RESET_ALL)
            self.main_menu_actions()

        self.get_definition()

    def get_definition(self):
        word_info = self.word_details[self.current_result_idx]
        self.definition = word_info["definition"]
        if word_info["partOfSpeech"] is None:
            self.part_of_speech = ""
        else:
            self.part_of_speech = "\x1B[3m" + word_info["partOfSpeech"] + "\x1B[0m"
        self.word_definition_display()

    def search_word(self):
        self.word = inquirer.text(message="Enter a word:").execute()
        self.progress_bar("Getting word...")
        self.current_result_idx = 0
        self.get_searched_word_details()
    
    def word_definition_display(self):
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
            choices = ["Example: View in a sentence", "Synonyms:", "Antonyms", "Pronunciation", "New search", "Exit"]
        else:
            if self.current_result_idx < self.num_definitions:
                choices = ["Different definition", "New search", "Exit"]
            else:
                choices = ["New search", "Exit"]
        self.word_info_actions(action, choices)
    
    def word_info_actions(self, action, choices):
        print("")
        if action == "Yes":
            while True:
                action = inquirer.select(
                    message="Select an action:",
                    choices = choices          
                ).execute()
                self.word_info_selection(action, choices)
                   
        elif action == "No":
            while True:
                action = inquirer.select(
                    message="Select an action:",
                    choices = choices
                ).execute()
                self.word_info_selection(action, choices)


    
    def word_info_selection(self, action, choices):
        if action == "Example":
            self.progress_bar("Getting example...")
            self.get_example()
            self.display_example(choices)
        elif action == "Synonyms":
            self.progress_bar("Getting synonyms...")
            self.get_synonyms()
            self.display_synonyms(choices)
        elif action == "Antonyms":
            self.progress_bar("Getting antonyms...")
            self.get_antonyms()
            self.display_antonyms(choices)
        elif action == "Pronunciation":
            self.progress_bar("Getting pronunciation...")
            self.get_pronunciation()
            self.display_pronunciation(choices)
        elif action == "Different definition":
            self.current_result_idx += 1
            self.progress_bar("Getting another definition...")
            self.get_definition()
        elif action == "New search":
            print("")
            self.main_menu_actions()
        elif action == "Exit":
            self.goodbye()

    def get_example(self):
        word_info = self.word_details[self.current_result_idx]
        if "examples" in word_info:
            self.examples = word_info["examples"]
        else:
            self.examples = ["Sorry, no available examples for this word."]
        
        return

    def display_example(self, choices):
        print("")
        print(Fore.BLUE + self.word + Style.RESET_ALL)

        if len(self.examples) > 1:
            print("|" + Style.DIM +  " examples" + Style.RESET_ALL)
        else:
            print("|"  + Style.DIM +  " example" + Style.RESET_ALL)

        for example in self.examples:
            print("| \u2022 " + example)

        print("")
        choices.remove("Example")

        return
    
    def get_synonyms(self):
        word_info = self.word_details[self.current_result_idx]
        if "synonyms" in word_info:
             self.synonyms = word_info["synonyms"]
        else:
            self.synonyms = ["Sorry, no available synonyms for this definition."]
        return
    
         
    def display_synonyms(self, choices):
        print("")
        print(Fore.BLUE + self.word + Style.RESET_ALL)

        if len(self.synonyms) > 1:
            print("|" + Style.DIM + " synonyms" + Style.RESET_ALL)
        else:
            print("|" + Style.DIM + " synonym" + Style.RESET_ALL)

        for synonym in self.synonyms:
            print("| \u2022 " + synonym)
        
        print("")
        choices.remove("Synonyms")
        return
    
    def get_antonyms(self):
        word_info = self.word_details[self.current_result_idx]
        if "antonyms" in word_info:
             self.antonyms = word_info["antonyms"]
        else:
            self.antonyms=["Sorry, no available antonyms for this definition."]
        
        return
    
    def display_antonyms(self, choices):
        print("")
        print(Fore.BLUE + self.word + Style.RESET_ALL)

        if len(self.antonyms) > 1:
            print("|" + Style.DIM +  " antonyms" + Style.RESET_ALL)
        else:
            print("|" + Style.DIM + " antonym" + Style.RESET_ALL)

        for antonym in self.antonyms:
            print("| \u2022 " + antonym)

        print("")
        choices.remove("Antonyms")
        return
    
    def get_pronunciation(self):
        if self.pronunciation is None:
            self.pronunciation = ["Sorry, no available pronunciation for this word."]
    
    def display_pronunciation(self, choices):
        print("")
        print(Fore.BLUE + self.word + Style.RESET_ALL)
        if len(self.pronunciation) > 1:     
            print("|" + Style.DIM +  " pronunciations" + Style.RESET_ALL)
        else:
            print("|" + Style.DIM + " pronunciation" + Style.RESET_ALL)
        
        for key in self.pronunciation:
            print("| \u2022 " + self.pronunciation[key])
        
        print("")
        choices.remove("Pronunciation")
        
             
    def goodbye(self):
        print("")
        exit_art = pyfiglet.figlet_format("Goodbye", font="roman")
        print(exit_art)
        exit()


if __name__ == "__main__":
    Dictionary()