import streamlit as st
import wikipedia as wiki
import spacy 
from spacy import displacy
ner_Obj = spacy.load("en_core_web_sm")



def app():
    st.title("Named Entity Recognition on Wikipedia pages")
    searchtitle = st.text_input(" Enter the topic you want to search on wikipedia")
    print("Enetered main")
    if st.button("Analyze"):
        print("Entered If")
        print(type(searchtitle))
        print(searchtitle)
        datasearch = wiki.page(searchtitle).content
        print(datasearch)
        data = ner_Obj(datasearch)
        html = displacy.render(data,style='ent')
        print(html)
        st.markdown(html,unsafe_allow_html=True)

if __name__=="__main__":
    app()