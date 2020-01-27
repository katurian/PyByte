
import requests 

authtoken = 'XXXXXXEXNFWBXXXXXXYCZRXXXX'

def getAccountInfo():
    r = requests.get('https://api.byte.co/account/me', headers={'Authorization': authtoken})
    accountJSON = r.json()
    return accountJSON
    
def getBlockedList():
    r = requests.get('https://api.byte.co/account/me/blocking', headers={'Authorization': authtoken})
    blockedJSON = r.json()
    return blockedJSON
    
def getFeed():
    r = requests.get('https://api.byte.co/feed/global', headers={'Authorization': authtoken})
    feedJSON = r.json()
    return feedJSON
    
def getUserInfo(userID): 
    r = requests.get(f'https://api.byte.co/account/id/{userID}', headers={'Authorization': authtoken})
    userJSON = r.json()
    return userJSON
    
def likePost(postID):
    r = requests.put(f'https://api.byte.co/post/id/{postID}/feedback/like', headers={'Authorization': authtoken})
  
def commentPost(postID):
    r = requests.post(f'https://api.byte.co/post/id/{postID}/feedback/comment', headers={'Authorization': authtoken}, json={'body':'comment'})
  
def blockUser(userID): 
    r = requests.put(f'https://api.byte.co/account/id/{userID}/block', headers={'Authorization': authtoken})
    
def followUser(userID): 
    r = requests.put(f'https://api.byte.co/account/id/{userID}/follow', headers={'Authorization': authtoken})
   
    
   
    

