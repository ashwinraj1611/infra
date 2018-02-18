import heapq
import sys
import operator
import os, os.path

directory = "/"
numfiles = int(10)

try:
    filenames = (os.path.join(p, n) for p, _,f in os.walk(directory) for n in f)
    filesizes = ((name, os.path.getsize(name)) for name in filenames)

    actual_names = []
    _exhausted = object()

    while(1):
        file = next(filenames,_exhausted)
        if file == _exhausted:
           # print 'Generator empty !'
            break
        if file.startswith('/proc/') or file.startswith('/run/') or file.startswith('/etc/') or file.startswith('/usr/') or file.startswith('/var/') or "mozilla" in file or "chrome" in file:
            continue
            
        check = file.split('/')[-1]
        #print file
        if check == 'SingletonCookie' or check == 'SingletonLock':
            continue
        actual_names.append(file)

    # print len(actual_names)

    bigfiles = heapq.nlargest(numfiles, actual_names, key = os.path.getsize)

    for b in bigfiles:
        temp = b[1:]+"{: "+str(round(os.path.getsize(b)/(1024.0*1024.0), 2))+" MB}"
        print temp
	        # print temp
except OSError as e:
    print 'Error: ',e    
    pass
#print (*("{}\t{:>}".format(b, os.path.getsize(b)) for b in bigfiles))