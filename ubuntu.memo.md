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

# speaker no sound after update

Although headphone works well.

Some of the below update will break the speaker
```
apport/bionic-updates,bionic-updates 2.20.9-0ubuntu7.21 all [upgradable from: 2.20.9-0ubuntu7.20]
apport-gtk/bionic-updates,bionic-updates 2.20.9-0ubuntu7.21 all [upgradable from: 2.20.9-0ubuntu7.20]
containerd/bionic-updates 1.3.3-0ubuntu1~18.04.4 amd64 [upgradable from: 1.3.3-0ubuntu1~18.04.2]
docker.io/bionic-updates 19.03.6-0ubuntu1~18.04.3 amd64 [upgradable from: 19.03.6-0ubuntu1~18.04.2]
linux-generic-hwe-18.04/bionic-security,bionic-updates 5.4.0.60.67~18.04.55 amd64 [upgradable from: 5.4.0.58.64~18.04.53]
linux-headers-generic-hwe-18.04/bionic-security,bionic-updates 5.4.0.60.67~18.04.55 amd64 [upgradable from: 5.4.0.58.64~18.04.53]
linux-hwe-5.4-tools-common/bionic-security,bionic-security,bionic-updates,bionic-updates 5.4.0-60.67~18.04.1 all [upgradable from: 5.4.0-58.64~18.04.1]
linux-image-generic-hwe-18.04/bionic-security,bionic-updates 5.4.0.60.67~18.04.55 amd64 [upgradable from: 5.4.0.58.64~18.04.53]
python3-apport/bionic-updates,bionic-updates 2.20.9-0ubuntu7.21 all [upgradable from: 2.20.9-0ubuntu7.20]
python3-problem-report/bionic-updates,bionic-updates 2.20.9-0ubuntu7.21 all [upgradable from: 2.20.9-0ubuntu7.20]
```

lemme find time to figure out how have sound after update`

https://askubuntu.com/questions/1218041/ubuntu-18-04-audio-disappeared-after-update

# stop to modify `/etc/default/grub` to make sound device work

previously, an update broke my sound device

memo: https://gist.github.com/y56/ffcf21204620a21b629906c1d6abe8e7

but now it fixes.


`sudo vim /etc/default/grub`

```
# /etc/default/grub

GRUB_CMDLINE_LINUX_DEFAULT="quiet splash snd_hda_intel.dmic_detect=0"
```

no need any more, I can now have normal sound without this

and look like this is deprecated

