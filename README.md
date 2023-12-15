# Google Gmail API

#### This code provides a simple terminal interface to interact with the Gmail API, allowing users to create drafts with subject, email, and content.

## Deployment
1. Clone the repository: `git clone "url repository"`
2. Create virtual venv
3. Activate venv
4. Install dependencies: `pip install -r requirements.txt`


## Warning
A secret file is required for correct work obtain client secret JSON file from the Google Cloud Console.

For this you need:
1. Sign in to Google Cloud console and create a New Project or continue with an existing project.

2. Go to APIs and Services.

3. Enable Gmail API for the selected project.

4. Now, configure the Consent screen by clicking on OAuth Consent Screen if it is not already configured.

5. Enter the Application name and save it.

6. Now go to Credentials.

7. Click on Create credentials, and go to OAuth Client ID.


8. Choose application type as Desktop Application.
9. Enter the Application name, and click on the Create button.
10. The Client ID will be created. Download it to your computer and save it as credentials.json


## Description

##### I used OOP in the code, for cleaner and readable code and also the following benefits:

- __Encapsulation__: A class allows you to group together related data and functionality using an object-oriented approach. This additionally hides the internal implementation from the user and divides the code into logical blocks.

- __Parameters and Constructor__: The __init__ constructor is used to initialize an object with the specified parameters. This allows you to ensure the initial state of the object when it is created.

##### Logging 
also I used logging, it provides more convenience such as logging level, info, error, others and error tracking time