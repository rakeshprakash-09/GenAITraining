import streamlit as st
import math

# Area calculation functions
def area_circle(radius):
    return math.pi * radius ** 2

def area_rectangle(length, width):
    return length * width

def area_triangle(base, height):
    return 0.5 * base * height

st.title('Area Calculator')

shape = st.selectbox('Select a shape:', ['Circle', 'Rectangle', 'Triangle'])

if shape == 'Circle':
    radius = st.number_input('Enter the radius:', min_value=0.0, format='%f')
    if st.button('Calculate Area'):
        area = area_circle(radius)
        st.success(f'The area of the circle is {area:.2f}')
elif shape == 'Rectangle':
    length = st.number_input('Enter the length:', min_value=0.0, format='%f')
    width = st.number_input('Enter the width:', min_value=0.0, format='%f')
    if st.button('Calculate Area'):
        area = area_rectangle(length, width)
        st.success(f'The area of the rectangle is {area:.2f}')
elif shape == 'Triangle':
    base = st.number_input('Enter the base:', min_value=0.0, format='%f')
    height = st.number_input('Enter the height:', min_value=0.0, format='%f')
    if st.button('Calculate Area'):
        area = area_triangle(base, height)
        st.success(f'The area of the triangle is {area:.2f}') 