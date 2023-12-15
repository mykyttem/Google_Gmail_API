import os
import base64
import logging

# google utils
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.errors import HttpError

# for dealing with attachement MIME types
from email.message import EmailMessage


# Request all access (permission to read/send/receive emails, manage the inbox, and more)
# your secret file must have a name "credentials"
CLIENT_SECRET = 'credentials.json'
SCOPES = ['https://mail.google.com/']
API_NAME = 'gmail'
API_VERSION = 'v1'

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Gmail_API:
    def __init__(self, subject: str, email: str, content: str, access: bool = False):
        self.subject = subject
        self.email = email
        self.content = content
        self.access = access
        self.creds = None

    
    def main(self):

        if os.path.exists(CLIENT_SECRET):

            # If there are no (valid) credentials available, let the user log in.
            if not self.creds or not self.creds.valid:
                if self.creds and self.creds.expired and self.creds.refresh_token:
                    self.creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        CLIENT_SECRET, SCOPES
                    )
                    self.creds = flow.run_local_server(port=0)

            # Save the credentials for the next run
            with open("token.json", "w") as token:
                token.write(self.creds.to_json())

            try:
                # Call the Gmail API
                service = build(API_NAME, API_VERSION, credentials=self.creds)
                results = service.users().labels().list(userId="me").execute()
                labels = results.get("labels", [])

                if not labels:
                    logger.warning("No labels found")
                    return

                # set True, to control the API
                self.access = True
                logger.info(f"Access {self.access}")

            except HttpError as error:
                logger.error(f"An error occured: {error}")
        else:
            logger.error("No such SECRET file")


    def gmail_create_draft(self):
        if self.access == True:
            try:
                # create gmail api client
                service = build(API_NAME, API_VERSION, credentials=self.creds)

                # message
                message = EmailMessage()
                message.set_content(self.content)
                
                message["To"] = self.email
                message["From"] = self.email
                message["Subject"] = self.subject

                # encoded message
                encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()
                
                create_message = {"message": {"raw": encoded_message}}
                # pylint: disable=E1101
                draft = (
                    service.users()
                    .drafts()
                    .create(userId="me", body=create_message)
                    .execute()
                )

                logger.info(f'Draft id: {draft["id"]}\nDraft message: {draft["message"]}')
            except HttpError as error:
                logger.info(f"An error occurred: {error}")
                draft = None

            return draft
        else:
            logger.warning("Access is not granted. Cannot create draft.")


# user input
subject = input("Type subject: ")
email = input("Type email: ") 
content = input("Type content: ")


if __name__ == "__main__":
    gmail = Gmail_API(subject=subject, email=email, content=content)
    gmail.main()
    gmail.gmail_create_draft()