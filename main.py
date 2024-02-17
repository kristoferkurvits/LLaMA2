from flask import Flask, request, jsonify
from llama_cpp import Llama
import logging

# Create a Flask object
app = Flask("Llama server")
model = None

# Configure Flask logger
app.logger.setLevel(logging.DEBUG)  # Set the desired logging level

@app.route('/llama', methods=['POST'])
def generate_response():
    global model
    
    try:
        data = request.get_json()

        if 'system_message' in data and 'user_message' in data and 'max_tokens' in data:
            system_message = data['system_message']
            user_message = data['user_message']
            max_tokens = int(data['max_tokens'])

            prompt = f"""<s>[INST] <<SYS>>
            {system_message}
            <</SYS>>
            {user_message} [/INST]"""
            
            if model is None:
                model_path = "llama-2-7b-chat.Q2_K.gguf"
                model = Llama(model_path=model_path)
             
            output = model(prompt, max_tokens=max_tokens, echo=True)
            return jsonify(output)

        else:
            return jsonify({"error": "Missing required parameters"}), 400

    except Exception as e:
        app.logger.error(f"An error occurred: {str(e)}")  # Log the error
        return jsonify({"Error": str(e)}), 500


@app.errorhandler(415)
def handle_unsupported_media_type(error):
    return jsonify({"error": "Unsupported Media Type: Content-Type must be 'application/json'."}), 415



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
