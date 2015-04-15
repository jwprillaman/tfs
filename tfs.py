import os
import sys

TRACKER = "udp://tracker.openbittorrent.com:80"

if len(sys.argv) != 3:
  print("Usage: tfs [-save|-get] [directory |file] [password]") 
  exit()

#Saves encrypted home directory to torrent file
def save( saveFile ):
  #working dir of the program
  workDir = os.path.dirname(os.path.abspath(__file__))
  #zips up ./home dir and encrypts with given password. Saves to ./temp
  os.system("zip -e -P " + sys.argv[2] + " " +  workDir + "/temp/" + "homeZip " + "-r "  +workDir + "/home") 
  #creats torrent file using TRACKER saves to temp
  os.system("transmission-create -o " + workDir + "/temp/homeTor.torrent " + "-t " + TRACKER + " " + workDir + "/temp/homeZip.zip")
def get( getFiles ):
  print('get')



if sys.argv[1] == '-save':
  print('save')
  save('file')
elif sys.argv[1] == '-get':
  print('get')


