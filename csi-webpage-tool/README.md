## some bashes

```bash
tail -n +2 RMS_NJ_STD.txt | cut -f4         | sed "s/^/\'/" | sed "s/$/\'/" | tr '\n' ','            | sed "s/^/[/"        | sed 's/.$//'     | sed "s/$/]/" | clip.exe
# from 2nd line           # by tab, col 4th # \' at head    # \' at tail    # \n to ,, into one line # [ at head ] at tail # remove last char # ] at tail 
```
