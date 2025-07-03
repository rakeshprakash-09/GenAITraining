def personal_greeting():
    print("👋 Welcome! Let's get to know you better.")

    # Ask for user inputs
    name = input("What's your name? ")
    age = input("How old are you? ")
    favorite_color = input("What's your favorite color? ")

    # Generate and print personalized message
    print("\n--- Personalized Greeting ---")
    print(f"Hi {name}! 🌟 You're {age} years young and love the color {favorite_color}. That's awesome!")
    print("Have a colorful and amazing day! 🎉")

# Run the function
if __name__ == "__main__":
    personal_greeting()
