class LoginPageConstant:
    """Constants related to Login Page"""

    # Sign up

    SIGN_UP_USERNAME_XPATH = ".//input[@id='username-register']"
    SIGN_UP_EMAIL_XPATH = ".//input[@id='email-register']"
    SIGN_UP_PASSWORD_XPATH = ".//input[@id='password-register']"
    SIGN_UP_BUTTON_XPATH = ".//button[@type='submit']"

    # Sign In

    SIGN_IN_USERNAME_XPATH = ".//input[@placeholder='Username']"
    SIGN_IN_PASSWORD_XPATH = ".//input[@placeholder='Password']"
    SIGN_IN_BUTTON_TEXT = "Sign In"
    SIGN_IN_BUTTON_XPATH = f".//button[contains(text(), '{SIGN_IN_BUTTON_TEXT}')]"

    # Messages

    INVALID_LOGIN_MESSAGE_TEXT = 'Invalid username / password'
    # INVALID_LOGIN_MESSAGE_XPATH = f".//div[contains(text(), '{INVALID_LOGIN_MESSAGE_TEXT}')]"
    INCORRECT_USERNAME_MESSAGE_TEXT = 'Username can only contain letters and numbers.'
    INCORRECT_USERNAME_MESSAGE_XPATH = f".//div[contains(text(), '{INCORRECT_USERNAME_MESSAGE_TEXT}')]"
    INCORRECT_PASSWORD_MESSAGE_TEXT = 'Password must be at least 12 characters.'
    INCORRECT_PASSWORD_MESSAGE_XPATH = f".//div//div[contains(text(), '{INCORRECT_PASSWORD_MESSAGE_TEXT}')]"
    INCORRECT_EMAIL_MESSAGE_TEXT = 'You must provide a valid email address.'
    INCORRECT_EMAIL_MESSAGE_XPATH = f".//div[contains(text(), '{INCORRECT_EMAIL_MESSAGE_TEXT}')]"
    EXISTING_EMAIL_TEXT = 'That email is already being used.'
    EXISTING_EMAIL_XPATH = f".//div[contains(text(), '{EXISTING_EMAIL_TEXT}')]"
    EXISTING_USERNAME_TEXT = 'That username is already taken.'
    EXISTING_USERNAME_XPATH = f".//div[contains(text(), '{EXISTING_USERNAME_TEXT}')]"
