import urllib.request
from bs4 import BeautifulSoup
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Download stopwords (only first time)
nltk.download('stopwords')

# URL
url = 'https://en.wikipedia.org/wiki/Apple'

# Add User-Agent (IMPORTANT)
headers = {
    'User-Agent': 'Mozilla/5.0'
}

# Create request
request = urllib.request.Request(url, headers=headers)

# Fetch HTML
response = urllib.request.urlopen(request)
html = response.read()

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')
text = soup.get_text()

# Tokenize
tokens = text.split()

# Remove stopwords
stop_words = set(stopwords.words('english'))
clean_tokens = [token for token in tokens if token.lower() not in stop_words]

# Frequency distribution
freq = nltk.FreqDist(clean_tokens)

# Print word frequencies
for key, val in freq.items():
    print(f"{key}: {val}")

# Plot top 20 words
freq.plot(20)
plt.show()
