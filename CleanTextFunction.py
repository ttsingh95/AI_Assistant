
contractions = { 
"ain't": "is not",
"aren't": "are not",
"can't": "cannot",
"can't've": "cannot have",
"'cause": "because",
"could've": "could have",
"couldn't": "could not",
"couldn't've": "could not have",
"didn't": "did not",
"doesn't": "does not",
"don't": "do not",
"hadn't": "had not",
"hadn't've": "had not have",
"hasn't": "has not",
"haven't": "have not",
"he'd": "he would",
"he'd've": "he would have",
"he'll": "he will",
"he'll've": "he will have",
"he's": "he is",
"how'd": "how did",
"how'd'y": "how do you",
"how'll": "how will",
"how's": "how is",
"i'd": "I would",
"i'd've": "I would have",
"i'll": "I will",
"i'll've": "I will have",
"i'm": "I am",
"i've": "I have",
"isn't": "is not",
"it'd": "it would",
"it'd've": "it would have",
"it'll": "it will",
"it'll've": "it will have",
"it's": "it is",
"let's": "let us",
"ma'am": "madam",
"mayn't": "may not",
"might've": "might have",
"mightn't": "might not",
"mightn't've": "might not have",
"must've": "must have",
"mustn't": "must not",
"mustn't've": "must not have",
"needn't": "need not",
"needn't've": "need not have",
"o'clock": "of the clock",
"oughtn't": "ought not",
"oughtn't've": "ought not have",
"shan't": "shall not",
"sha'n't": "shall not",
"shan't've": "shall not have",
"she'd": "she would",
"she'd've": "she would have",
"she'll": "she will",
"she'll've": "she will have",
"she's": "she is",
"should've": "should have",
"shouldn't": "should not",
"shouldn't've": "should not have",
"so've": "so have",
"so's": "so is",
"that'd": "that had",
"that'd've": "that would have",
"that's": "that is",
"there'd": "there would",
"there'd've": "there would have",
"there's": "there is",
"they'd": "they would",
"they'd've": "they would have",
"they'll": "they shall / they will",
"they'll've": "they will have",
"they're": "they are",
"they've": "they have",
"to've": "to have",
"wasn't": "was not",
"we'd": "we would",
"we'd've": "we would have",
"we'll": "we will",
"we'll've": "we will have",
"we're": "we are",
"we've": "we have",
"weren't": "were not",
"what'll": "what will",
"what'll've": "what will have",
"what're": "what are",
"what's": "what is",
"what've": "what have",
"when's": "when is",
"when've": "when have",
"where'd": "where did",
"where's": "where is",
"where've": "where have",
"who'll": "who will",
"who'll've": "who will have",
"who's": "who is",
"who've": "who have",
"why's": "why is",
"why've": "why have",
"will've": "will have",
"won't": "will not",
"won't've": "will not have",
"would've": "would have",
"wouldn't": "would not",
"wouldn't've": "would not have",
"y'all": "you all",
"y'all'd": "you all would",
"y'all'd've": "you all would have",
"y'all're": "you all are",
"y'all've": "you all have",
"you'd": "you would",
"you'd've": "you would have",
"you'll": "you will",
"you'll've": "you will have",
"you're": "you are",
"you've": "you have"
}




import nltk
import unicodedata
import string
import re
nltk.download('wordnet')
nltk.download('words')


def clean_text(text):
    text_lower = convert_to_lowercase(text)
    text_rem_acc = strip_accents(text_lower)
    text_token = tokenizer(text_rem_acc)
    text_post_contr = contract(text_token)
    text_post_punct = punctuation(text_post_contr)
    text_stop = stop_words(text_post_punct)
    text_doc_wd = doc_words(text_stop)
    clean_text = lemmatizer(text_doc_wd, format)
    return clean_text

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
#Convert Text to lowercase
def convert_to_lowercase(text): 
    text = text.lower()
    return text

#Replace letters with accents
def strip_accents(text):
    try:
        text = unicode(text, 'utf-8')
    except NameError: 
        pass

    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")

    return str(text)

#Split each word in a text
def tokenizer(text): 
    tokenizer = nltk.tokenize.WhitespaceTokenizer()
    text = tokenizer.tokenize(text)
    return text

#Break down contractions
def contract(text):
    text = [contractions[word] if word in contractions else word for word in text]
    return text



#Remove any unneccesary punctuation
def punctuation(text):
    import re
    text = [re.sub('['+string.punctuation+']', '', word) for word in text]
    return text

#Remove any stop words 
def stop_words(text):
    stop = nltk.corpus.stopwords.words('english')
    text = [word for word in text if word not in stop]
    return text

#Fix Document Words
def doc_words(text):
    text = [word.upper() if re.match(r'[A-Za-z]+\d+',word) else word for word in text]
    return text

#Convert each word to its based form
def lemmatizer(text,format=string):
    
    lemmatizer = nltk.stem.WordNetLemmatizer()
    if format == string:
        text = " ".join([lemmatizer.lemmatize(word) for word in text])
    if format == list:
        text = [lemmatizer.lemmatize(word) for word in text]
    return text

