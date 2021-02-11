# Custom ping

Send a custom message to a discord server by accesing a url.

## Deploy custom server
If you want to deploy your own copy for personal use, just:
1) Fork the project (or copy/paste it, but forking is nicer and it will automatically comply with the license, otherwise you need to mention me).
1) Deploy your fork to Heroku or any other web service. The app is ready-to-deploy on Heroku, but it is just a Flask one-file app so other services should be fine.
1) Add an environment variable named 'URL' with the Discord webhook.

## Usage
Access the main page with a message after the '?' that will be sent to discord: Example `$curl https://<server>.heroku.app?Hello` will post a 'Hello' message to the discord channel of the webhook.

## Contributions
Although this project was made for personal use, if you want to send pull requests or make/suggest changes I'll be happy to discuss them. The conversion was manually made so it may not have all type of events into consideration.

## Disclaimer
This app is not affiliated with nor endorsed by [Heroku](https://www.heroku.com/home) nor [Discord](https://discordapp.com/). The names, logos and services belongs to their respective owners.
