from pyboxen import boxen
from rich.table import Table

class Generator:
    def __init__(self):
        self.user_input = None
        self.filters = []
        self.genres = ["action", "adventure","animation","biography","comedy","crime", "documentary", "drama", "family", "fantasy",  "history", "horror", "musical", "mystery", "romance", "sciFi", "sport","thriller", "war", "western"]
        self.times = ["60", "90", "120", "150", "180"]
        self.ratings = ["G", "PG", "PG13", "R", 'NC17']
        self.decades= ["1900-1909", "1910-1919", "1920-1929", "1930-1939", "1940-1949", "1950-1959", "1960-1969", "1970-1979", "1980-1989", "1990-1999", "2000-2009", "2010-2019", "2020-2029"]

        self.welcome_message()

    def welcome_message(self):
        print("")

        print(
            boxen(
                "[green]Enter [green]1[/green] to generate a random movie[/green]",
                "[blue]Enter 2 to browse or enter a filter[blue]",
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
            self.show_movies()
        elif num =="2":
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
        elif usr_input == "-t" or usr_input == "--time":
            self.time()
        elif usr_input == "-r" or usr_input == "--rated":
            self.rated()
        elif usr_input == "-d" or usr_input == "--decade":
            self.decade()
        elif usr_input == "-s" or usr_input == "--snob":
            self.snob()
        elif usr_input == "-n" or usr_input == "--num":
            self.num()
        elif usr_input == "1":
            self.show_filters()
        elif usr_input == "2":
            self.welcome_message()
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
                "[blue]Enter 1 to see a list of movie genres",
                "[dark_orange3]Enter 2 to go back",
                "[bright_red]Enter 0 to exit",
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
                print("\nInvalid entry")
                print("Returning back to filters...")
        elif usr_input == "2":
            print("Returning back to filters...")
        elif usr_input == "0":
            print("Goodbye!")
            exit()
        else:
            print("\nInvalid entry - please select from an acceptabl genre")
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
                "[blue]Enter 1 to see a list of movie genres",
                "[dark_orange3]Enter 2 to go back",
                "[bright_red]Enter 0 to exit",
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
                print("\nInvalid entry")
                print("Returning back to filters...")
        elif usr_input == "2":
            print("Returning back to filters...")
        elif usr_input == "0":
            print("Goodbye!")
            exit()
        else:
            print("\nInvalid entry - please select from an acceptable genre")
            self.show_movies("d")

        self.browse_filters()

    def time(self):
        print("")
        print(
            boxen(
                "[green]Enter the maximum movie duration",
                "",
                "[blue]Enter 1 to see a list of acceptable times",
                "[dark_orange3]Enter 2 to go back",
                "[bright_red]Enter 0 to exit",
                title="-t: Time Select",
                color="white",
                padding=1,
            )
        )

        self.user_input = input("Enter here: ")
        self.time_options(self.user_input)
        
    def time_options(self, usr_input):
        if usr_input == "1":
            self.show_time()
        elif usr_input in self.times:
            print("Are you sure you want to generate movies with a maximum duration of " + str(usr_input) + " minutes?")
            confirm = input("Y/N: ")
            if confirm.lower() == "y":
                print("\nSuccessfully added movie duration of max " + str(usr_input) + " minutes to filters!")  
                print("Returning back to filters...")
            elif confirm.lower() == "n":
                print("\nUnsucessfully added movie duration of max " + str(usr_input) + " minutes to filters")
                print("Returning back to filters...")
            else: 
                print("\nInvalid input")
                print("Returning back to filters...")
        elif usr_input == "2":
            print("Returning back to filters...")
        elif usr_input == "0":
            print("Goodbye!")
            exit()
        else:
            print("\nInvalid input - please select from an acceptable time")
            self.show_time()
        
        self.browse_filters()


    def show_time(self):
        table = Table(show_header=False, header_style="bold magenta")

        table.add_column
        table.add_column
        table.add_column
        table.add_column
        table.add_column
        table.add_row(
            "60", "90", "120", "150", "180"
        )

        print("")

        print(
            boxen(
                "Movie Time Durations in Minutes",
                "",
                "[dark_orange3]Enter 1 to go back and enter a time  [/dark_orange3]",
                "[bright_red]Enter 0 to exit[/bright_red]",
                table
            )
        )

        self.user_input = input("Enter here: ")
        if self.user_input == "1":
            self.time()
        elif self.user_input == "0":
            print("Goodbye!")
        else:
            print("Invalid entry - returning to time select...")
            self.time()
        
    def rated(self):
        print("")
        print(
            boxen(
                "[green]Enter a movie rating category to NOT generate from ",
                "",
                "[blue]Enter 1 to see a list of acceptable ratings",
                "[dark_orange3]Enter 2 to go back",
                "[bright_red]Enter 0 to exit",
                title="-r: Rated Deselect",
                color="white",
                padding=1,
            )
        )

        self.user_input = input("Enter here: ")
        self.r_options(self.user_input)

    def r_options(self, usr_input):
        if usr_input == "1":
            self.show_ratings()
        elif usr_input.upper() in self.ratings:
            print("Are you sure you want to exclude movies with a " + str(usr_input.upper()) + " rating?")
            confirm = input("Y/N: ")
            if confirm.lower() == "y":
                print("\nSuccessfully removed " + str(usr_input.upper()) + " movies from generator")
                print("Returning back to filters...")
            elif confirm.lower() == "n":
                print("\nUnsuccessfully removed " + str(usr_input.upper()) + " movies from generator")
                print("Returning back to filters...")
            else:
                print("\nInvalid entry")
                print("Returning back to filters...")
        elif usr_input == "2":
            print("Returning back to filters...")
        elif usr_input == "0":
            print("Goodbye!")
            exit()
        else:
            print("\nInvalid entry - please select from an acceptable rating")
            self.show_ratings()

        self.browse_filters()
    
    def show_ratings(self):
        table = Table(show_header=False, header_style="bold magenta")

        table.add_column
        table.add_column
        table.add_column
        table.add_column
        table.add_column
        table.add_row(
            "G", "PG", "PG13", "R", "NC17"
        )

        print("")

        print(
            boxen(
                "Movie Ratings",
                "",
                "[dark_orange3]Enter 1 to go back and enter a rating  [/dark_orange3]",
                "[bright_red]Enter 0 to exit[/bright_red]",
                table
            )
        )

        self.user_input = input("Enter here: ")
        if self.user_input == "1":
            self.rated()
        elif self.user_input == "0":
            print("Goodbye!")
        else:
            print("Invalid entry - returning to rating select...")
            self.rated()
    
    def decade(self):
        print("")
        print(
            boxen(
                "[green]Enter a decade to generate from",
                "",
                "[blue]Enter 1 to see a list of acceptable decades",
                "[dark_orange3]Enter 2 to go back",
                "[bright_red]Enter 0 to exit",
                title="-d: Decade Select",
                color="white",
                padding=1,
            )
        )

        self.user_input = input("Enter here: ")
        self.decade_options(self.user_input)

    def decade_options(self, usr_input):
        if usr_input == "1":
            self.show_decades()
        elif usr_input in self.decades:
            print("Are you sure you want to generate movies from " + str(usr_input) + "?")
            confirm = input("Y/N: ")
            if confirm.lower() == "y":
                print("\nSuccessfully added movies from " + str(usr_input) + " to filters!")
                print("Returning back to filters...")
            elif confirm.lower() == "n":
                print("\nUnsuccessfully added movies from " +str(usr_input) + " to filters")
                print("Returning back to filters...")
            else:
                print("\nInvalid entry")
                print("Returning back to filters...")
        elif usr_input == "2":
            print("Returning back to filters...")
        elif usr_input == "0":
            print("Goodbye!")
            exit()
        else:
            print("\nInvalid input - please select from an acceptable decade")
            self.show_decades()
        
        self.browse_filters()
        
    
    def show_decades(self):
        table = Table(show_header=False, header_style="bold magenta")

        table.add_column
        table.add_column
        table.add_column
        table.add_column
        table.add_row(
            "1900-1909", "1910-1919", "1920-1929", "1930-1939",
        )
        table.add_row(
            "1940-1949", "1950-1959", "1960-1969", "1970-1979",
        )
        table.add_row(
            "1980-1989", "1990-1999", "2000-2009", "2010-2019",
        )
        table.add_row(
            "2020-2029"
        )

        print("")

        print(
            boxen(
                "Decades",
                "",
                "[dark_orange3]Enter 1 to go back and enter a decade  [/dark_orange3]",
                "[bright_red]Enter 0 to exit[/bright_red]",
                table
            )
        )

        self.user_input = input("Enter here: ")
        if self.user_input == "1":
            self.decade()
        elif self.user_input == "0":
            print("Goodbye!")
        else:
            print("Invalid entry - returning to time select...")
            self.decade()

    def snob(self):
        print("")
        print(
            boxen(
                "[green]Generate movies with 3.5 stars or higher",
                "",
                "[blue]Enter 1 to activate snob mode",
                "[dark_orange3]Enter 2 to go back",
                "[bright_red]Enter 0 to exit",
                title="-s: Snob Toggle",
                color="white",
                padding=1,
            )
        )

        self.user_input = input("Enter here: ")
        self.snob_options(self.user_input)

    def snob_options(self, usr_input):
        if usr_input == "1":
            print("Are you sure you want to only generate movies with 3.5 stars or higher?")
            confirm = input("Y/N: ")
            if confirm.lower() == "y":
                print("\nSuccesfully turned on snob mode")
                print("Returning back to filters...")
            elif confirm.lower() == "n":
                print("\nUnsuccessfully turned on snob mode")
                print("Returning back to filters...")
            else:
                print("\nInvalid entry")
                print("Returning back to filters...")
        elif usr_input == "2":
            print("Returning back to filters...")
        elif usr_input == "0":
            print("Goodbye!")
            exit()
        else:
            print("\nInvalid entry - returning back to filters")

        self.browse_filters()

    def num(self):
        print("")
        print(
            boxen(
                "[green]Please enter the number of movies to generate",
                "",
                "Minimum: 1",
                "Maximum: 10",
                "",
                "[dark_orange3]Enter - to go back",
                "[bright_red]Enter 0 to exit",
                title="-n: Number to Generate",
                color="white",
                padding=1,
            )
        )

        self.user_input = input("Enter here: ")
        self.num_options(self.user_input)
    
    def num_options(self, usr_input):
        if usr_input == "-" or usr_input.isnumeric() == False:
            print("Returning back to filters...")
            self.browse_filters()
        if 10 >= int(usr_input) and int(usr_input) >= 1:
            print("\nAre you sure you want to generate " + str(usr_input) + " movies?")
            confirm = input("Y/N: ")
            if confirm.lower() == "y":
                print("\nSuccessfully configured generator to generat " + str(usr_input) + " movies")
            elif confirm.lower() == "n":
                print("\nUnsuccessfully configured generator to generate " + str(usr_input) + " movies")
                print("Generating 1 movie")
            else:
                print("\nInvalid entry")
                print("Returning back to filters...")
        elif usr_input == "0":
            print("Goodbye")
            exit()
        else:
            print("\nInvalid number - please enter a number between 1 and 10")
            self.num()

        self.browse_filters()

    def show_filters(self):
        print("")
        print(
    boxen(
        "A. 90 minute movies",
        "B. No horror movies",
        "C. 1920-1929 decade",
    
        "",
        "[blue]Enter the letter of the filter to remove",
        "[yellow]Enter 1 to remove all",
        "",
        "[dark_orange3]Enter 2 to go back",
        "[bright_red]Enter 0 to exit",
        title="[magenta]Current Filters Applied to Generator",
        color="white",
        padding=1,
        )
        )
    
        self.user_input = input("Enter here: ")
        self.curr_options(self.user_input)

    def curr_options(self, usr_input):
        if usr_input.lower() == "a":
            print("Are you sure you want to remove filter A?")
            confirm = input("Y/N: ")
            if confirm.lower() == "y":
                print("\nSuccessfully removed A from current filters")
                print("Returning to current filters...")
            elif confirm.lower() == "n":
                print("\nUnsuccessfully removed A from current filters")
                print("Returning back to current filters...")
            else:
                print("\nInvalid entry - returning to current filters...")
        elif usr_input == '1':
            print("Are you sure you want to remove all current filters?")
            confirm = input("Y/N: ")
            if confirm.lower() == "y":
                print("\nSuccessfully removed all current filters")
                print("Returning back to current filters...")
            elif confirm.lower() == "n":
                print("\nUnsuccessfully removed all current filters")
                print("Returning back to current filters...")
            else:
                print("\nInvalid entry - returning to current filters...")
        elif usr_input == "2":
            print("Returning back to filters options...")
            self.browse_filters()
        elif usr_input == "0":
            print("\nGoodbye!")
            exit()
        else:
            print("Invalid entry - returning to filters options...")
            self.browse_filters()
        
        self.show_filters()

    def show_movies(self):
        print("")
        print(
    boxen(
        "A. The Blues Brothers",
        "B. Evil Dead II",
        "C. Rosemary's Baby",
        "D. Burlesque",
        "",
         "[blue]Enter the letter of the movie you'd like to see a description of",
         "",
        "[green]Enter 1 to generate again",
        "[dark_orange3]Enter 2 to go back",
        "[bright_red]Enter 0 to exit",
        title="Here are your random movies!",
        color="magenta",
        padding=1,
    )
)
        self.user_input = input("Enter here: ")
        self.movies_input(self.user_input)

    def movies_input(self, usr_input):
        if usr_input.lower() == "A":
            print(
                boxen(
                    "The story is a tale of redemption for paroled convict Jake and his blood",
                    "brother Elwood, who set out on a 'mission' from God to prevent foreclosure",
                    "of the Roman Catholic orphanage in which they were raised.",
                    "",
                     "[dark_orange3]Press 1 to go back",
                    "[bright_red]Press 0 to exit",
                    padding=1,
                    margin=1,
                    title="The Blues Brothers",
                    color="blue"
                )
            )
            option = input("Enter here: ")
            if option == "1":
                self.show_movies()
            elif option =="0":
                print("\nGoodbye!")
                exit()
            else:
                self.show_movies()
        elif usr_input == "1":
            print("\nGenerating new movies...")
            self.show_movies()
        elif usr_input == "0":
            print("\nGoodbye!")
            exit()
        elif usr_input == "2":
            self.welcome_message()
        else:
            print("\nInvalid entry - returning home")
            self.welcome_message()      
if __name__ == "__main__":
    Generator()