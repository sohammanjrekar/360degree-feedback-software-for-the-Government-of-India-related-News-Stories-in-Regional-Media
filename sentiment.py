import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

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

# Example text paragraphs
text1 = "The government of India is corrupt and inefficient."
text2 = "India is making significant progress in economic development."
text3 = "The india is incompetent and dishonest."

# Analyze sentiment for each text
sentiment1 = custom_sentiment(text1)
sentiment2 = custom_sentiment(text2)
sentiment3 = custom_sentiment(text3)

# Print the sentiment results
print("Sentiment 1:", sentiment1)
print("Sentiment 2:", sentiment2)
print("Sentiment 3:", sentiment3)
