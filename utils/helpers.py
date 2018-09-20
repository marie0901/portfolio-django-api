import string
import unicodedata
from django.utils.http import urlquote

def generate_url_name(name):
    table = str.maketrans({key: None for key in string.punctuation})
    name = str(name).translate(table).replace(' ', '-').lower()
    name = remove_accents(name)
    return urlquote(name)

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([c for c in nfkd_form if not unicodedata.combining(c)])