import requests
url = "https://api.discord.gx.games/v1/direct-fulfillment"
headers = {
    "Content-Type": "application/json"
}
data = {
    "partnerUserId": "49d7cf18-ac48-4488-b971-b1e8346ae9b4"
}
response = requests.post(url, json=data, headers=headers)
if response.status_code == 200:
    result = response.json()
    print("https://discord.com/billing/partner-promotions/1180231712274387115/" + result['some_key'])
else:
    print("Error:", response.status_code)
