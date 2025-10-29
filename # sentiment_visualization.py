# sentiment_visualization.py

from textblob import TextBlob
import matplotlib.pyplot as plt
import pandas as pd

# Sample dataset (you can replace this with CSV input)
data = {
    'Review': [
        'I love this product!',
        'This is the worst service I ever had.',
        'It is okay, nothing special.',
        'Amazing experience, very satisfied!',
        'Not good, I expected more.',
        'Excellent work, totally worth it!',
        'Terrible quality and rude staff.'
    ]
}

df = pd.DataFrame(data)

# Function to analyze sentiment
def get_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return 'Positive'
    elif polarity == 0:
        return 'Neutral'
    else:
        return 'Negative'

# Apply the function
df['Sentiment'] = df['Review'].apply(get_sentiment)

# Display data
print(df)

# Count of sentiments
sentiment_counts = df['Sentiment'].value_counts()

# Visualization 1: Pie chart
plt.figure(figsize=(6, 6))
plt.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=['green', 'blue', 'red'])
plt.title('Sentiment Distribution')
plt.show()

# Visualization 2: Bar chart
plt.figure(figsize=(6, 4))
plt.bar(sentiment_counts.index, sentiment_counts.values, color=['green', 'blue', 'red'])
plt.title('Sentiment Count Bar Chart')
plt.xlabel('Sentiment Type')
plt.ylabel('Count')
plt.show()

# Visualization 3: Polarity histogram
polarities = [TextBlob(text).sentiment.polarity for text in df['Review']]
plt.hist(polarities, bins=5, color='purple', edgecolor='black')
plt.title('Sentiment Polarity Distribution')
plt.xlabel('Polarity')
plt.ylabel('Frequency')
plt.show()