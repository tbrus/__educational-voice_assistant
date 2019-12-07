# Voice Assistant


## About

App is simple voice assistant based od google tools.

Some commands are only available for linux - ubuntu users.

To make use of sending email one has to edit config.py.

Config.py consists of 3 variables: city (for weather), login and password to email.

There is possibility to change language. One has to do it in main_fucntions.py in speak and get_audio functions,
in simple functions change locale and change words or sentences in files.


## Technologies

Used gTTS and speech recognition from google.


## Features

User can:

* use simple commands for time, date, weather, etc.
* open apps like (only for linux - ubuntu users and distros which support opening files with name in terminal)
* open sites like google, facebook, gmail, youtube
* send mails via gmail
* play first youtube video or choose whichever during searching
