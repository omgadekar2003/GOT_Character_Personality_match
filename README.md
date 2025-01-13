# 🐉 Game of Thrones Personality Matcher  

An **interactive Streamlit app** that matches your favorite Game of Thrones character with their closest personality match! Dive into the world of Westeros and discover exciting character connections.  

🔗 **Live Demo**: [Game of Thrones Personality Matcher](https://got-ml-om.streamlit.app/)  

---

## 🚀 Features  

- 🔍 **Interactive Character Selector**: Choose from a list of iconic Game of Thrones characters.  
- 🖼 **Visual Character Match**: See your selected character alongside their closest match with images.  
- 📊 **Data-Driven Matching**: Matches are calculated based on personality embeddings using Euclidean distance.  
- 🌐 **Real-Time Data Fetching**: Character details and images are fetched from the **Thrones API**.  

---

## 📚 How It Works  

1. Select a character from the dropdown menu.  
2. The app calculates the closest match based on personality embeddings.  
3. View the selected character and their match with side-by-side images.  

---

## 🛠 Tech Stack  

- **Frontend**: [Streamlit](https://streamlit.io/)  
- **Backend**: Python  
- **Data**: Thrones API, Pickle  
- **Libraries**:  
  - `streamlit`  
  - `numpy`  
  - `pandas`  
  - `requests`  

---

## 📂 Project Structure  

```plaintext
GOT_Character_Personality_match/
├── app.py                # Main application file
├── got_character_embeddings.pkl  # Dataset with personality embeddings
├── requirements.txt      # List of dependencies
├── README.md             # Project documentation
```

---

## ⚙️ Installation  

1. **Clone the repository**:  
   ```bash
   git clone https://github.com/omgadekar2003/GOT_Character_Personality_match.git
   cd GOT_Character_Personality_match
   ```  

2. **Install dependencies**:  
   ```bash
   pip install -r requirements.txt
   ```  

3. **Run the app**:  
   ```bash
   streamlit run app.py
   ```  

4. Open the app in your browser at `http://localhost:8501`.  

---

## 🌟 Live Demo  

Experience the app in action here: [Game of Thrones Personality Matcher](https://got-ml-om.streamlit.app/)  

---

## 👤 Author  

- **Name**: Om Gadekar  
- **Email**: omgadekar25@gmail.com  
- **GitHub**: [omgadekar2003](https://github.com/omgadekar2003)  

---

## 📝 License  

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).  

---

## 🤝 Contributing  

1. Fork the repository.  
2. Create a new branch for your feature: `git checkout -b feature-name`.  
3. Commit your changes: `git commit -m "Add feature-name"`.  
4. Push to the branch: `git push origin feature-name`.  
5. Submit a pull request.  

---

## 🙌 Acknowledgments  

- **Thrones API**: For providing detailed character data.  
- **Streamlit**: For building an interactive and intuitive UI.  
- **Game of Thrones**: For being the inspiration behind this project.  

