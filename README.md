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

To save and seed your home dir:
```
python tfs.py -save password

```
where password is the user created encryption password. Please keep this in a safe location as you will need it to access your tfs.

The torrent file ,homeTor.torrent, to access your tfs is located in the downloads directory in the tfs file structure.

To get your seeded home dir:
```
python tfs.py -get torrentFile password
```
where torrentFile is the torrent file returned from the -save command and password is the password used to encrypt in the -save command.


