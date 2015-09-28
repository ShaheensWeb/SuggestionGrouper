#https://en.wikipedia.org/wiki/Jaccard_index

import nltk.corpus
import string
import nltk.data

from nltk.corpus    import wordnet
from nltk.tokenize  import word_tokenize
from nltk.stem      import WordNetLemmatizer

#stop words are words like 'me' 'you' and 'the'
stopwords = nltk.corpus.stopwords.words('english')
#adds all the punctuation
stopwords.extend(string.punctuation)
lemmer = WordNetLemmatizer()

def get_wordnet_pos(pos_tag):
    if pos_tag[1].startswith('J'):
        return (pos_tag[0], wordnet.ADJ)
    elif pos_tag[1].startswith('V'):
        return (pos_tag[0], wordnet.VERB)
    elif pos_tag[1].startswith('N'):
        return (pos_tag[0], wordnet.NOUN)
    elif pos_tag[1].startswith('R'):
        return (pos_tag[0], wordnet.ADV)
    else:
        return (pos_tag[0], wordnet.NOUN)


def foo(a, b, threshold=0.5):    

    pos_a = map(get_wordnet_pos, nltk.pos_tag(word_tokenize(a)))
    pos_b = map(get_wordnet_pos, nltk.pos_tag(word_tokenize(b)))
    lemmas_a = [lemmer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_a \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]
    lemmas_b = [lemmer.lemmatize(token.lower().strip(string.punctuation), pos) for token, pos in pos_b \
                    if pos == wordnet.NOUN and token.lower().strip(string.punctuation) not in stopwords]

    # Calculate Jaccard similarity
    ratio = len(set(lemmas_a).intersection(lemmas_b)) / float(len(set(lemmas_a).union(lemmas_b)))

    print ('lemmas_a = %s' % [x for x in lemmas_a])
    print ('lemmas_b = %s' % [x for x in lemmas_b])
    return (ratio >= threshold)

x = 'I have a friend. His name is peter pan and he likes pickles'
y = 'I know a guy called peter pan. He likes pickles'

print foo(x, y, .20)
