"""
Author: Tarik Smith
Course: CSD 325 - Advanced Python
Assignment: Module 1.3 - On the Wall + Flowchart
Date: 12/7/2025

Description:
This program asks the user how many bottles of beer are on the wall,
then passes the number to a countdown function. The function displays
the reverse counting lyrics of the 'Bottles of Beer on the Wall' song.
After reaching 1 bottle, the program reminds the user to buy more beer.
"""

def countdown(n):
    """Prints the countdown for the bottles of beer song."""
    while n > 1:
        print(f"{n} bottles of beer on the wall, {n} bottles of beer.")
        print(f"Take one down, pass it around, {n-1} bottles of beer on the wall.\n")
        n -= 1

    # Handle final bottle
    print("1 bottle of beer on the wall, 1 bottle of beer.")
    print("Take one down, pass it around, no more bottles of beer on the wall!\n")


def main():
    """Main program loop."""
    num = int(input("How many bottles of beer are on the wall? "))
    countdown(num)
    print("Time to buy more beer!")


if __name__ == "__main__":
    main()
