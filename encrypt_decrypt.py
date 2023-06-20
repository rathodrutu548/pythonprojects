from cryptography.fernet import Fernet
import getpass

def generate_key(password):
    # Generates a key from the provided password
    password_bytes = password.encode()
    key = Fernet.generate_key()
    cipher_suite = Fernet(key)
    encrypted_password = cipher_suite.encrypt(password_bytes)
    return encrypted_password, key

def encrypt_file(file_path, key):
    # Encrypts the file using the provided key
    with open(file_path, 'rb') as file:
        plaintext = file.read()
    
    cipher_suite = Fernet(key)
    encrypted_text = cipher_suite.encrypt(plaintext)
    
    encrypted_file_path = file_path + '.encrypted'
    with open(encrypted_file_path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted_text)
    
    print(f'File encrypted successfully. Encrypted file saved as {encrypted_file_path}.')

def decrypt_file(file_path, key):
    # Decrypts the file using the provided key
    with open(file_path, 'rb') as encrypted_file:
        encrypted_text = encrypted_file.read()
    
    cipher_suite = Fernet(key)
    decrypted_text = cipher_suite.decrypt(encrypted_text)
    
    decrypted_file_path = file_path[:-10]  # Remove '.encrypted' from the file name
    with open(decrypted_file_path, 'wb') as decrypted_file:
        decrypted_file.write(decrypted_text)
    
    print(f'File decrypted successfully. Decrypted file saved as {decrypted_file_path}.')

def main():
    file_path = input('Enter the path to the file: ')
    password = getpass.getpass('Enter the password: ')
    operation = input('Enter "encrypt" or "decrypt": ')
    
    encrypted_password, key = generate_key(password)
    
    if operation.lower() == 'encrypt':
        encrypt_file(file_path, key)
    elif operation.lower() == 'decrypt':
        decrypt_file(file_path, key)
    else:
        print('Invalid operation. Please choose "encrypt" or "decrypt".')

if __name__ == '__main__':
    main()
