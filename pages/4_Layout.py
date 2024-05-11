# ./pages/4_Layout.py

import time
import numpy as np
import streamlit as st
from modules.nav import Navbar

st.set_page_config(
    page_title="Layout",
    page_icon="📦",
)


def main():
    Navbar()

    st.title("[:blue-background[📦 Layout and Containers]](https://docs.streamlit.io/develop/api-reference/layout)")
    st.markdown(
        """
        Streamlit provides several options for controlling how 
        different elements are laid out on the screen.
        """
    )

    # COLUMNS
    # -------
    # st.write("Overview of the different layout options available in Streamlit.")
    st.header("[Columns](https://docs.streamlit.io/develop/api-reference/layout/st.columns)")
    st.markdown(
        """
        Insert containers laid out as side-by-side columns.

        Inserts a number of multi-element containers laid out side-by-side and returns a list of container objects.

        To add elements to the returned containers, you can use the
        `with` notation (preferred) or just call methods directly on the returned object. See examples below.

        Columns can only be placed inside other columns up to one level of nesting.
        """
    )
    st.markdown(
        """
        ### Examples
        You can use the `with` notation to insert any element into a column:
        """
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg")

    with col2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg")

    with col3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg")

    # Or you can just call methods directly on the returned objects:
    # col1, col2 = st.columns([3, 1])
    # data = np.random.randn(10, 1)

    # col1.subheader("A wide column with a chart")
    # col1.line_chart(data)

    # col2.subheader("A narrow column with the data")
    # col2.write(data)
    st.text("")

    # CONTAINERS
    # ----------
    st.header("[Containers](https://docs.streamlit.io/develop/api-reference/layout/st.container)")
    st.markdown(
        """
        Insert a multi-element container.

        Inserts an invisible container into your app that can be used to hold multiple elements. This allows you to, for example, insert multiple elements into your app out of order.

        To add elements to the returned container, you can use the `with` notation (preferred) or just call methods directly on the returned object. See examples below.
        """
    )

    st.markdown(
        """
        ### Examples
        **Inserting elements using with notation:**
        """
    )

    with st.container():
        st.write("This is inside the container")

        # You can call any Streamlit command, including custom components:
        st.bar_chart(np.random.randn(50, 3))

    st.write("This is outside the container")

    st.divider()

    st.markdown(
        """
        **Inserting elements out of order:**
        """
    )

    container = st.container(border=True)
    container.write("This is inside the container")
    st.write("This is outside the container")

    # Now insert some more in the container
    container.write("This is inside too")

    st.divider()

    st.write("**Using `height` to make a grid:**")
    row1 = st.columns(3)
    row2 = st.columns(3)

    for col in row1 + row2:
        tile = col.container(height=200)
        tile.title(":balloon:")

    st.divider()

    st.markdown("**Using `height` to create a scrolling container for long content:**")
    long_text = "Lorem ipsum. " * 1000

    with st.container(height=300):
        st.markdown(long_text)
    st.text("")

    # EMPTY
    # -----
    st.header("[Empty](https://docs.streamlit.io/develop/api-reference/layout/st.empty)")
    st.markdown(
        """
        Insert a single-element container.

        Inserts a container into your app that can be used to hold a
        **single element**. This allows you to, for example, remove elements
        at any point, or replace several elements at once (using a child multi-element container).

        To insert/replace/clear an element on the returned container,
        you can use `with` notation or just call methods directly on the returned object. See examples below.
        """
    )
    st.markdown(
        """
        ### Examples
        """
    )

    # EXAMPLE 1
    # ---------
    st.markdown("**Overwriting elements in-place using `with` notation:**")

    with st.empty():
        for seconds in range(1):
            st.write(f"⏳ {seconds} seconds have passed")
            time.sleep(1)
        st.write("✔️ 1 second(s) over!")

    st.divider()

    # EXAMPLE 2
    # ---------
    st.markdown("**Replacing several elements, then clearing them (see code):**")
    placeholder = st.empty()

    # Replace the placeholder with some text:
    placeholder.text("Hello")

    # Replace the text with a chart:
    placeholder.line_chart({"data": [1, 5, 2, 6]})
    # input('f')
    # input('test')
    # Replace the chart with several elements:
    with placeholder.container():
        # pass
        # st.text("")
        st.write("This is one element")
        st.write("This is another")

    # Clear all those elements:
    placeholder.empty()

    st.divider()

    # EXAMPLE 3
    # ---------
    st.markdown("**Using `st.container()` inside `st.empty()`:**")
    # Create an empty placeholder
    placeholder = st.empty()

    # Insert a container into the empty placeholder
    with placeholder.container():
        # Now you can add multiple elements into this container
        st.write("Here's a list of items:")
        for i in range(5):
            st.write(f"Item {i + 1}")

        # You can also add charts, images, etc.
        st.line_chart([10, 20, 30, 40])

    # You can update the entire container later
    if st.button("Update Content"):
        with placeholder.container():
            st.write("The content has been updated!")
            st.bar_chart([40, 30, 20, 10])

    # Or clear the contents entirely
    if st.button("Clear Content"):
        placeholder.empty()

    st.text("")

    # EXPANDER
    # --------
    st.header("[Expander](https://docs.streamlit.io/develop/api-reference/layout/st.expander)") 
    st.markdown(
        """
        Insert a multi-element container that can be expanded/collapsed.

        Inserts a container into your app that can be used to
        hold multiple elements and can be expanded or collapsed by the user.
        When collapsed, all that is visible is the provided label.

        To add elements to the returned container,
        you can use the `with` notation (preferred) or just call methods directly
        on the returned object. See examples below.
        """
    )

    st.markdown(
        """
        ### Examples
        """
    )

    # EXAMPLE 1
    # ---------
    st.markdown("**You can use the `with` notation to insert any element into an expander:**")
    st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

    with st.expander("See explanation"):
        st.write('''
            The chart above shows some numbers I picked for you.
            I rolled actual dice for these, so they're *guaranteed* to
            be random.
        ''')
        st.image("https://static.streamlit.io/examples/dice.jpg")

    # st.divider()

    # # EXAMPLE 2
    # # ---------
    # st.markdown("Or you can just call methods directly on the returned objects:")

    # st.bar_chart({"data": [1, 5, 2, 6, 2, 1]})

    # expander = st.expander("See explanation")
    # expander.write('''
    #     The chart above shows some numbers I picked for you.
    #     I rolled actual dice for these, so they're *guaranteed* to
    #     be random.
    # ''')
    # expander.image("https://static.streamlit.io/examples/dice.jpg")

    st.text("")

    # POPOVER
    # --------
    st.header("[Popover](https://docs.streamlit.io/develop/api-reference/layout/st.popover)")
    st.markdown(
        """
        Insert a popover container.

        Inserts a multi-element container as a popover. 
        It consists of a button-like element and a container that opens when the button is clicked.

        Opening and closing the popover will not trigger a rerun. 
        Interacting with widgets inside of an open popover will rerun the app while keeping the popover open. Clicking outside of the popover will close it.

        To add elements to the returned container, 
        you can use the `with` notation (preferred) or just call methods directly on the returned object. See examples below.
        """
    )

    st.markdown(
        """
        ### Examples
        """
    )
    # EXAMPLE 1
    # ---------
    st.markdown("**You can use the with `notation` to insert any element into a popover:**")
    with st.popover("Open popover"):
        st.markdown("Hello World 👋")
        name = st.text_input("What's your name?")

    st.write("Your name:", name)

    st.divider()

    # EXAMPLE 2
    # ---------
    st.markdown("**Or you can just call methods directly on the returned objects:**")
    popover = st.popover("Filter items")
    red = popover.checkbox("Show red items.", True)
    blue = popover.checkbox("Show blue items.", True)

    if red:
        st.write(":red[This is a red item.]")
    if blue:
        st.write(":blue[This is a blue item.]")

    # TABS
    # ----
    st.header("[Tabs](https://docs.streamlit.io/develop/api-reference/layout/st.tabs)")
    st.markdown(
        """
        Insert containers separated into tabs.

        Inserts a number of multi-element containers as tabs.
        Tabs are a navigational element that allows users to easily move between groups of related content.

        To add elements to the returned containers,
        you can use the `with` notation (preferred) or just call methods directly on the
        returned object. See examples below.
        """
    )

    st.markdown(
        """
        ### Examples
        """
    )

    # EXAMPLE 1
    # ---------
    st.markdown("**You can use the with notation to insert any element into a tab:**")

    tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

    with tab1:
        st.header("A cat")
        st.image("https://static.streamlit.io/examples/cat.jpg", width=200)

    with tab2:
        st.header("A dog")
        st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

    with tab3:
        st.header("An owl")
        st.image("https://static.streamlit.io/examples/owl.jpg", width=200)

    st.divider()

    # EXAMPLE 2
    # ---------
    st.markdown("**Or you can just call methods directly on the returned objects:**")

    tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])
    data = np.random.randn(10, 1)

    tab1.subheader("A tab with a chart")
    tab1.line_chart(data)

    tab2.subheader("A tab with the data")
    tab2.write(data)

    st.text("")

    # Modal Dialogs
    # -------------
    st.header("[Modal dialogs](https://docs.streamlit.io/develop/api-reference/execution-flow/st.dialog)")
    st.markdown(
        """
        Function decorator to create a modal dialog.

        A function decorated with `@st.experimental_dialog` becomes a dialog function. 
        When you call a dialog function, Streamlit inserts a modal dialog into your 
        app. Streamlit element commands called within the dialog function render 
        inside the modal dialog.

        The dialog function can accept arguments that can be passed when it is called.
        Any values from the dialog that need to be accessed from the wider app
        should generally be stored in Session State.

        A user can dismiss a modal dialog by clicking outside of it, 
        clicking the "X" in its upper-right corner, or pressing``ESC`` 
        on their keyboard. Dismissing a modal dialog does not trigger an app rerun.
        To close the modal dialog programmatically, call `st.rerun()` explicitly inside of the dialog function.

        `st.experimental_dialog` inherits behavior from `st.experimental_fragment`.
        When a user interacts with an input widget created inside a dialog function, Streamlit only reruns the dialog function instead of the full script.

        Calling `st.sidebar` in a dialog function is not supported.

        Dialog code can interact with Session State, imported modules,
        and other Streamlit elements created outside the dialog.
        Note that these interactions are additive across multiple dialog reruns. 
        You are responsible for handling any side effects of that behavior.
        """
    )

    st.markdown(
        """
        ### Examples
        """
    )

    # EXAMPLE 1
    # ---------
    st.markdown(
        """
        The following example demonstrates the basic usage of
        `@st.experimental_dialog`.
        In this app, clicking "A" or "B" will open a modal
        dialog and prompt you to enter a reason for your vote.
        In the modal dialog, click "Submit" to record your vote into Session State
        and rerun the app. This will close the modal dialog since the dialog
        function is not called during the full-script rerun.
        """
    )

    @st.experimental_dialog("Cast your vote")
    def vote(item):
        st.write(f"Why is {item} your favorite?")
        reason = st.text_input("Because...")
        if st.button("Submit"):
            st.session_state.vote = {"item": item, "reason": reason}
            st.rerun()

    if "vote" not in st.session_state:
        st.write("Vote for your favorite")
        if st.button("A"):
            vote("A")
        if st.button("B"):
            vote("B")
    else:
        f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}"


if __name__ == '__main__':
    main()
