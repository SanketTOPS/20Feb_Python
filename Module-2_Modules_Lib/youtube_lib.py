from pytube import YouTube

"""url="https://www.youtube.com/watch?v=QZAEI6wO6jM"

you=YouTube(url=url)

you.streams.first().download()"""

#yt=YouTube("https://www.youtube.com/watch?v=QZAEI6wO6jM").streams.first().download()
yt=YouTube("https://www.youtube.com/watch?v=deztUdPApiM").streams.filter(only_audio=True).first().download()
print("Download Successfully!")