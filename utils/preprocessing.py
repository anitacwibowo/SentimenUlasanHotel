import re
import string
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factory = StopWordRemoverFactory()
stopword_remover = factory.create_stop_word_remover()

stem_factory = StemmerFactory()
stemmer = stem_factory.create_stemmer()

def clean_text(text):
    text = text.lower()  # Mengubah ke huruf kecil
    text = re.sub(r'@\w+', '', text)  # Menghapus mention
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Menghapus URL
    emoji_pattern = re.compile(
        "["
        u"\U0001F600-\U0001F64F"  # Emotikon wajah
        u"\U0001F300-\U0001F5FF"  # Simbol & ikon
        u"\U0001F680-\U0001F6FF"  # Transportasi & simbol lainnya
        u"\U0001F1E0-\U0001F1FF"  # Bendera negara
        u"\U00002700-\U000027BF"  # Simbol tambahan
        u"\U000024C2-\U0001F251"  # Simbol lainnya
        "]+",
        flags=re.UNICODE,
    )
    text = emoji_pattern.sub(r'', text) #menghapus emoji
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)  # Menghapus semua simbol kecuali huruf, angka, dan spasi
    #text = stopword_remover.remove(text)
    #text = stemmer.stem(text)
    return text.strip()

def preprocess_series(series):
    return series.astype(str).apply(clean_text)