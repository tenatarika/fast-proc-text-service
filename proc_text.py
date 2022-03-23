import nltk

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("stopwords")
# --------#

from nltk.corpus import stopwords
from pymystem3 import Mystem
from string import punctuation

import pymorphy2

morph = pymorphy2.MorphAnalyzer()
# print(morph.parse('стали'))
# Create lemmatizer and stopwords list
mystem = Mystem()
russian_stopwords = stopwords.words("russian")


# Preprocess function
def preprocess_text(text):
    tokens = mystem.lemmatize(text.lower())
    tokens = [token for token in tokens if token not in russian_stopwords \
              and token != " " \
              and token.strip() not in punctuation]

    # text = " ".join(tokens)

    return tokens

irden = "Ну что сказать, я вижу кто-то наступил на грабли, Ты разочаровал меня, ты был натравлен."
post_proc_text = preprocess_text(
    irden
)
# Examples
# for word in irden.split(" "):
#     print(morph.parse(word))

print(post_proc_text)
