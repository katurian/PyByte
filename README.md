# PyByte

PyByte is a Python wrapper for [Byte's](https://byte.co/) private API. It's only dependencies are [Python 3.7](https://www.python.org/downloads/release/python-370/), [Node](https://nodejs.org/en/) and the HTTP [Requests](https://requests.readthedocs.io/en/master/) library.


## Usage
Before you use any of the API calls in this repository, you need an authentication token from Byte. To acquire one, open a terminal and run the following: 

```
git clone https://github.com/69/byte-auth.git
npm install
node auth.js
```
Another cmd.exe window will pop up, with directions to go to this oauth login page:

![oauth](https://github.com/katurian/PyByte/blob/master/oauth.PNG =250x300)

Sign in through Google and follow the rest of the directions. Your Authentication Token will print to the cmd.exe window.

Now go to ``functions.py`` 

```python

import requests 

authtoken = 'XXXXXXEXNFWBXXXXXXYCZRXXXX'
```
Replace ``'XXXXXXEXNFWBXXXXXXYCZRXXXX'`` with the token you just received. Now you're ready to run the functions and call Byte's API.

## Functions

To be added.


## Contributing
Pull requests are welcome. Feel free to email me at **katekulinski@gmail.com** or message me at **genova#6601** if you have any questions.

[https://discord.gg/TeRvHSC](https://discord.gg/TeRvHSC)

## License
[MIT](https://choosealicense.com/licenses/mit/)
