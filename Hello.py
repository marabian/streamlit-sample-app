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
        - [Streamlit Plotly Cheat Sheet App](https://plotly.streamlit.app/)

        ### Forum Posts
        - [Setting up a multi-page Streamlit app using using `st.page_link`](https://discuss.streamlit.io/t/rename-the-home-page-in-a-multi-page-app/65533)
        - [How to build a unique button](https://discuss.streamlit.io/t/how-to-build-an-unique-button-in-streamlit-web-program/12012/1)
        - [How to change font size/color/etc](https://discuss.streamlit.io/t/change-font-size-in-st-write/7606)
        - [Applying custom CSS to button using `stylable_container`](https://discuss.streamlit.io/t/issue-with-coloring-buttons-in-streamlit/56914/6)
        - [How to create dynamic content using `st.empty` placeholders](https://discuss.streamlit.io/t/ugly-screen-shifting-when-rendering-how-to-avoid-this/7790/11)
        - [How to use new CSS `:has` pseudo-class on a simple <span> tag (this is how Stylable Containers works)](https://discuss.streamlit.io/t/applying-custom-css-to-manually-created-containers/33428/7)
        - [How to create dynamic number of tabs](https://discuss.streamlit.io/t/create-a-variable-number-of-tabs-based-on-dataframe-values/31297/3)
        - [How to save widget values when navigating between pages](https://docs.streamlit.io/develop/concepts/architecture/widget-behavior#save-widget-values-in-session-state-to-preserve-them-between-pages)
        - [Very important post on how to get Streamlit deployment working on GCP Cloud Run](https://discuss.streamlit.io/t/problems-with-streamlit-deployment-on-gcp/23604)
        - [Important post on how to fix issue of config.toml not being read/loaded in Cloud Run](https://discuss.streamlit.io/t/config-toml-not-being-used-in-google-cloud-run/55596/5)
        - [Issue being tracked for problem above](https://issuetracker.google.com/issues/221496605?pli=1)
        - [GitHub Issue for same thing above](https://github.com/streamlit/streamlit/issues/7731)
        - [config.toml not working in Streamlit Cloud Deployment](https://discuss.streamlit.io/t/config-toml-do-not-work-after-deployed/24422/3)
        - [How to use Streamlit authenticator with `secrets.toml` file](https://discuss.streamlit.io/t/deploying-streamlit-authenticator-via-streamlit-community-cloud/39085/2)
        - [Putting space between radio buttons](https://discuss.streamlit.io/t/space-between-radio-buttons/37325)
        - [Having some control over hamburger menu on top-right](https://discuss.streamlit.io/t/edit-hamburger-menu/46060)
        - [How to clear Streamlit file uploader widget of cache after uploading files](https://discuss.streamlit.io/t/are-there-any-ways-to-clear-file-uploader-values-without-using-streamlit-form/40903)
        - [How to make plotly charts responsive to layout/screen size](https://discuss.streamlit.io/t/plotly-chart-overlapping-st-columns/30114)
        - [How to put multiple lines in an error message](https://discuss.streamlit.io/t/writing-text-on-multiple-lines-in-an-error-message/29043)
        - [How to style a Select Box](https://discuss.streamlit.io/t/how-to-style-a-selectbox/45465/5)
        - [Flicker after login (no answer/fix yet)](https://discuss.streamlit.io/t/little-flicker-after-login-in-streamlit-authenticator-component/66317)
        - [Change choice in st.selectbox by clicking on a button in a side bar](https://discuss.streamlit.io/t/change-choice-in-st-selectbox-by-clicking-on-a-button-in-a-side-bar/41461)
        - [How to put links in dataframe columns](https://discuss.streamlit.io/t/how-to-display-a-clickable-link-pandas-dataframe/32612/6)
        - [Also see this for putting a label instead of url in columns in dataframes](https://docs.streamlit.io/develop/api-reference/data/st.column_config/st.column_config.linkcolumn)
        - [Clear file uploader/any widget on form submit](https://discuss.streamlit.io/t/file-uploader-how-to-clear-the-list-of-uploaded-files/32729)
        - [Creating a new `text_input` widget every time I click a button](https://discuss.streamlit.io/t/create-a-new-text-input-every-time-i-click-the-button/14124/5)
        - [Recent forum post on python logging on working and fix](https://discuss.streamlit.io/t/simple-logging-am-i-missing-something-obvious/67060)
        - [Guide on GCP Logging](https://cloud.google.com/logging/docs/setup/python)
        - [Set gatherUsageStats via streamlit run paramter](https://github.com/streamlit/streamlit/issues/1299)
        - [How to write to a file, using the Python logging module](https://stackoverflow.com/questions/6386698/how-to-write-to-a-file-using-the-logging-python-module)
        - [Good StackOverflow post on how GCP logger works with the Python logger](https://stackoverflow.com/questions/73687617/send-a-json-payload-with-labels-using-google-cloud-logging-python-library)
        - [Deleting a value in session state](https://discuss.streamlit.io/t/session-state-del-a-value/14785)
        - [Simple/effective way of clearing value of `st.text_input` widget](https://github.com/streamlit/streamlit/issues/4195#issuecomment-998909519)


        ### Tutorials
        - [Setting up a multi-page Streamlit app](https://docs.streamlit.io/get-started/tutorials/create-a-multipage-app)
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
        - [How to configure secrets on Cloud Run](https://cloud.google.com/run/docs/configuring/services/secrets#disallowed_paths_and_limitations)
        - [Useful Tutorial App](https://st-experimental-fragment.streamlit.app/)


        ### GCP/Cloud Stuff
        - [How to delete GCP logs from CLI](https://stackoverflow.com/questions/43969874/how-to-delete-logs-on-google-app-engine)

        ### Random
        - Use `&nbsp;` to put space in markdown
        - How to generate a secure 32bit token for cookie auth token. `import secrets` then `secure_token = secrets.token_urlsafe(32)`


        """
    )



if __name__ == '__main__':
    main()
