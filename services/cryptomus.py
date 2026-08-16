import requests

CRYPTOMUS_API_KEY = "حط_المفتاح_تاعك_هنا"
CRYPTOMUS_MERCHANT_ID = "حط_id_تاعك_هنا"

def create_payment(amount, plan):
    url = "https://api.cryptomus.com/v1/payment"
    headers = {"merchant": CRYPTOMUS_MERCHANT_ID, "sign": CRYPTOMUS_API_KEY}
    data = {
        "amount": str(amount),
        "currency": "USD",
        "order_id": plan,
        "url_return": "http://localhost:5000/success",
        "url_callback": "http://localhost:5000/webhook"
    }
    response = requests.post(url, json=data, headers=headers)
    return response.json().get("result", {}).get("url")