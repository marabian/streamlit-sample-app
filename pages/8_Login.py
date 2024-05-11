# ./pages/8_Login.py

import yaml
from yaml.loader import SafeLoader
import pandas as pd
import streamlit as st
from streamlit_extras.stylable_container import stylable_container
import streamlit_authenticator as stauth
from streamlit_authenticator.utilities.hasher import Hasher
from modules.nav import Navbar

st.set_page_config(
    page_title="Login",
    page_icon="🔒",
    # layout="wide",
)


def main():
    Navbar()

    st.title(":lock[🔒 Login]")

    # HOW TO HASH USER PASSWORDS AND SETUP CONFIG FILE
    # ------------------------------------------------
    passwords_to_hash = ['abc', 'def']
    hashed_passwords = Hasher(passwords_to_hash).generate()
    print(hashed_passwords)

    with open('./config.yaml') as f:
        config = yaml.load(f, Loader=SafeLoader)
    # hashed_passwords = stauth.Hasher(['abc', 'def']).generate()

    print(hashed_passwords)

    authenticator = stauth.Authenticate(
        config['credentials'],
        config['cookie']['name'],
        config['cookie']['key'],
        config['cookie']['expiry_days'],
        config['preauthorized']
    )

    # Render the login module
    authenticator.login(location='main')

    # HOW TO AUTHENTICATE USERS
    # -------------------------
    # Step 3. Authenticate users
    if st.session_state["authentication_status"]:
        authenticator.logout("Logout", "sidebar")
        st.write(f'Welcome :rainbow[*{st.session_state["name"]}*]')

        if st.session_state["username"] == 'test':
            st.markdown("TESTING TESTING TESTING")
            # st.switch_page("pages/1_Widgets.py")

        st.title('How to Setup Authentication in Streamlit')

        st.header("How to hash user passwords", divider=True)

        st.subheader('Step 1: Create the YAML file:')
        code = """
            credentials:
                usernames:
                        jsmith:
                        email: jsmith@gmail.com
                        name: John Smith
                        password: abc # To be replaced with hashed password
                    rbriggs:
                        email: rbriggs@gmail.com
                        name: Rebecca Briggs
                        password: def # To be replaced with hashed password
            cookie:
                expiry_days: 30
                key: random_signature_key # Must be string
                name: random_cookie_name
            preauthorized:
                emails:
                    - melsby@gmail.com
            """

        st.code(code, language='yaml')

        st.subheader("Step 2. Get hashed password(s) and generate secret token to use as signature key:")


        code = """
            passwords_to_hash = ['abc', 'def']
            hashed_passwords = stauth.Hasher(['abc', 'def']).generate()
        """

        st.code(code, language='python')

        st.markdown(
            """
            Also make sure to replace `random_signature_key` and `random_cookie_name` with your own values.

            Here is how you can generate a secret key in python to use as a signature key:
            """
        )

        code = """
            import secrets
            secret_key = secrets.token_urlsafe(32)
            print(secret_key)
        """

        st.code(code, language='python')

        st.subheader("Step 3: Replace plain text passwords with hashed passwords in the YAML file:")
        st.markdown(
            """
            Make sure to replace occurrences of `password` in the YAML file above with the hashed password(s).

            Also make sure to replace the `key` and `name` in the YAML file with the secret key and cookie name generated above (create oen).
            """
        )

        st.header("How to create a login widget", divider=True)

        st.markdown(
            """
            Now that you’ve defined your users’ credentials and configuration settings,
            you’re ready to create an authenticator object.
            """
        )

        st.subheader("Step 1. Import the YAML file into your script:")

        code = """
            import yaml
            from yaml.loader import SafeLoader
            with open('../config.yaml') as file:
                config = yaml.load(file, Loader=SafeLoader)
        """

        st.code(code, language='python')

        st.subheader("Step 2. Create the authenticator object:")

        code = """
            authenticator = Authenticate(
                config['credentials'],
                config['cookie']['name'],
                config['cookie']['key'],
                config['cookie']['expiry_days'],
                config['preauthorized']
            )
            """

        st.code(code, language='python')

        st.subheader("Step 3. Render the login widget by providing a name for the form and its location (i.e., sidebar or main):")

        code = """
            authenticator.login(location='main')
            """

        st.code(code, language='python')
        # st.subheader('Step 2: Generate a secret key to use as JWT token')
        # code = """
        # import secrets
        # secret_key = secrets.token_urlsafe(32)  # Generates a 32-byte base64 URL-safe key
        # print(secret_key)
        # """

        # st.code(code, language='python')

        st.header("How to authenticate users", divider=True)

        st.markdown(
            """
            Once you have your authenticator object up and running,
            use the return values to read the name, authentication_status, and username of the authenticated user.

            You can ppt-in for a logout button and add it as follows:
            """
        )

        st.code(
            """
            if authentication_status:
                authenticator.logout('Logout', 'main')
                st.write(f'Welcome *{name}*')
                st.title('Some content')
            elif authentication_status == False:
                st.error('Username/password is incorrect')
            elif authentication_status == None:
                st.warning('Please enter your username and password')
            """
        )

        st.write('Or you can access the same values through a session state:')

        st.code(
            """
            if st.session_state["authentication_status"]:
                authenticator.logout('Logout', 'main')
                st.write(f'Welcome *{st.session_state["name"]}*')
                st.title('Some content')
            elif st.session_state["authentication_status"] == False:
                st.error('Username/password is incorrect')
            elif st.session_state["authentication_status"] == None:
                st.warning('Please enter your username and password')
            """
        )

        st.markdown("After logging out, the `authentication_status` will revert back to None and the authentication cookie will be removed.")
        st.text("")

        st.markdown(
            """
            **Note on JWT tokens:**

            The first time the user logs in, the auth module uses the username (must be unique) and the secret token to generate a JWT token. At every subsequent request to the server, they must send this token.

            This ensures that another client can't just call our server and get the user info of any user.
            """
        )

        # HOW TO IMPLEMENT USER PRIVILEGES
        # ---------------------------------
        st.header("How to implement user privileges", divider=True)

        st.markdown(
            """
            Given that the authenticator object returns the username of your
            logged-in user, you can utilize that to implement user privileges where each user
            receives a more personalized experience as shown below:
            """
        )

        st.code(
            """
            name, authentication_status, username = authenticator.login('Login', 'main')
            if authentication_status:
                authenticator.logout('Logout', 'main')
                if username == 'jsmith':
                    st.write(f'Welcome *{name}*')
                    st.title('Application 1')
                elif username == 'rbriggs':
                    st.write(f'Welcome *{name}*')
                    st.title('Application 2')
            elif authentication_status == False:
                st.error('Username/password is incorrect')
            elif authentication_status == None:
                st.warning('Please enter your username and password')
            """
        )

        st.markdown(
            """
            As you can see, each user is redirected to a separate application
            to cater to that specific user’s needs.
            """
        )


        # CREATE A PASSWORD RESET WIDGET
        # -------------------------------
        st.header("How to create a password reset widget", divider=True)

        st.markdown(
            """
            If your user needs to reset their password to a new one, use the `reset_password` widget to allow the already logged-in user to change their password:
            """
        )

        code = """
        if st.session_state["authentication_status"]:
            try:
                if authenticator.reset_password(st.session_state["username"]):
                    st.success('Password modified successfully')
            except Exception as e:
                st.error(e)
            """
        st.code(code, language='python')





        # HOW TO CREATE A NEW USER REGISTRATION WIDGET
        # ---------------------------------------------
        st.header("How to create a new user registration widget", divider=True)

        st.markdown(
            """
            If you want to allow pre-authorized or even non-pre-authorized users to register,
            use the `register_user` widget to allow a user to register for your app.
            If you want the user to be pre-authorized, set the `preauthorization` argument to True and add their email to the `preauthorized` list in the configuration file. Once they have registered, their email will automatically be removed from the preauthorized list in the configuration file.

            To let any user register, set the `preauthorization` argument to False:
            """
        )

        code = """
        try:
            email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(pre_authorization=False)
            if email_of_registered_user:
                st.success('User registered successfully')
        except Exception as e:
            st.error(e)
            """

        st.code(code, language='python')


        # HOW TO CREATE A FORGOT PASSWORD WIDGET
        st.header("How to create a forgot password widget", divider=True)

        st.markdown(
            """
            If you want to allow a user to reset a forgotten password, 
            use the `forgot_password` widget to allow them to generate a new random password. 
            This new password will be automatically hashed and stored in the configuration file.
            The widget will also return the user's username, email, and new random password (for you to securely send to the user):
            """
        )

        code = """
            try:
                username_forgot_pw, email_forgot_password, random_password = authenticator.forgot_password('Forgot password')
                if username_forgot_pw:
                    st.success('New password sent securely')
                    # Random password to be transferred to user securely
                elif username_forgot_pw == False:
                    st.error('Username not found')
            except Exception as e:
                st.error(e)
            """

        st.code(code, language='python')

        # UPDATING THE CONFIGURATION FILE
        # -------------------------------
        st.header("Updating the configuration file", divider=True)

        st.markdown(
            """
            Please ensure that the configuration file is re-saved anytime the credentials are
            updated or whenever the `reset_password`, `register_user`, `forgot_password`, or `update_user_details`
            widgets are used.
            """
        )

        code = """
            with open('../config.yaml', 'w') as file:
                yaml.dump(config, file, default_flow_style=False)
            """

        st.code(code, language='python')

        st.markdown("Can store this YAML file on the cloud (e.g. AWS S3):")

        code = """
            import yaml
            yaml_data = yaml.dump(config, default_flow_style=False)
            s3 = boto3.client('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name = region)
            s3.put_object(Bucket=user_config_bucket, Key=user_config_key, Body=yaml_data)
            """

        st.code(code, language='python')


        # SEE MORE
        # --------
        st.markdown(
            """
            [Read this](https://blog.streamlit.io/streamlit-authenticator-part-2-adding-advanced-features-to-your-authentication-component/)
            for more advanced features forgotten username widget, update user details widget.

            Also read [this](https://pypi.org/project/streamlit-authenticator/). Might be more up-to-date.
            """
        )

    elif st.session_state["authentication_status"] is False:
        st.error('Username/password is incorrect')
    elif st.session_state["authentication_status"] is None:
        st.warning('Please enter your username and password')


if __name__ == '__main__':
    main()
