# Movie-Recommendation-System 🎥
This project is a Movie Recommendation System built using the Cosine Similarity technique for measuring similarity between movies based on their content features. The system leverages PorterStemmer, CountVectorizer, and various data processing libraries such as pandas and ast. The recommendation model is saved using pickle for efficient loading, and a user-friendly web interface has been developed using Streamlit.

# Features ⚙️
1. Content-based movie recommendations using cosine similarity.
2. Preprocessing of movie metadata with stemming to improve recommendation accuracy.
3. Efficient model persistence using pickle.
4. Interactive and responsive frontend built with Streamlit.

# Libraries Used 📚
1. numpy: For numerical computations.
2. pandas: To manage and preprocess tabular data.
3. scikit-learn: For using CountVectorizer and computing cosine similarity.
4. nltk (Natural Language Toolkit): For stemming using PorterStemmer.
5. ast: To safely evaluate and parse strings from movie metadata.
6. pickle: For saving and loading the trained recommendation model.
7. streamlit: For creating the web application.

# Conclusion 🏁
This project demonstrates an effective way to build a movie recommendation system using text-based features. With a clean and simple interface powered by Streamlit, users can easily discover new movie recommendations.
