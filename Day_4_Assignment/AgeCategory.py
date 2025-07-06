def determine_age_category(age):
    """
    Determine age category based on age.
    
    Args:
        age (int): Age of the person
        
    Returns:
        str: Age category (child, teenager, adult, senior)
    """
    if age < 0:
        return "Invalid age"
    elif age < 13:
        return "child"
    elif age < 20:
        return "teenager"
    elif age < 65:
        return "adult"
    else:
        return "senior"

def get_age_category_description(category):
    """
    Get a description for each age category.
    
    Args:
        category (str): Age category
        
    Returns:
        str: Description of the age category
    """
    descriptions = {
        "child": "A child is someone under 13 years old.",
        "teenager": "A teenager is someone between 13 and 19 years old.",
        "adult": "An adult is someone between 20 and 64 years old.",
        "senior": "A senior is someone 65 years old or older.",
        "Invalid age": "Age cannot be negative."
    }
    return descriptions.get(category, "Unknown category")

def main():
    """Main function to run the age category program."""
    print("=" * 50)
    print("AGE CATEGORY DETERMINER")
    print("=" * 50)
    
    while True:
        try:
            # Get age input from user
            age_input = input("\nEnter age (or 'quit' to exit): ").strip()
            
            # Check if user wants to quit
            if age_input.lower() in ['quit', 'q', 'exit']:
                print("\nThank you for using Age Category Determiner!")
                break
            
            # Convert input to integer
            age = int(age_input)
            
            # Determine age category
            category = determine_age_category(age)
            description = get_age_category_description(category)
            
            # Display results
            print(f"\nAge: {age}")
            print(f"Category: {category.title()}")
            print(f"Description: {description}")
            
        except ValueError:
            print("Error: Please enter a valid number for age.")
        except KeyboardInterrupt:
            print("\n\nProgram interrupted. Goodbye!")
            break

def test_age_categories():
    """Test function to demonstrate age categories with sample ages."""
    print("Testing age categories with sample ages:")
    print("-" * 40)
    
    test_ages = [5, 12, 13, 15, 19, 20, 30, 50, 64, 65, 70, 80, -5]
    
    for age in test_ages:
        category = determine_age_category(age)
        print(f"Age {age:2d}: {category.title()}")
    
    print("-" * 40)

if __name__ == "__main__":
    # Run test function first to show examples
    test_age_categories()
    print("\n" + "=" * 50)
    
    # Run main program
    main()
