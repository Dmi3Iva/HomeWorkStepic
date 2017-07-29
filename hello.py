def simple_app(environ, start_response):
    """Simplest possible application object"""
    response_headers = [('Content-type', 'text/plain')]
    start_response('200 OK', response_headers)
    return ["\n".join(environ.get('QUERY_STRING').split("&"))]
