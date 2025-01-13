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

# Set up the page title and layout
st.set_page_config(page_title="Game of Thrones Personality Matcher", page_icon=":dragon:", layout="wide")

# Display a header with logo and app title
st.markdown("""
    <style>
        .title {
            font-size: 40px;
            font-weight: bold;
            color: #FF6347;
        }
        .header {
            font-size: 25px;
            font-weight: bold;
            color: #4682B4;
        }
        .footer {
            font-size: 15px;
            color: #808080;
        }
    </style>
    <h1 class="title">🐉 Game of Thrones Personality Matcher</h1>
    <p class="header">Find your closest character match from the world of Westeros!</p>
""", unsafe_allow_html=True)

# Display an introductory image (replace with a URL of a GOT image)
st.image("https://upload.wikimedia.org/wikipedia/commons/2/2f/Game_of_Thrones_Logo.png", width=500)

# Fetch data from API
api_data = requests.get("https://thronesapi.com/api/v2/Characters").json()

# Load dataset
df = pickle.load(open('got_character_embeddings.pkl', 'rb'))
df = df.head(25)

# Correct character names
df['character'] = df['character'].str.replace('Jaime', 'Jamie')
df['character'] = df['character'].str.replace('Lord Varys', 'Varys')
df['character'] = df['character'].str.replace('Bronn', 'Lord Bronn')
df['character'] = df['character'].str.replace('Sandor Clegane', 'The Hound')
df['character'] = df['character'].str.replace('Robb Stark', 'Rob Stark')

# Function to fetch character images
def fetch_image(name, api_data):
    for item in api_data:
        if item['fullName'] == name:
            return item['imageUrl']

# Streamlit UI
st.subheader("Select a character to find your closest match:")

characters = df['character'].values
selected_character = st.selectbox("Choose your favorite character:", characters)

# Fetch closest match
character_id = np.where(df['character'].values == selected_character)[0][0]
x = df[['x', 'y']].values

distances = [np.linalg.norm(x[character_id] - x[i]) for i in range(len(x))]
recommended_id = sorted(list(enumerate(distances)), key=lambda x: x[1])[1][0]
recommended_character = df['character'].values[recommended_id]

# Fetch images for both selected and recommended characters
image_url = fetch_image(selected_character, api_data)
recommended_character_image_url = fetch_image(recommended_character, api_data)

# Display results
col1, col2 = st.columns(2)

with col1:
    st.header(f"{selected_character}")
    st.image(image_url, use_column_width=True)

with col2:
    st.header(f"Recommended Match: {recommended_character}")
    st.image(recommended_character_image_url, use_column_width=True)

# Footer section with contact information
st.markdown("""
    <div class="footer">
        <p>If you have any questions or suggestions, feel free to reach out to me:</p>
        <p><b>Email:</b> [omgadekar25@gmail.com](mailto:omgadekar25@gmail.com)</p>
        <p><b>GitHub:</b> [GOT_Character_Personality_Matcher](https://github.com/omgadekar2003/GOT_Character_Personality_match)</p>
    </div>
""", unsafe_allow_html=True)

# Display a closing message
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("""
    <div class="footer">
        <p>Thank you for using the Game of Thrones Personality Matcher! 🐉</p>
    </div>
""", unsafe_allow_html=True)
