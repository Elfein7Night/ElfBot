# ElfBot [![CodeFactor](https://www.codefactor.io/repository/github/elfein7night/elfbot/badge)](https://www.codefactor.io/repository/github/elfein7night/elfbot)
A Simple Discord Bot For Handling Music Bots' Spam

##### Usage:
  - Deploying Your Own Bot:
    - Self Hosted:
      - Add a ```token``` file to the project dir with your bot user token
      - Run ```elfbot.py```
      - Invite the bot to a server you manage
    - Heroku:
      - Fork this repo
      - Create a new ```heroku``` app, link it to your fork and enable automatic deploys
      - Under the apps's settings add a config var ```DISCORD_BOT_TOKEN``` and give it your bot user token as a value
      - Under the app's resources tab enable the worker
      - Invite the bot to a server you manage
  - Or Using My Deployed Bot:
    - https://bit.ly/31cs0qz
  - Go into the designated music spam text channel and enter the command ```?setmusic``` (```?``` - prefix)
  - Enjoy cleaner text channels without all the spam from music bots related messages
