from pyboxen import boxen
from rich.table import Table

class Generator:
    def __init__(self):
        self.user_input = None
        self.filters = []
        self.genres = ["action", "adventure","animation","biography","comedy","crime", "documentary", "drama", "family", "fantasy",  "history", "horror", "musical", "mystery", "romance", "sciFi", "sport","thriller", "war", "western"]

        self.welcome_message()

    def welcome_message(self):
        print("")

        print(
            boxen(
                "[green]Enter [green]1[/green] to generate a random movie[/green]",
                "[blue]Enter 2 to enter a filter[blue]",
                "[purple4]Enter 3 to browse filters[/purple4]",
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
            "-gs     --genre-s", "Select a movie genre", 
        )
        table.add_row(
            "-gd     --genre-d",
            "Deselect a movie genre",

        )
        table.add_row(
            "-t      --time",
            "Select a maximum movie duration",

        )
        table.add_row(
            "-r      --rated",
            "Select a movie rating to exclude",
        )
        table.add_row(
            "-d      --decade",
            "Select a movie decade",
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
                "Optional Filters",
                "",
                "[green]Enter an option code to alter the generator[/green]",
                "",
                "[blue]Enter 1 to see current applied filters[/blue]",
                "[dark_orange3]Enter 2 to go back[/dark_orange3]",
                "[bright_red]Enter 0 to exit[/bright_red]",
                "",
                table
            )
        )

        self.user_input = input("Enter here: ")
        self.option_select(self.user_input)
    
    def option_select(self, usr_input):
        if usr_input == "-gs" or usr_input == "--genre-s":
            self.gs()
        elif usr_input == "-gd" or usr_input == "--genre-d":
            self.gd()
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

    def gs(self):
        print("")
        print(
            boxen(
                "[green]Enter a movie genre to generate from",
                "",
                "[blue]Press 1 to see a list of movie genres",
                "[dark_orange3]Press 2 to go back",
                "[bright_red]Press 0 to exit",
                title="-gs: Genre Select",
                color="white",
                padding=1,
            )
        )

        self.user_input = input("Enter here: ")
        self.gs_options(self.user_input)

    def gs_options(self, usr_input):

        if usr_input == "1":
            self.show_movies("s")
        elif usr_input.lower() in self.genres:
            print("\nAre you sure you want to generate " + str(usr_input) + " movies? ")
            confirm = input("Y/N: ")
            if confirm.lower() == "y":
                print("\nSuccessfully added " + str(usr_input) + " movies to filters!")
                print("Returning back to filters...")
                self.filters.append(usr_input)
            elif confirm.lower() == "n":
                print("\nUnsuccessfully added " + str(usr_input) + " movies to filters")
                print("Returning back to filters...")
            else:
                print("\nInvalid input")
                print("Returning back to filters...")
        elif usr_input == "2":
            print("Returning back to filters...")
            self.browse_filters()
        elif usr_input == "3":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input - please select from an available genre")
            self.show_movies("s")

        self.browse_filters()
        
        

    def show_movies(self, o):
        table = Table(show_header=False, header_style="bold magenta")
        table.add_column
        table.add_column
        table.add_column
        table.add_column
        table.add_column

        table.add_row(
            "Action", "Adventure","Animation","Biography","Comedy",
        )
        table.add_row(
            "Crime", "Documentary", "Drama", "Family", "Fantasy",
        )
        table.add_row(
            "History", "Horror", "Musical", "Mystery", "Romance",
        )
        table.add_row(
            "SciFi", "Sport","Thriller", "War", "Western"
        )


        print(
            boxen(
                "Movie Genres",
                "",
                "[dark_orange3]Enter 1 to go back and enter a genre[/dark_orange3]",
                "[bright_red]Enter 0 to exit[/bright_red]",
                table
            )
        )

        self.user_input = input("Enter here: ")
        if self.user_input == "1":
            if o == "s":
                self.gs()
            else:
                self.gd()
        elif self.user_input == "0":
            print("Goodbye!")
            exit()
        else:
            print("Invalid entry - returning to genre select...")
            if o == "s":
                self.gs()
            else:
                self.gd()

    def gd(self):
        print("")
        print(
            boxen(
                "[green]Enter a movie genre to NOT generate from",
                "",
                "[blue]Press 1 to see a list of movie genres",
                "[dark_orange3]Press 2 to go back",
                "[bright_red]Press 0 to exit",
                title="-gd: Genre Deselect",
                color="white",
                padding=1,
            )
        )

        self.user_input = input("Enter here: ")
        self.gd_options(self.user_input)       

    def gd_options(self, usr_input):

        if usr_input == "1":
            self.show_movies("d")
        elif usr_input.lower() in self.genres:
            print("\nAre you sure you want to NOT generate any " + str(usr_input) + " movies? ")
            confirm = input("Y/N: ")
            if confirm.lower() == "y":
                print("\nSuccessfully removed " + str(usr_input) + " movies from generator!")
                print("Returning back to filters...")
                self.filters.append(usr_input)
            elif confirm.lower() == "n":
                print("\nUnsuccessfully removed " + str(usr_input) + " movies from generator")
                print("Returning back to filters...")
            else:
                print("\nInvalid input")
                print("Returning back to filters...")
        elif usr_input == "2":
            print("Returning back to filters...")
            self.browse_filters()
        elif usr_input == "0":
            print("Goodbye!")
            exit()
        else:
            print("Invalid input - please select from an available genre")
            self.show_movies("d")

        self.browse_filters()

if __name__ == "__main__":
    Generator()