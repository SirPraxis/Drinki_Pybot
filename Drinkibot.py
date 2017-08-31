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

    def send_message(recipient_id, message_text):
        params = { "access_token": "EAAVF0JSSBhkBAKbekZBSzt0WpCzhXHLzIgRN5NwjAKzlSwbZAZAoUUz2D1l8Co4xDAPoQrmAA1ZASrdAdvGIfds8GF4UnUbJZBz3Oj4ZCodYt071Q7aQZB8ZCwgy1qBuZAnbvf4cK5FtHd15DjTTtmp4JqL8oD4JxjMZCBTIz7W9dU7Xb6ro7AJtbx" }
        headers = { "Content-Type": "application/json" }
        data = json.dumps({ "recipient": { "id": recipient_id },"message": { "text": message_text} })
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)

    def send_quick_reply(recipient_id, message_text, quick_reply_title, quick_reply_payload, quick_reply_title2, quick_reply_payload2):
        params = { "access_token": "EAAVF0JSSBhkBAKbekZBSzt0WpCzhXHLzIgRN5NwjAKzlSwbZAZAoUUz2D1l8Co4xDAPoQrmAA1ZASrdAdvGIfds8GF4UnUbJZBz3Oj4ZCodYt071Q7aQZB8ZCwgy1qBuZAnbvf4cK5FtHd15DjTTtmp4JqL8oD4JxjMZCBTIz7W9dU7Xb6ro7AJtbx" }
        headers = { "Content-Type": "application/json" }
        data = json.dumps({ "recipient": { "id": recipient_id },"message": { "text": message_text, "quick_replies": [{"content_type": "text", "title": quick_reply_title, "payload": quick_reply_payload}, {"content_type": "text", "title": quick_reply_title2, "payload": quick_reply_payload2}]} })
        r = requests.post("https://graph.facebook.com/v2.6/me/messages", params=params, headers=headers, data=data)

    if fb_deleg == "Benito Juarez":
        send_message(user_id, "Vemos que estás en {}, dentro de nuestra área de cobertura :)".format(fb_deleg))
        send_quick_reply(user_id, "Por el momento sólo tenemos dos bebidas, ¿cuál te gustaría?", "Chela", "Chela", "Ron", "Ron")
    else:
        send_message(user_id, "Lo sentimos, por el momento no tenemos servicio en esta parte de {} :(".format(fb_deleg))
        send_message(user_id, "¡Hasta luego!")
    return 'PASS'
