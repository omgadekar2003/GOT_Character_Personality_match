# import streamlit as st
# import pickle
# import requests
# import numpy as np

# # Fetch data from API
# api_data = requests.get("https://thronesapi.com/api/v2/Characters").json()

# # Load dataset
# df = pickle.load(open('got_character_embeddings.pkl', 'rb'))
# df = df.head(25)

# # Correct character names
# df['character'] = df['character'].str.replace('Jaime', 'Jamie')
# df['character'] = df['character'].str.replace('Lord Varys', 'Varys')
# df['character'] = df['character'].str.replace('Bronn', 'Lord Bronn')
# df['character'] = df['character'].str.replace('Sandor Clegane', 'The Hound')
# df['character'] = df['character'].str.replace('Robb Stark', 'Rob Stark')

# # Function to fetch character images
# def fetch_image(name, api_data):
#     for item in api_data:
#         if item['fullName'] == name:
#             return item['imageUrl']

# # Streamlit UI
# st.title("Game Of Thrones Personality Matcher")

# characters = df['character'].values
# selected_character = st.selectbox("Select a character", characters)

# # Fetch closest match
# character_id = np.where(df['character'].values == selected_character)[0][0]
# x = df[['x', 'y']].values

# distances = [np.linalg.norm(x[character_id] - x[i]) for i in range(len(x))]
# recommended_id = sorted(list(enumerate(distances)), key=lambda x: x[1])[1][0]
# recommended_character = df['character'].values[recommended_id]

# # Fetch images
# image_url = fetch_image(selected_character, api_data)
# recommended_character_image_url = fetch_image(recommended_character, api_data)

# # Display results
# col1, col2 = st.columns(2)

# with col1:
#     st.header(selected_character)
#     st.image(image_url)

# with col2:
#     st.header(recommended_character)
#     st.image(recommended_character_image_url)



###
##
#


import streamlit as st
import pickle
import requests
import numpy as np

# Set page configuration with an icon and title
st.set_page_config(page_title="GOT Personality Matcher", page_icon="🐉", layout="wide")

# Custom header and styling
st.markdown("""
    <style>
    .header {
        font-size: 36px;
        font-weight: bold;
        color: #2E86C1;
        text-align: center;
        padding: 10px;
    }
    .sub-header {
        font-size: 18px;
        font-weight: lighter;
        color: #34495E;
        text-align: center;
    }
    .footer {
        font-size: 12px;
        color: #7F8C8D;
        text-align: center;
        padding: 20px;
    }
    .stSelectbox select {
        font-size: 18px;
    }
    </style>
""", unsafe_allow_html=True)

# Display header
st.markdown('<div class="header">🐉 Game of Thrones Personality Matcher</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">Find out which Game of Thrones character shares your vibe!</div>', unsafe_allow_html=True)

# Fetch data from Thrones API
api_data = requests.get("https://thronesapi.com/api/v2/Characters").json()

# Load dataset
df = pickle.load(open('got_character_embeddings.pkl', 'rb'))
df = df.head(25)

# Correct character names for consistency
df['character'] = df['character'].str.replace('Jaime', 'Jamie')
df['character'] = df['character'].str.replace('Lord Varys', 'Varys')
df['character'] = df['character'].str.replace('Bronn', 'Lord Bronn')
df['character'] = df['character'].str.replace('Sandor Clegane', 'The Hound')
df['character'] = df['character'].str.replace('Robb Stark', 'Rob Stark')

# Function to fetch character images from API data
def fetch_image(name, api_data):
    for item in api_data:
        if item['fullName'] == name:
            return item['imageUrl']

# Streamlit UI
st.title("Game Of Thrones Personality Matcher")

# Character selection dropdown
characters = df['character'].values
selected_character = st.selectbox("Select a character", characters, index=0)

# Calculate the closest match
character_id = np.where(df['character'].values == selected_character)[0][0]
x = df[['x', 'y']].values

# Calculate distances between the selected character and others
distances = [np.linalg.norm(x[character_id] - x[i]) for i in range(len(x))]
recommended_id = sorted(list(enumerate(distances)), key=lambda x: x[1])[1][0]
recommended_character = df['character'].values[recommended_id]

# Fetch images for the selected and recommended characters
image_url = fetch_image(selected_character, api_data)
recommended_character_image_url = fetch_image(recommended_character, api_data)

# Display results in columns
col1, col2 = st.columns(2)

with col1:
    st.header(f"Your Character: {selected_character}")
    st.image(image_url, use_container_width=True)

with col2:
    st.header(f"Recommended Match: {recommended_character}")
    st.image(recommended_character_image_url, use_container_width=True)

# Footer with additional info
st.markdown('<div class="footer">Created by <b>Om Gadekar</b> | GitHub: <a href="https://github.com/omgadekar2003/GOT_Character_Personality_match" target="_blank">GOT Character Personality Matcher</a> | Email: <a href="mailto:omgadekar25@gmail.com">omgadekar25@gmail.com</a></div>', unsafe_allow_html=True)
