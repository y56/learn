# to word-level highlighted colorful diff to html (dark mode) 

## diff + ydiff

### installation -- pip 
```
python3 -m pip install --user ydiff
```

### installation -- from git repo
https://github.com/ymattw/ydiff.git
```
git clone https://github.com/ymattw/ydiff.git
cd ydiff
./setup.py install
```

### conclusion, ydiff, interactive 
```
diff -u foo bar | ydiff -s
```

## git diff + ansi2html

## installation
```
wget "http://www.pixelbeat.org/scripts/ansi2html.sh" -O /tmp/ansi2html.sh
chmod +x /tmp/ansi2html.sh
```

## conclusion, to html
```
git diff --color-words --no-index  foo bar | /tmp/ansi2html.sh --bg=dark > foobar.html
```

