# ./modules/nav.py

# Using `st.page_link()` to navigate between pages in sidebar:
# https://docs.streamlit.io/develop/api-reference/widgets/st.page_link

# Notice that we set `showSidebarNavigation = false` in config.toml to do this

import streamlit as st

# add add_logo from streamlit extras
# from streamlit_extras.app_logo import add_logo


def add_logo():
    st.markdown(
        """
        <style>
            [data-testid="stSidebarNav"] {
                background-image: url(http://placekitten.com/200/200);
                background-repeat: no-repeat;
                padding-top: 120px;
                background-position: 20px 20px;
            }
            [data-testid="stSidebarNav"]::before {
                content: "My Company Name";
                margin-left: 20px;
                margin-top: 20px;
                font-size: 30px;
                position: relative;
                top: 100px;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def Navbar():
    # builds the sidebar menu
    with st.sidebar:
        # add app logo
        # add_logo()
        # st.image("logo/golden_hippo_logo_test.png")

        # https://docs.streamlit.io/develop/api-reference/widgets/st.page_link
        st.page_link("Hello.py", label="Hello", icon="📄")
        st.page_link("pages/1_Widgets.py", label="Widgets", icon="🕹")
        # st.page_link('pages/2_Plotting.py', label='Plotting', icon='📊')
        st.page_link("pages/3_Miscellaneous.py", label="Miscellaneous", icon="📦")
        st.page_link("pages/4_Layout.py", label="Layout", icon="📦")
        st.page_link("pages/5_Styling.py", label="Styling", icon="🎨")
        # st.page_link('pages/6_Extras.py', label='Extras', icon='🎉')
        st.page_link("pages/7_Test.py", label="Test", icon="🧪")
        st.page_link("pages/8_Login.py", label="Login", icon="🔒")
        st.page_link("pages/9_Register.py", label="Register", icon="🔒")
        st.markdown("---")

        # COMMENT OUT THIS PART AFTER DEVELOPMENT
        st.markdown("### To-do")
        st.markdown(
            """
            - [x] Finish Widgets page
            - [x] Finish Layout page
            - [ ] Finish Login page
            - [ ] Finish Styling page
            - [ ] Finish Plotting page
            - [ ] Finish Extras page
            """
        )
        st.text("")

        st.markdown("### Session State")
        st.markdown("---")
        st.session_state
        # END OF COMMENT

        # add_logo("https://static.streamlit.io/examples/cat.jpg")
