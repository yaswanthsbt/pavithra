import smtplib
from email.mime.text import MIMEText

def send_emergency_message(location, language, contact_email):
    try:
        subject = "Emergency Assistance Needed"
        body = f"An emergency message has been triggered from {location}. The user is using {language} language. Please provide immediate assistance."
        
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = 'your-email@example.com'
        msg['To'] = contact_email

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login('your-email@example.com', 'your-password')
            server.sendmail('your-email@example.com', contact_email, msg.as_string())
            print("Emergency message sent successfully.")
    except Exception as e:
        print(f"Error sending emergency message: {e}")

if __name__ == "__main__":
    location = input("Enter your location: ")
    language = input("Enter your preferred language: ")
    contact_email = input("Enter emergency contact email: ")
    send_emergency_message(location, language, contact_email)
