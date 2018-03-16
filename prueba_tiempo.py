import time
import datetime

now = datetime.datetime.now()
nuevo = now + datetime.timedelta(minutes = 10)

now_str = str(now).split('.')[0]
nuevo_str = str(nuevo).split('.')[0]

print "Now   : ", now_str
print "future: ", nuevo_str

if now_str > nuevo_str:
    print "mayor"
elif now_str < nuevo_str:
    print "menor"
else:
    print "igual"
