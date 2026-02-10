#!/usr/bin/env python3
"""
Simple HTTP server for testing the portfolio locally
Run: python serve.py
Then visit: http://localhost:8000
"""

import http.server
import socketserver
import os

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"🚀 Server running at http://localhost:{PORT}")
    print(f"📂 Serving from: {os.getcwd()}")
    print("Press Ctrl+C to stop the server")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n✓ Server stopped")
