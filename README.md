# izieng
This repository contains the code for a Telegram bot that allows users to generate bills in the style of the popular website Izi. The bot can be easily integrated with Telegram and once set up, it allows users to generate bills by providing the necessary information through the Telegram chat interface.
In addition to the Telegram integration, this repository also includes a backend built using the Django web framework. The backend serves as the bridge between the Telegram bot and the Izi API, handling the communication and data processing necessary to generate bills.
# How to start
1. Clone the repository to your local machine using the command 'git clone https://github.com/andriiko489/izieng.git'
2. Open the file containing the Telegram token and, optionally, the secret and allowed host settings, and update the values to match your own.
3. Navigate to the izieng folder in your terminal and run the command python manage.py runserver to start the server.
4. Log in to the Django admin panel, navigate to the "Creators" section, and update the information as necessary to restrict access.
5. Send the command /newlink to the Telegram bot and follow the instructions provided by the bot.
