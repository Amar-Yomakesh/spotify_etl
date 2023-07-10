import requests as req

# externalise the connection properties and handle the caching the conntion details to reduce API call
def connect_spotify():
    
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    connection = req.post("https://accounts.spotify.com/api/token", headers= header, data="grant_type=client_credentials&client_id=3cd101ba46f4491ebbdd199a71c5fa65&client_secret=647b6802bf39478c8b5f68bb18f4ece0&scope=user-modify-playback-state")
    print(connection.json())
    return connection.json()

def get_artist(artist_id,token):
    url = "https://api.spotify.com/v1/artists/" + artist_id
    header= {'Authorization' : 'Bearer ' + token}
    # print(header)
    artist = req.get(url,headers=header)
    return artist.json()

def recently_played(token):
    url = "https://api.spotify.com/v1/me/player/next"
    #url = "https://api.spotify.com/v1/me/player/currently-playing"
    header= {'Authorization' : 'Bearer ' + token}
    response = req.post(url,headers=header)
    print(response.json())
    return response

# my_artist= get_artist('6qqNVTkY8uBg9cP3Jd7DAH?si=dwtBaR6ER_ewrQRlJJEMhw',connect_spotify()['access_token'])
# print(my_artist)

my_recently_played = recently_played(connect_spotify()['access_token'])
print(my_recently_played)

