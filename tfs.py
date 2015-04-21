import os
import sys

#TRACKER = "udp://tracker.openbittorrent.com:80"
TRACKER = "udp://open.demonii.com:1337"
TOR_DIR = "/var/lib/transmission-daemon/downloads"

if len(sys.argv) != 3:
  print("Usage: tfs [-save|-get] [directory |file] [password]") 
  exit()

#Saves encrypted home directory to torrent file
def save( saveFile ):
  #working dir of the program
  workDir = os.path.dirname(os.path.abspath(__file__))
  #zips up ./home dir and encrypts with given password. Saves to ./temp
  os.system("zip -e -P " + sys.argv[2] + " " +  workDir + "/downloads/" + "homeZip " + "-r "  +workDir + "/home") 
  #creats torrent file using TRACKER saves to temp
  os.system("transmission-create -o " + workDir + "/downloads/homeTor.torrent " + "-t " + TRACKER + " " + workDir + "/downloads/homeZip.zip")
  #Add torrent to transmission for seeding
  os.system("transmission-remote --add " + workDir + "/downloads/homeTor.torrent")

def get( getFiles ):
  print('get')



if sys.argv[1] == '-save':
  print('save')
  save('file')
elif sys.argv[1] == '-get':
  print('get')


