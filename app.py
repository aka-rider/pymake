from http.server import HTTPServer, BaseHTTPRequestHandler
from io import BytesIO
import requests


def random_cat_gif():
    url = 'https://api.giphy.com/v1/gifs/random?api_key=dc6zaTOxFJmzC&tag=cat'
    return requests.get(url)


class Handler(BaseHTTPRequestHandler):
    template = '''
<!DOCTYPE HTML>
<html>
<head>
  <meta charset="UTF-8">
  <title>Cats gifs</title>
</head>
<body>
    {body}
</body>
</html>'''

    def do_GET(self):
        r = random_cat_gif()
        self.send_response(r.status_code)
        self.end_headers()
        if r.status_code == 200:
            data = r.json()
            body = '<img src="{imgurl}"/>'.format(imgurl=data['data']['image_url'])
            content = Handler.template.format(body=body)
        else:
            body = '<h1>HTTP - {code}</h1>'.format(code=r.status_code)
            content = Handler.template.format(body=body)

        self.wfile.write(content.encode('utf-8'))



httpd = HTTPServer(('localhost', 8000), Handler)
httpd.serve_forever()

