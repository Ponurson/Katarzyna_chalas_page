#!/usr/bin/env python3
"""Local static preview. Serves only the website; private inputs stay inaccessible."""
import argparse
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent.parent
PAGES = {'index.html', 'moja-droga.html', 'twoja-droga.html', 'coaching.html', 'interwencja-kryzysowa.html', 'prism-brain-mapping.html', 'mtq-plus.html', 'terapia-dzwiekiem.html', 'warsztaty-i-szkolenia.html', 'styles.css', 'script.js'}


class Preview(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT), **kwargs)

    def send_error(self, code, message=None, explain=None):
        if code == 404 and (ROOT / '404.html').is_file():
            content = (ROOT / '404.html').read_bytes()
            self.send_response(404)
            self.send_header('Content-Type', 'text/html; charset=utf-8')
            self.send_header('Content-Length', str(len(content)))
            self.end_headers()
            if self.command != 'HEAD':
                self.wfile.write(content)
            return
        super().send_error(code, message, explain)

    def send_head(self):
        path = unquote(urlsplit(self.path).path).lstrip('/') or 'index.html'
        target = (ROOT / path).resolve()
        allowed_asset = target.is_relative_to(ROOT / 'assets') and target.is_file()
        if path not in PAGES and not allowed_asset:
            self.send_error(404)
            return None
        return super().send_head()

    def log_message(self, format, *args):
        pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8765)
    parser.add_argument('--site-dir', type=Path, default=ROOT,
                        help='Katalog witryny, np. dist po npm run build')
    args = parser.parse_args()
    ROOT = args.site_dir.resolve()
    server = ThreadingHTTPServer(('127.0.0.1', args.port), Preview)
    print(f'Demo: http://127.0.0.1:{server.server_port} (tylko lokalnie)', flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
