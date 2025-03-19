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
