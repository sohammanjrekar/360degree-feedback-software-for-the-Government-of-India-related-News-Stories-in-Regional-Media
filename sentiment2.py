import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Download the VADER lexicon if not already downloaded
nltk.download('vader_lexicon')

# Define a custom sentiment analysis function
def custom_sentiment(text):
    # List of negative words
    negative_words = [
        "corrupt", "inefficient", "incompetent", "dishonest", "unreliable",
        "untrustworthy", "inept", "unpopular", "incapable"
    ]

    # Initialize the VADER sentiment analyzer
    sid = SentimentIntensityAnalyzer()

    # Tokenize the text and convert to lowercase
    tokens = nltk.word_tokenize(text.lower())

    # Calculate sentiment scores using VADER
    sentiment_scores = sid.polarity_scores(text)

    # Check if any negative word is present in the text
    has_negative_word = any(word in tokens for word in negative_words)

    # Check if the text mentions "government" or "India"
    mentions_government_or_india = "government" in tokens or "india" in tokens

    # Determine the overall sentiment
    if has_negative_word and mentions_government_or_india:
        return "Negative"
    else:
        return "Positive"

# List of news articles
news_articles = [
    "The government of India is corrupt and inefficient.",
    "India is making significant progress in economic development.",
    "The soham is incompetent and dishonest."
]

# Labels for the news articles (Positive or Negative)
labels = ["Negative", "Positive", "Negative"]

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(news_articles, labels, test_size=0.2, random_state=42)

# Initialize TF-IDF vectorizer
tfidf_vectorizer = TfidfVectorizer(max_features=5000)
X_train_tfidf = tfidf_vectorizer.fit_transform(X_train)
X_test_tfidf = tfidf_vectorizer.transform(X_test)

# Initialize and train a Support Vector Machine (SVM) classifier
svm_classifier = SVC(kernel='linear')
svm_classifier.fit(X_train_tfidf, y_train)

# Predict sentiments on the test set
y_pred = svm_classifier.predict(X_test_tfidf)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
report = classification_report(y_test, y_pred)

# Print results
print(f'Accuracy: {accuracy}')
print(report)
