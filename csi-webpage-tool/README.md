## some bashes

###
```bash
tail -n +2 RMS_NJ_STD.txt | cut -f4         | sed "s/^/\'/" | sed "s/$/\'/" | tr '\n' ','            | sed "s/^/[/"        | sed 's/.$//'     | sed "s/$/]/" | clip.exe
# from 2nd line           # by tab, col 4th # \' at head    # \' at tail    # \n to ,, into one line # [ at head ] at tail # remove last char # ] at tail 
```

### 
in a dir like
Package0000001_20210126_XHUANG_26110.zip
Package0000002_20210207_dlzhang_26144.zip
Package0000003_20210207_dlzhang_26145.zip
```bash
ls -1 | cut -f4 | cut -c 16-999 | cut -d '.' -f1 | sed "s/^/\'/" | sed "s/$/\'/" | tr '\n' ',' | sed 's/.$//' | sed "s/^/[/" | sed "s/$/]/" | clip.exe
      # by tab  # mystr[16::]                                                                  # mystr[:-1]
```
