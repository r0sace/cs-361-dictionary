from pyboxen import boxen
from rich.table import Table

class Generator:
    def __init__(self):
        self.user_input = None

        self.welcome_message()

    def welcome_message(self):
        print("")

        print(
            boxen(
                "[green]Enter [green]1[/green] to generate a random movie[/green]",
                "[blue]Enter 2 to enter a filter[blue]",
                "[dark_orange3]Enter 3 to browse filters[/dark_orange3]",
                "",
                "[bright_red]Enter 0 to exit[/bright_red]",
                title="Welcome to the Random Movie Generator!",
                subtitle="What would you like to do?",
                subtitle_alignment="center",
                color="white",
                padding=1
            )
        )

        self.user_input = input("Enter here: ")
        self.welcome_input(self.user_input)

    def welcome_input(self, num):
        if num == "1":
            pass
        elif num =="2":
            pass
        elif num == "3":
            self.browse_filters()
        elif num == "0":
            print("Goodbye!")
            exit()
        else:
            self.user_input = input("\nInvalid entry. Try again: ")        
            self.welcome_input(self.user_input)
    
    def browse_filters(self):
        print("")

        table = Table(show_header=True, header_style="bold magenta")

        table.add_column("Option Code")
        table.add_column("Description", justify="left")
        table.add_row(
            "-gs     --genre-s", "Select the movie genre", 
        )
        table.add_row(
            "-gd     --genre-d",
            "Select the movie genre to exclude",

        )
        table.add_row(
            "-t      --time",
            "Select the maximum movie duration",

        )
        table.add_row(
            "-r      --rated",
            "Select the movie rating to exclude",
        )
        table.add_row(
            "-d      --decade",
            "Select the movie decade",
        )
        table.add_row(
            "-s      --snob",
            "Returns movies with 3.5 stars or higher",
        )
        table.add_row(
            "-n      --num",
            "Adjusts number of movies to generate"
        )

        print(
            boxen(
                "Optional filters",
                "",
                "Enter an option code to alter the generator",
                "Enter 1 to see current applied filters",
                "Enter 2 to go back",
                "Enter 0 to exit",
                "",
                table
            )
        )

        self.user_input = input("Enter here: ")
        self.option_select(self.user_input)
    
    def option_select(self, usr_input):
        if usr_input == "-gs" or usr_input == "--genre-s":
            pass
        elif usr_input == "-gd" or usr_input == "--genre-d":
            pass
        elif usr_input == "-time" or usr_input == "--time":
            pass
        elif usr_input == "-r" or usr_input == "--rated":
            pass
        elif usr_input == "-d" or usr_input == "--decade":
            pass
        elif usr_input == "-s" or usr_input == "--snob":
            pass
        elif usr_input == "-n" or usr_input == "--num":
            pass
        elif usr_input == "1":
            pass
        elif usr_input == "2":
            pass
        elif usr_input == "0":
            print("Goodbye!")
            exit()
        else:
            self.user_input = input("\nInvalid entry. Try again: ")
            self.option_select(self.user_input)
            


if __name__ == "__main__":
    Generator()