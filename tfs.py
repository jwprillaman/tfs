import os
import sys

if len(sys.argv) != 3:
  print("Usage: tfs [-save|-get] [directory |file] [password]") 
  exit()

def save( saveFile ):
  workDir = os.path.dirname(os.path.abspath(__file__))
  print("zip -e -P " + sys.argv[2] + " " +  workDir + "/temp/" + "homeZip " + "-r "  +workDir + "/home")
  os.system("zip -e -P " + sys.argv[2] + " " +  workDir + "/temp/" + "homeZip " + "-r "  +workDir + "/home") 

def get( getFiles ):
  print('get')



if sys.argv[1] == '-save':
  print('save')
  save('file')
elif sys.argv[1] == '-get':
  print('get')


