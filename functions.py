
import requests 

authtoken = 'XXXXXXEXNFWBXXXXXXYCZRXXXX'

def searchUsers(query):
    r = requests.get(f'https://api.byte.co/account/prefix/{query}', headers={'Authorization': authtoken})
    resultJSON = r.json()
    return resultJSON

def getFeed():
    r = requests.get('https://api.byte.co/feed/global', headers={'Authorization': authtoken})
    feedJSON = r.json()
    return feedJSON

def getAccountInfo():
    r = requests.get('https://api.byte.co/account/me', headers={'Authorization': authtoken})
    accountJSON = r.json()
    return accountJSON
    
def getBlockedList():
    r = requests.get('https://api.byte.co/account/me/blocking', headers={'Authorization': authtoken})
    blockedJSON = r.json()
    return blockedJSON

def getMyPosts():
    r = requests.get('https://api.byte.co/account/me/posts', headers={'Authorization': authtoken})
    myPostsJSON = r.json()
    return myPostsJSON
    
def getUserPosts(userID):
    r = requests.get('https://api.byte.co/account/id/{userID}/posts', headers={'Authorization': authtoken})
    userPostsJSON = r.json()
    return userPostsJSON
    
def getUserInfo(userID): 
    r = requests.get(f'https://api.byte.co/account/id/{userID}', headers={'Authorization': authtoken})
    userJSON = r.json()
    return userJSON
    
def likePost(postID):
    requests.put(f'https://api.byte.co/post/id/{postID}/feedback/like', headers={'Authorization': authtoken})
  
def commentPost(postID):
    requests.post(f'https://api.byte.co/post/id/{postID}/feedback/comment', headers={'Authorization': authtoken}, json={'body':'comment'})
  
def blockUser(userID): 
    requests.put(f'https://api.byte.co/account/id/{userID}/block', headers={'Authorization': authtoken})
    
def followUser(userID): 
    requests.put(f'https://api.byte.co/account/id/{userID}/follow', headers={'Authorization': authtoken})
   
