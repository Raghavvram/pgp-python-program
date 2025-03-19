
    encrypted_data = gpg.encrypt(
        message,
        recipients=fingerprint,
        always_trust=True
    )
    return str(encrypted_data)

def send_email(sender_email, sender_password, recipient_email, subject, body):
    # Create the email content
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    
    # Connect to the SMTP server and send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, sender_password)  # Login
            server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    # Key creation
    email = input("Enter your email address for the key pair: ")
    fingerprint = create_keys(email)
    print(f"Key pair generated. Key fingerprint: {fingerprint}")
    
    # Encrypt the message
    user_input = input("Enter the message to encrypt: ")
    encrypted_message = encrypt_message(fingerprint, user_input)
    print(f"Encrypted message:\n{encrypted_message}")
    
    # Sending the email
    sender_email = input("Enter your email address (sender): ")
    sender_password = input("Enter your email password (or app password): ")
    recipient_email = input("Enter the recipient's email address: ")
    subject = "Encrypted Message"
    
    # Send the email with the encrypted message
    send_email(sender_email, sender_password, recipient_email, subject, encrypted_message)
```

### Pre-requisites:
1. Enable **"Allow less secure apps"** or generate an **App Password** in your Gmail account for authentication.
2. Install the necessary library using: `pip install python-gnupg`.

This program now seamlessly encrypts a message and sends it via email. Let me know if you'd like further refinements! 🚀
