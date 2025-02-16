from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
import subprocess
import os

app = Flask(__name__)
CORS(app)  # Aktifkan CORS

@app.route('/compile', methods=['POST'])
def compile_code():
    data = request.json
    code = data.get('code', '')
    
    # Simpan kode ke file sementara
    with open('temp.cpp', 'w') as f:
        f.write(code)
    
    # Compile kode
    compile_process = subprocess.run(['g++', 'temp.cpp', '-o', 'temp'], capture_output=True, text=True)
    if compile_process.returncode != 0:
        return jsonify({'error': compile_process.stderr}), 400
    
    # Jalankan program
    run_process = subprocess.run(['./temp'], capture_output=True, text=True)
    return jsonify({'output': run_process.stdout, 'error': run_process.stderr})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Gunakan port dari environment
    app.run(host="0.0.0.0", port=port)