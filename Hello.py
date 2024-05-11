# ./Hello.py

import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher

import streamlit as st
from modules.nav import Navbar
# from streamlit_extras.app_logo import add_logo

st.set_page_config(
    page_title="Hello",
    page_icon="📄",
    # layout="wide",
)

# def logo():
#     add_logo("http://placekitten.com/200/200", height=300)

def main():

    Navbar()


    # # Step 1. Import YAML file into script
    # with open('./config.yaml') as f:
    #     config = yaml.load(f, Loader=SafeLoader)


    # your content
    st.write("# Welcome to the Sample Multi-page Streamlit App 👋")

    st.sidebar.success("Select a demo above.")

    st.markdown(
        """
        This is a sample multi-page Streamlit app, built as documentation/reference and to showcase the capabilities of Streamlit.

        **👈 Select a page from the sidebar** to
        get started!
        ### Resources
        - [Streamlit Documentation](https://docs.streamlit.io/)
        - [Streamlit Extras](https://extras.streamlit.app/)
        - [Fanilo Andrianasolo's YouTube Channel](https://www.youtube.com/@andfanilo)
        - [Misra Turp's YouTube Channel](https://www.youtube.com/@misraturp)

        ### Forum Posts
        - [Setting up a multi-page Streamlit app using using `st.page_link`](https://discuss.streamlit.io/t/rename-the-home-page-in-a-multi-page-app/65533)
        - [How to build a unique button](https://discuss.streamlit.io/t/how-to-build-an-unique-button-in-streamlit-web-program/12012/1)
        - [How to change font size/color/etc](https://discuss.streamlit.io/t/change-font-size-in-st-write/7606)
        - [Applying custom CSS to button using `stylable_container`](https://discuss.streamlit.io/t/issue-with-coloring-buttons-in-streamlit/56914/6)
        - [How to create dynamic content using `st.empty` placeholders](https://discuss.streamlit.io/t/ugly-screen-shifting-when-rendering-how-to-avoid-this/7790/11)
        - [How to use new CSS `:has` pseudo-class on a simple <span> tag (this is how Stylable Containers works)](https://discuss.streamlit.io/t/applying-custom-css-to-manually-created-containers/33428/7)

        ### Tutorials
        - [Build a custom navigation menu with `st.page_link` (also includes guide on how to display pages to authenticated users only)](https://docs.streamlit.io/develop/tutorials/multipage/st.page_link-nav)
        - [Session State](https://docs.streamlit.io/develop/api-reference/caching-and-state/st.session_state)
        - [Button behavior and examples](https://docs.streamlit.io/develop/concepts/design/buttons)
        - [Understanding widget behavior](https://docs.streamlit.io/develop/concepts/architecture/widget-behavior)
        - [Overview of `st.chat_input` and `st.chat_message` (video)](https://www.youtube.com/watch?v=4sPnOqeUDmk&list=TLGG5KJRkm-s0qYxMDA1MjAyNA)
        - [New layout options for Streamlit](https://blog.streamlit.io/introducing-new-layout-options-for-streamlit/)
        - [When to use `st.rerun`](https://docs.streamlit.io/develop/api-reference/execution-flow/st.rerun)
        - Authentication
            * [Streamlit Authenticator](https://pypi.org/project/streamlit-authenticator/)
            * [Streamlit-Authenticator, Part 1](https://blog.streamlit.io/streamlit-authenticator-part-1-adding-an-authentication-component-to-your-app/)
            * [Streamlit-Authenticator, Part 2](https://blog.streamlit.io/streamlit-authenticator-part-2-adding-advanced-features-to-your-authentication-component/)

        """
    )



if __name__ == '__main__':
    main()
