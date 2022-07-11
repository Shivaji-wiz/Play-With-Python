import pytube

link = input("Enter URL: ")
yt = pytube.YouTube(link)
yt.streams.first().download()
print('Downloaded',link)
