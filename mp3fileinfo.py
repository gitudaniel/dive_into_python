import fileinfo 
import types
#from fileinfo import MP3FileInfo

mp3file = fileinfo.MP3FileInfo()

#print mp3file

#print MP3FileInfo.__setitem__("name", "/Music/1. B.o.B - Dont Let Me Fall.mp3")

#print type(fileinfo.MP3FileInfo)

#print fileinfo.MP3FileInfo.tagDataMap

m = fileinfo.MP3FileInfo()

#print m.tagDataMap

f = open("/home/grenouille/Music/1. B.o.B - Dont Let Me Fall.mp3", "rb")
print f.name
print f
#print f.tell()
f.seek(-128, 2)
#print f.tell()
tagData = f.read(128)
#print tagData
#print f.tell()
print f.closed
f.close()
print f
#print f.closed
print f.tell()
print f.seek(0)

#fsock = open("/notthere", "r")

#try:
#    fsock = open("/notthere")
#except IOError:
#    print "The file does not exist, exiting gracefully"
#print "This line will always print"

