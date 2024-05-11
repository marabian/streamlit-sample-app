import streamlit as st

# # Access the GCP API key
# gcp_api_key = st.secrets["gcp"]["api_key"]

# # Example use of the API key
# st.write("Your GCP API Key is:", gcp_api_key)

# Define a function for the home page
def page_one():
    st.title('Page one')
    st.write('Welcome to the page one!')

    st.divider()

    # form with border=True/False
    st.header('Forms', divider='violet')
    # st.header('_Streamlit_ is :blue[cool] :sunglasses:')
    with st.form("login", border=True):
        st.markdown("**Hello World**")
        st.form_submit_button("Submit")

    st.divider()

    with st.form("my_form"):
        st.write("Inside the form")
        slider_val = st.slider("Form slider")
        checkbox_val = st.checkbox("Form checkbox")

        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write("slider", slider_val, "checkbox", checkbox_val)

    st.write("Outside the form")

    st.header('Popover', divider='violet')
    with st.popover("Open popover"):
        st.markdown("Hello World 👋")
        name = st.text_input("What's your name?")

    st.write("Your name:", name)

    st.divider()

    popover = st.popover("Filter items")
    red = popover.checkbox("Show red items.", True)
    blue = popover.checkbox("Show blue items.", True)

    if red:
        st.write(":red[This is a red item.]")
    if blue:
        st.write(":blue[This is a blue item.]")

    st.header('Experimental Dialog', divider='violet')

    @st.experimental_dialog("Cast your vote")
    def vote(item):
        st.write(f"Why is {item} your favorite?")
        reason = st.text_input("Because...")
        if st.button("Submit"):
            print('lol')
            st.session_state.vote = {"item": item, "reason": reason}
            st.rerun()

    if "vote" not in st.session_state:
        st.write("Vote for your favorite")
        if st.button("A"):
            vote("A")
        if st.button("B"):
            vote("B")
    else:
        print('lool')
        st.markdown(f"You voted for {st.session_state.vote['item']} because {st.session_state.vote['reason']}")



# Define a function for the second page
def page_two():
    st.title('Page Two')
    st.write('Welcome to page two!')

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to', ['Page One', 'Page Two'])

# Page routing
if page == 'Page One':
    page_one()
elif page == 'Page Two':
    page_two()
