import hashlib
import crypt
username = []
algo = []
salt = []
hashedpass = []
algosalt = []
worklist = ["hakc","Put in ur pass here or map it to dictionary file"]
def crack(algos, hashs):
    checkfor=algos+hashs
    for i in range (0,2):
        if ((crypt.crypt(worklist[i],algos) == checkfor)): # accepts in the format of crypto.crypto(word, $algo$salt$)
            print "Found"

for line in open("/tmp/1", 'r'):
    print line
    if ((line.split(':')[1]!= "*")^(line.split(':')[1] == "!")):
        username.append(line.split(':')[0])
        algo.append(line.split(':')[1].split('$')[1])
        salt.append(line.split(':')[1].split('$')[2])
        hashedpass.append(line.split(':')[1].split('$')[3])
        algosalt.append("$"+line.split(':')[1].split('$')[1]+"$"+line.split(':')[1].split('$')[2]+"$")

for i in range (0,2):    
    crack(algosalt[i],hashedpass[i] )
