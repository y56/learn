# keyboard shorcut to delete the latest downnloaded file
put `trashld` in /usr/bin
register it as a program
it is:
```
trash ~/Downloads/$(ls -1t ~/Downloads/ | head -1)
```

chmod +x filename
to make it executable

Reload .profile or .bash_profle:
$ . ~/.bash_profile

ref:
https://unix.stackexchange.com/questions/84686/how-to-create-custom-commands-in-unix-linux
ctrl + alt + super + eject: trashld
// keyboard shortcut only accepts valid commands

# pikachu volleyball p2p

If your computer is assigned a public IP address (since your computer is connected directly to the internet without a router), the server reflexive candidate is not necessary. But it can be the case the public IP address is obfuscated to mDNS by the web browser since it is somehow treated as a local IP address. In this case, you can use Firefox to play this game. In your Firefox browser, visit the page about:config (by copying and pasting the address) and change the setting of "media.peerconnection.ice.obfuscate_host_addresses" to "false". Then, this P2P online version would work.

# remove certain string in file names

How can I remove a string of text from a files name?

ref: https://askubuntu.com/questions/210293/how-can-i-remove-a-string-of-text-from-a-files-name

```
for file in *; do mv "${file}" "${file//\.svg/}"; done
```

# print to clipboard

cat myfile | xclip -sel clip
echo lalala | xclip -sel clip

alias clipb='xclip -sel clip'

myfile | clipb
echo lalala | clipb

# clipboard to file

xclip -selection clipboard -o > myfile

alias clipf='xclip -selection clipboard -o'

clipf > myfile


