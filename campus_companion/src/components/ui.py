from streamlit import button, text_input, selectbox, color_picker, markdown

def custom_button(label, key=None):
    return button(label, key=key)

def custom_text_input(label, placeholder="", key=None):
    return text_input(label, placeholder=placeholder, key=key)

def custom_selectbox(label, options, index=0, key=None):
    return selectbox(label, options, index=index, key=key)

def custom_color_picker(label, value="#ffffff", key=None):
    return color_picker(label, value=value, key=key)

def card(content):
    markdown(f'<div class="card">{content}</div>', unsafe_allow_html=True)