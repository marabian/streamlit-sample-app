# ./pages/3_Miscellaneous.py

import time
import streamlit as st
from modules.nav import Navbar

st.set_page_config(
    page_title="Miscellaneous",
    page_icon="📦",
    # layout="wide",
)


def main():
    Navbar()

    # st.title("")
    st.title(":blue-background[:orange[📦 Miscellaneous]]")
    st.write("Miscellaneous features of Streamlit.")

    # Content goes here
    # -----------------
    # st.header(":blue-background[:orange[Display progress and status]]")
    # st.header("[Display progress and status](https://docs.streamlit.io/develop/api-reference/status)")

    # st.markdown("""
    #     <style>
    #     a.custom-link {
    #         text-decoration: none;  # Removes the underline
    #         # color: red;  # Optional: Ensures the link uses the default text color
    #     }
    #     </style>

    #     <h2>
    #         <a href="https://docs.streamlit.io/develop/api-reference/status" class="custom-link">
    #             Display progress and status
    #         </a>
    #     </h2>
    # """, unsafe_allow_html=True)

    st.header("[:rainbow[Status Elements]](https://docs.streamlit.io/develop/api-reference/status)")
    # Animated status elements
    # ------------------------

    # st.header("Display progress and status")

    # Progress bar
    # ------------
    st.subheader("[Progress bar](https://docs.streamlit.io/develop/api-reference/status/st.progress)")
    progress_text = "Operation in progress. Please wait."
    st.markdown(
        """
        Here is an example of a progress bar increasing over time
        and disappearing when it reaches completion:
        """
    )
    if st.button("Start progress bar"):
        my_bar = st.progress(0, text=progress_text)

        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1, text=progress_text)
        time.sleep(1)
        my_bar.empty()
    st.text("")

    # Spinner
    # -------
    st.subheader("[Spinner](https://docs.streamlit.io/develop/api-reference/status/st.spinner)")
    # with st.spinner('Wait for it...'):
    #     time.sleep(2)
    # st.success('Done!')
    if st.button("Start spinner"):
        with st.spinner('In progress...'):
            time.sleep(2)
        st.success('Done!')
    st.text("")

    # Status
    # ------
    st.subheader("[Status](https://docs.streamlit.io/develop/api-reference/status/st.status)")
    st.markdown(
        """
        Insert a status container to display output from long-running tasks.

        Inserts a container into your app that is typically
        used to show the status and details of a process or task.
        The container can hold multiple elements and can be expanded
        or collapsed by the user similar to `st.expander`.
        When collapsed, all that is visible is the status icon
        and label.

        The label, state, and expanded state can all be 
        updated by calling `.update()` on the returned object.
        To add elements to the returned container, 
        you can use with notation (preferred) or just call
        methods directly on the returned object.

        By default, `st.status()` initializes in the "running" state. 
        When called using `with` notation, it automatically updates 
        to the "complete" state at the end of the "with" block. 
        See examples below for more details.
        """
    )

    if st.button("Start status"):
        with st.status("Downloading data..."):
            st.write("Searching for data...")
            time.sleep(0.5)
            st.write("Found URL.")
            time.sleep(0.5)
            st.write("Downloading data...")
            time.sleep(0.5)
    st.text("")
    # You can also use `.update()` on the container to change the label, state, or expanded state:

    # # st.write(st.session_state)
    # with st.status("Downloading data...", expanded=True) as status:
    #     st.write("Searching for data...")
    #     time.sleep(2)
    #     st.write("Found URL.")
    #     time.sleep(1)
    #     st.write("Downloading data...")
    #     time.sleep(1)
    #     status.update(label="Download complete!", state="complete", expanded=False)

    # st.button("Rerun")

    # Toast
    # -----
    st.subheader("[Toast](https://docs.streamlit.io/develop/api-reference/status/st.toast)")
    st.markdown(
        """
        Display a short message, known as a notification "toast".

        The toast appears in the app's bottom-right corner and disappears after four seconds.
        """
    )
    if st.button("Show toast"):

        st.toast('Your edited image was saved!', icon='😍')

    st.divider()

    st.markdown(
        """
        When multiple toasts are generated, 
        they will stack. Hovering over a toast will stop
        it from disappearing. When hovering ends, the toast will
        disappear after four more seconds.
        """
    )

    if st.button('Three cheers'):
        st.toast('Hip!')
        time.sleep(.5)
        st.toast('Hip!')
        time.sleep(.5)
        st.toast('Hooray!', icon='🎉')
    st.text("")

    # Balloons
    # --------
    st.subheader("[Balloons](https://docs.streamlit.io/develop/api-reference/status/st.balloons)")
    st.markdown("Draw celebratory balloons.")
    if st.button("Balloons"):
        st.balloons()
    st.text("")


    # Snowflakes
    # ----------
    st.subheader("[Snowflakes](https://docs.streamlit.io/develop/api-reference/status/st.snow)")
    if st.button("Snowflakes"):
        st.snow()
    st.text("")

    # Callouts
    # --------


    # Success callout
    # ---------------
    st.subheader("[Success box](https://docs.streamlit.io/develop/api-reference/status/st.success)")
    st.success('This is a success message!', icon="✅")
    st.write("")

    # Info callout
    # ------------
    st.subheader("[Info box](https://docs.streamlit.io/develop/api-reference/status/st.info)")
    st.info('This is a purely informational message', icon="ℹ️")
    st.write("")

    # Warning callout
    # ---------------
    st.subheader("[Warning box](https://docs.streamlit.io/develop/api-reference/status/st.warning)")
    st.warning('This is a warning', icon="⚠️")
    st.write("")

    # Error callout
    # ------------
    st.subheader("[Error box](https://docs.streamlit.io/develop/api-reference/status/st.error)")
    st.error('This is an error', icon="🚨")
    st.write("")

    # Exception
    # ---------
    st.subheader("[Exception](https://docs.streamlit.io/develop/api-reference/status/st.exception)")
    e = RuntimeError('This is an exception of type RuntimeError')
    st.exception(e)
    st.write("")

    # st.header("[:rainbow[Data elements]](https://docs.streamlit.io/develop/api-reference/data)")

    # # Simple callout messages
    # # -----------------------
    # st.subheader("[Success, Info, Warning, Error](https://docs.streamlit.io/develop/api-reference/status)")
if __name__ == '__main__':
    main()






# st.set_page_config(page_title="Plotting Demo", page_icon="📈")

# st.markdown("# Plotting Demo")
