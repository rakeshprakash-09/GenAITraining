import streamlit as st

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


st.title("Age Category Determiner")

st.write("Enter your age to find out your age category.")

age_input = st.number_input("Enter your age", min_value=-100, max_value=150, value=20, step=1)

if st.button("Determine Category"):
    category = determine_age_category(age_input)
    description = get_age_category_description(category)
    st.markdown(f"**Category:** {category.title()}")
    st.info(description)

# Show test cases as a table
st.markdown("---")
st.subheader("Sample Age Categories")
test_ages = [5, 12, 13, 15, 19, 20, 30, 50, 64, 65, 70, 80, -5]
test_data = []
for age in test_ages:
    category = determine_age_category(age)
    test_data.append({"Age": age, "Category": category.title()})
st.table(test_data)
