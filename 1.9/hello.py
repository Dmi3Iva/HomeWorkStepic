def wsgi_app(environ, start_responce){
    #/?a=1&a=2&b=3
    status = '200 OK'
    headers =  [
        ('Content-Type', ' text/plain')
    ]
    start_responce(status, headers)
    return ["\n".join(environ.get('QUERY_STRING').split("&"))]
}
