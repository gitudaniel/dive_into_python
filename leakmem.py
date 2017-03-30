import fileinfo

def leakmem():
    f = fileinfo.FileInfo('/music/1. B.o.B - Dont Let Me Fall.mp3')
    #print f
    print f['name']

    f.__setitem__('genre', 31)
    print f

    f['genre'] = 32
    print f

#for i in range(100):
#    leakmem()

leakmem()
