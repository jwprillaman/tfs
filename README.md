# Torrent File System
### Create By: James Prillaman

##Description

TFS is a python application that allows users to encrypt and save a working directory. Then TFS will create a torrent for this directory so as that it can be shared accross multiple computers.


## Dependencies

transmission
```
sudo apt-get install transmission-cli

```

zip

```
sudo apt-get install zip

```

unzip

```
sudo apt-get install unzip

```
7zip
```
sudo apt-get install p7zip-full
```
##Configuration

edit /etc/transmission-daemon/settings.json

Set Download directory to the download directy of the tfs folder
```
"download-dir":"/home/myUser/tfs/downloads"
```
Also remove the rpc authentication
```
"rpc-authentication-required":"false"
```

Then reload the daemon
```
sudo services transmission-daemon reload
```

##Usage

```
python tfs.py -save [password]

```
Save current working directory of tfs/home to zip file and encrypt with given password. creates torrent for Home directory in tfs/downloads
