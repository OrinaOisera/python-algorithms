from wsgiref.simple_server import make_server

def web_app(environment, response):
    status = '200 OK'
    headers = [('Content-type' , 'text/html;charset=utf-8')]
    response(status, headers)
    str = "New stroty alert"

    return [str]

with make_server('' ,8000, web_app) as server:
    print("servering on port 800....\n Visitng http://127.0.0.1:800\n To kill server enter ctrl + c")

    server.serve_forever()