import os
import sys

#TRACKER = "udp://tracker.openbittorrent.com:80"
TRACKER = "udp://open.demonii.com:1337"
TOR_DIR = "/var/lib/transmission-daemon/downloads"

print(len(sys.argv))
if (len(sys.argv) != 3) and (len(sys.argv) != 4):
  print("Usage: tfs [-save [password] |-get [file] [password]]") 
  exit()

workDir = os.path.dirname(os.path.abspath(__file__))
#Saves encrypted home directory to torrent file
def save( saveFile ):
  #working dir of the program
  #zips up ./home dir and encrypts with given password. Saves to ./temp
  #os.system("zip -e -P " + sys.argv[2] + " " +  workDir + "/downloads/" + "homeZip " + "-r "  +workDir + "/home") 
  os.system("7z a -t7z -p" + sys.argv[2] + " " + workDir + "/downloads/homeZip " + workDir + "/home")
  #creats torrent file using TRACKER saves to temp
  os.system("transmission-create -o " + workDir + "/downloads/homeTor.torrent " + "-t " + TRACKER + " " + workDir + "/downloads/homeZip.7z")
  #Add torrent to transmission for seeding
  os.system("transmission-remote --add " + workDir + "/downloads/homeTor.torrent")

def get( getFiles ):
  #copy given torrent file to download directory
  os.system("cp " + getFiles + " " + workDir + "/downloads/")
  #download torrent file
  os.system("aria2c " + workDir + "/downloads/homeTor.torrent -d " + workDir + "/downloads/ --on-bt-download-complete=" + workDir + "/done.sh")
  # " + "> " + workDir + "/log.txt 2>&1 &")

def done(password ):
  print("pass: " + password)
  #os.system("7z x -p" + password + " -o" + workDir + "/home/ " + workDir + "/downloads/homeZip.7z")
  print("Finished")

if sys.argv[1] == '-save':
  print('save')
  save('file')
elif sys.argv[1] == '-get':
  print('get')
  get(sys.argv[2])
elif sys.argv[1] == '-done':
  print('Inflating')
  done(sys.argv[2])

