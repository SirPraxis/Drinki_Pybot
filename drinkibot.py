import requests
import json
from flask import Flask, request
app = Flask(__name__)

@app.route('/drinkibot', methods=['GET','POST'])
def valida_Ubicacion():
    user_id = json.loads(request.data)['originalRequest']['data']['sender']['id']
    fb_lat = json.loads(request.data)['originalRequest']['data']['postback']['data']['lat']
    fb_lon = json.loads(request.data)['originalRequest']['data']['postback']['data']['long']
    fb_deleg = requests.get('https://maps.googleapis.com/maps/api/geocode/json?latlng={},{}&key=AIzaSyBDc_xtcop2zh2Mw9_D6UnOgQguetTq3_s'.format(fb_lat, fb_lon)).json()['results'][0]['address_components'][4]['long_name']
    mensaje_SI = {
        "recipient": {
            "id": user_id
        },
        "message": {
            "text": "Vemos que estás en {}, dentro de nuestra área de cobertura :)".format(fb_deleg)
        }
    }
    mensaje_NO = {
        "recipient": {
            "id": user_id
        },
        "message": {
            "text": "Lo sentimos, por el momento no tenemos servicio en esa delegación :("
        }
    }
    pregunta_Promo = message= {
        "recipient": {
            "id": user_id
        },
        "message": {
            "quick_replies": [{
                "content_type": "text",
                "title": "Chela",
                "payload": "Chela"
            },
            {
                "content_type": "text",
                "title": "Ron",
                "payload": "Ron"
            }]
        }
    }
    headers={"Content-Type": "application/json"}
    if fb_deleg == "Benito Juarez":
        print (requests.post('https://graph.facebook.com/v2.6/me/messages?access_token=EAAVF0JSSBhkBAKbekZBSzt0WpCzhXHLzIgRN5NwjAKzlSwbZAZAoUUz2D1l8Co4xDAPoQrmAA1ZASrdAdvGIfds8GF4UnUbJZBz3Oj4ZCodYt071Q7aQZB8ZCwgy1qBuZAnbvf4cK5FtHd15DjTTtmp4JqL8oD4JxjMZCBTIz7W9dU7Xb6ro7AJtbx', data = json.dumps(mensaje_SI), headers=headers))
        print (requests.post('https://graph.facebook.com/v2.6/me/messages?access_token=EAAVF0JSSBhkBAKbekZBSzt0WpCzhXHLzIgRN5NwjAKzlSwbZAZAoUUz2D1l8Co4xDAPoQrmAA1ZASrdAdvGIfds8GF4UnUbJZBz3Oj4ZCodYt071Q7aQZB8ZCwgy1qBuZAnbvf4cK5FtHd15DjTTtmp4JqL8oD4JxjMZCBTIz7W9dU7Xb6ro7AJtbx', data = json.dumps(pregunta_Promo), headers=headers))
    else:
        print (requests.post('https://graph.facebook.com/v2.6/me/messages?access_token=EAAVF0JSSBhkBAKbekZBSzt0WpCzhXHLzIgRN5NwjAKzlSwbZAZAoUUz2D1l8Co4xDAPoQrmAA1ZASrdAdvGIfds8GF4UnUbJZBz3Oj4ZCodYt071Q7aQZB8ZCwgy1qBuZAnbvf4cK5FtHd15DjTTtmp4JqL8oD4JxjMZCBTIz7W9dU7Xb6ro7AJtbx', data = json.dumps(mensaje_NO), headers=headers))
    return 'PASS'
