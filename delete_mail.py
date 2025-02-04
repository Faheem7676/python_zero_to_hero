# import imaplib
# import email
# from email.header import decode_header

# # Email credentials
# EMAIL_USER = "farooqui.faheem033@gmail.com"
# EMAIL_PASS = "kbgx ovqe dbai vamd"
# IMAP_SERVER = "imap.gmail.com"  # Example: 'imap.gmail.com' for Gmail

# # Function to delete emails based on subject text
# def delete_emails(subject_to_delete):
#     try:
#         # Connect to IMAP server
#         mail = imaplib.IMAP4_SSL(IMAP_SERVER)
#         mail.login(EMAIL_USER, EMAIL_PASS)
        
#         # Select the inbox
#         mail.select("inbox")

#         # Search for emails with the specified subject
#         result, data = mail.search(None, 'ALL')

#         # Loop through email IDs
#         for num in data[0].split():
#             result, msg_data = mail.fetch(num, "(RFC822)")
#             for response_part in msg_data:
#                 if isinstance(response_part, tuple):
#                     msg = email.message_from_bytes(response_part[1])
                    
#                     # Decode the subject
#                     subject, encoding = decode_header(msg["Subject"])[0]
#                     if isinstance(subject, bytes):
#                         subject = subject.decode(encoding if encoding else "utf-8")

#                     # Check if subject matches the text we want to delete
#                     if subject_to_delete in subject:
#                         print(f"Deleting email: {subject}")
#                         mail.store(num, "+FLAGS", "\\Deleted")

#         # Permanently delete emails
#         mail.expunge()
#         mail.logout()
#         print("Emails deleted successfully.")

#     except Exception as e:
#         print(f"Error: {e}")

# # Delete emails with subject "LinkedIn Job Alerts"
# delete_emails("LinkedIn Job Alerts")

# # If you want to delete Facebook notifications, change the text below:
# # delete_emails("Facebook Notificatio)




import imaplib
import email
from email.header import decode_header

# Email credentials
EMAIL_USER = "farooqui.faheem033@gmail.com"
EMAIL_PASS = "kbgxovqedbaivamd"
IMAP_SERVER = "imap.gmail.com"

def decode_subject(raw_subject, encoding):
    """ Decodes email subjects and handles 'unknown-8bit' encoding more robustly """
    if raw_subject is None:
        return "(No Subject)"  # Handle missing subject gracefully

    if isinstance(raw_subject, bytes):
        try:
            if encoding is None or encoding.lower() == "unknown-8bit":
                return raw_subject.decode("utf-8", errors="replace")
            return raw_subject.decode(encoding, errors="replace")
        except (UnicodeDecodeError, LookupError):  # Catch any unknown encoding
            return raw_subject.decode("latin-1", errors="replace")  # Fallback
    return raw_subject  # Already a string

def delete_emails(subject_to_delete):
    try:
        # Connect to IMAP server
        mail = imaplib.IMAP4_SSL(IMAP_SERVER)
        mail.login(EMAIL_USER, EMAIL_PASS)
        
        # Select the inbox
        mail.select("inbox")

        # Search for all emails
        result, data = mail.search(None, 'ALL')

        for num in data[0].split():
            result, msg_data = mail.fetch(num, "(RFC822)")
            for response_part in msg_data:
                if isinstance(response_part, tuple):
                    msg = email.message_from_bytes(response_part[1])

                    # Decode the email subject
                    raw_subject, encoding = decode_header(msg["Subject"] or "")[0]  # Handle None
                    subject = decode_subject(raw_subject, encoding)

                    # Normalize subject to avoid hidden characters
                    subject = subject.replace("\xa0", " ").strip()

                    # Debug: Print the email subject safely
                    print(f"Email Subject: {repr(subject)}")  # Show raw format

                    # Convert both to lowercase to ensure case-insensitive match
                    if subject_to_delete.lower() in subject.lower():
                        print(f"Deleting email: {subject}")
                        mail.store(num, "+FLAGS", "\\Deleted")

        # Permanently delete emails
        mail.expunge()
        mail.logout()
        print("Emails deleted successfully.")

    except Exception as e:
        print(f"Error: {e}")

# Call function to delete emails with "orkut" in the subject
delete_emails("orkut")
