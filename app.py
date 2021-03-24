#importing packages
import streamlit as st
import wikipedia as wiki
import spacy 
from spacy import displacy

#creating object to perform NLP
ner_Obj = spacy.load("en_core_web_sm")


def app():
    st.title("Named Entity Recognition on Wikipedia pages")
    searchtitle = st.text_input(" Enter the topic you want to search on wikipedia")
    if st.button("Analyze"):
        #collecting datafrom wikipedia
        datasearch = wiki.page(searchtitle).content
        
        #performing NER on data
        data = ner_Obj(datasearch)
        
        #Storing the final output (i.e, data along with NER tags with HTML and css for beautification
        html = displacy.render(data,style='ent')
        
        #displaying the results on the app
        st.markdown(html,unsafe_allow_html=True)

        
#main function
if __name__=="__main__":
    app()
