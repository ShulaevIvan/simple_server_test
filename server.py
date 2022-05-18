from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO

APP_HOST = 'localhost'
APP_PORT = 8000


class CreateHandler(BaseHTTPRequestHandler):

    def _set_headers(self):

        self.send_response(200)
        self.send_header('Content-type', 'text/html; charset=utf-8')
        self.end_headers()


    def _html(self, text):

        content =  f"""
        <!DOCTYPE html>
        <html lang="en">
        <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        </head>
        <body>
        {text}
        </body>
        </html>
        """

        return content.encode('utf-8')

    
    def do_GET(self):

        self._set_headers()
        content = 'This is GET request TEST.'
        self.wfile.write(self._html(content))

    
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        body = self.rfile.read(content_length)
        self.send_response(201)
        self.end_headers()
        response = BytesIO()
        response.write(b'This is POST request TEST. ')
        response.write(b'Received: ')
        response.write(body)
        self.wfile.write(response.getvalue())


    def runserver(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):

        server_adress = (APP_HOST, APP_PORT)
        httpd = server_class(server_adress, handler_class)
        httpd.serve_forever()


if __name__ == '__main__':

    CreateHandler.runserver(handler_class=CreateHandler)

