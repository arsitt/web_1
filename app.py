import os
from bottle import route, run, TEMPLATE_PATH, jinja2_view, static_file

TEMPLATE_PATH.append(os.path.join(os.path.dirname(__file__), 'templates'))

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='./static')


@route('/')
@jinja2_view('home.html')
def home():
    return {}

@route('/datos')
@jinja2_view('datos.html')
def hola():
    return {'datos':[
            ('Alejandro','28/09/2022','contento'),
            ('Alejandro','29/09/2022','Sussy')
    ]}

@route('/info')
@jinja2_view('info.html')
def hola():
    return {}

run(host='localhost', port=8080, debug=True)


