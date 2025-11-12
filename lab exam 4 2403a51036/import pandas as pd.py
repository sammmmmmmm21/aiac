import pandas as pd
import re
from nltk.corpus import stopwords
import nltk

# Download stopwords (run once) - suppress download messages
import os
import warnings
warnings.filterwarnings('ignore')

try:
    stopwords.words('english')
except LookupError:
    print("Downloading NLTK stopwords...")
    nltk.download('stopwords', quiet=True)

# Generate sample data
data = {
    'review': [
        "Great Product! Rating: 5/5. Highly recommended!!!",
        "Terrible quality. NOT worth $50. Very disappointed.",
        "Amazing service! 100% satisfied. Will buy again!",
        "Poor packaging & damaged items. Refund requested ASAP!",
        "Best purchase ever made! 10/10 would recommend."
    ]
}

df = pd.DataFrame(data)

# Display original data
print("=" * 80)
print("ORIGINAL REVIEWS:")
print("=" * 80)
print(df['review'].to_string())

# Task 1: Remove special characters and numbers
df['cleaned_review'] = df['review'].str.replace(r'[^a-zA-Z\s]', '', regex=True)

# Task 2: Convert to lowercase and remove stop words
stop_words = set(stopwords.words('english'))
df['processed_review'] = df['cleaned_review'].apply(
    lambda x: ' '.join([word for word in x.lower().split() if word not in stop_words])
)

# Display processed data
print("\n" + "=" * 80)
print("AFTER CLEANING (Removed special characters and numbers):")
print("=" * 80)
print(df['cleaned_review'].to_string())

print("\n" + "=" * 80)
print("AFTER PROCESSING (Removed stopwords and converted to lowercase):")
print("=" * 80)
print(df['processed_review'].to_string())

print("\n" + "=" * 80)
print("FINAL DATAFRAME:")
print("=" * 80)
print(df)