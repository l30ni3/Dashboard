GovData Dashboard
==============================

A small <a target="_blank" href="https://github.com/plotly/dasht">Dash</a> application, that provides a dashboard showing how many data sets each federal ministry has made available. This project uses the <a target="_blank" href="http://docs.ckan.org/en/2.9/api/">CKAN API</a> to retrieve data from  <a target="_blank" href="https://www.govdata.de/">GovData</a>.

Getting Started 
------------
Download the project files and navigate to the project. Make sure, you have Python 3 and pip installed. 

#### Install packages with pip
To install all dependencies create and activate a virtual environment first and run the following command to install from requirements.txt:

`pip install -r requirements.txt`

#### Install packages with pipenv
You can also install the packages with the package manager pipenv. Therefore install the package manager first by typing:

`pip install pipenv` 

Next, activate the pipenv shell, to create a virtual environment for this project. This will spawn a new shell subprocess and can be deactivated by using exit.

`pipenv shell`

You can now install all packages from Pipfile:

`pipenv install` 

Run the app from root directory. The Dash app is now running on https://127.0.0.1:8050/

`py app.py`

Project Organization
------------

    ├── test               <- Tests with test app and test data 
    │   ├── __init__.py    
    │   ├── app.py         
    │   └── departments.json
    │   └── test_app.py
    │
    ├── app.py             <- app code
    │
    ├── departments.json   <- data of ministries
    │
    ├── Pipfile            <- The requirements file to reproduce the app environment
    ├── Pipfile.lock       
    │
    └── README.md          <- The top-level README for developers using this project.
    

Testing
------------

<a target="_blank" href="https://dash.plotly.com/testing">dash.testing</a> is a <a target="_blank" href="https://github.com/pytest-dev/pytest">pytest</a> plugin for <a target="_blank" href="https://github.com/plotly/dash">Dash</a>. It uses the <a target="_blank" href="https://github.com/plotly/dasht">Selenium Driver</a> to do automated real user interactions with browesers. 

To install and initialize the WebDrive, please refer to these <a target="_blank" href="https://chromedriver.chromium.org/getting-started">instructions</a>. To help WebDriver find the downloaded ChromeDriver executable, it is best to include the ChromeDriver location in your PATH environment variable. To run the tests, make sure you’re in the root directory of the project and then type:

`pytest test/`

--------

<p><small>This project uses the <a target="_blank" href="http://docs.ckan.org/en/2.9/api/">CKAN API</a> to retrieve data from  <a target="_blank" href="https://www.govdata.de/">GovData</a>.</small></p>
