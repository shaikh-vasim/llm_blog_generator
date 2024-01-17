import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_google_genai import GoogleGenerativeAI
import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()


googel_api = os.environ.get('GOOGLE_API_KEY') or 'GOOGLE_API_KEY'
GOOGLE_API_KEY = googel_api
genai.configure(api_key=GOOGLE_API_KEY)


# Function To get response from LLAma 2 model
def getgeminiresponse(input_text, no_words, blog_style):
    # Gemini-pro model
    llm = GoogleGenerativeAI(model="gemini-pro",
                             temperature=0.3,
                             google_api_key=GOOGLE_API_KEY)

    # Prompt Template
    template = """Write a blog for {blog_style} job
                profile for a topic {input_text} within {no_words} words. """
    prompt = PromptTemplate.from_template(template)
    print(prompt)

    # chain = prompt | llm
    prompt_ = PromptTemplate(input_variables=["blog_style",
                                              "input_text",
                                              'no_words'], template=template)

    promt_format = prompt_.format(blog_style=blog_style,
                                  input_text=input_text,
                                  no_words=no_words)

    st.write("Subject:- " + promt_format)

    response = llm(promt_format)

    print(response)
    return response


st.set_page_config(page_title="Generate Blogs",
                   page_icon='🤖',
                   layout='centered',
                   initial_sidebar_state='collapsed')

st.header("Generate Blogs 🤖")

input_text = st.text_input("Enter the Blog Topic")

# creating to more columns for additonal 2 fields
col1, col2 = st.columns([5, 5])

with col1:
    no_words = st.text_input('No of Words')
with col2:
    blog_style = st.selectbox('Writing the blog for',
                              ('Researchers',
                               'Data Scientist',
                               'Common People'))

submit = st.button("Generate")

# Final response
if submit:
    blog = getgeminiresponse(input_text, no_words, blog_style)
    st.write(blog)
