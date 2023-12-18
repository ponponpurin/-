import streamlit as st
import os
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from pydantic import BaseModel

class AIMessage(BaseModel):
    content: str


# 環境変数を読み込む
load_dotenv()

# APIキーを取得
api_key = os.getenv("API_KEY")

llm = ChatOpenAI(api_key=api_key)  # ChatOpenAIのコンストラクタにAPIキーを渡す

# st.session_stateの初期化
if 'messages' not in st.session_state:
    st.session_state.messages = []

st.title("平易化Webアプリケーション")
container = st.container()

# ... (以前のコード)

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
        
        # ChatGPTの応答を表示
        st.write("ChatGPT's Response:")
        st.write(response)

        with open('gpt_input.txt', 'a', encoding='utf-8') as input_file:
            input_file.write(message)

        # APIからの応答をgpt_output.txtに保存
        with open('gpt_output.txt', 'a', encoding='utf-8') as output_file:
            output_file.write(response)