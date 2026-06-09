import os
import pickle
import base64
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/gmail.modify']

def get_gmail_service():
    """Authenticate and return Gmail service."""
    creds = None
    
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    return build('gmail', 'v1', credentials=creds)

def read_emails(service, max_results=5):
    """Read unread emails from inbox."""
    results = service.users().messages().list(
        userId='me',
        labelIds=['INBOX'],
        q='is:unread',
        maxResults=max_results
    ).execute()
    
    messages = results.get('messages', [])
    
    emails = []
    for msg in messages:
        message = service.users().messages().get(
            userId='me', 
            id=msg['id'],
            format='full'
        ).execute()
        
        headers = message['payload']['headers']
        subject = next(h['value'] for h in headers if h['name'] == 'Subject')
        sender = next(h['value'] for h in headers if h['name'] == 'From')
        
        # Get email body
        body = ""
        if 'parts' in message['payload']:
            for part in message['payload']['parts']:
                if part['mimeType'] == 'text/plain':
                    data = part['body']['data']
                    body = base64.urlsafe_b64decode(data).decode()
        elif 'body' in message['payload']:
            data = message['payload']['body']['data']
            body = base64.urlsafe_b64decode(data).decode()
        
        emails.append({
            'id': msg['id'],
            'subject': subject,
            'sender': sender,
            'body': body[:500],
            'thread_id': message['threadId']
        })
    
    return emails

def list_recent_emails():
    """Test function to list recent emails."""
    service = get_gmail_service()
    emails = read_emails(service, max_results=10)
    
    for i, email in enumerate(emails):
        print(f"\n{'='*50}")
        print(f"Email #{i+1}")
        print(f"From: {email['sender']}")
        print(f"Subject: {email['subject']}")
        print(f"Body: {email['body'][:200]}...")

if __name__ == '__main__':
    list_recent_emails()