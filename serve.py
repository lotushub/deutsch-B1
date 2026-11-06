"""Serve this offline course locally. Requires Python 3; no dependencies."""
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

if __name__ == '__main__':
    root = Path(__file__).resolve().parent
    handler = partial(SimpleHTTPRequestHandler, directory=str(root))
    try:
        with ThreadingHTTPServer(('127.0.0.1', 8000), handler) as server:
            print('Klar Deutsch: http://127.0.0.1:8000 — Ctrl+C to stop', flush=True)
            server.serve_forever()
    except KeyboardInterrupt:
        print('\nStopped.')
    except OSError as error:
        raise SystemExit(f'Could not start local server: {error}. Close any other server using port 8000 and retry.')
