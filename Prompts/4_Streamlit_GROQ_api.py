from langchain_groq import ChatGroq
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

llm = ChatGroq(
    model="llama-3.3-70b-versatile",   # https://console.groq.com/docs/models from here i can get the model
    temperature=0
)

st.header("Research Tool (Groq Powered)")

paper_input = st.selectbox("Select Research Paper Name",["Select...",
                                                        "Attention Is All You Need", 
                                                        "BERT: Pre-training of Deep Bidirectional Transformers", 
                                                        "GPT-3: Language Models are Few-Shot Learners",
                                                        "Diffusion Models Beat GANs on Image Synthesis"] )

style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical",
                                                        "Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explanation LengthShort",
                            ["Short (1-2 paragraphs)","Medium(3-5 paragraphs)",
                            "Long(detailed explanation)"])

template = load_prompt('4.Prompts/template.json')


if st.button("Summarize"):

    chain = template | llm
    result = chain.invoke(
        {
        "paper_input":paper_input,
        "style_input":style_input,
        "length_input":length_input
        }
        )
    st.write(result.content)
