Here's a Python program that uses the `gnupg` library to generate PGP keys, encrypt user input, and return the encrypted output. The `python-gnupg` library is a wrapper around GPG and allows you to manage keys and encryption programmatically. Make sure you have GPG installed on your system and the `python-gnupg` library (`pip install python-gnupg`) before running this code:

```python
import gnupg

def create_keys(email):
    # Initialize GPG instance
    gpg = gnupg.GPG()

    # Generate key pair
    input_data = gpg.gen_key_input(
        name_email=email,
        key_type="RSA",
        key_length=2048
    )
    key = gpg.gen_key(input_data)
    return key.fingerprint

def encrypt_message(fingerprint, message):
    gpg = gnupg.GPG()
    
    # Encrypt the message for the key owner
    public_keys = gpg.list_keys()
    encrypted_data = gpg.encrypt(
        message,
        recipients=fingerprint,
        always_trust=True
    )
    return str(encrypted_data)

if __name__ == "__main__":
    # Create PGP keys
    email = input("Enter your email address for the key pair: ")
    fingerprint = create_keys(email)
    print(f"Key pair generated. Key fingerprint: {fingerprint}")

    # Get user input and encrypt it
    user_input = input("Enter the message to encrypt: ")
    encrypted_output = encrypt_message(fingerprint, user_input)
    print(f"Encrypted output:\n{encrypted_output}")
```

### Key Points:
1. **Key Generation**: A pair of PGP keys is created using the email address provided by the user.
2. **Encryption**: The user enters a message that gets encrypted using the public key.
3. **Requirements**: You must have GPG installed on your system. Use `gpg --version` to check if it’s installed. Install `python-gnupg` via `pip`.

Let me know if you'd like me to explain any part of the code or assist with setting up GPG on your system! 🚀
