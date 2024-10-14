# GOT_Character_Personality_match
The **Game of Thrones Personality Matcher** uses Machine Learning to analyze character dialogues from all 8 seasons, predicting similar personalities. Using the **T-SNE algorithm**, high-dimensional data is visualized in 2D. Through an interactive **Streamlit app**, users can select a character and discover others with similar dialogue patterns.
Project Overview: Game of Thrones Personality Matcher
I recently completed a Machine Learning project titled Game of Thrones Personality Matcher, where I aimed to predict characters with similar personalities based solely on their dialogues from the entire series. I used a T-SNE algorithm (T-distributed Stochastic Neighbor Embedding), which is commonly used for reducing high-dimensional data into 2D or 3D for visualization purposes.

Data Extraction and Processing
I sourced the dataset from Kaggle, which included all spoken dialogues from Season 1, Episode 1 to Season 8, Episode 8 of Game of Thrones. The dataset was structured in JSON format and contained the following columns:

episodeAlt: Alternate episode numbering
seasonNum: Season number
episodeNum: Episode number
episodeTitle: Title of the episode
text: The actual dialogue spoken by a character
From this dataset, I focused primarily on the text column to analyze each character’s dialogue and personality based on their spoken words. I restructured the data into the following columns:

character: Name of the character
words: The exact dialogue spoken
word_count: Total number of words spoken by each character
Key Insights
One interesting insight during the data processing was that Tyrion Lannister was the most talkative character throughout the series, having spoken 25,924 words.

Additionally, from 100 major characters, I identified around 15,335 unique words. These unique words were used to create 100-dimensional vectors (one vector for each character). In essence, each character’s dialogue was transformed into a high-dimensional vector based on the words they used, representing their speaking style and content.

Dimensionality Reduction & T-SNE Algorithm
Handling data in 15,000+ dimensions can be challenging, so I used the T-SNE algorithm to reduce the data from 15K dimensions into 2D for easier visualization. This allowed me to observe and plot the distance between characters based on the similarity of their dialogues. Characters with similar personalities (in terms of the words they frequently used) would be plotted closer together in the 2D space.

Streamlit App Integration
Once the analysis was completed, I integrated the results into a Streamlit app with a simple and intuitive user interface. The app allows users to select any character from the Game of Thrones series and view other characters who share similar speech patterns and, potentially, personality traits. To facilitate this, I serialized the data into a data.pkl file and loaded it into the Streamlit app to make it interactive.

Project Results
The app provides interesting personality matches based on dialogue structure. While the algorithm works well in many cases, there are some instances where dialogues might not perfectly reflect a character’s personality, especially for characters with fewer spoken lines. Overall, this project demonstrates how dialogue-based analysis can reveal potential personality matches.
