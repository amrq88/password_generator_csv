import secrets
import string

class PasswordGenerator:
    def generate_password(self, length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_symbols=True):
        
        # Define character sets
        lowercase_chars = string.ascii_lowercase
        uppercase_chars = string.ascii_uppercase
        digit_chars = string.digits
        symbol_chars = string.punctuation
        
        # Initialize character set for password generation
        chars = ''
        
        if use_lowercase:
            chars += lowercase_chars
        if use_uppercase:
            chars += uppercase_chars
        if use_digits:
            chars += digit_chars
        if use_symbols:
            chars += symbol_chars
        
        # Generate random password
        password = ''.join(secrets.choice(chars) for _ in range(length))
        return password