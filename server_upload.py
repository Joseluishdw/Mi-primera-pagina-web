#!/usr/bin/env python3
"""
Servidor simple que sirve archivos estáticos y acepta POST en /upload
Guarda los archivos subidos en la carpeta 'uploads' dentro de la misma carpeta.
Uso: python server_upload.py
"""
import http.server
import socketserver
import os
import cgi
import urllib.parse
import json
from datetime import datetime

PORT = 8000
UPLOAD_DIR = 'uploads'

class UploadHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Endpoint para listar archivos subidos
        if self.path == '/list-uploads':
            os.makedirs(UPLOAD_DIR, exist_ok=True)
            try:
                files = sorted(os.listdir(UPLOAD_DIR), reverse=True)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = json.dumps({'files': files}).encode('utf-8')
                self.wfile.write(response)
                return
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                response = json.dumps({'error': str(e)}).encode('utf-8')
                self.wfile.write(response)
                return
        # Servir archivos estáticos normalmente
        super().do_GET()

    def do_POST(self):
        if self.path != '/upload':
            self.send_error(404, "File not found")
            return
        # Ensure upload dir exists
        os.makedirs(UPLOAD_DIR, exist_ok=True)
        ctype, pdict = cgi.parse_header(self.headers.get('Content-Type'))
        if ctype != 'multipart/form-data':
            self.send_error(400, 'Bad request: expected multipart/form-data')
            return
        pdict['boundary'] = bytes(pdict['boundary'], 'utf-8')
        pdict['CONTENT-LENGTH'] = int(self.headers.get('Content-Length'))
        try:
            fs = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD':'POST'}, keep_blank_values=True)
        except Exception as e:
            self.send_error(400, 'Failed to parse form data')
            return
        if 'file' not in fs:
            self.send_error(400, 'No file field')
            return
        fileitem = fs['file']
        if not fileitem.filename:
            self.send_error(400, 'No filename')
            return
        # Sanitize filename
        filename = os.path.basename(fileitem.filename)
        # Append timestamp to avoid overwrite
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        save_name = f"{timestamp}_{filename}"
        save_path = os.path.join(UPLOAD_DIR, save_name)
        try:
            with open(save_path, 'wb') as out:
                data = fileitem.file.read()
                out.write(data)
        except Exception as e:
            self.send_error(500, 'Failed to save file')
            return
        # Return JSON response instead of redirect (para AJAX)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        response = json.dumps({'success': True, 'filename': save_name}).encode('utf-8')
        self.wfile.write(response)


if __name__ == '__main__':
    os.makedirs(UPLOAD_DIR, exist_ok=True)
    handler = UploadHTTPRequestHandler
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at port {PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print('\nShutting down server')
            httpd.server_close()
