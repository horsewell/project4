import streamlit as st
from pandasai import SmartDataframe
from pandasai.llm import OpenAI
from pandasai.responses.response_parser import ResponseParser
import pandas as pd
from api_keys import API_KEY



df = pd.read_pickle('import_df.pkl')

st.title("Chat with the Open University Dataset")

st.divider()

class StreamlitResponse(ResponseParser):
    def __init__(self, context) -> None:
        super().__init__(context)

    def format_dataframe(self, result):
        st.dataframe(result["value"])
        return

    def format_plot(self, result):
        st.image(result["value"])
        return

    def format_other(self, result):
        st.write(result["value"])
        return

with st.expander("🤖Chatbot"):
    st.write("This is a simple chatbot that can answer questions about the Open University Dataset.")
    st.write("Try asking questions like:")
    st.write("- What is the average score for students in the dataset?")
    st.write("- What is the distribution of scores for students in the dataset?")
    st.write("- How many students failed the courses?")

query = st.text_area("Chat with the Dataset")
st.write(query)

if query:
    llm = OpenAI(api_token= API_KEY)
    query_engine = SmartDataframe(df, config={"llm": llm, "response_parser": StreamlitResponse})
    answer = query_engine.chat(query)
    st.write(answer)

    
    
    

