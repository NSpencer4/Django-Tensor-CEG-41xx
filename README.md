# Group-4110 SeeFood Project

**Team Members:**
Chase Spencer, Alyssa Carpenter, Sam Stevens, Joe Dobrovolc

**File Navigation For The Grader:**
This is a Django project (https://www.djangoproject.com/). We cannot split the code into a server and a client directory 
without MAJOR rework of how this platform works. Instead, I have identified the server side and client side below.

**Server-side**
1. seefood/Media/uploads: This is where we store images to be used with TensorFlow.
2. seefood/Media/migrations: This is where our database migrations live.
3. seefood/Media/saved_model: This is where we store the TensorFlow models.
4. seefood/Media/views.py: This is where we make handle data, interact with the database, and call the findfood API.
5. seefood/Media/find_food.py: This is where the findfood API is located.
6. seefood/Media/urls.py: This is where we define our routes for our API.
7. seefood/Media/models.py: This is where we define what needs stored in the database.
8. seefood/manage.py: This is used for running the server, performing migrations and much more.


**Client-side**
1. seefood/Media/static: This is where our css and our npm installed external libraries live.
2. seefood/seefood/templates: This is where you will find out base templates as well as our navigation as well as 
registration templates.
3. seefood/Media/templates: This is where you will find all of the templates used for the body of our views.

**Environment Setup Guide:**

**Linux Environment:**
1. Install Python 3.5.2
  1. sudo apt-get -y update
  2. sudo apt-get install build-essential checkinstall
  3. sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
  4. cd ~/Downloads/
  5. wget [https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz](https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz)
  6. tar -xvf Python-3.5.2.tgz
  7. cd Python-3.5.2
  8. ./configure
  9. make
  10. sudo checkinstall
    1. For the prompts, y, n, y, n, y
2. Install Pip
  1. sudo apt-get -y upgrade
  2. sudo apt-get install python-pip
3. Install Django with Pip
  1. pip install Django
4. Install NodeJS
  1. sudo apt-get -y upgrade
  2. sudo apt-get install nodejs
5. Install NPM
  1. sudo apt-get -y upgrade
  2. sudo apt-get install npm
6. Clone the GitHub Repository
  1. Cd into a project directory example: cd ~/Documents
  2. Git clone [git@github.com](mailto:git@github.com):NSpencer4/group-4110.git
  3. Cd into the project
  4. Pip install -r requirements.txt
  5. Cd into /seefood/Media/static
  6. npm install
7. Setup the DB
  1. Cd into seefood (this directory has the Media directory)
  2. Python manage.py makemigrations
  3. Python manage.py migrate

**Windows Environment:**

1. Install Python 3.5.2
  1. Download: [https://www.python.org/ftp/python/3.5.2/python-3.5.2.amd64.msi](https://www.python.org/ftp/python/3.5.2/python-3.5.2.amd64.msi)
  2. Run the installer
2. Install Pip
  1. python get-pip.py
3. Install Django with Pip
  1. pip install Django
4. Install NodeJS
  1. Download: https://nodejs.org/dist/v9.0.0/node-v9.0.0-x64.msi
  2. Run the installation
5. Install the latest NPM
  1. Make sure you open your command prompt/bash as &quot;run as administrator&quot;
  2. npm install npm -g
6. Clone the GitHub Repository
  1. Cd into a project directory example: cd ~/Documents
  2. Git clone [git@github.com](mailto:git@github.com):NSpencer4/group-4110.git
  3. Cd into the project
  4. Pip install -r requirements.txt
  5. Cd into /seefood/Media/static
  6. npm install
7. Setup the DB
  1. Cd into seefood (this directory has the Media directory)
  2. Python manage.py makemigrations
  3. Python manage.py migrate

**Mac Environment:**

1. Install Python 3.5.2
  1. Download: [https://www.python.org/ftp/python/3.5.2/python-3.5.2-macosx10.6.pkg](https://www.python.org/ftp/python/3.5.2/python-3.5.2-macosx10.6.pkg)
  2. Run the installer
2. Install Pip
  1. python get-pip.py
3. Install Django with Pip
  1. pip install Django
4. Install NodeJS
  1. Download: https://nodejs.org/dist/v9.0.0/node-v9.0.0.pkg
  2. Run the installation
5. Install the latest NPM
  1. sudo npm install npm -g
6. Clone the GitHub Repository
  1. Cd into a project directory example: cd ~/Documents
  2. Git clone [git@github.com](mailto:git@github.com):NSpencer4/group-4110.git
  3. Cd into the project
  4. Pip install -r requirements.txt
  5. Cd into /seefood/Media/static
  6. npm install
7. Setup the DB
  1. Cd into seefood (this directory has the Media directory)
  2. Python manage.py makemigrations
  3. Python manage.py migrate

After Environment Setup:

To run the app locally:

1. Cd into seefood (this directory has the Media directory)
2. Python manage.py runserver

To access the app in a browser:

1. Go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
