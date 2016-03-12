def wsgi_app (environ, start_response):
    lines = []
    for key, value in environ.items():
        lines.append("%s=%r" % (key, value))
    start_response("200 OK", [("Content-Type", "text/plain")])
    return ["\n".join(lines)]
