# AI Assistant

I wanted to take out time during my day and work on a side project that would incorporate a lot of what I learnt during my master's program as well as build a tool that would be useful in terms of its application.

Often people don't transcribe meetings or take meeting minutes so the majority of information discussed in calls are often lost. 

Currently I'm using 140,000 interviews from NPR since it would be a good way to identify a range of topics and different phrases.

## Process
- Clean Text Function (iterates through rows)
  - Convert words to lowercase (e.g. Hello → hello
  - Replac accented characters (e.g. à → a)
  - Break down contractions (e.g. don’t → do not)
  - Filter out Stopwords (e.g. and, the)
  - Remove punctuation (e.g. .,!/?)
  - Lemmatize or (convert words to its base form)
 - Descriptive Stats (add to dataframe)
  - Total length of call
  - Extract words spoken by each speaker
    - Avg # words spoken
    - % words spoken compared to all speakers
 - Summarization function
  - User can specify # sentences to summarize into


## Features 
- Transcription in real-time (and saved as a .txt/.csv file)
- Meeting/Lecture Summarization (so one doesn't waste time re-reading the whole transcribed text)
  - Weekly summary of meetings (e.g. what topics were discussed)
- Identification of important words/phrases/topics (quicker way to see what were the most prominent & important words/phrases)
- Sentiment (useful in sales calls with potential customers- capture and see where things took a turn)
- Descriptive Statistics (metadata - # words per speaker; avg time of calls/each speaker)
