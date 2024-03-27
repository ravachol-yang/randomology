# Randomology
A telegram bot to generate random stuff, I built this to chat with my friend randomly.
Using [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI) for talking with telegram server.
The project structure is inspired by classic MVC web frameworks..

## Dependency
Install system dependencies: 
`ffmpeg` (for converting media), 
`nginx` (optional, for hosting static resources & proxy)
``` shell
# this is an example for debian-based distros
sudo apt-get install ffmpeg
# optional but highly recommanded
sudo apt-get install nginx
```
Use pip to install dependencies in `requirements.txt`
``` shell
python3 -m pip install -r requirements.txt
```

## Test && Deploy
The bot uses webhook in production environment, you will need a server reachable for telegram server and has `https` support (unless you want to use infinity polling...)
**Here we go !!!!**
### Configuration
This repo includes a config example `.env.toml`.
Copy the example config and change it to meet your own environment:
``` shell
# copy the config example, don't forget to change it
cp .env.toml env.toml
```
### Testing
run `pytest` && check if every test passes
``` shell
python3 -m pytest
```
### Hosting static resources
Static resources are hosted in `public/` and the bot-generated contents are under `storage/`, use `link_storage.sh` to create a symlic:
``` shell
./link_storage.sh
```
copy and change the config file to configure Nginx:
``` shell
cp nginx.conf /etc/nginx/sites-available/example.com
# don't forget to change it !!
ln /etc/nginx/sites-available/example.com /etc/nginx/sites-enabled
```
restart `nginx.service`
### Running
In the project directory, run `python3`
``` shell
python3 bot.py
```
> if you don't have https:
telegram only allow webhooks with https, but you can still use `polling`:
in `env.toml`,set `bot.environment` to `"dev"`:

``` toml
[bot]
environment = "dev"
```
now you can run it !

## LICENSE
random LICENSE &^$%^&*()_)(*&^*)
