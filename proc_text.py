import string
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import FreqDist
import ssl
from pymystem3 import Mystem
from string import punctuation

import pymorphy2

morph = pymorphy2.MorphAnalyzer()

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download("stopwords")
nltk.download('punkt')
# --------#


def remove_spec_chars(text, spec_chars=string.punctuation):
    return "".join([ch for ch in text if ch not in spec_chars])


def remover_stop_words(text):
    return [word for word in text if not word in stopwords.words("russian")]


def sort_dict(input: dict):
    return dict(sorted(input.items()))


def process_text(text: str) -> dict:
    text = remove_spec_chars(text.lower())
    text_tokens = word_tokenize(text)
    # rw_text = remover_stop_words(text_tokens)
    count_words = sort_dict(FreqDist(text_tokens))
    return count_words

irden = "Ну что сказать сказать, я вижу кто-то наступил на грабли, Ты разочаровал меня, ты был натравлен. Натравлен на меня."
print(process_text(irden))
proc_irden = process_text(irden)

print(morph.parse('стали'))
