import requests
import json

url = "https://api.discord.gx.games/v1/direct-fulfillment"
payload = {
    "partnerUserId": "e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855"
}
headers = {
    'accept': "*/*",
    'accept-language': "en-US,en;q=0.9",
    'content-type': "application/json",
    'origin': "https://www.opera.com",
    'referer': "https://www.opera.com/",
    'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': "?0",
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': "empty",
    'sec-fetch-mode': "cors",
    'sec-fetch-site': "cross-site",
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0"
}

response = requests.request("POST", url, headers=headers, data=json.dumps(payload))

print(response.text)