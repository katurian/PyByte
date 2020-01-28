
import requests 
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

authtoken = 'XXXXXXEXNFWBXXXXXXYCZRXXXX'

def searchUsers(query):
    r = requests.get(f'https://api.byte.co/account/prefix/{query}', headers={'Authorization': authtoken}, verify=False)
    resultJSON = r.json()
    return resultJSON

def getFeed():
    r = requests.get('https://api.byte.co/feed/global', headers={'Authorization': authtoken}, verify=False)
    feedJSON = r.json()
    return feedJSON

def getAccountInfo():
    r = requests.get('https://api.byte.co/account/me', headers={'Authorization': authtoken}, verify=False)
    accountJSON = r.json()
    return accountJSON

def setBio(bioText):
    requests.put('https://api.byte.co/account/me', headers={'Authorization': authtoken}, json={'bio': bioText}, verify=False)
    
def getBlockedList():
    r = requests.get('https://api.byte.co/account/me/blocking', headers={'Authorization': authtoken}, verify=False)
    blockedJSON = r.json()
    return blockedJSON

def getMyPosts():
    r = requests.get('https://api.byte.co/account/me/posts', headers={'Authorization': authtoken}, verify=False)
    myPostsJSON = r.json()
    return myPostsJSON
    
def getUserPosts(userID):
    r = requests.get('https://api.byte.co/account/id/{userID}/posts', headers={'Authorization': authtoken}, verify=False)
    userPostsJSON = r.json()
    return userPostsJSON
    
def getUserInfo(userID): 
    r = requests.get(f'https://api.byte.co/account/id/{userID}', headers={'Authorization': authtoken}, verify=False)
    userJSON = r.json()
    return userJSON
    
def likePost(postID):
    requests.put(f'https://api.byte.co/post/id/{postID}/feedback/like', headers={'Authorization': authtoken}, verify=False)
    
def unlikePost(postID):
    requests.delete(f'https://api.byte.co/post/id/{postID}/feedback/like', headers={'Authorization': authtoken}, verify=False)
  
def commentPost(postID):
    requests.post(f'https://api.byte.co/post/id/{postID}/feedback/comment', headers={'Authorization': authtoken}, json={'body':'comment'}, verify=False)
 
def deleteComment(postID, commentID):
    requests.delete(f'https://api.byte.co/post/id/{postID}/feedback/comment/id/{commentid}', headers={'Authorization': authtoken}, verify=False)    
    
def rebytePost(postID):
    requests.put(f'https://api.byte.co/post/id/{postID}/rebyte', headers={'Authorization': authtoken}, verify=False)
    
def reportPost(postID):
    requests.put(f'https://api.byte.co/post/id/{postID}/report', headers={'Authorization': authtoken}, verify=False)
    
def blockUser(userID): 
    requests.put(f'https://api.byte.co/account/id/{userID}/block', headers={'Authorization': authtoken}, verify=False)
    
def followUser(userID): 
    requests.put(f'https://api.byte.co/account/id/{userID}/follow', headers={'Authorization': authtoken}, verify=False)
   
