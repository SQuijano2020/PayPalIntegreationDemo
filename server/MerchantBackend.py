import paypalhttp
from flask import Flask, jsonify
from server.PayPal.CreateOrder import CreateOrder
from server.PayPal.CaptureOrder import CaptureOrder

CLIENT_ID = "AYq4OhkTifONDo-ELsGRXMYpPDiurnSI2F3cdwSYZxHQr4014MRgOS2NBpYx88bBwO3OePRbZdGIhVIT"
CLIENT_SECRET = "EICyTyWGHZngsxaGBV7klCYslKwzDXh5ipWOoqHnQySEYwgo6yRM4HF79KYiq-Z16uuNu6MpaXnhuoBF"

api = Flask(__name__)
api.response_class(paypalhttp.http_response.HttpResponse)

# Handle create order request and other merchant backend functions (db queries, client loyalty programs, etc.)
@api.route('/demo/checkout/api/paypal/order/create/', methods=['POST'])
def create_order():
    print('Execute needed functions previous to create the order with PayPal API...\n\n')

    response = CreateOrder(CLIENT_ID, CLIENT_SECRET, True).create_order(debug=True)

    print('Execute needed functions after order is created with PayPal API...\n')
    order_id = response.result.id

    print('Sending back order data with id {} to client...\n\n'.format(order_id))

    #return jsonify(response.result)
    return response


# Handle capture order request and other merchant backend functions (db queries, client loyalty programs, etc.)
@api.route('/demo/checkout/api/paypal/order/<string:order_id>/capture/', methods=['POST'])
def capture_order(order_id):
    print('Execute needed functions previous to create the order with PayPal API...\n\n')

    response = CaptureOrder(CLIENT_ID, CLIENT_SECRET, True).capture_order(order_id, debug=True)

    print('Execute needed functions after order is captured with PayPal API...\n')
    order_id = response.result.id

    print('Sending back order data with id {} to client...\n\n', order_id)

    return response


if __name__ == '__main__':
    api.run()
