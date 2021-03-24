# StreamlitWiki
This app is made using streamlit framework that helps in building the frontend of the app.

Wikipedia library is used to fetch data from wikipedia on which we have to perform Named Entity recognition.
spacy is used to perform NER in which "en_core_web_sm" package served as a corpus to help the program to understand which words are organization, name of persons etc.


#packages used:
spacy
streamlit
wikipedia

#process to use
Just type the word which you want to search on wikipedia like 'facebook' ,'london' etc and the app will display information embeded with NER
if for some keywords no page was found it will return an error, just try another word .
