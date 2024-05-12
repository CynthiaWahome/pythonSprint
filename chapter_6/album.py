def make_album(artist_name, album_title):
    album_details = {'name':artist_name, 'title': album_title}
    return album_details

album_records = make_album('Davido', 'Timeless')
print(album_records)

album_records = make_album('Burna Boy', 'I told them')
print(album_records)

album_records = make_album('Asake', 'Work of Art')
print(album_records)

# An optional parameter

def make_album(artist_name,album_title,album_tracks=''):
    album_dets = {'name': artist_name, 'title': album_title}
    
    if album_tracks:
        album_dets ['number of tracks'] = album_tracks
    return album_dets

album_archives = make_album('Rema','Ravage',album_tracks=10)
print (album_archives)


# Creating a while loop

def describe_album(album_artist, album_cover):
    album_info = {'name':album_artist, 'title': album_cover}
    return album_info

while True:
    artist = (input("What is the name of the artist? "))
    if artist == 'q':
        break

    cover = (input("What is the title of the album? "))
    
    if cover == 'q':
        break

album_inventory = describe_album(artist, cover)    
print(album_inventory)