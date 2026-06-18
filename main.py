import streamlit as st

st.set_page_config(page_title="ログイン",page_icon="👀")
st.header("ログイン")
email = st.text_input(label="メールアドレス",placeholder="Hello123@example.com")
if not email:
    st.warning(":rainbow[メールアドレスを入力してください]")
passw = st.text_input(label="パスワード",type="password",max_chars=15)
if not passw:
    st.warning(":rainbow[パスワードを入力してください]")
elif email:
    st.error(":rainbow[メールアドレスかパスワードが間違っています]")
