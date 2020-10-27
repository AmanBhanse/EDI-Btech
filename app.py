######################### Flask Imports ###################################
from flask import Flask
from flask import request
###########################################################################

app = Flask(__name__)

menu = [
    ('Open door', 'Opening door'),
    ('Close door', 'Closing door')
]

@app.route('/', methods = [ 'GET', 'POST' ])
def index():
    if(request.method == 'GET'):
        return {
            'success': True,
            'data': [ option[0] for option in menu ]
        }
    elif(request.method == 'POST'):
        try:
            finger_count = int(request.args.get('fingers').strip())
            return {
                'success': True,
                'data': menu[finger_count - 1][1]
            }
        except Exception as e:
            return {
                'success': False,
                'data': 'Invalid option!'
            }
    else:
        return {
            'success': False,
            'data': 'Invalid request!'
        }

# app.run()
