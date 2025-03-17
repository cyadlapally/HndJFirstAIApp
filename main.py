# pip install --upgrade langchain langchain-google-genai streamlit 

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain import PromptTemplate
from langchain import LLMChain

import os
os.environ["GOOGLE_API_KEY"] = "AIzaSyCs2DeQxumMSmDDWtgdRQpvU1hJB3MEZrA"

tweet_template = "Give me {number} of tweets on the {topic}"

tweet_prompt = PromptTemplate(
    input_variables=["number", "topic"],
    template=tweet_template
)


gemini_model = ChatGoogleGenerativeAI(model ="gemini-1.5-flash-latest")

tweet_chain = tweet_prompt | gemini_model

import streamlit as st

st.header("H & J Solutions Tweet Generator")

st.subheader("Generate tweets using Generative AI")

topic = st.text_input("Topic")

number = st.number_input("Number of tweets", min_value=1, max_value=10, value=1)

if st.button("Generate"):
    tweets = tweet_chain.invoke({"number": number, "topic": topic})
    st.write(tweets.content)



