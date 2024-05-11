# ./pages/5_Styling.py

import pandas as pd
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
from modules.nav import Navbar

st.set_page_config(
    page_title="Miscellaneous",
    page_icon="🎨",
    # layout="wide",
)


def main():
    Navbar()

    # st.title("")
    st.title(":red-background[:orange[🎨 Styling]]")
    # st.write("Styling tips for Streamlit.")
    st.markdown(
        """
        There are multiple ways to style your Streamlit widget. Here are some tips:
        """
    )

    # MARKDOWN TRICK
    # --------------
    st.header(":rainbow[Markdown Trick]")

    # STYLING BUTTONS
    # ---------------
    # Styling Buttons
    st.subheader("Styling Buttons", divider=True)

    col1, col2 = st.columns(2)
    with col1:
        st.code("""
st.markdown(\"\"\"
<style>
div.stButton > button {
    color: white;
    background-color: blue;
    border-radius: 1em;
    border: 2px solid white;
}
</style>
\"\"\", unsafe_allow_html=True)
st.button("Styled Button")
""", language='python')
    with col2:
        st.markdown("""
<style>
div.stButton > button {
    color: white;
    background-color: blue;
    border-radius: 1em;
    border: 2px solid white;
}
</style>
""", unsafe_allow_html=True)
        st.button("Styled Button")

    # STYLING TEXT INPUTS
    # -------------------
    st.subheader("Styling Text Inputs", divider=True)
    # Styling Text Inputs
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
st.markdown(\"\"\"
<style>
div.stTextInput > div > div > input {
    color: black;
    background-color: yellow;
    border-radius: 10px;
    border: 2px solid gray;
}
</style>
\"\"\", unsafe_allow_html=True)
st.text_input("Styled Text Input")
""", language='python')
    with col2:
        st.markdown("""
<style>
div.stTextInput > div > div > input {
    color: black;
    background-color: yellow;
    border-radius: 10px;
    border: 2px solid gray;
}
</style>
""", unsafe_allow_html=True)
        st.text_input("Styled Text Input")

    # STYLING SLIDERS
    # ----------------
    st.subheader("Styling Sliders", divider=True)
    # Styling Sliders
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
st.markdown(\"\"\"
<style>
div[data-baseweb="slider"] > div {
    background-color: #f63366; /* Slider track background */
}
div[data-baseweb="slider"] > div > div:first-child {
    background-color: #0d6efd; /* Slider handle */
}
</style>
\"\"\", unsafe_allow_html=True)
st.slider("Styled Slider", 0, 100, 50)
""", language='python')
    with col2:
        st.markdown("""
<style>
div[data-baseweb="slider"] > div {
    background-color: #f63366;
}
div[data-baseweb="slider"] > div > div:first-child {
    background-color: #0d6efd;
}
</style>
""", unsafe_allow_html=True)
        st.slider("Styled Slider", 0, 100, 50)


    # STYLING CHECKBOXES
    # ------------------
    st.subheader("Styling Checkboxes", divider=True)
    # Styling Checkboxes
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
st.markdown(\"\"\"
<style>
div.stCheckbox > label {
    background-color: #f1f1f1;
    border-radius: 10px;
    padding: 10px;
    border: 1px solid #ccc;
}
</style>
\"\"\", unsafe_allow_html=True)
st.checkbox("Styled Checkbox")
""", language='python')
    with col2:
        st.markdown("""
<style>
div.stCheckbox > label {
    background-color: #f1f1f1;
    border-radius: 10px;
    padding: 10px;
    border: 1px solid #ccc;
}
</style>
""", unsafe_allow_html=True)
        st.checkbox("Styled Checkbox")


    # RADIO BUTTONS
    # -------------
    st.subheader("Styling Radio Buttons", divider=True)
    # Styling Radio Buttons
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
st.markdown(\"\"\"
<style>
div.stRadio > div {
    background-color: #abc;
    border-radius: 10px;
    padding: 10px;
    border: 2px solid #def;
}
</style>
\"\"\", unsafe_allow_html=True)
st.radio("Styled Radio", ['Option 1', 'Option 2', 'Option 3'])
""", language='python')
    with col2:
        st.markdown("""
<style>
div.stRadio > div {
    background-color: red;
    border-radius: 10px;
    padding: 10px;
    border: 2px solid #def;
}
</style>
""", unsafe_allow_html=True)
        st.radio("Styled Radio", ['Option 1', 'Option 2', 'Option 3'])


    # DATA FRAME
    # ----------
    st.subheader("Styling DataFrames", divider=True)

    df = pd.DataFrame({
        'A': range(1, 6),
        'B': range(10, 15)
    })

    # Styling DataFrames
    col1, col2 = st.columns(2)
    with col1:
        st.code("""
st.markdown(\"\"\"
<style>
.stDataFrame {
    font-family: 'Courier New', monospace;
    background-color: #f4f4f2;
    border: 2px solid #666;
    border-radius: 10px;
}
</style>
\"\"\", unsafe_allow_html=True)
st.dataframe(df)
""", language='python')
    with col2:
        st.markdown("""
<style>
.stDataFrame {
    font-family: 'Courier New', monospace;
    background-color: #f4f4f2;
    border: 2px solid #666;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)
        st.dataframe(df)



    # NEW TRICK
    # ---------
    st.header(":rainbow[New Trick]")
    st.markdown(
        """
        The secret is in the new CSS `:has` *psuedo-class*. One can inject a Markdown span element with a key class
        in a `st.container` and a CSS selector which only selects containers
        that contains a span with a certain key class.

        This is how Streamlit's new `st.stylable_container` works!

        [See here for Stylable Container](https://arnaudmiribel.github.io/streamlit-extras/extras/stylable_container/)

        See code.
        """,

    )
    st.subheader("Styling image and markdown text", divider=True)


    code = """
    import streamlit as st
    from streamlit_extras.stylable_container import stylable_container

    def main():
        st.header("Example with Cat Image and Markdown Text")

        c1, c2 = st.columns(2)

        with c1:
            with stylable_container(
                key="markdown_container",
                css_styles=[
                    "{ background-color: coral; border-radius: 1em; padding: 0.5em; }",
                    ".stMarkdown { padding-right: 1.5em; }"
                ]
            ):
                st.markdown("The cat (Felis catus) is a domestic species of small carnivorous mammal.")

        with c2:
            with stylable_container(
                key="cat_image",
                css_styles='''
                div[data-testid='stImage'] > img {
                    border-radius: 100px;
                }
                '''
            ):
                st.image("https://static.streamlit.io/examples/cat.jpg")

    if __name__ == '__main__':
        main()
    """

    st.code(code, language='python')

    st.text("")

    # Example with cat image and markdown text
    c1, c2 = st.columns(2)

    with c1:
        # st.markdown("The cat (Felis catus) is a domestic species of small carnivorous mammal.")
        with stylable_container(
            key="markdown_container",
            css_styles=["""
            {
                background-color: coral;
                border-radius: 1em;
                padding: 0.5em;
            }
            """,
            """
            .stMarkdown {
                padding-right: 1.5em;
            }
            """]
        ):
            # st.image("https://static.streamlit.io/examples/cat.jpg")
            st.markdown("The cat (Felis catus) is a domestic species of small carnivorous mammal.")

    with c2:
        with stylable_container(
            key="cat_image",
            css_styles="""
            div[data-testid="stImage"] > img {
                border-radius: 100px;
                # border: 2px solid #f00;
            }
            """,
        ):
            st.image("https://static.streamlit.io/examples/cat.jpg")

    # st.divider()


    # STYLING BUTTONS
    # ---------------
    st.subheader("Styling buttons", divider=True)
    code = """
    import streamlit as st
    from streamlit_extras.stylable_container import stylable_container

    def main():
        st.header("Advanced Button Styling")

        # Setting up columns for two buttons
        c1, c2, _ = st.columns([1, 1, 2])

        with c1:
            with stylable_container(
                key="green_button",
                css_styles=\"\"\"
                    button {
                        background-color: green;
                        color: red;
                        border-radius: 1em;
                        padding: 0.5em;
                    }
                \"\"\"
            ):
                st.button("Green button")

        with c2:
            with stylable_container(
                key="normal_button",
                css_styles=[
                    \"\"\"
                    button {
                        border: solid .2em #292746;
                        border-radius: 50px;
                        color: #fff;
                        background-color: #292746;
                    }
                    \"\"\",
                    \"\"\"
                    button:hover {
                        background-color: red;
                    }
                    \"\"\",
                ]
            ):
                st.button("Normal button")

    if __name__ == '__main__':
        main()
    """

    st.code(code, language='python')

    st.text("")

    c1, c2, _ = st.columns([1,1,2])

    with c1:
        with stylable_container(
            key="green_button",
            css_styles="""
                button {
                    background-color: green;
                    color: red;
                    border-radius: 1em;
                    padding: 0.5em;
                }
                """
        ):
            st.button("Green button")

    with c2:
        with stylable_container(
            key="normal_button",
            css_styles=["""
                button {
                    border: solid .2em #292746;
                    border-radius: 50px;
                    color: #fff;
                    background-color: #292746;
                }
                """,
                """
                button:hover {
                    background-color: red;
                }
                """,
            ]
        ):
            st.button("Normal button")

    
    # STYLING TEXT INPUTS
    # -------------------
    st.subheader("Styling text inputs", divider=True)

    code_text_inputs = """
    import streamlit as st
    from streamlit_extras.stylable_container import stylable_container

    def main():
        st.header("Styling Text Inputs")

        with stylable_container(
            key="styled_text_input",
            css_styles=[
                "{ color: black; background-color: yellow; border-radius: 8px; padding: 5px; }",
                "input { border: 2px solid black; }"
            ]
        ):
            st.text_input("Styled Text Input", placeholder="Type here...")

    if __name__ == '__main__':
        main()
    """

    st.code(code_text_inputs, language='python')

    with stylable_container(
        key="styled_text_input",
        css_styles=[
            "{ color: black; background-color: red; border-radius: 8px; padding: 5px; }",
            "input { border: 10px solid black; background-color: #f1f1f1; }"
        ]
    ):
        st.text_input("Styled Text Input", placeholder="Type here...")

    st.text("")

    # # STYLING CHECKBOXES
    # st.subheader("Styling checkboxes", divider=True)

    # with stylable_container(
    #     key="styled_checkbox",
    #     css_styles=[
    #         "{ background-color: green; border-radius: 10px; padding: 2px; }",
    #         "label { color: yellow; font-weight: bold; }"
    #     ]
    # ):
    #     st.checkbox("Styled Checkbox", key="styled_checkbox")

if __name__ == '__main__':
    main()
