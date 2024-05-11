# ./pages/9_Register.py

import yaml
from yaml.loader import SafeLoader
import pandas as pd
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher
from modules.nav import Navbar

st.set_page_config(
    page_title="Register",
    page_icon="🔒",
    # layout="wide",
)


def main():
    Navbar()

    st.title(":lock[🔒 Register]")

    with open('./config.yaml') as f:
        config = yaml.load(f, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
        if email_of_registered_user:
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)

if __name__ == '__main__':
    main()
