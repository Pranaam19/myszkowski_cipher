#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify
from cipher import MyszkowskiCipher

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    data = request.get_json()
    key = data.get('key', '')
    text = data.get('text', '')
    mode = data.get('mode', 'encrypt')
    
    if not key or not text:
        return jsonify({'error': 'Key and text are required'}), 400
    
    cipher = MyszkowskiCipher(key)
    
    try:
        if mode == 'encrypt':
            result = cipher.encrypt(text)
        else:  # decrypt
            result = cipher.decrypt(text)
        
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5001)
