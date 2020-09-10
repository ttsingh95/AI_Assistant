import streamlit as st
from spacy import displacy

from gensim.summarization import summarize

from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize

st.title("TLDR: Text Summarization App")
st.write("Sometimes we just want the **highlights** instead of reading the *whole* document. With this simple app you can add text and select your summarizer of choice")

txt_input = st.text_area("Type or Paste Text Here")
sum_tool = st.selectbox("Select Summarizer Tool", ("Gensim", "Lex Rank"))

def lrsummarizer(txt_input):
    parser = PlaintextParser.from_string(txt_input, Tokenizer("english"))
    lex_summarizer = LexRankSummarizer()
    summary = lex_summarizer(parser.document, params["L"])
    summary_list = [str(sentence) for sentence in summary]
    result = ' '.join(summary_list)
    return result

def add_parameter (summarizer_type):
    params = dict()
    if summarizer_type == "Gensim":
        st.write(
            "Use slider to select % of original content")
        st.write("######  *For example: 0.5 = A summarized version that is 50% of the original content*")
        G = st.slider("",0.01,1.0,step=0.01)
        params["G"] = G
    elif summarizer_type == "Lex Rank":
        st.write(
            "Use slider to select no. of sentences to return")
        L = st.slider("",1,20)
        params["L"] = L
    return params

params = add_parameter(sum_tool)

def get_summarizer(summarizer_type,params,txt_input):
    if st.button("Summarize Text"):
        if summarizer_type == 'Gensim':
            summarized_text = summarize(txt_input, ratio=params["G"])
        elif summarizer_type == 'Lex Rank':
            summarized_text = lrsummarizer(txt_input)
        st.write(summarized_text)
get_summarizer(sum_tool, params,txt_input)