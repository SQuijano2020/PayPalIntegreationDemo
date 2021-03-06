# 1. Import the PayPal SDK client that was created in `Set up Server-Side SDK`.
import json

from server.PayPal.PayPalClient import PayPalClient
from paypalcheckoutsdk.orders import OrdersCreateRequest

CLIENT_ID = "AYq4OhkTifONDo-ELsGRXMYpPDiurnSI2F3cdwSYZxHQr4014MRgOS2NBpYx88bBwO3OePRbZdGIhVIT"
CLIENT_SECRET = "EICyTyWGHZngsxaGBV7klCYslKwzDXh5ipWOoqHnQySEYwgo6yRM4HF79KYiq-Z16uuNu6MpaXnhuoBF"


class CreateOrder(PayPalClient):
    # 2. Set up your server to receive a call from the client
    """ This is the sample function to create an order. It uses the
    JSON body returned by buildRequestBody() to create an order."""

    def create_order(self, debug=False):
        request = OrdersCreateRequest()
        request.prefer('return=representation')

        # 3. Call PayPal to set up a transaction
        request.request_body(self.build_request_body_basic())
        response = self.client.execute(request)
        if debug:
            print('Status Code: ', response.status_code)
            print('Status: ', response.result.status)
            print('Order ID: ', response.result.id)
            print('Intent: ', response.result.intent)
            print('Links:')
            for link in response.result.links:
                print('\t{}: {}\tCall Type: {}'.format(link.rel, link.href, link.method))
            print('Total Amount: {} {}'.format(response.result.purchase_units[0].amount.currency_code,
                                               response.result.purchase_units[0].amount.value))
        return response

    """Setting up the JSON request body for creating the order. Set the intent in the
    request body to "CAPTURE" for capture intent flow."""

    @staticmethod
    def build_request_body_basic():
        """Method to create body with CAPTURE intent. For the full list of parameters and example responses,
        see https://developer.paypal.com/docs/api/orders/v2/#orders_create.
        """
        return \
            {
                "intent": "CAPTURE",
                "purchase_units": [
                    {
                        "amount": {
                            "currency_code": "MXN",
                            "value": "100.00"
                        }
                    }
                ]
            }

    @staticmethod
    def build_request_body():
        """Method to create body with CAPTURE intent. For the full list of parameters and example responses,
        see https://developer.paypal.com/docs/api/orders/v2/#orders_create.
        """

        return \
            {
                "intent": "CAPTURE",
                "application_context": {
                    "brand_name": "SQUIJANO INTERVIEW",
                    "landing_page": "BILLING",
                    "shipping_preference": "SET_PROVIDED_ADDRESS",
                    "user_action": "CONTINUE"
                },
                "purchase_units": [
                    {
                        "reference_id": "PUHF",
                        "description": "Sporting Goods",

                        "custom_id": "CUST-HighFashions",
                        "soft_descriptor": "HighFashions",
                        "amount": {
                            "currency_code": "USD",
                            "value": "230.00",
                            "breakdown": {
                                "item_total": {
                                    "currency_code": "USD",
                                    "value": "180.00"
                                },
                                "shipping": {
                                    "currency_code": "USD",
                                    "value": "30.00"
                                },
                                "handling": {
                                    "currency_code": "USD",
                                    "value": "10.00"
                                },
                                "tax_total": {
                                    "currency_code": "USD",
                                    "value": "20.00"
                                },
                                "shipping_discount": {
                                    "currency_code": "USD",
                                    "value": "10"
                                }
                            }
                        },
                        "items": [
                            {
                                "name": "T-Shirt",
                                "description": "Green XL",
                                "sku": "sku01",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "90.00"
                                },
                                "tax": {
                                    "currency_code": "USD",
                                    "value": "10.00"
                                },
                                "quantity": "1",
                                "category": "PHYSICAL_GOODS"
                            },
                            {
                                "name": "Shoes",
                                "description": "Running, Size 10.5",
                                "sku": "sku02",
                                "unit_amount": {
                                    "currency_code": "USD",
                                    "value": "45.00"
                                },
                                "tax": {
                                    "currency_code": "USD",
                                    "value": "5.00"
                                },
                                "quantity": "2",
                                "category": "PHYSICAL_GOODS"
                            }
                        ],
                        "shipping": {
                            "method": "United States Postal Service",
                            "address": {
                                "name": {
                                    "full_name": "John",
                                    "surname": "Doe"
                                },
                                "address_line_1": "123 Townsend St",
                                "address_line_2": "Floor 6",
                                "admin_area_2": "San Francisco",
                                "admin_area_1": "CA",
                                "postal_code": "94107",
                                "country_code": "US"
                            }
                        }
                    }
                ]
            }


"""This is the driver function that invokes the createOrder function to create
   a sample order."""
if __name__ == "__main__":

    CreateOrder(CLIENT_ID, CLIENT_SECRET, True).create_order(debug=True)
