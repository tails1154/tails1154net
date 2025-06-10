import http.server
import socketserver
import urllib.parse
import threading
from main import WebTVRequests
import main
import webtv_state


global wtv_host
global wtv_port

def setHostPort(host, port):
    wtv_host = host
    wtv_port = port


class WebTVProxyHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        # Parse URL and path
        url = self.path
        if url.startswith("http://") or url.startswith("https://"):
            # full URL, use as is
            target_url = url
        else:
            # relative path, construct a URL with the host header
            host = self.headers.get('Host')
            target_url = f"http://{host}{url}"

        print(f"[PROXY] Handling GET for {target_url}")

        ssid = webtv_state.getSsid()

        # You may want to initialize WebTVRequests here, or reuse an instance
        # For example, create once per connection or globally.
        # Here, we'll assume host and port are known ahead of time:
        # Change these to your WebTV server host and port:

        # Create a WebTVRequests instance

        wtv = WebTVRequests(webtv_state.getIp(), webtv_state.getPort())

        # Use your class to get the response bytes
        try:
            response_bytes = wtv.getResponse(target_url, f"wtv-client-serial-number: {ssid}\r\nwtv-encryption: false\r\nwtv-client-bootrom-version: 2046\r\nUser-Agent: Mozilla/4.0 WebTV/2.5.5 (compatible; MSIE 4.0)").decode('utf-8', errors='replace').encode('utf-8')
        except Exception as e:
            print(f"[PROXY ERROR] {e}")
            self.send_error(502, "Bad Gateway")
            return
        finally:
            wtv.disconnect()

        # Send response back to client (browser)
        self.send_response(200)
        self.send_header('Content-type', 'text/html')  # You can try to guess MIME type here
        self.send_header('Content-length', str(len(response_bytes)))
        self.end_headers()
        self.wfile.write(response_bytes)

def run_proxy(port=8080):
    with socketserver.ThreadingTCPServer(('', port), WebTVProxyHandler) as httpd:
        print(f"Starting proxy server on port {port}")
        httpd.serve_forever()

if __name__ == '__main__':
    print("run main.py")
