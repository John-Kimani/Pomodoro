# Pomodoro App
Blue Chip is a pitch web application.
A simple Pomodoro Timer app that works on a desktop & mobile browser
# App screenshot
![Pomodoro App]()
## Installation
Guide to install Horizon News application:
### Clone this repository
```bash
 git clone https://github.com/John-Kimani/Pomodoro.git
```
* Move into the cloned directory:
```bash
cd POMODORO_APP
```
* Create and activate your virtual environment:
```bash
mkvirtualenv virtual
```
* Install project dependancies within your active environment: (Read: requirements.txt and use command below)
```bash
(virtual)$ pip3 Install -r requirements.txt
```
* Environment variables:
    *  Create a file called ```.env``` in the root folder
    ```bash
    (virtual)$ touch .env
    ```
    * Add the following lines to the file as seen in ```.env-template```
    ```bash
    SECRET_KEY=
    DATABASE_URL=
    ```
* Start the flask server
```bash
(Virtual)$ flask run
```
* or
```bash
(Virtual)$ python3 bluechip.py
```
## Features and BDD
- Users are able to manage their time and let gives them focus on any tasks         
## Technology Used
**Framework:** Flask
**Language** Python
### Developed with
**Structure:** Bootstrap, HTML
**Styles:** CSS
## Authors
John Kimani
Imelda Wade
* *MIT [License](/LICENSE)*
* Copyright (c) 2022 ** Imelda Wade ** 