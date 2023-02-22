import json
from http.server import HTTPServer, BaseHTTPRequestHandler

USERS_LIST = [
    {
        "id": 1,
        "username": "theUser",
        "firstName": "John",
        "lastName": "James",
        "email": "john@email.com",
        "password": "12345",
    }
]

usernames = []


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def _set_response(self, status_code=200, body=None):
        self.send_response(status_code)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(body if body else {}).encode('utf-8'))

    def _pars_body(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        return json.loads(self.rfile.read(content_length).decode('utf-8'))  # <--- Gets the data itself

    # def do_GET(self):
    #     self._set_response(418)

    def do_GET(self, arg=None):
        # self._set_response(415)
        if self.path == "/users":
            status = 200
            body = USERS_LIST
            self._set_response(status, body)
        elif self.path.startswith('/user/'):
            username = self.path.lstrip('/user/')
            for user in USERS_LIST:
                if user.get('username') == username:
                    find_user = user
                    self._set_response(status_code=200, body=find_user)
            else:
                status = 400
                body = {"error": "User not found"}
                self._set_response(status, body)

        elif self.path == 'reset/': pass

        else:
            self._set_response(418)

    def do_POST(self):
        body = self._pars_body()

        if self.path.endswith('createWithList'):
            error = 0
            for item in body:
                if item.get('id') in [user_id.get('id') for user_id in USERS_LIST] \
                        or len(item.values()) != 6:
                    self._set_response(400, {})
                    error += 1
                    break
            if not error:
                self._set_response(201, body)

        elif body.get('id') in [user_id.get('id') for user_id in USERS_LIST] \
                or len(body.values()) != 6:
            self._set_response(400, {})

        elif body:
            self._set_response(201, body)
            usernames.append(body.get('username'))



    def do_PUT(self):
        id_req = int(self.path.rsplit('/', 1)[-1])
        ids = [i.get('id') for i in USERS_LIST]

        if id_req in ids:
            body = self._pars_body()

            for item in USERS_LIST:

                if item.get('id') == id_req and len(body.values()) == 5:
                    item.update(body)
                    self._set_response(200, item)

                else:
                    self._set_response(400, {"error": "not valid request data"})
        else:
            self._set_response(404, {"error": "User not found"})

    def do_DELETE(self):
        id_req = int(self.path.rsplit('/', 1)[-1])
        ids = [i.get('id') for i in USERS_LIST]

        if id_req in ids:
            body = {}

            for item in USERS_LIST:

                if item.get('id') == id_req:
                    del item
                    self._set_response(200, body)

        else:
            self._set_response(404, {"error": "User not found"})


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, host='localhost', port=8000):
    server_address = (host, port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
