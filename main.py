import langchain_helper as lch 
import streamlit as st 

st.title("Pets name Generator")

animal_type = st.sidebar.selectbox("What is the name of your pet?", ("Cat", "Dog", "Parrot","Hamster"))

if animal_type == "Cat":
    pet_color = st.sidebar.text_area("What color is your cat?", max_chars=15)

if animal_type == "Dog":
    pet_color = st.sidebar.text_area("What color is your dog?", max_chars=15)

if animal_type == "Parrot":
    pet_color = st.sidebar.text_area("What color is your parrot?", max_chars=15)

if animal_type == "Hamster":
    pet_color = st.sidebar.text_area("What color is your hamster?", max_chars=15)


if pet_color:
    response = lch.generate_pet_name(animal_type=animal_type, pet_color=pet_color)    
    st.text(response["pet_name"])