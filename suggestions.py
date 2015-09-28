#https://en.wikipedia.org/wiki/Jaccard_index

import nltk.corpus
import nltk.stem.snowball
import string
import nltk.data

from nltk.tokenize import word_tokenize


#stop words are words like 'me' 'you' and 'the'
stopwords = nltk.corpus.stopwords.words('english')
#adds all the punctuation
stopwords.extend(string.punctuation)


def foo(a, b, threshold=0.5):    
    tokens_a = [token.lower().strip(string.punctuation) for token in word_tokenize(a) \
                    if token.lower().strip(string.punctuation) not in stopwords]
    tokens_b = [token.lower().strip(string.punctuation) for token in word_tokenize(b) \
                    if token.lower().strip(string.punctuation) not in stopwords]

    # Calculate Jaccard similarity
    ratio = len(set(tokens_a).intersection(tokens_b)) / float(len(set(tokens_a).union(tokens_b)))
    return (ratio >= threshold)

x = 'I like big butts'
y = 'I enjoy butts'

print foo(x, y)
