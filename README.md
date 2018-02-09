# EIKONREST
===========

#### EIKON RESTful Wrapper (EIKONREST)

A Python RESTful wrapper for Thomson Reuters EIKON proxy. Unleash the EIKON proxy with RESTful API.

This project is not a direct API to access Thomson Reuters data. This is just a wrapper to enable you to access EIKON proxy and retrieve the data which is accessible by your Thomson Reuters account.

To start this wrapper, install Python 2.7 and pip. Add Python and pip to your PATH in environment variable.

##### Install Python Virtual Environment
Execute: `pip install virtualenv`


##### Install virtualenvwrapper-win
Execute: `pip install virtualenvwrapper-win`

##### Run Terminal as Administrator

##### Set policy for scripts
Execute: `Set-ExecutionPolicy AllSigned`. Enter `A` when it asks.

##### Create virtual env for this project
Execute `mkvirtualenv eikonrest`

_Copy the Python data source wrapper to the created virtual env directory_ e.g. C:\Users\[your_user]\Envs\eikonrest\dev\EIKONREST)

##### Go to the virtual environment directory

##### Dive into the virtual environment
Execute: `workon eikonrest`

##### Go to the dev directory which has this project source code

##### Set this project directory to this folder
Execute: `setproject dir .`

##### Install project dependencies for this virtual environment
Execute: `pip install -r requirements.txt`

##### Start the Python API server
1. Edit config.yml
2. Execute: `python server.py`


**Remember!** this project listens to port 1368. Configure your firewall to allow inbound traffic for that port.


### Usage
##### To make API call
Send HTTP request to `<your_server_url>:1368/query/<symbol1>,<symbol2>/<field1>,<field2>/<parameters>`

#### Example:
`<your_server_url>:1368/query/GOOG.O/TR.OPEN,TR.CLOSE`
`<your_server_url>:1368/query/0%23HSI*.HF/CALL_PUT,CF_ASK,CF_BID,CF_LAST`
