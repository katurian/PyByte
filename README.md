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

![oauth](https://github.com/katurian/PyByte/blob/master/oauth.PNG)

Sign in through Google and follow the rest of the directions. Your Authentication Token will print to the cmd.exe window.

Now go to ``functions.py`` 

```python

import requests 

authtoken = 'XXXXXXEXNFWBXXXXXXYCZRXXXX'
```
Replace ``'XXXXXXEXNFWBXXXXXXYCZRXXXX'`` with the token you just received. Now you're ready to run the functions and call Byte's API.

## Functions

**Function**|**Endpoint**|**Parameters**|**Description**
:-----:|:-----:|:-----:|:-----:
searchUsers()|/account/prefix/{query}|query|Queries a string and returns a JSON of users with similar names along with their profile information.
getAccountInfo()|/account/me|N/A|Returns a JSON containing your account information.
setBio()|/account/me|bioText|Sets your profile biography to bioText.
setColor()|/account/me|scheme |Takes an integer from 1 to 17, each representing a different color scheme, and sets your profile's scheme accordingly.
getBlockedList()|/account/me/blocking| |Returns a JSON of users you are currently blocking.
getMyPosts()|/account/me/posts| |Returns a JSON of your post titles, likes, rebytes, comments, etc.
getUserPosts()|account/id/{userID}/posts|userID|Takes a user's ID, represented as a string, and returns a JSON of their post titles, likes, rebytes, comments, etc.
getUserInfo()|/account/id/{userID}|userID|Takes a user's ID, represented as a string, and returns a JSON of their account information.
followUser()|/account/id/{userID}/follow|userID|Follows a user given their ID.
blockUser()|/account/id/{userID}/block|userID|Blocks a user given their ID.
getFeed()|/feed/global|N/A|Returns a JSON of users and posts. 
rebytePost()|post/id/{postID}/rebyte|postID|Rebytes a post given its ID.
reportPost()|/post/id/{postID}/report|postID|Reports a post given its ID.
commentPost()|/post/id/{postID}/feedback/comment|postID|Comments on a post given its ID.
likePost()|/post/id/{postID}/feedback/like|postID|Likes a post given its ID.
unlikePost()|/post/id/{postID}/feedback/like|postID|Unlikes a post given its ID.
deleteComment()|/post/id/{postID}/feedback/comment/id/{commentid}|postID, commentID|Deletes a comment given a post ID and a comment ID, only works on your own post and on your own comment.
deleteComment()|/post/id/{postID}/feedback/comment/id/{commentid}|postID, commentID|Deletes a comment given a post ID and a comment ID, only works on your own post and on your own comment.

![colors1](https://cdn.discordapp.com/attachments/397194055995490308/671745842067275786/image0.png)

![colors2](https://cdn.discordapp.com/attachments/397194055995490308/671745842478055444/image1.png)

## Contributing
Pull requests are welcome. Feel free to email me at **katekulinski@gmail.com** or message me at **genova#6601** if you have any questions.

[https://discord.gg/TeRvHSC](https://discord.gg/TeRvHSC)

## License
[MIT](https://choosealicense.com/licenses/mit/)
