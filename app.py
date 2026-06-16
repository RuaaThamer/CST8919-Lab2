from flask import Flask, request, jsonify
import logging
import sys

app = Flask(__name__)

# Configure logging to output to standard out so Azure captures it
logging.basicConfig(stream=sys.stdout, level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@app.route('/')
def home():
    return "Demo Web App is running!"

@app.route('/login', methods=['POST'])
def login():
    # Expecting JSON payload: {"username": "...", "password": "..."}
    data = request.json or {}
    username = data.get('username', 'unknown_user')
    password = data.get('password', '')

    # Hardcoded credentials for demo purposes
    if username == 'admin' and password == 'securepassword':
        logger.info(f"Successful login attempt for user: {username}")
        return jsonify({"status": "success", "message": "Logged in!"}), 200
    else:
        logger.warning(f"Failed login attempt for user: {username}")
        return jsonify({"status": "error", "message": "Invalid credentials"}), 401

if __name__ == '__main__':
    # Azure App Service defaults to port 8000 for Python apps
    app.run(host='0.0.0.0', port=8000)
    