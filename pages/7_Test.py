import time
import numpy as np
import streamlit as st
from modules.nav import Navbar

st.set_page_config(
    page_title="Plotting",
    page_icon="📊",
    # layout="wide",
)


def main():
    Navbar()

    st.title(":blue[🧪 Testing]")

    # 1. Using st.rerun to update an earlier header
    # ---------------------------------------------
    # if "value" not in st.session_state:
    #     st.session_state.value = "Title"

    # ##### Option using st.rerun #####
    # st.header(st.session_state.value)

    # if st.button("Foo"):
    #     st.session_state.value = "Foo"
    #     st.rerun()

    # 2. Using a callback to update an earlier header
    # -----------------------------------------------
    ##### Option using a callback #####
    # st.header(st.session_state.value)

    # def update_value():
    #     st.session_state.value = "Bar"

    # st.button("Bar", on_click=update_value)

    # 3. Using containers to update an earlier header
    # -----------------------------------------------
    ##### Option using a container #####
    if "value" not in st.session_state:
        st.session_state.value = "Bar"

    container = st.container()

    if st.button("Baz"):
        st.session_state.value = "Baz"

    container.header(st.session_state.value)
    # container.markdown("Hello world")
    # container.checkbox("H")
    # container.empty()
    # Content goes here
    # -----------------
    # st.sidebar.header("Plotting Demo")

    # st.header(":rainbow[Simple chart elements]")


if __name__ == '__main__':
    main()
