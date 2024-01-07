import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from wordcloud import WordCloud


# Download NLTK resources (run this once)
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')


EXCLUDE = ['problem', 'business', 'solution', 'model', 'also',
           'would', 'should', 'could', 'use']
IMAGE_DIR = 'images/'


def load_csv(file_name):
    # Load your dataset (replace 'your_dataset.csv' with your actual dataset file path)
    df = pd.read_csv(file_name, encoding='ISO-8859-1')
    df.dropna(inplace=True)
    return df


def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = ''.join([char for char in text if char.isalpha() or char.isspace()])

    # Tokenize the text
    tokens = word_tokenize(text)

    # Remove stop words
    stop_words = set(stopwords.words('english').extend(EXCLUDE))
    tokens = [word for word in tokens if word not in stop_words]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(word) for word in tokens]

    # Join the tokens back into a single string
    cleaned_text = ' '.join(tokens)

    return cleaned_text


# Generate a word cloud
def createWordCloud(text_combined, filename, excluded_words=None):
    wordcloud = WordCloud(width=800, height=400, background_color='white', stopwords=excluded_words).generate(text_combined)
    # Save the word cloud to an image file
    wordcloud.to_file(IMAGE_DIR + filename)
