## Discord IP Logger

Its an Advanced Tool to Trick users and get their IP.<br>
Its very easy to Setup.<br>
<br>
**The log includes:**
- [x] IP
- [x] Geolocation
- [x] User-Agent

### Requirements

- VPS/KVM
- Discord Webhook

### Setup

First install Python on your VPS.<br>
Go into the `main.py` file.<br>
Paste your Webhook URL into the Variable `webhookURL`<br>
Then open the CMD and enter the following command: `pip install flask`<br>
Then after it run the file on your VPS.<br>
<br>
**Windows**<br>
`py main.py`<br>
<br>
**Linux**<br>
`python3 main.oy`<br>

### Usage

Send in any chat your VPS IP with the Port `6969` and add `uploads/latest.gif` to the url.<br>
**Example:** https://192.0.0.1:6969/uploads/latest.gif<br>
And now everyone see's in discord the discord loading gif, like if the image isnt loading.
Then they will click on the image and click on `Show Original`.
And then his IP and his location get logged and send it to the Webhook.

### Information

If you found a bug or you have a Suggestion, open a pull request.

**ToDo's**
- [x] VPN/Proxy Checker
- [ ] Self Hosting
