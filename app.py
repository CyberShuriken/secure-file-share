from flask import Flask, render_template, request, jsonify, send_file
import os
import uuid
import json

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
METADATA_FILE = 'metadata.json'

# Ensure upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Simple metadata storage (In production, use a DB)
def load_metadata():
    if os.path.exists(METADATA_FILE):
        with open(METADATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_metadata(data):
    with open(METADATA_FILE, 'w') as f:
        json.dump(data, f)

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    iv = request.form.get('iv') # Initialization Vector
    original_name = request.form.get('filename')
    
    if file:
        file_id = str(uuid.uuid4())
        # Save the encrypted blob
        file.save(os.path.join(UPLOAD_FOLDER, file_id))
        
        # Save metadata
        metadata = load_metadata()
        metadata[file_id] = {
            'original_name': original_name,
            'iv': iv
        }
        save_metadata(metadata)
        
        return jsonify({'file_id': file_id})
    
    return jsonify({'error': 'Upload failed'}), 500

@app.route('/file/<file_id>')
def download_page(file_id):
    metadata = load_metadata()
    if file_id not in metadata:
        return "File not found", 404
    return render_template('download.html', file_id=file_id, filename=metadata[file_id]['original_name'])

@app.route('/api/file/<file_id>')
def get_file(file_id):
    metadata = load_metadata()
    if file_id not in metadata:
        return jsonify({'error': 'Not found'}), 404
        
    return jsonify({
        'iv': metadata[file_id]['iv'],
        'filename': metadata[file_id]['original_name'],
        'download_url': f'/api/blob/{file_id}'
    })

@app.route('/api/blob/<file_id>')
def get_blob(file_id):
    return send_file(os.path.join(UPLOAD_FOLDER, file_id))

if __name__ == '__main__':
    print("Starting Secure File Share...")
    app.run(debug=True, port=5000)
