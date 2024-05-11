# ./pages/2_Plotting.py

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

    st.title("[:blue-background[📊 Charts]](https://docs.streamlit.io/develop/api-reference/charts)")
    st.write("Overview of plotting in Streamlit")

    # Content goes here
    # -----------------
    st.sidebar.header("Plotting Demo")

    st.header(":rainbow[Simple chart elements]")

    # ANIMATED LINE CHART
    # -------------------
    st.subheader("[Animated Line Chart](https://docs.streamlit.io/develop/api-reference/charts/st.line_chart)")


    st.write(
        """
        This demo illustrates a combination of plotting and animation with
        Streamlit. We're generating a bunch of random numbers in a loop for around
        5 seconds. Enjoy!
        """
    )

    progress_bar = st.sidebar.progress(0)
    status_text = st.sidebar.empty()
    last_rows = np.random.randn(1, 1)
    chart = st.line_chart(last_rows)

    for i in range(1, 101):
        new_rows = last_rows[-1, :] + np.random.randn(5, 1).cumsum(axis=0)
        status_text.text("%i%% Complete" % i)
        chart.add_rows(new_rows)
        progress_bar.progress(i)
        last_rows = new_rows
        time.sleep(0.05)

    progress_bar.empty()


    st.text("")

    # AREA CHART
    # ----------
    # st.subheader("[Area Chart](https://docs.streamlit.io/develop/api-reference/charts/st.area_chart)")

if __name__ == '__main__':
    main()






# st.set_page_config(page_title="Plotting Demo", page_icon="📈")

# st.markdown("# Plotting Demo")
