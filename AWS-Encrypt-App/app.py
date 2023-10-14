from flask import Flask, render_template, request
import subprocess  # Import subprocess module for executing commands

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_key', methods=['GET', 'POST'])
def generate_key():
    # Handle RSA key generation logic here
    return render_template('generate_key.html')

@app.route('/encrypt_file', methods=['GET', 'POST'])
def encrypt_file():
    # Handle file encryption logic here
    return render_template('encrypt_file.html')

@app.route('/decrypt_file', methods=['GET', 'POST'])
def decrypt_file():
    # Handle file decryption logic here
    return render_template('decrypt_file.html')

@app.route('/process', methods=['POST'])
def process():
    selected_action = request.form.get('action')

    # Define the Linux command based on the selected action
    if selected_action == 'action1':
        command = 'openssl aes-256-cbc -e -in file1.txt -out encrypted_file1.txt'
    elif selected_action == 'action2':
        command = 'openssl aes-256-cbc -e -in file2.txt -out encrypted_file2.txt'
    elif selected_action == 'action3':
        command = 'openssl aes-256-cbc -e -in file3.txt -out encrypted_file3.txt'
    else:
        return "Invalid action selected"

    # Execute the Linux command
    try:
        subprocess.run(command, shell=True, check=True)
        return f"Command executed for action: {selected_action}"
    except subprocess.CalledProcessError as e:
        return f"Command execution failed for action: {selected_action}, Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
