

if __name__ == "__main__":
    # Key creation
    email = input("Enter your email address for the key pair: ")
    fingerprint = create_keys(email)
    print(f"Key pair generated. Key fingerprint: {fingerprint}")
er_input)

```

### Pre-requisites:
1. Enable **"Allow less secure apps"** or generate an **App Password** in your Gmail account for authentication.
2. Install the necessary library using: `pip install python-gnupg`.

This program now seamlessly encrypts a message and sends it via email. Let me know if you'd like further refinements! 🚀
