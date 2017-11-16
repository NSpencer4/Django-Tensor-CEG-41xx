# Group-4110 SeeFood Project

**Linux Environment:**

1. Install Python 3.5.2
  1. sudo apt-get -y update
  2. sudo apt-get install build-essential checkinstall
  3. sudo apt-get install libreadline-gplv2-dev libncursesw5-dev libssl-dev libsqlite3-dev tk-dev libgdbm-dev libc6-dev libbz2-dev
  4. cd ~/Downloads/
  5. wget [https://www.python.org/ftp/python/3.5.2/Python-3.5.2.tgz](https://www.python.org/ftp/python/2.7.12/Python-2.7.12.tgz)
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
  1. Download: [https://www.python.org/ftp/python/3.5.2/python-3.5.2.amd64.msi](https://www.python.org/ftp/python/2.7.12/python-2.7.12.amd64.msi)
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
  1. Download: [https://www.python.org/ftp/python/3.5.2/python-3.5.2-macosx10.6.pkg](https://www.python.org/ftp/python/2.7.12/python-2.7.12-macosx10.6.pkg)
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
