import os
import sys

if len(sys.argv) != 3:
  print("Usage: tfs [-save|-get] [file]") 
  exit()

def save( saveFile ):
  workDir = os.path.dirname(os.path.abspath(__file__))
  print(workDir)

def get( getFiles ):
  print('get')



if sys.argv[1] == '-save':
  print('save')
  save('file')
elif sys.argv[1] == '-get':
  print('get')


