from bottle import run, route, template, view, static_file

# route for pages

@route('/')
@view('suprise')
def home():
    return {}


@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')

if __name__ == "__main__":
    run(host='localhost', port=8080, debug=True, reloader=True)