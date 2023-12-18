import streamlit as st
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage

llm = ChatOpenAI()

st.title("平易化Webアプリケーション")
container = st.container()

with container:
    with st.form(key='my_form', clear_on_submit=True):
        user_input = st.text_area(label='Message: ', key='input', height=100)
        submit_button = st.form_submit_button(label='Send')
    if submit_button and user_input:
        message = user_input
        # メッセージリストに新しいメッセージを追加
        st.session_state.messages.append(SystemMessage(content="質問文に対して平易化した文章のみを出力してください"))
        st.session_state.messages.append(HumanMessage(content=message))

        with st.spinner("ChatGPT is typing ..."):
            # ChatGPTにメッセージを送信
            response = llm(st.session_state.messages)

        # ChatGPTの応答をメッセージリストに追加
        st.session_state.messages.append(AIMessage(content=response))

        # ChatGPTの応答を表示
        st.write("ChatGPT's Response:")
        st.write(response)