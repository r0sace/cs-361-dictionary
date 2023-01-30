from pyboxen import boxen
import keyboard

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

num = input("Enter here: ")

#stop fucking with the fucking key presses and just do input
#figure out a way to get the input to look nice -_-