# keyboard shorcut to delete the latest downnloaded file
put `trashld` in /usr/bin
it is:
```
trash ~/Downloads/$(ls -1t ~/Downloads/ | head -1)
```
ref:
https://unix.stackexchange.com/questions/84686/how-to-create-custom-commands-in-unix-linux
ctrl + alt + super + eject: trashld
// keyboard shortcut only accepts valid commands
