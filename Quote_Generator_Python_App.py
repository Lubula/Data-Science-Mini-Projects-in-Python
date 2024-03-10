# Overview: command-line app allowing user to generate random quotes and add their own quotes to the collection. 
# Am a fan of beautiful quotes
# The quotes are stored in a text file for persistence.

import os
import random

# File to store quotes
QUOTES_FILE = "quotes.txt"

# Function to load quotes from a file
def load_quotes():
    """Load quotes from the file if it exists."""
    quotes = []
    if not quotes_file_exists():
        return quotes

    with open(QUOTES_FILE, "r") as file:
        for line in file:
            quotes.append(line.strip())
    return quotes

# Function to save quotes to a file
def save_quotes(quotes):
    """Save quotes to the file."""
    with open(QUOTES_FILE, "w") as file:
        for quote in quotes:
            file.write(quote + "\n")

# Function to check if the quotes file exists
def quotes_file_exists():
    """Check if the quotes file exists."""
    return os.path.exists(QUOTES_FILE)

# Function to display the menu
def display_menu():
    """Display the menu options for the user."""
    print("1. Generate Random Quote")
    print("2. Add Your Own Quote")
    print("3. Exit")

# Function to generate a random quote
def generate_random_quote(quotes):
    """Generate and display a random quote."""
    if not quotes:
        print("No quotes available. Add some quotes first.")
    else:
        print("Random Quote:")
        print(random.choice(quotes))

# Function to add a user-defined quote
def add_user_quote(quotes):
    """Allow the user to add their own quote."""
    user_quote = input("Enter your quote: ")
    if user_quote.strip():  # Check if the user provided a non-empty quote
        quotes.append(user_quote)
        save_quotes(quotes)
        print("Quote added successfully!")
    else:
        print("Invalid input. Quote cannot be empty.")

# Main function
def main():
    """Main function to run the quote generator."""
    # Load existing quotes from the file
    quotes = load_quotes()

    while True:
        # Display the menu
        display_menu()
        # Get user input for the menu choice
        choice = input("Enter your choice: ")

        # Perform the corresponding action based on the user's choice
        if choice == "1":
            generate_random_quote(quotes)
        elif choice == "2":
            add_user_quote(quotes)
        elif choice == "3":
            print("Exiting the Quote Generator.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")

if __name__ == "__main__":
    # Run the main function when the script is executed
    main()
