import string
import nltk
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.probability import FreqDist
import ssl
from pymystem3 import Mystem
from string import punctuation
import requests
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


def analyze_word(word):
    return morph.parse(word)





def get_list_category(text: str):
    __url = "https://api.meaningcloud.com/class-2.0"
    payload = {
        'key': "SECRET_KEY",
        'txt': f'{text}',
        'model': 'IPTC_en'
    }

    response = requests.post(__url, data=payload)
    return response.json().get('category_list')

if __name__ == '__main__':
    print(get_list_category("A mythic and emotionally charged hero's journey, DUNE tells the story of Paul Atreides, a brilliant and gifted young man born into a great destiny beyond his understanding, who must travel to the most dangerous planet in the universe to ensure the future of his family and his people. As malevolent forces explode into conflict over the planet's exclusive supply of the most precious resource in existence-a commodity capable of unlocking humanity's greatest potential-only those who can conquer their fear will survive."))
