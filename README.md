GovData Dashboard
==============================

A small <a target="_blank" href="https://github.com/plotly/dasht">Dash</a> application, that provides a dashboard showing how many data sets each federal ministry has made available. This project uses the <a target="_blank" href="http://docs.ckan.org/en/2.9/api/">CKAN API</a> to retrieve data from  <a target="_blank" href="https://www.govdata.de/">GovData</a>.

Getting Started
------------
Download the project files and navigate to the project.

`cd Dashboard`

Make sure, you have Python 3 and pip installed. To install all dependencies please install the package manager pipenv and install all packages from the Pipfile.

`pip install pipenv` 

`pipenv install` 

Next, activate the pipenv shell. This will spawn a new shell subprocess and can be deactivated by using exit.

`pipenv shell`

Run the app from root directory:

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

<a target="_blank" href="https://dash.plotly.com/testing">dash.testing</a> is a <a target="_blank" href="https://github.com/pytest-dev/pytest">pytest</a> plugin for <a target="_blank" href="https://github.com/plotly/dash">Dash</a>. It uses the <a target="_blank" href="https://github.com/plotly/dasht">Selenium Driver</a> to do automated real user interactions with browesers. It needs to be installed and initialized, please refer to these <a target="_blank" href="https://chromedriver.chromium.org/getting-started">instructions</a>. To help WebDriver find the downloaded ChromeDriver executable, it is best to include the ChromeDriver location in your PATH environment variable. To run the tests, make sure you’re in the root directory of the project and then type:

`pytest test/`

--------

<p><small>This project uses the <a target="_blank" href="http://docs.ckan.org/en/2.9/api/">CKAN API</a> to retrieve data from  <a target="_blank" href="https://www.govdata.de/">GovData</a>.</small></p>
