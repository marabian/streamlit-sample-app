# ./pages/1_Widgets.py

from io import StringIO
from datetime import time, datetime, date
import pandas as pd
import streamlit as st
from modules.nav import Navbar

# this sets the page tab's title and favicon
st.set_page_config(
    page_title="Widgets",
    page_icon="🕹",
    # layout="wide",
)


def main():
    Navbar()

    st.title("[:blue-background[🕹 Input Widgets]](https://docs.streamlit.io/develop/api-reference/widgets)")
    # st.title("🕹 Input Widgets")
    st.write("Overview of the different input widgets available in Streamlit.")
    # st.write("[Documentation](https://docs.streamlit.io/develop/api-reference/widgets)")

    st.header(":rainbow[Button elements]", divider=False)

    # BUTTON ELEMENTS
    # ---------------

    # Button
    # ------
    st.subheader("[Button](https://docs.streamlit.io/develop/api-reference/widgets/st.button)")
    st.button("Reset", type="primary")
    if st.button("Say hello"):
        st.write("Why hello there")
    else:
        st.write("Goodbye")
    st.write("")

    # Form button
    # -----------
    st.subheader("[Form button](https://docs.streamlit.io/develop/api-reference/execution-flow/st.form_submit_button)")
    st.markdown(
        """
        When button is clicked, all widgets inside form sent to Streamlit in a batch.
        Every form must have a `st.form_submit_button()`. This button cannot exist outside of a form.
        """
    )

    # Using the "with" syntax
    with st.form(key='my_form'):
        text_input = st.text_input(label='Enter some text')
        slider_input = st.slider(label='Enter a value', min_value=0.0, max_value=1.0)
        checkbox_input = st.checkbox(label='Checkbox')
        submit_button = st.form_submit_button(label='Submit')

    if submit_button:
        st.write(f'Text input value: {text_input}')
        st.write("Slider value: ", slider_input)
        st.write("Checkbox value: ", checkbox_input)
    st.write("")
    # Or using object notation
    # Declare a form and call methods directly on the returned object
    # ---------------------------------------------------------------
    # form = st.form(key='my_form')
    # form.text_input(label='Enter some text')
    # submit_button = form.form_submit_button(label='Submit')

    # Testing
    # -------
    # Testing input widgets without form. Notice how every interaction triggers a rerun of the script
    # Unlike the form, where all widgets are sent to Streamlit in a batch when `form_submit_button` is clicked
    # print('Testing Slider Input')
    # st.slider(label='Slider')

    # print("Testing Checkbox Input")
    # st.checkbox(label='Checkbox')

    # print("Testing text input")
    # st.text_input(label='Text Input')

    # Link button
    # -----------
    st.subheader("[Link button](https://docs.streamlit.io/develop/api-reference/widgets/st.link_button)")
    st.link_button("Go to Streamlit app gallery", "https://streamlit.io/gallery")
    st.write("")

    # Page link button
    # ----------------
    st.subheader("[Page link button](https://docs.streamlit.io/develop/api-reference/widgets/st.page_link)")
    st.markdown(
        """
        If another page in a multipage app is specified,
        clicking `st.page_link()` stops the current page execution and 
        runs the specified page as if the user clicked on it in the sidebar navigation.
        """
    )
    st.page_link("http://www.google.com", label="Google", icon="🌎")
    st.write("")

    # Download button
    # ---------------
    # Useful when you would like to provide a way for your users to download a file directly from your app.
    # data to be downloaded is stored in-memory while the user is connected,
    # so it's a good idea to keep file sizes under a couple hundred megabytes to conserve memory
    st.subheader("[Download button](https://docs.streamlit.io/develop/api-reference/widgets/st.download_button)")
    # st.markdown(
    #     """
    #     Usefu when you would like to provide a way for your users to download a file directly from your app.
    #     data to be downloaded is stored in-memory while the user is connected,
    #     so it's a good idea to keep file sizes under a couple hundred megabytes to conserve memory.
    #     """
    # )

    st.markdown(
        """
        **Download a large DataFrame as a CSV:**
        """
    )
    # Create a dictionary of data
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
        'Age': [25, 30, 35, 40, 45],
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
    }

    # Create DataFrame
    df = pd.DataFrame(data)

    @st.cache_data
    def convert_df(df):
        # IMPORTANT: Cache the conversion to prevent computation on every rerun
        return df.to_csv().encode("utf-8")

    csv = convert_df(df)

    st.download_button(
        label="Download data as CSV",
        data=csv,
        file_name="df.csv",
        mime="text/csv",
    )

    st.divider()

    st.markdown(
        """
        **Download a string as a file:**
        """
    )

    text_contents = '''This is some text'''
    st.download_button("Download some text", text_contents)
    st.write("")

    # SELECTION ELEMENTS
    # ------------------
    st.header(":rainbow[Selection elements]", divider=False)

    # Checkbox
    # --------
    st.subheader("[Checkbox](https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox)")
    agree = st.checkbox("I agree")
    st.write("")

    # print("Rerun registered")
    if agree:
        st.write("Great!")

    # Toggle
    # ------
    st.subheader("[Toggle](https://docs.streamlit.io/develop/api-reference/widgets/st.checkbox)")
    # on = st.toggle(label="$\overleftrightarrow{AB}$")
    on = st.toggle("Activate feature", False)

    if on:
        st.write("Feature activated!")
    st.write("")

    # Radio
    # -----
    st.subheader("[Radio](https://docs.streamlit.io/develop/api-reference/widgets/st.radio)")
    genre = st.radio(
        "What's your favorite movie genre",
        [":rainbow[Comedy]", "***Drama***", "Documentary :movie_camera:"],
        captions = ["Laugh out loud.", "Get the popcorn.", "Never stop learning."])

    if genre == ":rainbow[Comedy]":
        st.write("You selected comedy.")
    else:
        st.write("You didn't select comedy.")
    st.write("")

    # Selectbox
    # ---------
    st.subheader("[Selectbox](https://docs.streamlit.io/develop/api-reference/widgets/st.selectbox)")
    # print("Rerun registered")
    option = st.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone"))

    st.write("You selected:", option)
    st.write("")

    # Multiselect
    # -----------
    st.subheader("[Multiselect](https://docs.streamlit.io/develop/api-reference/widgets/st.multiselect)")
    options = st.multiselect(
        "What are your favorite colors",
        ["Green", "Yellow", "Red", "Blue"],
        ["Yellow", "Red"])

    # `st.write()` is the Swiss Army knife of Streamlit commands, will infer type and print accordingly
    # can also use `magic`!
    options  # magic
    st.write("")
    # st.write("You selected:", options)

    # Select slider
    # -------------
    # print("Rerun registered")
    st.subheader("[Select slider](https://docs.streamlit.io/develop/api-reference/widgets/st.slider)")
    color = st.select_slider(
        "Select a color of the rainbow",
        options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"])
    st.write("My favorite color is", color)

    st.divider()

    st.markdown("**And here's an example of a range select slider:**")
    start_color, end_color = st.select_slider(
        "Select a range of color wavelength",
        options=["red", "orange", "yellow", "green", "blue", "indigo", "violet"],
        value=("red", "blue"))
    st.write("You selected wavelengths between", start_color, "and", end_color)
    st.write("")

    # Color picker
    st.subheader("[Color picker](https://docs.streamlit.io/develop/api-reference/widgets/st.color_picker)")

    color = st.color_picker("Pick A Color", "#00f900")
    st.write("The current color is", color)
    st.write("")

    st.header(":rainbow[Numeric input elements]", divider=False)

    # NUMERIC INPUT ELEMENTS
    # ----------------------

    # Number input
    # ------------
    # To initialize an empty number input, pass value=`None`
    st.subheader("[Number input](https://docs.streamlit.io/develop/api-reference/widgets/st.number_input)")
    number = st.number_input("Insert a number")
    st.write("The current number is ", number)
    # st.divider()
    st.write("")
    # print("Rerun registered")


    # Slider
    # ------
    st.subheader("[Slider](https://docs.streamlit.io/develop/api-reference/widgets/st.slider)")
    age = st.slider("How old are you?", 0, 130, 25)
    st.write("I'm ", age, "years old")

    st.divider()

    st.markdown("**And here's an example of a range slider:**")
    values = st.slider(
        "Select a range of values",
        0.0, 100.0, (25.0, 75.0))
    st.write("Values:", values)

    st.divider()

    st.markdown("**This is a range time slider:**")
    appointment = st.slider(
        "Schedule your appointment:",
        value=(time(11, 30), time(12, 45)))
    st.write("You're scheduled for:", appointment)

    st.divider()

    st.markdown("**Finally, a datetime slider:**")
    start_time = st.slider(
        "When do you start?",
        value=datetime(2020, 1, 1, 9, 30),
        format="MM/DD/YY - hh:mm")
    st.write("Start time:", start_time)
    st.text("")

    # DATE AND TIME INPUT ELEMENTS
    # ----------------------------

    st.header(":rainbow[Date and time input elements]", divider=False)

    # Date input
    # ----------
    # To initialize an empty date input, pass value=None:
    st.subheader("[Date input](https://docs.streamlit.io/develop/api-reference/widgets/st.date_input)")
    today = datetime.now()
    next_year = today.year + 1
    jan_1 = date(next_year, 1, 1)
    dec_31 = date(next_year, 12, 31)

    d = st.date_input(
        "Select your vacation for next year",
        (jan_1, date(next_year, 1, 7)),
        jan_1,
        dec_31,
        format="MM.DD.YYYY",
    )
    d
    st.write("")

    # Time input
    # ----------
    # To initialize an empty time input, pass value=None:
    st.subheader("[Time input](https://docs.streamlit.io/develop/api-reference/widgets/st.time_input)")
    t = st.time_input("Set an alarm for", time(8, 45))
    st.write("Alarm is set for", t)
    st.write("")

    # TEXT INPUT ELEMENTS
    # -------------------
    st.header(":rainbow[Text input elements]", divider=False)

    # Text input
    # ----------
    st.subheader("[Text input](https://docs.streamlit.io/develop/api-reference/widgets/st.text_input)")
    title = st.text_input("Movie title", "Life of Brian")
    st.write("The current movie title is", title)

    st.divider()

    st.markdown(
        """
        Text input widgets can customize how to hide their 
        labels with the `label_visibility` parameter. If "hidden",
        the label doesn’t show but there is still empty space for it
        above the widget (equivalent to `label=""`). If "collapsed", both
        the label and the space are removed. Default is "visible".
        Text input widgets can also be `disabled` with the disabled parameter,
        and can display an optional `placeholder` text when the text input is
        empty using the placeholder parameter:
        """
    )

    # Adds invisible new line
    st.text("")
    # Store the initial value of widgets in session state
    if "visibility" not in st.session_state:
        st.session_state.visibility = "visible"
        st.session_state.disabled = False

    col1, col2 = st.columns(2)

    with col1:
        st.checkbox("Disable text input widget", key="disabled")
        st.radio(
            "Set text input label visibility 👉",
            key="visibility",
            options=["visible", "hidden", "collapsed"],
        )
        st.text_input(
            "Placeholder for the other text input widget",
            "This is a placeholder",
            key="placeholder",
        )

    # print(type(st.session_state.disabled))
    # print(st.session_state.disabled)
    with col2:
        text_input = st.text_input(
            "Enter some text 👇",
            label_visibility=st.session_state.visibility,
            disabled=st.session_state.disabled,
            placeholder=st.session_state.placeholder,
        )

        if text_input:
            st.write("You entered: ", text_input)
    st.write("")

    # Text area input
    # ---------------
    st.subheader("[Text area](https://docs.streamlit.io/develop/api-reference/widgets/st.text_area)")
    txt = st.text_area(
        "Text to analyze",
        "It was the best of times, it was the worst of times, it was the age of "
        "wisdom, it was the age of foolishness, it was the epoch of belief, it "
        "was the epoch of incredulity, it was the season of Light, it was the "
        "season of Darkness, it was the spring of hope, it was the winter of "
        "despair, (...)",
        )

    st.write(f"You wrote {len(txt)} characters.")
    # print("Rerun registered")
    st.write("")

    # Chat input
    # ----------
    st.subheader("[Chat input](https://docs.streamlit.io/develop/api-reference/chat/st.chat_input)")
    st.markdown(
        """
        When `st.chat_input` is used in the main body of an app, it will be pinned to the bottom of the page.
        It's a very heavy widget, also makes your entire window scroll down on page refresh.
        One way to get around this is to nest it inside a layout container (container, columns, tabs, sidebar, etc).
        Can even create chat interfaces embedded next to other content or have
        multiple chat bots!
        """
    )
    # prompt = st.chat_input("Say something")
    # if prompt:
    #     st.write(f"User has sent the following prompt: {prompt}")

    # st.divider()

    # The chat input can also be used inline by nesting it inside any
    # layout container (container, columns, tabs, sidebar, etc).
    # Create chat interfaces embedded next to other content or have
    # multiple chat bots!

    # with st.sidebar:
    #     messages = st.container(height=300)
    #     if prompt := st.chat_input("Say something"):
    #         messages.chat_message("user").write(prompt)
    #         messages.chat_message("assistant").write(f"Echo: {prompt}")

    with st.container():
        prompt = st.chat_input("Say something")
        if prompt:
            st.write(f"User has sent the following prompt: {prompt}")

        # st.write("This is a container")
        # st.write("This is another container")
        # st.write("This is a third container")
    st.write("")
    # OTHER INPUT ELEMENTS
    # --------------------
    st.header(":rainbow[Other input elements]", divider=False)

    # Data editor
    # -----------
    st.subheader("[Data editor](https://docs.streamlit.io/develop/api-reference/data/st.data_editor)")
    st.markdown(
        """
        **The data editor widget allows you to edit dataframes
        and many other data structures in a table-like UI**.
        """
    )
    df = pd.DataFrame(
        [
            {"command": "st.selectbox", "rating": 4, "is_widget": True},
            {"command": "st.balloons", "rating": 5, "is_widget": False},
            {"command": "st.time_input", "rating": 3, "is_widget": True},
        ]
    )
    edited_df = st.data_editor(df)

    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    st.divider()

    st.markdown(
        """
        **You can also allow the user to add and delete rows by setting `num_rows` to "dynamic"**:
        """
    )

    df = pd.DataFrame(
        [
            {"command": "st.selectbox", "rating": 4, "is_widget": True},
            {"command": "st.balloons", "rating": 5, "is_widget": False},
            {"command": "st.time_input", "rating": 3, "is_widget": True},
        ]
    )
    edited_df = st.data_editor(df, num_rows="dynamic")

    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    st.divider()

    st.markdown(
        """
        **Or you can customize the data editor via `column_config`, `hide_index`
        `column_order`, or `disabled`**:
        """
    )

    df = pd.DataFrame(
        [
            {"command": "st.selectbox", "rating": 4, "is_widget": True},
            {"command": "st.balloons", "rating": 5, "is_widget": False},
            {"command": "st.time_input", "rating": 3, "is_widget": True},
        ]
    )
    edited_df = st.data_editor(
        df,
        column_config={
            "command": "Streamlit Command",
            "rating": st.column_config.NumberColumn(
                "Your rating",
                help="How much do you like this command (1-5)?",
                min_value=1,
                max_value=5,
                step=1,
                format="%d ⭐",
            ),
            "is_widget": "Widget ?",
        },
        disabled=["command", "is_widget"],
        hide_index=True,
    )

    favorite_command = edited_df.loc[edited_df["rating"].idxmax()]["command"]
    st.markdown(f"Your favorite command is **{favorite_command}** 🎈")

    st.divider()

    st.markdown(
        """
        **Configuring columns**\n
        You can configure the display and editing behavior of columns
        in `st.dataframe` and `st.data_editor` via the 
        [Column configuration](https://docs.streamlit.io/develop/api-reference/data/st.column_config) 
        API. We have developed the API to let you add images, charts,
        and clickable URLs in dataframe and data editor columns.
        Additionally, you can make individual columns editable,
        set columns as categorical and specify which options they can take,
        hide the index of the dataframe, and much more.
        """
    )
    st.write("")

    # File uploader
    # -------------
    st.subheader("[File uploader](https://docs.streamlit.io/develop/api-reference/widgets/st.file_uploader)")
    st.markdown(
        """
        **Insert a file uploader that accepts a single file at a time**:
        """
    )
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # To read file as bytes:
        bytes_data = uploaded_file.getvalue()
        st.write(bytes_data)

        # To convert to a string based IO:
        stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
        st.write(stringio)

        # To read file as string:
        string_data = stringio.read()
        st.write(string_data)

        # Can be used wherever a "file-like" object is accepted:
        dataframe = pd.read_csv(uploaded_file)
        st.write(dataframe)

    st.divider()

    st.markdown(
        """
        **Insert a file uploader that accepts multiple files at a time:**
        """
    )

    uploaded_files = st.file_uploader("Choose a CSV file", accept_multiple_files=True)
    for uploaded_file in uploaded_files:
        bytes_data = uploaded_file.read()
        st.write("filename:", uploaded_file.name)
        st.write(bytes_data)

    st.write("")

    # Camera input
    # ------------
    st.subheader("[Camera input](https://docs.streamlit.io/develop/api-reference/widgets/st.camera_input)")
    st.markdown(
        """
        Display a widget that returns pictures from the user's webcam.\n
        Code commented out. See *./pages/1_Widgets.py* for the full code.
        """
    )

    # picture = st.camera_input("Take a picture")

    # if picture:
    #     st.image(picture)

    # st.divider()


    # To read the image file buffer as bytes`,
    # you can use `getvalue()` on the `UploadedFile` object.


    # img_file_buffer = st.camera_input("Take a picture")

    # if img_file_buffer is not None:
    #     # To read image file buffer as bytes:
    #     bytes_data = img_file_buffer.getvalue()
    #     # Check the type of bytes_data:
    #     # Should output: <class 'bytes'>
    #     st.write(type(bytes_data))

    # st.header("Third-party components", divider=True)
    # st.subheader("[Streamlit Option Menu](https://github.com/victoryhb/streamlit-option-menu)")
    # st.markdown(
    #     """
    #     Select a single item from a list of options in a menu.
    #     Created by @victoryhb.
    #     """
    # )



if __name__ == '__main__':
    main()
