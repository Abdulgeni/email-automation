import base64
from email.mime.text import MIMEText
from email_bot import get_gmail_service, read_emails
from classifier import classify_email, generate_reply

def send_reply(service, email_data, reply_text):
    """Send reply to an email."""
    message = MIMEText(reply_text)
    message['to'] = email_data['sender']
    message['subject'] = f"Re: {email_data['subject']}"
    
    raw = base64.urlsafe_b64encode(message.as_bytes()).decode()
    
    service.users().messages().send(
        userId='me',
        body={'raw': raw, 'threadId': email_data['thread_id']}
    ).execute()
    
    print(f"✅ Reply sent to: {email_data['sender']}")

def mark_as_read(service, email_id):
    """Mark email as read."""
    service.users().messages().modify(
        userId='me',
        id=email_id,
        body={'removeLabelIds': ['UNREAD']}
    ).execute()

def process_emails():
    """Main function to process all unread emails."""
    print("📧 Connecting to Gmail...")
    service = get_gmail_service()
    
    print("📥 Reading unread emails...")
    emails = read_emails(service, max_results=5)
    
    if not emails:
        print("✅ No unread emails!")
        return
    
    for email in emails:
        print(f"\n{'='*50}")
        print(f"📧 From: {email['sender']}")
        print(f"📝 Subject: {email['subject']}")
        
        # Classify
        category = classify_email(email['subject'], email['body'])
        print(f"🏷️ Category: {category}")
        
        # Generate reply
        reply = generate_reply(email['subject'], email['body'], category)
        print(f"💬 Draft Reply: {reply[:150]}...")
        
        # Ask before sending
        print("\n📤 Options:")
        print("1. Send automatically")
        print("2. Skip this email")
        print("3. Exit")
        
        choice = input("Choose (1/2/3): ")
        
        if choice == '1':
            send_reply(service, email, reply)
            mark_as_read(service, email['id'])
        elif choice == '2':
            print("⏭️ Skipped")
        else:
            print("👋 Exiting")
            break

if __name__ == '__main__':
    process_emails()