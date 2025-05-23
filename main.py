#import
import streamlit as st
import ollama
from dotenv import load_dotenv
import os

load_dotenv()

#set the title and a short description for the site
st.title("Talk This Recipe")
st.subheader("your health buddy")

#design the boxes to choose 
boxes = st.radio("Pick a meal box", ["5 ingredients style", "swap the plate (no regret)"])


#set the app
def prompt_generate_ollama(prompt):
    response = ollama.chat(
        model='llama3',
        messages=[{"role":"user", "content":prompt}],
        stream = False
    )
    return response['message']['content']

#choosing boxes
if boxes == "5 ingredients style":
    ingredients = st.text_input("enter 5 ingredients:", placeholder="spinach, tomato, onion, eggs, turmeric")

    if st.button("cook"):
        if len(ingredients.split(",")) < 5:
            st.warning("Please enter at least 5 ingredients")
        else:
            prompt = f"""You are now a chef, Given the ingredients: {ingredients}, generate a healthy dish but it should not be a smoothie, shake, or a salad bowl
            Include:
            1. Unique dish name
            2. Instructions to cook the dish(include every minute details like tablespoons, baking, sauteing)
            3. Nutritional information (calories, fat, protein, carbs)
            4. healthy benefit of having this dish in one sentence
            Make it fun, original, flvorful
            """
            output = prompt_generate_ollama(prompt)
            st.success("enjoy the meal")
            st.markdown(output)

elif boxes == "swap the plate (no regret)":
    junkie = st.text_input("well, I am craving for...", placeholder="burger, pizza, ice cream, soda")

    if st.button("swap it"):
        if not junkie:
            st.warning("enter your craving for a healthy swap, you will have no regrets")
        else:
            prompt = f"""You are a health freak, the user has entered their junk craving: {junkie}, generate the following:
            1. generate a healthier version of the food but satisfies the taste
            2. give a unique dish name and the ingredients required
            3. generate the steps to make the dish
            4. list out the junk version: calories, fat, protein, carb and healthy version generated: calories, fat, proteib, carb
            5. one sentence with healthier version benefit 
            Make it fun, original, flvorful
            """

            output = prompt_generate_ollama(prompt)
            st.success("zero regret swap")
            st.markdown(output)



