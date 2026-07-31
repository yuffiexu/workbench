# -*- coding: utf-8 -*-
import http.server
import socketserver
import socket
import os
import sys

# Force UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

PORT = 8080

# ── Get all LAN IPs ──
def get_ips():
    ips = []
    try:
        hostname = socket.gethostname()
        all_ips = socket.gethostbyname_ex(hostname)[2]
        for ip in all_ips:
            if ip.startswith('192.168.') or ip.startswith('10.') or ip.startswith('172.'):
                ips.append(ip)
    except:
        pass
    if not ips:
        ips.append('127.0.0.1')
    return ips

# ── Go to workbench folder ──
os.chdir(os.path.dirname(os.path.abspath(__file__)))

ips = get_ips()

print()
print("=" * 50)
print("  My Workbench - Local Server")
print("=" * 50)
print()
print("  Open this address on your phone:")
print("  " + "-" * 40)
print()
for ip in ips:
    print(f"  >>  http://{ip}:{PORT}")
print()
print("  " + "-" * 40)
print()
print("  Tips:")
print("    - Try each address if one doesn't work")
print("    - Phone and PC must be on same WiFi")
print("    - If all fail, turn off Windows Firewall temporarily")
print("    - Press Ctrl+C to stop the server")
print()
print("  Add to Home Screen:")
print("    Chrome -> ... -> Add to Home Screen")
print("    Safari -> Share -> Add to Home Screen")
print()
print("=" * 50)
print("  Server running, waiting for connection...")
print()

# ── Start server ──
Handler = http.server.SimpleHTTPRequestHandler
Handler.extensions_map.update({
    '.json': 'application/json',
    '.js': 'application/javascript',
    '.webmanifest': 'application/json',
})

try:
    with socketserver.TCPServer(("0.0.0.0", PORT), Handler) as httpd:
        httpd.serve_forever()
except KeyboardInterrupt:
    print()
    print("Server stopped.")
