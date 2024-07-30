import streamlit as st
import random
import string
import warnings
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from nltk.stem import WordNetLemmatizer
import json

# Download necessary NLTK packages
nltk.download('popular', quiet=True)

# Define lemmatizer
Netlemmer = WordNetLemmatizer()

def LemTok(tokens):
    return [Netlemmer.lemmatize(token) for token in tokens]

# Remove punctuation and normalize text
rem_punct_dict = dict((ord(punct), None) for punct in string.punctuation)

def LemNorm(text):
    return LemTok(nltk.word_tokenize(text.lower().translate(rem_punct_dict)))

# Load intents
with open('intents.json') as json_file:
    intents = json.load(json_file)

# Function to get greeting response
def greet(sentence):
    for intent in intents['intents']:
        if intent['tag'] == 'greeting':
            for pattern in intent['patterns']:
                if pattern.lower() in sentence.lower():
                    return random.choice(intent['responses'])

# Generate response from the chatbot
def response(user_response):
    user_response = user_response.lower()
    TfidfVec = TfidfVectorizer(tokenizer=LemNorm, stop_words='english')
    tfidf = TfidfVec.fit_transform([user_response] + [pattern for intent in intents['intents'] for pattern in intent['patterns']])
    vals = cosine_similarity(tfidf[0:1], tfidf[1:])
    idx = vals.argsort()[0][-1]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-1]

    if req_tfidf == 0:
        return "I am sorry! I don't understand you"
    else:
        # Find the intent with the pattern that matches the user response
        matching_intent = None
        for intent in intents['intents']:
            if user_response in intent['patterns']:
                matching_intent = intent
                break
        if matching_intent:
            return random.choice(matching_intent['responses'])
        else:
            return "I am sorry! I don't understand you"

# BMI calculator
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert height from cm to meters
    bmi = weight / (height_m ** 2)
    return bmi

# Streamlit app
def main():
    st.title("Aasha: Your Fitness Guidance Buddy")
    st.write("Aasha: My name is Aasha. I will answer your queries about fitness and nutrition. If you want to exit, type Bye!")

    if 'conversation' not in st.session_state:
        st.session_state.conversation = []

    if 'bmi' not in st.session_state:
        st.session_state.bmi = None
        st.session_state.bmi_status = None
        st.session_state.show_bmi_input = False

    # Display chat messages from history on app rerun
    for message in st.session_state.conversation:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Accept user input
    user_input = st.chat_input("Type your query:")
    if user_input:
        user_input = user_input.lower()
        
        # Display user message in chat message container
        with st.chat_message("user"):
            st.markdown(user_input)
        
        # Add user message to chat history
        st.session_state.conversation.append({"role": "user", "content": user_input})
        
        if user_input == 'bye':
            response_content = "Bye! take care.."
        elif user_input in ('thanks', 'thank you'):
            response_content = "You are welcome.."
        else:
            if greet(user_input) is not None:
                response_content = greet(user_input)
            else:
                response_content = response(user_input)
        
        # Display assistant response in chat message container
        with st.chat_message("assistant"):
            st.markdown(response_content)
        
        # Add assistant response to chat history
        st.session_state.conversation.append({"role": "assistant", "content": response_content})

        # Handle BMI calculation intent
        if 'bmi' in user_input:
            st.session_state.show_bmi_input = True

    # Display BMI input fields if the intent is to calculate BMI
    if st.session_state.show_bmi_input:
        with st.expander("Calculate your BMI"):
            st.write("Please enter your height and weight to calculate your BMI.")
            height = st.text_input('Enter your height in centimeters:')
            weight = st.text_input('Enter your weight in kilograms:')
            
            if st.button('Calculate BMI'):
                if height and weight:
                    try:
                        height = float(height)
                        weight = float(weight)
                        st.session_state.bmi = calculate_bmi(weight, height)
                        if st.session_state.bmi < 18.5:
                            st.session_state.bmi_status = "You are underweight."
                        elif 18.5 <= st.session_state.bmi < 24.9:
                            st.session_state.bmi_status = "You have a normal weight."
                        elif 25 <= st.session_state.bmi < 29.9:
                            st.session_state.bmi_status = "You are overweight."
                        else:
                            st.session_state.bmi_status = "You are obese."
                    except ValueError:
                        st.error("Please enter valid numbers for height and weight.")

            if st.session_state.bmi:
                st.write(f'Your BMI is {st.session_state.bmi:.2f}')
                st.write(st.session_state.bmi_status)

if __name__ == "__main__":
    main()

