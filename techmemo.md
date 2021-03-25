tech note
====
# get a pink slip
= get fired

# install node.js ver 12
https://linuxize.com/post/how-to-install-node-js-on-ubuntu-18.04/

# one hot onehot

y_onehot = keras.utils.to_categorical(y, num_classes=1283)

encode label into onehot

https://www.tensorflow.org/api_docs/python/tf/keras/utils/to_categorical

# np.argmax()

# np.argsort()

# partial_model = keras.models.Model(inputs=modelinput, outputs=conv3output)

# model.get_layer(layer_name).output

# model.predict()

# data = h5py.File(filepath, 'r')

# weights, bias = model.get_layer(layer_name).get_weights()

## delete neurons

weights[:, :, :, idx] = np.zeros(np.shape(weights[:, :, :, idx]))

bias[idx] = 0

# pickle to save store dump

pickle

f = open('filename.pkl', 'wb')

pickle.dump(var_want_to_save, f)

f.close()

# pickle to load file

import pickle

file = open('filename.pkl','rb'))

obj = pickle.load(file)

file.close()

# Python, difference between 'open' and 'with open'

https://stackoverflow.com/questions/34429519/python-difference-between-open-and-with-open

https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for

# h5py 

model = ...  # Get model (Sequential, Functional Model, or Model subclass)

model.save('path/to/location')

from tensorflow import keras

model = keras.models.load_model('path/to/location')

https://www.tensorflow.org/guide/keras/save_and_serialize

# range() and reversed(range())

```python
my_iter_1 = range()
for ele in li:
    for i in my_iter_1:
        # good 
        # new instance of iterator are created
```
```python
my_iter_2 = reversed(range())
for ele in li:
    for i in my_iter_2:
        # bad
        # only one instance of iterator ever
```
# I want to zoom just ONE tab/window - not all of them - Help!

https://support.mozilla.org/en-US/questions/681298

Zoom is driving me nuts!  I use multiple tabs and windows, and to maximize screen space I need to make some pages very small.  In IE each window can be zoomed independently- but with firefox they all change if you change any window's zoom.  I've tried NoSquint add-on and it adds site-specific zoom, which is still not what I need.  Surely there's an add-on that allows each window to have its own zoom level.

Are these tabs perhaps in the same site? If they are, you need to configure Firefox not to remember zoom levels for a specific site. Do this:

    1. type about:config in your address bar and press enter
    2. if Firefox asks you, say you'll be careful
    3. search this string browser.zoom.siteSpecific (if it doesn't exist, create one, it's a boolean string)
    4. set it to false (rightclick > "Toogle").

Now your Firefox won't remember the zoom level. You can restore your zoom level by click CTRL+0 (that's zero) in your keyboard, or going into View > Zoom > Reset.

# Queue interface in java
## https://javagoal.com/queue-interface-in-java/


Queue interface in java

queue interface in java extends the collection interface and it is available in java.util package. Java queue maintains the orders the elements in FIFO(First In First Out) manner. In FIFO, the first element removes first, and the last element removes at last. Java queue is a collection that is used to hold the elements and perform various operations like insertion, removal, etc. In Queue the element inserts at the end of the list and deleting elements from the start of the list. The Queue interface has its implementation in PriorityQueue and the LinkedList class is also implementing it through the Deque. PriorityQueue and LinkedList class are not thread-safe But there is another alternative implementation that is PriorityBlockingQueue which is thread-safe.
Queue interface in java
Java queue class diagram
Important points about Java Queue

1. Java Queue is just like a real-world queue, It based on FIFO (First In First Out). In queue inserts elements at the end and removes from the beginning.

2. Java Queue represents an ordered list of elements and it supports all methods of Collection interface.

3. LinkedList, PriorityQueue, and ArrayBlockingQueue are the most frequently used Queue implementations.

4. BlockingQueue is the thread-safe implementation of Queue and it doesn’t accept any null element.
Java queue methods

1. add() method

This method is used to add the element in the Queue, it adds the element at the tail(Rear). As you know the Queue interface is implemented by PriorityQueue and LinkedList. In both classes add method work differently. In LinkedList, the element will be added at the last. But in PriorityQueue, the element will be added according to the priority in case of priority queue implementation.

2. peek() method

This method is used to get the head(First) element of the queue without removing it. If the queue is empty it will return null.

3. element() method

This method is also used to get the head(First) element of the queue without removing it. It is very similar to peek() method. If the queue is empty it will throw NoSuchElementException.

4. remove() method

This method is used to remove and get the head(First) element from the queue. If queue is empty it will throw NoSuchElementException.

5. poll() method

This method is also used to remove and get the head(First) element from the queue. It is very similar to remove() method. If the queue is empty it will return null.

6. size() method: This method returns the number of elements presents in the queue.
Java queue implementations

There are some classes that provides the implementation to queue interface.
```
PriorityQueue class


PriorityQueue extends the AbstarctQueue that implements the Queue interface. The PriorityQueue works based on priority and process the objects. It is also works based on the First-In-First-Out algorithm, but sometimes it processes the element according to the priority. Let’s take an example of java queue program
import java.util.PriorityQueue;
import java.util.Queue; 
  
public class ExampleOfQueue 
{ 
  public static void main(String[] args) 
  { 
    Queue<String> stringQueue = new PriorityQueue<String>(); 
  
    // Adding some number/elements in queue by use of add() method
    stringQueue.add("AA"); 
    stringQueue.add("BB"); 
    stringQueue.add("CC"); 
    stringQueue.add("DD");
    stringQueue.add("EE"); 
    
    // Showing all data from queue
    System.out.println("Elements from the queue: "+stringQueue); 
  
    // Getting the head(First) element from queue by use of peek() method. 
    String firstStringByPeek = stringQueue.peek(); 
    System.out.println("Getting the by peek() method: " + firstStringByPeek); 
  
    // Getting the head(First) element from queue by use of element() method. 
    String firstStringByElement = stringQueue.element(); 
    System.out.println("Getting the by element() method: " + firstStringByElement); 
    
    // Removing the head(First) element from queue by use of remove() method. 
    String removedElement = stringQueue.remove(); 
    System.out.println("Removing element by remove() method: " + removedElement); 
  
    // Removing the head(First) element from queue by use of poll() method. 
    String removedElementByPoll = stringQueue.poll(); 
    System.out.println("Removing element by poll() method: " + removedElementByPoll); 
  
    // Getting size of Queue
    int size = stringQueue.size(); 
    System.out.println("Size of queue: " + size); 
  } 
}

    Output: Elements from the queue: [AA, BB, CC, DD, EE]
    Getting the by peek() method: AA
    Getting the by element() method: AA
    Removing element by remove() method: AA
    Removing element by poll() method: BB
    Size of queue: 3

LinkedList class

LinkedList class is a very popular implementation of the Queue interface. It stores the elements in the contiguous memory location and maintains the insertion order of the element. Let’s take an example of java queue program
import java.util.LinkedList; 
import java.util.Queue; 
  
public class ExampleOfQueue 
{ 
  public static void main(String[] args) 
  { 
    Queue<Integer> numbers = new LinkedList<Integer>(); 
  
    // Adding some number/elements in queue by use of add() method
    numbers.add(1); 
    numbers.add(2); 
    numbers.add(3); 
    numbers.add(4);
    numbers.add(5); 
    
    // Showing all data from queue
    for(Integer num : numbers)
        System.out.println("Elements from the queue: "+num); 
  
    // Getting the head(First) element from queue by use of peek() method. 
    int firstNumberByPeek = numbers.peek(); 
    System.out.println("Getting the by peek() method: " + firstNumberByPeek); 
  
    // Getting the head(First) element from queue by use of element() method. 
    int firstNumberByElement = numbers.element(); 
    System.out.println("Getting the by element() method: " + firstNumberByElement); 
    
    // Removing the head(First) element from queue by use of remove() method. 
    int removedElement = numbers.remove(); 
    System.out.println("Removing element by remove() method: " + removedElement); 
  
    // Removing the head(First) element from queue by use of poll() method. 
    int removedElementByPoll = numbers.poll(); 
    System.out.println("Removing element by poll() method: " + removedElementByPoll); 
  
    // Getting size of Queue
    int size = numbers.size(); 
    System.out.println("Size of queue: " + size); 
  } 
}

    Output: Elements from the queue: 1
    Elements from the queue: 2
    Elements from the queue: 3
    Elements from the queue: 4
    Elements from the queue: 5
    Getting the by peek() method: 1
    Getting the by element() method: 1
    Removing element by remove() method: 1
    Removing element by poll() method: 2
    Size of queue: 3

PriorityBlockingQueue class

PriorityBlockingQueue class implements the Queue interface and provides the thread-safe implementation of the queue. The PriorityQueue and LinkedList are not thread-safe. Let’s take an example of java queue program
import java.util.Queue;
import java.util.concurrent.PriorityBlockingQueue; 
  
public class ExampleOfQueue 
{ 
  public static void main(String[] args) 
  { 
    Queue<String> stringQueue = new PriorityBlockingQueue<String>(); 
  
    // Adding some number/elements in queue by use of add() method
    stringQueue.add("AA"); 
    stringQueue.add("BB"); 
    stringQueue.add("CC"); 
    stringQueue.add("DD");
    stringQueue.add("EE"); 
    
    // Showing all data from queue
    System.out.println("Elements from the queue: "+stringQueue); 
  
    // Getting the head(First) element from queue by use of peek() method. 
    String firstStringByPeek = stringQueue.peek(); 
    System.out.println("Getting the by peek() method: " + firstStringByPeek); 
  
    // Getting the head(First) element from queue by use of element() method. 
    String firstStringByElement = stringQueue.element(); 
    System.out.println("Getting the by element() method: " + firstStringByElement); 
    
    // Removing the head(First) element from queue by use of remove() method. 
    String removedElement = stringQueue.remove(); 
    System.out.println("Removing element by remove() method: " + removedElement); 
  
    // Removing the head(First) element from queue by use of poll() method. 
    String removedElementByPoll = stringQueue.poll(); 
    System.out.println("Removing element by poll() method: " + removedElementByPoll); 
  
    // Getting size of Queue
    int size = stringQueue.size(); 
    System.out.println("Size of queue: " + size); 
  } 
}
```
```
    Output: Elements from the queue: [AA, BB, CC, DD, EE]
    Getting the by peek() method: AA
    Getting the by element() method: AA
    Removing element by remove() method: AA
    Removing element by poll() method: BB
    Size of queue: 3
```
# 教學-android-studio-開發環境安裝教學-linux版

https://xenby.com/b/227-%E6%95%99%E5%AD%B8-android-studio-%E9%96%8B%E7%99%BC%E7%92%B0%E5%A2%83%E5%AE%89%E8%A3%9D%E6%95%99%E5%AD%B8-linux%E7%89%88
# WSL: Am I running version 1 or version 2?
https://askubuntu.com/questions/1177729/wsl-am-i-running-version-1-or-version-2#
I have Windows Subsystem for Linux, but I don't know which version I have, and many things won't work in version 1. How do I check my version?

# write good commit message with Commitizen
https://commitizen-tools.github.io/commitizen/
https://www.coderbridge.com/series/66cb226274ea4d349abd49d2aef44037/posts/6770ab92a0654588b9d389664a36c449

cz bump 會自動提升版本號，
主要根據 cz commit 裡有沒有 BREAKING CHANGE，以及分類 (feat, fix, ... 那些)
如果要自行指定增加的版本號可以用選項 --increment {MAJOR,MINOR,PATCH}，
然後 --changelog 會把 cz commit 的那些 commit 整理起來。

# WSL font color
How to change the dark blue in wsl (Windows Subsystem for Linux) to something brighter? Here is a picture of a config file opened with vim. I basically see a black screen. I cannot read it. And the property window of the console does not allow to change specific colors. Only the background and the main text.
https://superuser.com/questions/1365258/how-to-change-the-dark-blue-in-wsl-to-something-brighter

# javascript console.log font color
```
console.log('\x1b[36m%s\x1b[0m', 'I am cyan');  //cyan
console.log('\x1b[33m%s\x1b[0m', stringToMakeYellow);  //yellow
'\x1b[31m%s\x1b[0m' // red
```
https://stackoverflow.com/questions/9781218/how-to-change-node-jss-console-font-color
```
Reset = "\x1b[0m"
Bright = "\x1b[1m"
Dim = "\x1b[2m"
Underscore = "\x1b[4m"
Blink = "\x1b[5m"
Reverse = "\x1b[7m"
Hidden = "\x1b[8m"

%s 

FgBlack = "\x1b[30m"
FgRed = "\x1b[31m"
FgGreen = "\x1b[32m"
FgYellow = "\x1b[33m"
FgBlue = "\x1b[34m"
FgMagenta = "\x1b[35m"
FgCyan = "\x1b[36m"
FgWhite = "\x1b[37m"

BgBlack = "\x1b[40m"
BgRed = "\x1b[41m"
BgGreen = "\x1b[42m"
BgYellow = "\x1b[43m"
BgBlue = "\x1b[44m"
BgMagenta = "\x1b[45m"
BgCyan = "\x1b[46m"
BgWhite = "\x1b[47m"
```
# terminology: bump version
What does Bump Version stand for?
https://stackoverflow.com/questions/4181185/what-does-bump-version-stand-for
It means to increment the version number to a new, unique value.

# VS Code color theme
https://code.visualstudio.com/docs/getstarted/themes

# run foo.exe in window
```
& "C:\Program Files\Sublime Text 3\sublime_text.exe"
```

# convert powershell script to exe
https://github.com/MScholtes/PS2EXE
```
PS C:\> Install-Module ps2exe // to install

ps2exe .\source.ps1 .\target.exe // to convert
```

# handle of object
http://www.cs.technion.ac.il/users/yechiel/c++-faq/what-is-a-handle.html
 [8.8] What is a handle to an object? Is it a pointer? Is it a reference? Is it a pointer-to-a-pointer? What is it?

The term handle is used to mean any technique that lets you get to another object — a generalized pseudo-pointer. The term is (intentionally) ambiguous and vague.

Ambiguity is actually an asset in certain cases. For example, during early design you might not be ready to commit to a specific representation for the handles. You might not be sure whether you'll want simple pointers vs. references vs. pointers-to-pointers vs. references-to-pointers vs. integer indices into an array vs. strings (or other key) that can be looked up in a hash-table (or other data structure) vs. database keys vs. some other technique. If you merely know that you'll need some sort of thingy that will uniquely identify and get to an object, you call the thingy a Handle. 

# COM Component Object Model
https://de.wikipedia.org/wiki/Component_Object_Model

# execute some sql query through feathers app.service('messages').find()
## how to do sql select
https://docs.feathersjs.com/api/databases/querying.html#sort
```json
// Only return the `text` and `userId` field in a message
app.service('messages').find({
  query: {
    $select: [ 'text', 'userId' ]
  }
});

app.service('messages').get(1, {
  query: {
    $select: [ 'text' ]
  }
});

```
# pySpark how to replace null into unique string
## See: https://stackoverflow.com/questions/41330387/how-to-fill-the-null-value-in-dataframe-to-uuid
## See: https://gist.github.com/zoltanctoth/2deccd69e3d1cde1dd78
```python
# QQ this python code doesnt work QQ
null_news_category_id_to_uuid4 = F.udf(lambda x: str(uuid.uuid4()), StringType())
self.df = self.df.withColumn('news_category_lv1_id', null_news_category_id_to_uuid4(F.col('news_category_lv1_id')))
self.df = self.df.withColumn('news_category_lv2_id', null_news_category_id_to_uuid4(F.col('news_category_lv2_id')))
```
# [skip ci] [ci skip] [skip Travis]
# spark pyspark fill null with 0 zero uuid
https://stackoverflow.com/questions/41330387/how-to-fill-the-null-value-in-dataframe-to-uuid
# user-defined function udf python pyspark
https://docs.databricks.com/spark/latest/spark-sql/udf-python.html
# display() vs df.show()
display() is more readable
# Generate a Unique String -- UUID
https://stackoverflow.com/questions/26030811/generate-a-unique-string-in-python-django/26032898
# How are Python's Built In Dictionaries Implemented? python dictionary implementation
https://stackoverflow.com/questions/327311/how-are-pythons-built-in-dictionaries-implemented
Here is everything about Python dicts that I was able to put together (probably more than anyone would like to know; but the answer is comprehensive).

    Python dictionaries are implemented as hash tables.

    Hash tables must allow for hash collisions i.e. even if two distinct keys have the same hash value, the table's implementation must have a strategy to insert and retrieve the key and value pairs unambiguously.

    Python dict uses open addressing to resolve hash collisions (explained below) (see dictobject.c:296-297).

    Python hash table is just a contiguous block of memory (sort of like an array, so you can do an O(1) lookup by index).

    Each slot in the table can store one and only one entry. This is important.

    Each entry in the table is actually a combination of the three values: < hash, key, value >. This is implemented as a C struct (see dictobject.h:51-56).

    The figure below is a logical representation of a Python hash table. In the figure below, 0, 1, ..., i, ... on the left are indices of the slots in the hash table (they are just for illustrative purposes and are not stored along with the table obviously!).

      # Logical model of Python Hash table
      -+-----------------+
      0| <hash|key|value>|
      -+-----------------+
      1|      ...        |
      -+-----------------+
      .|      ...        |
      -+-----------------+
      i|      ...        |
      -+-----------------+
      .|      ...        |
      -+-----------------+
      n|      ...        |
      -+-----------------+

    When a new dict is initialized it starts with 8 slots. (see dictobject.h:49)

    When adding entries to the table, we start with some slot, i, that is based on the hash of the key. CPython initially uses i = hash(key) & mask (where mask = PyDictMINSIZE - 1, but that's not really important). Just note that the initial slot, i, that is checked depends on the hash of the key.

    If that slot is empty, the entry is added to the slot (by entry, I mean, <hash|key|value>). But what if that slot is occupied!? Most likely because another entry has the same hash (hash collision!)

    If the slot is occupied, CPython (and even PyPy) compares the hash AND the key (by compare I mean == comparison not the is comparison) of the entry in the slot against the hash and key of the current entry to be inserted (dictobject.c:337,344-345) respectively. If both match, then it thinks the entry already exists, gives up and moves on to the next entry to be inserted. If either hash or the key don't match, it starts probing.

    Probing just means it searches the slots by slot to find an empty slot. Technically we could just go one by one, i+1, i+2, ... and use the first available one (that's linear probing). But for reasons explained beautifully in the comments (see dictobject.c:33-126), CPython uses random probing. In random probing, the next slot is picked in a pseudo random order. The entry is added to the first empty slot. For this discussion, the actual algorithm used to pick the next slot is not really important (see dictobject.c:33-126 for the algorithm for probing). What is important is that the slots are probed until first empty slot is found.

    The same thing happens for lookups, just starts with the initial slot i (where i depends on the hash of the key). If the hash and the key both don't match the entry in the slot, it starts probing, until it finds a slot with a match. If all slots are exhausted, it reports a fail.

    BTW, the dict will be resized if it is two-thirds full. This avoids slowing down lookups. (see dictobject.h:64-65)

NOTE: I did the research on Python Dict implementation in response to my own question about how multiple entries in a dict can have same hash values. I posted a slightly edited version of the response here because all the research is very relevant for this question as well.
# Memory-usage of dictionary in Python?
https://stackoverflow.com/questions/6579757/memory-usage-of-dictionary-in-python
Compute Memory footprint of an object and its contents (Python recipe) 
https://code.activestate.com/recipes/577504/
```python
from __future__ import print_function
from sys import getsizeof, stderr
from itertools import chain
from collections import deque
try:
    from reprlib import repr
except ImportError:
    pass

def total_size(o, handlers={}, verbose=False):
    """ Returns the approximate memory footprint an object and all of its contents.

    Automatically finds the contents of the following builtin containers and
    their subclasses:  tuple, list, deque, dict, set and frozenset.
    To search other containers, add handlers to iterate over their contents:

        handlers = {SomeContainerClass: iter,
                    OtherContainerClass: OtherContainerClass.get_elements}

    """
    dict_handler = lambda d: chain.from_iterable(d.items())
    all_handlers = {tuple: iter,
                    list: iter,
                    deque: iter,
                    dict: dict_handler,
                    set: iter,
                    frozenset: iter,
                   }
    all_handlers.update(handlers)     # user handlers take precedence
    seen = set()                      # track which object id's have already been seen
    default_size = getsizeof(0)       # estimate sizeof object without __sizeof__

    def sizeof(o):
        if id(o) in seen:       # do not double count the same object
            return 0
        seen.add(id(o))
        s = getsizeof(o, default_size)

        if verbose:
            print(s, type(o), repr(o), file=stderr)

        for typ, handler in all_handlers.items():
            if isinstance(o, typ):
                s += sum(map(sizeof, handler(o)))
                break
        return s

    return sizeof(o)


##### Example call #####

if __name__ == '__main__':
    d = dict(a=1, b=2, c=3, d=[4,5,6,7], e='a string of chars')
    print(total_size(d, verbose=True))

```
# can't login to aics github, login prompt doesn't pop up
clean history, cookie, and cache
https://support.mozilla.org/en-US/kb/fix-login-issues-on-websites-require-passwords 

# Integrity Confidentiality Authenticity
https://security.stackexchange.com/questions/148173/authenticity-confidentiality-integrity-general-questions
Integrity: Integrity is used to make sure that nobody in between site A and B (for example) changed some parts of the shared information. Therefore a hash is calculated and added to a packet. This can be achieved by using hashing algorithms like MD5, SHA(1,2) and so on. To really make sure that no one is even able to modify the hash HMACs are used. This stands for hashed message authentication code. The main difference between a hash and a hmac is that in addition to the value that should be hashed (checksum calculated) a secret passphrase that is common to both sites is added to the calculation process. E.g. [Value that should be hashed] + [secret passhrase] -> Hashed value of this "two" inputs. Here comes my first question: Can this be compared with a "salt"? Or what exactly is the difference between a HMAC and a Hash + Salt? And what is Pepper, if a Hash + Salt equals a HMAC?

Confidentiality: Confidentiality is used to make sure that nobody in between site A and B is able to read what data or information is sent between the to sites. To achieve this encryption algorithms are used. There are two kinds of encryption algorithms, symmetric and also asymmetric ones. Symmetric algorithms allow encryption and decryption with the same key. With asymmetric algorithms you have to kinds of keys: a public one and also a private one. The public key is often available to the public while the private key is just available for "yourself" (if the mentioned keypair is yours). Everything that you encrypt with the public key can only be decrypted with the private one and vice versa. When it comes to confidentiality you often just use symmetric algorithms like DES, 3DES (both outdated) or AES. Asymmetric encryption is used to transfer a symmetric key and also to make sure that the other site is really who it seems to be (when it comes to SSL/TLS).

Authenticity: And this last sentence of the confidentiality part leads directly to the authenticity part. Authenticity is used to make sure that you really communicate with the partner you want to. To achieve these different kinds of techniques can be used, e.g. Pre-shared keys that are configured on both sites, Elliptic Curves or RSA as public/private key algorithms. 
# vpn nyu vpn 
sudo openconnect vpn.nyu.edu
第一個密碼用2go加w
第二個用push
then confirm by DUO
# Add more color to the Python code of your Databricks notebook 
https://keestalkstech.com/2019/11/add-more-color-to-the-python-code-of-your-databricks-notebook/
# How do I resolve ExecutorLostFailure "Slave lost" errors in Spark on Amazon EMR?
https://aws.amazon.com/premiumsupport/knowledge-center/executorlostfailure-slave-lost-emr/
High disk utilization
Using Spot Instances for cluster nodes
Aggressive Amazon Elastic Compute Cloud (Amazon EC2) Auto Scaling policies
# mystery of pyspark
```python
21/03/15 06:03:50 ERROR TaskSchedulerImpl: Lost executor 163 on 10.139.64.28: worker decommissioned: Worker Decommissioned
21/03/15 06:03:50 ERROR TaskSchedulerImpl: Lost executor 171 on 10.139.64.18: worker decommissioned: Worker Decommissioned
21/03/15 06:03:50 ERROR TaskSchedulerImpl: Lost executor 189 on 10.139.64.26: worker decommissioned: Worker Decommissioned
21/03/15 06:03:50 ERROR TaskSchedulerImpl: Lost executor 190 on 10.139.64.16: worker decommissioned: Worker Decommissioned
21/03/15 06:03:50 ERROR TaskSchedulerImpl: Lost executor 192 on 10.139.64.6: worker decommissioned: Worker Decommissioned
21/03/15 06:03:50 ERROR TaskSchedulerImpl: Lost executor 193 on 10.139.64.22: worker decommissioned: Worker Decommissioned
21/03/15 06:03:50 ERROR TaskSchedulerImpl: Lost executor 194 on 10.139.64.12: worker decommissioned: Worker Decommissioned
21/03/15 06:03:50 ERROR TaskSchedulerImpl: Lost executor 196 on 10.139.64.30: worker decommissioned: Worker Decommissioned
21/03/15 06:06:20 ERROR TaskSchedulerImpl: Lost executor 191 on 10.139.64.23: worker decommissioned: Worker Decommissioned
21/03/15 06:06:20 ERROR TaskSchedulerImpl: Lost executor 195 on 10.139.64.14: worker decommissioned: Worker Decommissioned
21/03/15 06:06:20 ERROR TaskSchedulerImpl: Lost executor 197 on 10.139.64.29: worker decommissioned: Worker Decommissioned
21/03/15 06:16:59 ERROR TaskSchedulerImpl: Lost executor 166 on 10.139.64.25: Remote RPC client disassociated. Likely due to containers exceeding thresholds, or network issues. Check driver logs for WARN messages.
21/03/15 06:17:59 ERROR TaskSchedulerImpl: Lost executor 137 on 10.139.64.32: Remote RPC client disassociated. Likely due to containers exceeding thresholds, or network issues. Check driver logs for WARN messages.
21/03/15 06:17:59 ERROR TaskSchedulerImpl: Lost executor 142 on 10.139.64.17: Remote RPC client disassociated. Likely due to containers exceeding thresholds, or network issues. Check driver logs for WARN messages.
21/03/15 06:17:59 ERROR TaskSchedulerImpl: Lost executor 157 on 10.139.64.15: Remote RPC client disassociated. Likely due to containers exceeding thresholds, or network issues. Check driver logs for WARN messages.
21/03/15 06:17:59 ERROR TaskSchedulerImpl: Lost executor 158 on 10.139.64.24: Remote RPC client disassociated. Likely due to containers exceeding thresholds, or network issues. Check driver logs for WARN messages.
21/03/15 06:17:59 ERROR TaskSchedulerImpl: Lost executor 159 on 10.139.64.31: Remote RPC client disassociated. Likely due to containers exceeding thresholds, or network issues. Check driver logs for WARN messages.
21/03/15 06:17:59 ERROR TaskSchedulerImpl: Lost executor 160 on 10.139.64.20: Remote RPC client disassociated. Likely due to containers exceeding thresholds, or network issues. Check driver logs for WARN messages.
21/03/15 06:17:59 ERROR TaskSchedulerImpl: Lost executor 161 on 10.139.64.10: Remote RPC client disassociated. Likely due to containers exceeding thresholds, or network issues. Check driver logs for WARN messages.
21/03/15 06:17:59 ERROR TaskSchedulerImpl: Lost executor 162 on 10.139.64.11: Remote RPC client disassociated. Likely due to containers exceeding thresholds, or network issues. Check driver logs for WARN messages.
21/03/15 06:17:59 ERROR TaskSchedulerImpl: Lost executor 164 on 10.139.64.37: Remote RPC client disassociated. Likely due to containers exceeding thresholds, or network issues. Check driver logs for WARN messages.
21/03/15 06:29:10 ERROR TaskSchedulerImpl: Lost executor 198 on 10.139.64.25: worker decommissioned: Worker Decommissioned
21/03/15 06:29:10 ERROR TaskSchedulerImpl: Lost executor 199 on 10.139.64.24: worker decommissioned: Worker Decommissioned
21/03/15 06:29:10 ERROR TaskSchedulerImpl: Lost executor 200 on 10.139.64.15: worker decommissioned: Worker Decommissioned
21/03/15 06:29:10 ERROR TaskSchedulerImpl: Lost executor 201 on 10.139.64.11: worker decommissioned: Worker Decommissioned
21/03/15 06:29:10 ERROR TaskSchedulerImpl: Lost executor 202 on 10.139.64.20: worker decommissioned: Worker Decommissioned
21/03/15 06:29:10 ERROR TaskSchedulerImpl: Lost executor 203 on 10.139.64.10: worker decommissioned: Worker Decommissioned
21/03/15 06:29:10 ERROR TaskSchedulerImpl: Lost executor 204 on 10.139.64.17: worker decommissioned: Worker Decommissioned
21/03/15 06:29:10 ERROR TaskSchedulerImpl: Lost executor 205 on 10.139.64.31: worker decommissioned: Worker Decommissioned
21/03/15 06:29:10 ERROR TaskSchedulerImpl: Lost executor 206 on 10.139.64.32: worker decommissioned: Worker Decommissioned
21/03/15 06:29:10 ERROR TaskSchedulerImpl: Lost executor 207 on 10.139.64.37: worker decommissioned: Worker Decommissioned
21/03/15 06:31:40 ERROR TaskSchedulerImpl: Lost executor 208 on 10.139.64.23: worker decommissioned: Worker Decommissioned
21/03/15 06:31:40 ERROR TaskSchedulerImpl: Lost executor 209 on 10.139.64.16: worker decommissioned: Worker Decommissioned
21/03/15 06:31:40 ERROR TaskSchedulerImpl: Lost executor 210 on 10.139.64.28: worker decommissioned: Worker Decommissioned
21/03/15 06:31:40 ERROR TaskSchedulerImpl: Lost executor 211 on 10.139.64.22: worker decommissioned: Worker Decommissioned
21/03/15 06:31:40 ERROR TaskSchedulerImpl: Lost executor 212 on 10.139.64.14: worker decommissioned: Worker Decommissioned
21/03/15 06:31:40 ERROR TaskSchedulerImpl: Lost executor 214 on 10.139.64.29: worker decommissioned: Worker Decommissioned
21/03/15 06:43:25 ERROR TaskSchedulerImpl: Lost executor 213 on 10.139.64.26: worker decommissioned: Worker Decommissioned
21/03/15 06:43:25 ERROR TaskSchedulerImpl: Lost executor 215 on 10.139.64.12: worker decommissioned: Worker Decommissioned
21/03/15 06:43:25 ERROR TaskSchedulerImpl: Lost executor 216 on 10.139.64.18: worker decommissioned: Worker Decommissioned
21/03/15 06:43:25 ERROR TaskSchedulerImpl: Lost executor 217 on 10.139.64.30: worker decommissioned: Worker Decommissioned
21/03/15 06:43:25 ERROR TaskSchedulerImpl: Lost executor 218 on 10.139.64.33: worker decommissioned: Worker Decommissioned
21/03/15 06:43:25 ERROR TaskSchedulerImpl: Lost executor 219 on 10.139.64.44: worker decommissioned: Worker Decommissioned
21/03/15 06:43:25 ERROR TaskSchedulerImpl: Lost executor 220 on 10.139.64.41: worker decommissioned: Worker Decommissioned
```

```python
device_id_map
ad_id_map
lc_map
cookie_map
user_id_map

"device_id_map",
"ad_id_map",
"lc_map",
"cookie_map",
"user_id_map",

  print('app_device_id', res.where("app_device_id is NULL").count())
  print('app_advertising_id', res.where("app_advertising_id is NULL").count())
  print('local_cookie_id', res.where("local_cookie_id is NULL").count())
  print('cookie_id', res.where("cookie_id is NULL").count())
  print('user_id', res.where("user_id is NULL").count())
```

03 start XDD
XDD, before, null count
app_device_id 12246371
app_advertising_id 12237957
local_cookie_id 1104582
cookie_id 4979856
user_id 13881832
app_device_id 147148 147148
app_advertising_id 147175 145253
local_cookie_id 567940 567940
cookie_id 567951 566351
user_id 714983 58033
app_device_id
app_advertising_id
local_cookie_id
cookie_id
user_id
XDD, AFTER, null count
app_device_id 12246371
app_advertising_id 12237957
local_cookie_id 1104582
cookie_id 4979856
user_id 13881832

```python
import sys

sys.path.append('/dbfs/mnt/XXXdev/XXata-branch/model/integrate_app_a_month/XXX-data-analytics/')

from etl.utils.safe_operator import safe_union
from etl.utils.column_operator import recode

import pyspark.sql.functions as F
from pyspark.sql.types import StringType

from pyspark.sql.session import SparkSession

spark = SparkSession.builder.getOrCreate()
spark.sparkContext.setLogLevel("ERROR")

second_XXXmall = \
spark.read.format('parquet').\
load('dbfs:/mnt/XXXdev/personal/shared/replace_all_id_evaluation/XXX_fake_id_mapping_table__sec_test/').\
withColumn('source', F.when((F.col("type") == "android") | (F.col("type") == "ios"), "app").otherwise("web")).\
withColumn('bu', F.lit('XXmall')).\
select('source', 'bu', 'identify_id', 'fake_local_cookie_id', 'fake_cookie_id', 'fake_user_id', 'fake_device_id', 'fake_advertising_id')

second_XXXtoday = \
spark.read.format('parquet').\
load('dbfs:/mnt/XXX2dev/personal/shared/replace_all_id_evaluation/XXXtoday_fake_id_mapping_table__sec_test/').\
withColumn('source', F.when((F.col("type") == "android") | (F.col("type") == "ios"), "app").otherwise("web")).\
withColumn('bu', F.lit('XXXtoday')).\
select('source', 'bu', 'identify_id', 'fake_local_cookie_id', 'fake_cookie_id', 'fake_user_id', 'fake_device_id', 'fake_advertising_id')

first_XXXmall = \
spark.read.format('parquet').\
load('dbfs:/mnt/XXXdev/personal/shared/replace_all_id_evaluation/evaluation_result_XXXmall_s2_first_test_id_mapping_table/').\
withColumn('source', F.when((F.col("type") == "android") | (F.col("type") == "ios"), "app").otherwise("web")).\
withColumn('bu', F.lit('XXXtoday')).\
withColumnRenamed('fake_locak_cookie_id', 'fake_local_cookie_id').\
select('source', 'bu', 'identify_id', 'fake_local_cookie_id', 'fake_cookie_id', 'fake_user_id', 'fake_device_id', 'fake_advertising_id')


fake_data = \
safe_union(safe_union(second_XXXmall, second_XXXtoday), first_XXXmall).withColumn("fake_user_id",F.col('fake_user_id').cast(StringType()))

 

def working_fun(my_dict):
    def f(x):
        return my_dict.get(x,x)
    return F.udf(f)

####
for d in ['ALL']:
  print(d, "start XDD")
  
  feb_data = \
  spark.read.format('delta').\
  load('dbfs:/mnt/XXXdev/XXXdata-v5-prod/delta/XXX_id_optimize_v2/').\
  filter(F.col('month')=='02')
  
  print("XDD, before, null count")
  a1=feb_data.where("app_device_id is NULL").count()
  a2=feb_data.where("app_advertising_id is NULL").count()
  a3=feb_data.where("local_cookie_id is NULL").count()
  a4=feb_data.where("cookie_id is NULL").count()
  a5=feb_data.where("user_id is NULL").count()
  print('app_device_id', a1)
  print('app_advertising_id', a2)
  print('local_cookie_id', a3)
  print('cookie_id', a4)
  print('user_id', a5)
  print("++++++++")
    
  device_id_map = \
  fake_data.\
  filter(F.col('source')=='app').\
  drop('source').\
  withColumnRenamed('identify_id', 'app_device_id').\
  join(feb_data.\
       filter(F.col('source')=='app'),
       ['bu', 'app_device_id']).\
  select('fake_device_id', 'app_device_id').\
  toPandas().\
  set_index('fake_device_id')['app_device_id'].\
  to_dict()
  
  print('app_device_id:: ', len(set(device_id_map.keys())),
        len(set(device_id_map.values())), len(set(device_id_map.keys()))-
        len(set(device_id_map.values())))

  ad_id_map = \
  fake_data.\
  filter(F.col('source')=='app').\
  drop('source').\
  withColumnRenamed('identify_id', 'app_device_id').\
  join(feb_data.\
       filter(F.col('source')=='app'),
       ['bu', 'app_device_id']).\
  select('fake_advertising_id', 'app_advertising_id').\
  toPandas().\
  set_index('fake_advertising_id')['app_advertising_id'].\
  to_dict()
  
  print('app_advertising_id:: ', len(set(ad_id_map.keys())),
        len(set(ad_id_map.values())), len(set(ad_id_map.keys()))-
        len(set(ad_id_map.values())))

  lc_map = \
  fake_data.\
  filter(F.col('source')=='web').\
  drop('source').\
  withColumnRenamed('identify_id', 'local_cookie_id').\
  join(feb_data.\
       filter(F.col('source')=='web'),
       ['bu', 'local_cookie_id']).\
  select('fake_local_cookie_id', 'local_cookie_id').\
  toPandas().\
  set_index('fake_local_cookie_id')['local_cookie_id'].\
  to_dict()
  
  print('local_cookie_id:: ', len(set(lc_map.keys())),
        len(set(lc_map.values())), len(set(lc_map.keys()))-
        len(set(lc_map.values())))

  cookie_map = \
  fake_data.\
  filter(F.col('source')=='web').\
  drop('source').\
  withColumnRenamed('identify_id', 'local_cookie_id').\
  join(feb_data.\
       filter(F.col('source')=='web'),
       ['bu', 'local_cookie_id']).\
  select('fake_cookie_id', 'cookie_id').\
  toPandas().\
  set_index('fake_cookie_id')['cookie_id'].\
  to_dict()
  
  print('cookie_id:: ', len(set(cookie_map.keys())),
        len(set(cookie_map.values())), len(set(cookie_map.keys()))-
        len(set(cookie_map.values())))

  user_id_map = \
  safe_union(fake_data.\
  filter(F.col('source')=='web').\
  drop('source').\
  withColumnRenamed('identify_id', 'local_cookie_id').\
  join(feb_data.\
       filter(F.col('source')=='web'),
       ['bu', 'local_cookie_id']).\
  select('fake_user_id', 'user_id'),
             fake_data.\
  filter(F.col('source')=='app').\
  drop('source').\
  withColumnRenamed('identify_id', 'app_device_id').\
  join(feb_data.\
       filter(F.col('source')=='app'),
       ['bu', 'app_device_id']).\
  select('fake_user_id', 'user_id')).\
  toPandas().\
  set_index('fake_user_id')['user_id'].\
  to_dict()
  
  print('user_id:: ', len(set(user_id_map.keys())),
        len(set(user_id_map.values())), len(set(user_id_map.keys()))-
        len(set(user_id_map.values())))
  
  print("========")
  
  # get all dict

  # use udf to take dict
  feb_data = feb_data.withColumn('app_device_id', working_fun(device_id_map)(F.col('app_device_id')))\
                    .withColumn('app_advertising_id', working_fun(ad_id_map)(F.col('app_advertising_id')))\
                    .withColumn('local_cookie_id', working_fun(lc_map)(F.col('local_cookie_id')))\
                    .withColumn('cookie_id', working_fun(cookie_map)(F.col('cookie_id')))\
                    .withColumn('user_id', working_fun(user_id_map)(F.col('user_id')))

  
  # after 
  print("XDD, QQQQ, AFTER, null count")
  b1=feb_data.where("app_device_id is NULL").count()
  b2=feb_data.where("app_advertising_id is NULL").count()
  b3=feb_data.where("local_cookie_id is NULL").count()
  b4=feb_data.where("cookie_id is NULL").count()
  b5=feb_data.where("user_id is NULL").count()
  print('app_device_id', b1)
  print('app_advertising_id', b2)
  print('local_cookie_id', b3)
  print('cookie_id', b4)
  print('user_id', b5)
  print("QWQ xxxxxxxx")
  print('app_device_id', b1-a1)
  print('app_advertising_id', b2-a2)
  print('local_cookie_id', b3-a3)
  print('cookie_id', b4-a4)
  print('user_id', b5-a5)
  
  # disp to check
#   display(feb_data)
#   display(feb_data.groupBy('year','month','day').count())
  
  # write
  feb_data.write.format("delta").option("mergeSchema", "true").mode("overwrite").\
  partitionBy(['source','bu','year','month','day']).\
  save("dbfs:/mnt/XXXdev/personal/eugene/recovered_feb"+d)
  
  # load to disp to check
#   display(spark.read.format('delta').\
#   load("dbfs:/mnt/XXXdev/personal/eugene/recovered_feb"+d).\
#   groupBy('year','month','day').\
#   count())
  
  print(d, "finish XDD")

####
```
```python

for d in ['03','04','05','06','07','08','09','10','11','19','20','21','22','23']:
  print(d, "start XDD")
  
  feb_data = \
  spark.read.format('delta').\
  load('dbfs:/mnt/XXXdev/XXXdata-v5-prod/delta/kg_id_optimize_v2/').\
  filter(F.col('month')=='02').filter(F.col('day')==d)
  
  print("XDD, before, null count")
  a1=feb_data.where("app_device_id is NULL").count()
  a2=feb_data.where("app_advertising_id is NULL").count()
  a3=feb_data.where("local_cookie_id is NULL").count()
  a4=feb_data.where("cookie_id is NULL").count()
  a5=feb_data.where("user_id is NULL").count()
  print('app_device_id', a1)
  print('app_advertising_id', a2)
  print('local_cookie_id', a3)
  print('cookie_id', a4)
  print('user_id', a5)
  print("++++++++")
    
  device_id_map = \
  fake_data.\
  filter(F.col('source')=='app').\
  drop('source').\
  withColumnRenamed('identify_id', 'app_device_id').\
  join(feb_data.\
       filter(F.col('source')=='app'),
       ['bu', 'app_device_id']).\
  select('fake_device_id', 'app_device_id').\
  toPandas().\
  set_index('fake_device_id')['app_device_id'].\
  to_dict()
  
  print('app_device_id:: ', len(set(device_id_map.keys())),
        len(set(device_id_map.values())), len(set(device_id_map.keys()))-
        len(set(device_id_map.values())))

  ad_id_map = \
  fake_data.\
  filter(F.col('source')=='app').\
  drop('source').\
  withColumnRenamed('identify_id', 'app_device_id').\
  join(feb_data.\
       filter(F.col('source')=='app'),
       ['bu', 'app_device_id']).\
  select('fake_advertising_id', 'app_advertising_id').\
  toPandas().\
  set_index('fake_advertising_id')['app_advertising_id'].\
  to_dict()
  
  print('app_advertising_id:: ', len(set(ad_id_map.keys())),
        len(set(ad_id_map.values())), len(set(ad_id_map.keys()))-
        len(set(ad_id_map.values())))

  lc_map = \
  fake_data.\
  filter(F.col('source')=='web').\
  drop('source').\
  withColumnRenamed('identify_id', 'local_cookie_id').\
  join(feb_data.\
       filter(F.col('source')=='web'),
       ['bu', 'local_cookie_id']).\
  select('fake_local_cookie_id', 'local_cookie_id').\
  toPandas().\
  set_index('fake_local_cookie_id')['local_cookie_id'].\
  to_dict()
  
  print('local_cookie_id:: ', len(set(lc_map.keys())),
        len(set(lc_map.values())), len(set(lc_map.keys()))-
        len(set(lc_map.values())))

  cookie_map = \
  fake_data.\
  filter(F.col('source')=='web').\
  drop('source').\
  withColumnRenamed('identify_id', 'local_cookie_id').\
  join(feb_data.\
       filter(F.col('source')=='web'),
       ['bu', 'local_cookie_id']).\
  select('fake_cookie_id', 'cookie_id').\
  toPandas().\
  set_index('fake_cookie_id')['cookie_id'].\
  to_dict()
  
  print('cookie_id:: ', len(set(cookie_map.keys())),
        len(set(cookie_map.values())), len(set(cookie_map.keys()))-
        len(set(cookie_map.values())))

  user_id_map = \
  safe_union(fake_data.\
  filter(F.col('source')=='web').\
  drop('source').\
  withColumnRenamed('identify_id', 'local_cookie_id').\
  join(feb_data.\
       filter(F.col('source')=='web'),
       ['bu', 'local_cookie_id']).\
  select('fake_user_id', 'user_id'),
             fake_data.\
  filter(F.col('source')=='app').\
  drop('source').\
  withColumnRenamed('identify_id', 'app_device_id').\
  join(feb_data.\
       filter(F.col('source')=='app'),
       ['bu', 'app_device_id']).\
  select('fake_user_id', 'user_id')).\
  toPandas().\
  set_index('fake_user_id')['user_id'].\
  to_dict()
  
  print('user_id:: ', len(set(user_id_map.keys())),
        len(set(user_id_map.values())), len(set(user_id_map.keys()))-
        len(set(user_id_map.values())))
  
  print("========")
  
  # get all dict

  # use udf to take dict
  feb_data = feb_data.withColumn('app_device_id', working_fun(device_id_map)(F.col('app_device_id')))\
                    .withColumn('app_advertising_id', working_fun(ad_id_map)(F.col('app_advertising_id')))\
                    .withColumn('local_cookie_id', working_fun(lc_map)(F.col('local_cookie_id')))\
                    .withColumn('cookie_id', working_fun(cookie_map)(F.col('cookie_id')))\
                    .withColumn('user_id', working_fun(user_id_map)(F.col('user_id')))

  
  # after 
  print("XDD, QQQQ, AFTER, null count")
  b1=feb_data.where("app_device_id is NULL").count()
  b2=feb_data.where("app_advertising_id is NULL").count()
  b3=feb_data.where("local_cookie_id is NULL").count()
  b4=feb_data.where("cookie_id is NULL").count()
  b5=feb_data.where("user_id is NULL").count()
  print('app_device_id', b1)
  print('app_advertising_id', b2)
  print('local_cookie_id', b3)
  print('cookie_id', b4)
  print('user_id', b5)
  print("QWQ xxxxxxxx")
  print('app_device_id', b1-a1)
  print('app_advertising_id', b2-a2)
  print('local_cookie_id', b3-a3)
  print('cookie_id', b4-a4)
  print('user_id', b5-a5)
  
  # disp to check
#   display(feb_data)
#   display(feb_data.groupBy('year','month','day').count())
  
  # write
  feb_data.write.format("delta").option("mergeSchema", "true").mode("overwrite").\
  partitionBy(['source','bu','year','month','day']).\
  save("dbfs:/mnt/XXXdev/personal/eugene/recovered_feb"+d)
  
  # load to disp to check
#   display(spark.read.format('delta').\
#   load("dbfs:/mnt/XXXdev/personal/eugene/recovered_feb"+d).\
#   groupBy('year','month','day').\
#   count())
  
  print(d, "finish XDD")
  
```
```python
for d in ['03','04','05','06','07','08','09','10','11','19','20','21','22','23']:
  tmp=spark.read.format('delta').load("dbfs:/mnt/XXXdev/personal/eugene/recovered_feb"+d)\
  .write.format("delta").option("mergeSchema", "true").mode("append").\
  partitionBy(['source','bu','year','month','day']).save("dbfs:/mnt/XXXdev/XXXdata-e2e/model_20210305/delta/kg_id_optimize_v2/")
  
display(spark.read.format('delta').\
load("dbfs:/mnt/XXXdev/XXXdata-e2e/model_20210305/delta/kg_id_optimize_v2/").\
groupBy('year','month','day').\
count())

# before saving there are: 01 02 12 13 14 15 16 17 18; in Feb
```
# Faiss应用 - 召回框架  https://zhuanlan.zhihu.com/p/90768014
PaulC
PaulC
算法工程师

Faiss是为稠密向量提供高效相似度搜索的框架(Facebook AI Research），选择索引方式是faiss的核心内容，faiss 三个最常用的索引是：IndexFlatL2, IndexIVFFlat,IndexIVFPQ。

    IndexFlatL2/ IndexFlatIP为最基础的精确查找。应用样例：

user_vector_arr  # shape(526,066, 128)
gds_vector_arr   # shape(5,172, 128)
dim = 128# 向量维度
k = 10  # 定义召回向量个数
index = faiss.IndexFlatL2(dim)  # L2距离，即欧式距离（越小越好）
\# index=faiss.IndexFlatIP(dim) # 点乘，归一化的向量点乘即cosine相似度（越大越好）
index.add(gds_vector_arr) # 添加训练时的样本
D, I = index.search(user_vector_arr, k) # 寻找相似向量， I表示相似用户ID矩阵， D表示距离矩阵

2. IndexIVFFlat称为倒排文件索引，是使用K-means建立聚类中心，通过查询最近的聚类中心，比较聚类中的所有向量得到相似的向量，是一种加速搜索方法的索引。应用样例：

user_vector_arr  # shape(526,066, 128)
gds_vector_arr   # shape(5,172, 128)
dim = 128 # 向量维度
k = 10  # 定义召回向量个数
nlist = 100 #聚类中心的个数
quantizer = faiss.IndexFlatL2(dim)  # 定义量化器
index = faiss.IndexIVFFlat(quantizer, dim, nlist, faiss.METRIC_L2) #也可采用向量內积               
index.nprobe = 10 #查找聚类中心的个数，默认为1个，若nprobe=nlist则等同于精确查找
index.train(gds_vector_arr) #需要训练
index.add(gds_vector_arr) # 添加训练时的样本
D, I = index.search(user_vector_arr, k) # 寻找相似向量， I表示相似用户ID矩阵， D表示距离矩阵

3. IndexIVFPQ是一种减少内存的索引方式，IndexFlatL2和IndexIVFFlat都会全量存储所有的向量在内存中，面对大数据量，faiss提供一种基于Product Quantizer(乘积量化)的压缩算法编码向量到指定字节数来减少内存占用。但这种情况下，存储的向量是压缩过的，所以查询的距离也是近似的。应用样例：

user_vector_arr  # shape(526,066, 128)
gds_vector_arr   # shape(5,172, 128)
dim = 128 # 向量维度
k = 10  # 定义召回向量个数
nlist = 100  #聚类中心的个数
m = 8        # 压缩成8bits
quantizer = faiss.IndexFlatL2(dim) # 定义量化器  
index = faiss.IndexIVFPQ(quantizer, dim, nlist, m, 8)  # 8 specifies that each sub-vector is encoded as 8 bits
index.nprobe = 10 #查找聚类中心的个数，默认为1个，若nprobe=nlist则等同于精确查找
index.train(gds_vector_arr) #需要训练
index.add(gds_vector_arr) # 添加训练时的样本
D, I = index.search(user_vector_arr, k) # 寻找相似向量， I表示相似用户ID矩阵， D表示距离矩阵

4. index_factory是faiss实现的一个索引工厂模式,可以通过字符串来灵活的创建索引；PCA算法可将向量降到指定的维度。应用样例：

user_vector_arr  # shape(526,066, 128)
gds_vector_arr   # shape(5,172, 128)
dim = 128 # 向量维度
k = 10  # 定义召回向量个数
index = faiss.index_factory(dim, “PCAR32,IVF100,SQ8”)# PCA降到32位；搜索空间100；SQ8,scalar标量化，每个向量编码为8bit(1字节)
index.train(gds_vector_arr) #需要训练
index.add(gds_vector_arr) # 添加训练时的样本
D, I = index.search(user_vector_arr, k) # 寻找相似向量， I表示相似用户ID矩阵， D表示距离矩阵

\# 索引简写可查询：https://github.com/facebookresearch/faiss/wiki/Faiss-indexes

=>一般选用欧式距离，速度较快(KNN算法-KDTree? 处理高维向量 - BallTree?)；也可得到距离矩阵后转化为cosine(向量须为L2归一化后), 方便有用户商品对截断需求的阈值确定。

cosine = (2 - L2_Distance)/2

    官方文档：https://github.com/facebookresearch/faiss/wikihttps://blog.csdn.net/kanbuqinghuanyizhang/article/details/80774609https://zhuanlan.zhihu.com/p/40236865


编译安装：

    依赖库 – OpenBLAS 依赖库 – Lapack (yum install)安装swig & 环境配置 https://www.lizenghai.com/archives/29946.html安装faiss 手把手教你安装Faiss（Linux） (./configure --without-cuda)make py 然后 cd faiss/python 执行：python setup.py install

# windows powershell beautiful
* to set font
  * https://docs.microsoft.com/en-us/windows/terminal/tutorials/powerline-setup
* all themes
  * Get-PoshThemes
    * https://ohmyposh.dev/docs/themes/
* fonts
  * https://ohmyposh.dev/docs/fonts

# How did they ever come up with that kooky ‘Kubernetes’ name? Here’s the inside story
https://www.geekwire.com/2016/ever-come-kooky-kubernetes-name-heptio/
# apply a certificate for testing
https://letsencrypt.org/zh-tw/docs/staging-environment/
# k8s;; cert manager;; cert issuer
# use Helm to manager yaml files;; Helm Chart
can use variable etc
# acr
azure container registry
# `#!/bin/sh -e`
https://stackoverflow.com/questions/2936287/what-does-the-line-bin-sh-e-do
The -e flag's long name is errexit, causing the script to immediately exit on the first error. 
# Run terminal sudo command at startup
How to run a script during boot as root (7 answers)
Proper fstab entry to mount a samba share on boot? (2 answers) 
I need to run the following command at startup or upon login
https://askubuntu.com/questions/956237/run-terminal-sudo-command-at-startup

# apt install golang
https://askubuntu.com/questions/720260/updating-golang-on-ubuntu
First remove your current golang installation with this command, you don't need to manually remove files installed by apt-get,

sudo apt-get purge golang

For an easy install of golang 1.4 you can use this PPA

sudo add-apt-repository ppa:evarlast/golang1.4
sudo apt-get update

Now you can use

sudo apt-get install golang

# wget to install golang and add path by hand
```bash
wget https://golang.org/dl/go1.16.2.linux-amd64.tar.gz
rm -rf /usr/local/go && tar -C /usr/local -xzf go1.16.2.linux-amd64.tar.gz
echo "export PATH=\$PATH:/usr/local/go/bin" >>  /etc/profile
source  /etc/profile
go version
```
## where to add path
https://stackoverflow.com/questions/50554817/golang-installation
Add this line to your file /etc/profile, or better $HOME/.profile:
export PATH=$PATH:/usr/local/go/bin

# get wsl 2 // ref: 
check internet, if no, reboot
sudo apt update && sudo apt upgrade

# get minikube 
https://minikube.sigs.k8s.io/docs/start/
kubectl get node // list node

# noVNC
local to remote with gui

# apache druid on k8s on azure (aks=azure k8s service)

## [yet] deffer: this one uses helm 2, decrepted
https://medium.com/@aeli/apache-druid-setup-monitoring-and-auto-scaling-on-kubernetes-91739e350fac


## [?? 8080???] try splunk druid-operator in aks
https://github.com/druid-io/druid-operator/blob/master/docs/getting_started.md

git clone
cd into dir


kubectl create namespace druid-operator
helm -n druid-operator install cluster-druid-operator ./chart

### example of log output form splunk
https://www.slideshare.net/implydata/splunk-druid-on-kubernetes-with-druidoperator

### get into the druid service gui???
Check the Router URL ???

On the Kubernetes cluster, port forward the Druid router service using this command and open http://127.0.0.1:8080 in the browser

kubectl port-forward svc/druid-router 8080:8888

### note for cloud shell
```
azure portal ==> cloud shell // databricks notebook is not a terminal, some commands will fail, but we can sudo // cloud shell can't sudo QQ
az login // use azure cli (az) to login your azure accout
az account set --subscription xxxxxxxxxxxx  // login deeper
az aks get-credentials --resource-group kg-one-id-deploy-dev --name kg-aks-druid-dev // login deeper
kubectl create namespace druid-operator
kubectl get nodes // list nodes // cloud shell has installed kubectl for us
    // install go // no need for cloud shell
    // method 1: https://golang.org/doc/install + https://stackoverflow.com/questions/50554817/golang-installation // if you can't a `.profile`
    // method 2: https://askubuntu.com/questions/720260/updating-golang-on-ubuntu
git clone https://github.com/druid-io/druid-operator.git

cd druid-operator
helm -n druid-operator install cluster-druid-operator ./chart
kubectl apply -f examples/tiny-cluster-zk.yaml
make run
```
### get druid-operator pod name
```
druid-operator$ kubectl get po | grep druid-operator
```
### check druid-operator pod logs
```
druid-operator$ kubectl logs <druid-operator pod name>
```
### check the druid spec
druid-operator$ kubectl describe druids tiny-cluster
###  check if druid cluster is deployed
druid-operator$ kubectl get svc | grep tiny
druid-operator$ kubectl get cm | grep tiny
druid-operator$ kubectl get sts | grep tiny
### 8080 occupied 
```
2021-03-19T14:31:10.714Z        ERROR   controller-runtime.metrics      metrics server failed to listen. You may want to disable the metrics server or use another port if it is due to conflicts     {"error": "error listening on :8080: listen tcp :8080: bind: address already in use"}
github.com/go-logr/zapr.(*zapLogger).Error
        /home/eugene/go/pkg/mod/github.com/go-logr/zapr@v0.1.0/zapr.go:128
sigs.k8s.io/controller-runtime/pkg/metrics.NewListener
        /home/eugene/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.6.0/pkg/metrics/listener.go:48
sigs.k8s.io/controller-runtime/pkg/manager.New
        /home/eugene/go/pkg/mod/sigs.k8s.io/controller-runtime@v0.6.0/pkg/manager/manager.go:302
main.main
        /home/eugene/druid-operator/main.go:41
runtime.main
        /usr/local/go/src/runtime/proc.go:203
2021-03-19T14:31:10.714Z        ERROR   setup   unable to start manager {"error": "error listening on :8080: listen tcp :8080: bind: address already in use"}
github.com/go-logr/zapr.(*zapLogger).Error
        /home/eugene/go/pkg/mod/github.com/go-logr/zapr@v0.1.0/zapr.go:128
main.main
        /home/eugene/druid-operator/main.go:50
runtime.main
        /usr/local/go/src/runtime/proc.go:203
exit status 1
make: *** [Makefile:26: run] Error 1
```
###  check ports, without sudo or su
netstat -an --tcp --program  //  check port w/o sudo
forget to record output GG

### not sure whether druid operator provide gui??????

set a non-splunk druid @u5 to observe/play, get the gui endpoint
set a splunk druid-operator @u5 to observe/play, get the gui endpoint 
// make sure I am all correct with druid-operator @u5

set a splunk druid-operator @aks to observe/play, get the gui endpoint


## [GG] [their private hub]~~a hopeful github repo !!! Zenatix-Tech~~ GG
Note that Helm 2 is deprecated. The `stable` and `incubator` repos have been de-listed from the Helm Hub.
Using https://github.com/Zenatix-Tech/Druid-Kubernetes
```bash=
git clone https://github.com/Zenatix-Tech/Druid-Kubernetes
cd Druid-Kubernetes
helm repo add bitnami https://charts.bitnami.com/bitnami
kubectl create namespace druid
helm install dz -f k8s/zookeeper-values.yaml --namespace druid bitnami/zookeeper
```
> ```
> NAME: dz
> LAST DEPLOYED: Mon Mar 22 15:12:40 2021
> NAMESPACE: druid
> STATUS: deployed
> REVISION: 1
> TEST SUITE: None
> NOTES:
> ** Please be patient while the chart is being deployed **
> 
> ZooKeeper can be accessed via port 2181 on the following DNS name from within your cluster:
> 
> dz-zookeeper.druid.svc.cluster.local
> 
> To connect to your ZooKeeper server run the following commands:
> 
> export POD_NAME=$(kubectl get pods --namespace druid -l "app.kubernetes.io/name=zookeeper,app.kubernetes.io/instance=dz,app.kubernetes.io/component=zookeeper" -o jsonpath="{.items[0].metadata.name}")
> kubectl exec -it $POD_NAME -- zkCli.sh
> 
> To connect to your ZooKeeper server from outside the cluster execute the following commands:
> 
> kubectl port-forward --namespace druid svc/dz-zookeeper 2181:2181 &
> zkCli.sh 127.0.0.1:2181
> ```
```bash=
helm upgrade dz -f k8s/zookeeper-values.yaml --namespace druid bitnami/zookeeper
```
> ```
> Release "dz" has been upgraded. Happy Helming!
> NAME: dz
> LAST DEPLOYED: Mon Mar 22 15:13:30 2021
> NAMESPACE: druid
> STATUS: deployed
> REVISION: 2
> TEST SUITE: None
> NOTES:
> ** Please be patient while the chart is being deployed **
> 
> ZooKeeper can be accessed via port 2181 on the following DNS name from within your cluster:
> 
>     dz-zookeeper.druid.svc.cluster.local
> 
> To connect to your ZooKeeper server run the following commands:
> 
>     export POD_NAME=$(kubectl get pods --namespace druid -l "app.kubernetes.io/name=zookeeper,app.kubernetes.io/instance=dz,app.kubernetes.io/component=zookeeper" -o jsonpath="{.items[0].metadata.name}")
>     kubectl exec -it $POD_NAME -- zkCli.sh
> 
> To connect to your ZooKeeper server from outside the cluster execute the following commands:
> 
>     kubectl port-forward --namespace druid svc/dz-zookeeper 2181:2181 &
>     zkCli.sh 127.0.0.1:2181
> ```
```bash=
helm install dpg -f k8s/postgresql-values.yaml --namespace druid bitnami/postgresql
```
> ```
> coalesce.go:196: warning: cannot overwrite table with non table for tls (map[])
> coalesce.go:196: warning: cannot overwrite table with non table for tls (map[])
> NAME: dpg
> LAST DEPLOYED: Mon Mar 22 15:41:07 2021
> NAMESPACE: druid
> STATUS: deployed
> REVISION: 1
> TEST SUITE: None
> NOTES:
> ** Please be patient while the chart is being deployed **
> 
> PostgreSQL can be accessed via port 5432 on the following DNS name from within your cluster:
> 
>     dpg-postgresql.druid.svc.cluster.local - Read/Write connection
> 
> To get the password for "postgres" run:
> 
>     export POSTGRES_PASSWORD=$(kubectl get secret --namespace druid dpg-postgresql -o jsonpath="{.data.postgresql-password}" | base64 --decode)
> 
> To connect to your database run the following command:
> 
>     kubectl run dpg-postgresql-client --rm --tty -i --restart='Never' --namespace druid --image docker.io/bitnami/postgresql:11.5.0-debian-9-r84 --env="PGPASSWORD=$POSTGRES_PASSWORD" --command -- psql --host dpg-postgresql -U postgres -d druid -p 5432
> 
> 
> 
> To connect to your database from outside the cluster execute the following commands:
> 
>     kubectl port-forward --namespace druid svc/dpg-postgresql 5432:5432 &
>     PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d druid -p 5432
> ```
```bash=
helm upgrade dpg -f k8s/postgresql-values.yaml --namespace druid bitnami/postgresql
```
> ```
> coalesce.go:196: warning: cannot overwrite table with non table for tls (map[])
> coalesce.go:196: warning: cannot overwrite table with non table for tls (map[])
> Release "dpg" has been upgraded. Happy Helming!
> NAME: dpg
> LAST DEPLOYED: Mon Mar 22 15:41:59 2021
> NAMESPACE: druid
> STATUS: deployed
> REVISION: 2
> TEST SUITE: None
> NOTES:
> ** Please be patient while the chart is being deployed **
> 
> PostgreSQL can be accessed via port 5432 on the following DNS name from within your cluster:
> 
>     dpg-postgresql.druid.svc.cluster.local - Read/Write connection
> 
> To get the password for "postgres" run:
> 
>     export POSTGRES_PASSWORD=$(kubectl get secret --namespace druid dpg-postgresql -o jsonpath="{.data.postgresql-password}" | base64 --decode)
> 
> To connect to your database run the following command:
> 
>     kubectl run dpg-postgresql-client --rm --tty -i --restart='Never' --namespace druid --image docker.io/bitnami/postgresql:11.5.0-debian-9-r84 --env="PGPASSWORD=$POSTGRES_PASSWORD" --command -- psql --host dpg-postgresql -U postgres -d druid -p 5432
> 
> 
> 
> To connect to your database from outside the cluster execute the following commands:
> 
>     kubectl port-forward --namespace druid svc/dpg-postgresql 5432:5432 &
>     PGPASSWORD="$POSTGRES_PASSWORD" psql --host 127.0.0.1 -U postgres -d druid -p 5432
> ```
```bash=
eugene@Azure:~/Druid-Kubernetes$ kubectl apply -f k8s/druid
```
> ```
> deployment.apps/druid-broker created
> service/druid-broker created
> deployment.apps/druid-coordinator created
> service/druid-coordinator created
> service/druid-historical created
> statefulset.apps/druid-historical created
> service/druid-middlemanager created
> statefulset.apps/druid-middlemanager created
> deployment.apps/druid-overlord created
> service/druid-overlord created
> deployment.apps/druid-router created
> ```
Use `kubectl get all` to check but only have
```
NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)   AGE
service/kubernetes   ClusterIP   10.0.0.1     <none>        443/TCP   16h
```

```bash= 
kubectl get no
``` 
shows that my nodes are not ready,
so stop and start the cluster after start 
```bash= 
kubectl get no 
``` 
> ``` 
> NAME                                STATUS   ROLES   AGE   VERSION 
> aks-agentpool-28667265-vmss000006   Ready    agent   18m   v1.18.14 
> aks-agentpool-28667265-vmss000007   Ready    agent 19m   v1.18.14 
> aks-agentpool-28667265-vmss000008   Ready    agent   18m   v1.18.14 
> ```
```bash= 
kubectl get all --all-namespaces=true 
``` 
``` 
NAMESPACE     NAME                                      READY   STATUS             RESTARTS   AGE 
druid         pod/dpg-postgresql-0                      0/2     Pending            0          13h 
druid         pod/druid-broker-758c9c5d5f-dx24b         0/2     Pending            0          101m 
druid         pod/druid-coordinator-8675f4755b-7fvc4    0/2     Pending            0          101m 
druid         pod/druid-historical-0                    0/2     Pending            0          101m 
druid         pod/druid-middlemanager-0                 0/2     Pending            0          101m 
druid         pod/druid-overlord-6bbbc78d69-8qj2s       0/2     Pending            0          101m 
druid         pod/druid-router-7cf678f494-ps7zf         1/2     ImagePullBackOff   0          101m 
druid         pod/dz-zookeeper-0                        0/1     Pending            0          14h 
druid         pod/dz-zookeeper-1                        0/1     Pending            0          14h 
druid         pod/dz-zookeeper-2                        0/1     Pending            0          14h
kube-system   pod/coredns-748cdb7bf4-gs7br              1/1     Running            0          10h 
kube-system   pod/coredns-748cdb7bf4-zzctr              1/1     Running            0          16h 
kube-system   pod/coredns-autoscaler-868b684fd4-dgpv5   1/1     Running            0          16h 
kube-system   pod/kube-proxy-c2qqz                      1/1     Running            0          23m 
kube-system   pod/kube-proxy-f89t7                      1/1     Running            0          23m 
kube-system   pod/kube-proxy-qwpsv                      1/1     Running            0          22m 
kube-system   pod/metrics-server-58fdc875d5-5dvxn       1/1     Running            4          16h 
kube-system   pod/omsagent-6w7xq                        1/1     Running            0          23m 
kube-system   pod/omsagent-hn6lt                        1/1     Running            0          23m 
kube-system   pod/omsagent-j456f                        1/1     Running            1          22m 
kube-system   pod/omsagent-rs-5f8ccc6d89-9w8hn          1/1     Running            0          10h
kube-system   pod/tunnelfront-544d5fbfd9-h4qn4          1/1     Running            0          16h

NAMESPACE     NAME                                     TYPE           CLUSTER-IP     EXTERNAL-IP     PORT(S)
default       service/kubernetes                       ClusterIP      10.0.0.1       <none>          443/TCP         17h
druid         service/dpg-postgresql                   ClusterIP      10.0.170.172   <none>          5432/TCP        13h
druid         service/dpg-postgresql-headless          ClusterIP      None           <none>          5432/TCP        13h
druid         service/dpg-postgresql-metrics           ClusterIP      10.0.163.233   <none>          9187/TCP         3h
druid         service/druid-broker                     LoadBalancer   10.0.129.55    20.198.201.25   8082:31936/TCP  101m
druid         service/druid-coordinator                LoadBalancer   10.0.3.151     20.197.103.26   8081:30290/TCP  101m
druid         service/druid-historical                 ClusterIP      10.0.205.91    <none>          8083/TCP        101m
druid         service/druid-middlemanager              ClusterIP      10.0.3.211     <none>          8091/TCP,8100/TCP,8101/TCP,8102/TCP,8103/TCP,8104/TCP,8105/TCP,8106/TCP,8107/TCP,8108/TCP,8109/TCP,8110/TCP,8111/TCP,8112/TCP,8113/TCP,8114/TCP,8115/TCP,8116/TCP,8117/TCP,8118/TCP,8119/TCP,8120/TCP   101m
druid         service/druid-overlord                   ClusterIP      10.0.190.152   <none>          8090/TCP                    101m
druid         service/druid-router                     ClusterIP      10.0.135.146   <none>          8888/TCP                    101m
druid         service/dz-zookeeper                     ClusterIP      10.0.105.195   <none>          2181/TCP,2888/TCP,3888/TCP  14h
druid         service/dz-zookeeper-headless            ClusterIP      None           <none>          2181/TCP,2888/TCP,3888/TCP  14h
druid         service/dz-zookeeper-metrics             ClusterIP      10.0.245.12    <none>          9141/TCP                    14h
kube-system   service/healthmodel-replicaset-service   ClusterIP      10.0.145.54    <none>          25227/TCP                   17h
kube-system   service/kube-dns                         ClusterIP      10.0.0.10      <none>          53/UDP,53/TCP               17h
kube-system   service/metrics-server                   ClusterIP      10.0.228.28    <none>          443/TCP                     17h

NAMESPACE     NAME                          DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR                 AGE
kube-system   daemonset.apps/kube-proxy     3         3         3       3            3           beta.kubernetes.io/os=linux   17h
kube-system   daemonset.apps/omsagent       3         3         3       3            3           <none>                        17h
kube-system   daemonset.apps/omsagent-win   0         0         0       0            0           <none>                        17h

NAMESPACE     NAME                                 READY   UP-TO-DATE   AVAILABLE   AGE
druid         deployment.apps/druid-broker         0/1     1            0           101m
druid         deployment.apps/druid-coordinator    0/1     1            0           101m
druid         deployment.apps/druid-overlord       0/1     1            0           101m
druid         deployment.apps/druid-router         0/1     1            0           101m
kube-system   deployment.apps/coredns              2/2     2            2           17h
kube-system   deployment.apps/coredns-autoscaler   1/1     1            1           17h
kube-system   deployment.apps/metrics-server       1/1     1            1           17h
kube-system   deployment.apps/omsagent-rs          1/1     1            1           17h
kube-system   deployment.apps/tunnelfront          1/1     1            1           17h

NAMESPACE     NAME                                            DESIRED   CURRENT   READY   AGE
druid         replicaset.apps/druid-broker-758c9c5d5f         1         1         0       101m
druid         replicaset.apps/druid-coordinator-8675f4755b    1         1         0       101m
druid         replicaset.apps/druid-overlord-6bbbc78d69       1         1         0       101m
druid         replicaset.apps/druid-router-7cf678f494         1         1         0       101m
kube-system   replicaset.apps/coredns-748cdb7bf4              2         2         2       17h
kube-system   replicaset.apps/coredns-autoscaler-868b684fd4   1         1         1       17h
kube-system   replicaset.apps/metrics-server-58fdc875d5       1         1         1       17h
kube-system   replicaset.apps/omsagent-rs-5f8ccc6d89          1         1         1       17h
kube-system   replicaset.apps/tunnelfront-544d5fbfd9          1         1         1       17h

NAMESPACE   NAME                                   READY   AGE
druid       statefulset.apps/dpg-postgresql        0/1     13h
druid       statefulset.apps/druid-historical      0/1     101m
druid       statefulset.apps/druid-middlemanager   0/8     101m
druid       statefulset.apps/dz-zookeeper          0/3     14h
```

try to look into 
```
druid         pod/druid-router-7cf678f494-ps7zf         1/2     ImagePullBackOff   0          101m
```
```
eugene@Azure:~/Druid-Kubernetes$ kubectl describe pod/druid-router-7cf678f494-ps7zf -n druid
Name:         druid-router-7cf678f494-ps7zf
Namespace:    druid
Priority:     0
Node:         aks-agentpool-28667265-vmss000007/10.240.0.5
Start Time:   Tue, 23 Mar 2021 04:53:30 +0000
Labels:       component=router
              pod-template-hash=7cf678f494
Annotations:  prometheus.io/port: 8000
              prometheus.io/scrape: true
Status:       Pending
IP:           10.244.0.8
IPs:
  IP:           10.244.0.8
Controlled By:  ReplicaSet/druid-router-7cf678f494
Containers:
  druid:
    Container ID:
    Image:         gcr.io/zenatix-data-archiver/kube-druid:0.0.1
    Image ID:
    Port:          8888/TCP
    Host Port:     0/TCP
    Command:
      /bin/bash
      -c
      ip=$(awk 'END{print $1}' /etc/hosts) && sed -ri 's/druid.host=.*/druid.host='${ip}'/g' /druid/conf/router/runtime.properties && bin/run-druid router /druid/conf
    State:          Waiting
      Reason:       ImagePullBackOff
    Ready:          False
    Restart Count:  0
    Readiness:      http-get http://:8888/status/health delay=30s timeout=1s period=10s #success=1 #failure=3
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-vpwg6 (ro)
  druid-exporter:
    Container ID:   docker://4548c74ceb25d6c2052de2dc5d23e839d7c1e5bb2165de9b5ae8193ac28faa45
    Image:          deepaksood619/druid-exporter:0.0.2
    Image ID:       docker-pullable://deepaksood619/druid-exporter@sha256:9c9f729b651fdeeb0097044e9498026db76f243f8ba98e56cae1a1eb3d0f93d7
    Port:           8000/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Tue, 23 Mar 2021 04:54:18 +0000
    Ready:          True
    Restart Count:  0
    Environment:    <none>
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from default-token-vpwg6 (ro)
Conditions:
  Type              Status
  Initialized       True
  Ready             False
  ContainersReady   False
  PodScheduled      True
Volumes:
  default-token-vpwg6:
    Type:        Secret (a volume populated by a Secret)
    SecretName:  default-token-vpwg6
    Optional:    false
QoS Class:       BestEffort
Node-Selectors:  <none>
Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                 node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type     Reason            Age                    From               Message
  ----     ------            ----                   ----               -------
  Warning  FailedScheduling  113m                   default-scheduler  0/3 nodes are available: 3 node(s) had taint {node.kubernetes.io/unreachable: }, that the pod didn't tolerate.
  Warning  FailedScheduling  36m (x4 over 38m)      default-scheduler  no nodes available to schedule pods
  Warning  FailedScheduling  35m                    default-scheduler  0/1 nodes are available: 1 node(s) had taint {node.kubernetes.io/not-ready: }, that the pod didn't tolerate.
  Normal   Scheduled         35m                    default-scheduler  Successfully assigned druid/druid-router-7cf678f494-ps7zf to aks-agentpool-28667265-vmss000007
  Normal   Pulling           34m                    kubelet            Pulling image "deepaksood619/druid-exporter:0.0.2"
  Normal   Pulled            34m                    kubelet            Successfully pulled image "deepaksood619/druid-exporter:0.0.2"
  Normal   Created           34m                    kubelet            Created container druid-exporter
  Normal   Started           34m                    kubelet            Started container druid-exporter
  Warning  Failed            33m (x3 over 34m)      kubelet            Failed to pull image "gcr.io/zenatix-data-archiver/kube-druid:0.0.1": rpc error: code = Unknown desc = Error response from daemon: unauthorized: You don't have the needed permissions to perform this operation, and you may have invalid credentials. To authenticate your request, follow the steps in: https://cloud.google.com/container-registry/docs/advanced-authentication
  Normal   BackOff           33m (x5 over 34m)      kubelet            Back-off pulling image "gcr.io/zenatix-data-archiver/kube-druid:0.0.1"
  Normal   Pulling           33m (x4 over 35m)      kubelet            Pulling image "gcr.io/zenatix-data-archiver/kube-druid:0.0.1"
  Warning  Failed            33m (x4 over 34m)      kubelet            Error: ErrImagePull
  Warning  Failed            4m35s (x131 over 34m)  kubelet            Error: ImagePullBackOff
```
seem like nodes not enough and some permission issue, 
scale up to 6 nodes by azure portal gui
succeed
try to restart a pod... GG, don't want to spend time on this repo
:::danger
too much time spent this repo, try other methods
give up this repo
:::

See: https://ithelp.ithome.com.tw/articles/10193944
try:
```
// in WSL // sudo dockerd in another terminal
y56@AA2100083-NB:~$ docker pull gcr.io/zenatix-data-archiver/kube-druid:0.0.1
Error response from daemon: unauthorized: You don't have the needed permissions to perform this operation, and you may have invalid credentials. To authenticate your request, follow the steps in: https://cloud.google.com/container-registry/docs/advanced-authentication
y56@AA2100083-NB:~$ docker pull gcr.io/zenatix-data-archiver/kube-druid
Using default tag: latest
Error response from daemon: unauthorized: You don't have the needed permissions to perform this operation, and you may have invalid credentials. To authenticate your request, follow the steps in: https://cloud.google.com/container-registry/docs/advanced-authentication
y56@AA2100083-NB:~$ docker pull zenatix-data-archiver/kube-druid
Using default tag: latest
Error response from daemon: pull access denied for zenatix-data-archiver/kube-druid, repository does not exist or may require 'docker login': denied: requested access to the resource is denied
```
:::danger
That's a private docker hub, GG
:::


## [yet] try: Imply
https://docs.imply.io/2021.02/k8s-azure/
https://docs.imply.io/3.0/on-prem/quickstart


## tools

### delete some of them

kubectl delete deployment webfrontend  # clear all resources except service

helm uninstall webfrontend  # need to wait pod, few seconds 

### [bad, clean too much] clean all the stuff; get a clean aks env
will take a few minutes to derminate things
```
kubectl delete pods --all --all-namespaces
kubectl delete --all pods --all-namespaces
kubectl delete --all deployments --all-namespaces
kubectl delete --all namespaces  # bad, will break kube-system, need to restart nodes

kubectl get all --all-namespaces=true  # to check
```
However, the latter command is probably not something you want to do, since it will delete things in the kube-system namespace, which will make your cluster not usable. This command will delete all the namespaces except kube-system, which might be useful:
```
# for linux
for each in $(kubectl get ns -o jsonpath="{.items[*].metadata.name}" | grep -v kube-system);
do
  kubectl delete ns $each
done
```

### kill a process
kill pid_number

### list pid and port usage
sudo ss -lp "sport = :443"
sudo ss -lp "sport = :8080"
sudo ss -lp "sport = :domain"
sudo ss -lp "sport = :53"
sudo ss -lp "sport = :22"

### install kubectl on WSL2 or linux
```
// make sure you have internet QQ
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
kubectl version --client
```
#### [solved]: hard to use on WSL2/Linux to access AKS
```bash=
kubectl get all
```
```
The connection to the server 127.0.0.1:32769 was refused - did you specify the right host or port?
```
WSL is trying to connect minikube, don't know how to config it
give up; dont use wsl

replace the content of /home/y56/.kube/config by C:\Users\eugene_wang\.kube\config


# [OK] hello world, for minikube, on WSL
Use the Windows-native desktop docker as the docker engine, don't use dockerd in WSL
Otherwise, you will have
```
❗  This container is having trouble accessing https://k8s.gcr.io
💡  To pull new external images, you may need to configure a proxy: https://minikube.sigs.k8s.io/docs/reference/networking/proxy/
```
when doing minikube start
and will have status as `ErrImagePull` or `ImagePullBackOff` for the pod created by
```
kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.4
```
See: https://blog.miniasp.com/post/2020/08/21/Install-Kubernetes-cluster-in-WSL-2-Docker-on-Windows-using-kind

## command and printout
```
y56@AA2100083-NB:~$ minikube start
😄  minikube v1.18.1 on Ubuntu 20.04
✨  Using the docker driver based on existing profile

💣  Exiting due to PROVIDER_DOCKER_NOT_RUNNING: "docker version --format -" exit status 1: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
💡  Suggestion: Start the Docker service
📘  Documentation: https://minikube.sigs.k8s.io/docs/drivers/docker/

y56@AA2100083-NB:~$ minikube start
😄  minikube v1.18.1 on Ubuntu 20.04
✨  Using the docker driver based on existing profile

💣  Exiting due to PROVIDER_DOCKER_NOT_RUNNING: "docker version --format -" exit status 1: Cannot connect to the Docker daemon at unix:///var/run/docker.sock. Is the docker daemon running?
💡  Suggestion: Start the Docker service
📘  Documentation: https://minikube.sigs.k8s.io/docs/drivers/docker/

y56@AA2100083-NB:~$ minikube start
😄  minikube v1.18.1 on Ubuntu 20.04
✨  Using the docker driver based on existing profile
👍  Starting control plane node minikube in cluster minikube
🚜  Pulling base image ...
🤷  docker "minikube" container is missing, will recreate.
🔥  Creating docker container (CPUs=2, Memory=3100MB) ...
🐳  Preparing Kubernetes v1.20.2 on Docker 20.10.3 ...
    ▪ Generating certificates and keys ...
    ▪ Booting up control plane ...
    ▪ Configuring RBAC rules ...
🔎  Verifying Kubernetes components...
    ▪ Using image gcr.io/k8s-minikube/storage-provisioner:v4
🌟  Enabled addons: storage-provisioner, default-storageclass
🏄  Done! kubectl is now configured to use "minikube" cluster and "default" namespace by default
y56@AA2100083-NB:~$ kubectl get all -A
NAMESPACE     NAME                                   READY   STATUS    RESTARTS   AGE
kube-system   pod/coredns-74ff55c5b-jdqqh            1/1     Running   0          46s
kube-system   pod/etcd-minikube                      0/1     Running   0          54s
kube-system   pod/kube-apiserver-minikube            1/1     Running   0          54s
kube-system   pod/kube-controller-manager-minikube   1/1     Running   0          54s
kube-system   pod/kube-proxy-vwqd4                   1/1     Running   0          46s
kube-system   pod/kube-scheduler-minikube            0/1     Running   0          54s
kube-system   pod/storage-provisioner                1/1     Running   0          55s

NAMESPACE     NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
default       service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP                  66s
kube-system   service/kube-dns     ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   61s

NAMESPACE     NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR
AGE
kube-system   daemonset.apps/kube-proxy   1         1         1       1            1           kubernetes.io/os=linux   60s

NAMESPACE     NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
kube-system   deployment.apps/coredns   1/1     1            1           61s

NAMESPACE     NAME                                DESIRED   CURRENT   READY   AGE
y56@AA2100083-NB:~$ kubectl get all -A
NAMESPACE     NAME                                   READY   STATUS    RESTARTS   AGE
kube-system   pod/coredns-74ff55c5b-jdqqh            1/1     Running   0          64s
kube-system   pod/etcd-minikube                      0/1     Running   0          72s
kube-system   pod/kube-apiserver-minikube            1/1     Running   0          72s
kube-system   pod/kube-controller-manager-minikube   1/1     Running   0          72s
kube-system   pod/kube-proxy-vwqd4                   1/1     Running   0          64s
kube-system   pod/kube-scheduler-minikube            1/1     Running   0          72s
kube-system   pod/storage-provisioner                1/1     Running   0          73s

NAMESPACE     NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
default       service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP                  84s
kube-system   service/kube-dns     ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   79s

NAMESPACE     NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
kube-system   daemonset.apps/kube-proxy   1         1         1       1            1           kubernetes.io/os=linux   78s

NAMESPACE     NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
kube-system   deployment.apps/coredns   1/1     1            1           79s

NAMESPACE     NAME                                DESIRED   CURRENT   READY   AGE
kube-system   replicaset.apps/coredns-74ff55c5b   1         1         1       65s
y56@AA2100083-NB:~$ kubectl get all -A
NAMESPACE     NAME                                   READY   STATUS    RESTARTS   AGE
kube-system   pod/coredns-74ff55c5b-jdqqh            1/1     Running   0          76s
kube-system   pod/etcd-minikube                      1/1     Running   0          84s
kube-system   pod/kube-apiserver-minikube            1/1     Running   0          84s
kube-system   pod/kube-controller-manager-minikube   1/1     Running   0          84s
kube-system   pod/kube-proxy-vwqd4                   1/1     Running   0          76s
kube-system   pod/kube-scheduler-minikube            1/1     Running   0          84s
kube-system   pod/storage-provisioner                1/1     Running   0          85s

NAMESPACE     NAME                 TYPE        CLUSTER-IP   EXTERNAL-IP   PORT(S)                  AGE
default       service/kubernetes   ClusterIP   10.96.0.1    <none>        443/TCP                  96s
kube-system   service/kube-dns     ClusterIP   10.96.0.10   <none>        53/UDP,53/TCP,9153/TCP   91s

NAMESPACE     NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
kube-system   daemonset.apps/kube-proxy   1         1         1       1            1           kubernetes.io/os=linux   90s

NAMESPACE     NAME                      READY   UP-TO-DATE   AVAILABLE   AGE
kube-system   deployment.apps/coredns   1/1     1            1           91s

NAMESPACE     NAME                                DESIRED   CURRENT   READY   AGE
kube-system   replicaset.apps/coredns-74ff55c5b   1         1         1       77s
y56@AA2100083-NB:~$ kubectl create deployment hello-minikube --image=k8s.gcr.io/echoserver:1.4
deployment.apps/hello-minikube created
y56@AA2100083-NB:~$ kubectl expose deployment hello-minikube --type=NodePort --port=8080
service/hello-minikube exposed
y56@AA2100083-NB:~$ kubectl get services hello-minikube
NAME             TYPE       CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
hello-minikube   NodePort   10.107.169.186   <none>        8080:31472/TCP   7s
y56@AA2100083-NB:~$ minikube service hello-minikube
|-----------|----------------|-------------|---------------------------|
| NAMESPACE |      NAME      | TARGET PORT |            URL            |
|-----------|----------------|-------------|---------------------------|
| default   | hello-minikube |        8080 | http://192.168.49.2:31472 |
|-----------|----------------|-------------|---------------------------|
🏃  Starting tunnel for service hello-minikube.
|-----------|----------------|-------------|------------------------|
| NAMESPACE |      NAME      | TARGET PORT |          URL           |
|-----------|----------------|-------------|------------------------|
| default   | hello-minikube |             | http://127.0.0.1:35053 |
|-----------|----------------|-------------|------------------------|
🎉  Opening service default/hello-minikube in default browser...
👉  http://127.0.0.1:35053
❗  Because you are using a Docker driver on linux, the terminal needs to be open to run it.
^C✋  Stopping tunnel for service hello-minikube.

❌  Exiting due to SVC_TUNNEL_STOP: stopping ssh tunnel: os: process already finished

😿  If the above advice does not help, please let us know:
👉  https://github.com/kubernetes/minikube/issues/new/choose

y56@AA2100083-NB:~$ kubectl get all -A
NAMESPACE     NAME                                   READY   STATUS    RESTARTS   AGE
default       pod/hello-minikube-6ddfcc9757-9hdr6    1/1     Running   0          55m
kube-system   pod/coredns-74ff55c5b-jdqqh            1/1     Running   0          62m
kube-system   pod/etcd-minikube                      1/1     Running   0          62m
kube-system   pod/kube-apiserver-minikube            1/1     Running   0          62m
kube-system   pod/kube-controller-manager-minikube   1/1     Running   0          62m
kube-system   pod/kube-proxy-vwqd4                   1/1     Running   0          62m
kube-system   pod/kube-scheduler-minikube            1/1     Running   0          62m
kube-system   pod/storage-provisioner                1/1     Running   0          62m

NAMESPACE     NAME                     TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)                  AGE
default       service/hello-minikube   NodePort    10.107.169.186   <none>        8080:31472/TCP           55m
default       service/kubernetes       ClusterIP   10.96.0.1        <none>        443/TCP                  62m
kube-system   service/kube-dns         ClusterIP   10.96.0.10       <none>        53/UDP,53/TCP,9153/TCP   62m

NAMESPACE     NAME                        DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
kube-system   daemonset.apps/kube-proxy   1         1         1       1            1           kubernetes.io/os=linux   62m

NAMESPACE     NAME                             READY   UP-TO-DATE   AVAILABLE   AGE
default       deployment.apps/hello-minikube   1/1     1            1           55m
kube-system   deployment.apps/coredns          1/1     1            1           62m

NAMESPACE     NAME                                        DESIRED   CURRENT   READY   AGE
default       replicaset.apps/hello-minikube-6ddfcc9757   1         1         1       55m
kube-system   replicaset.apps/coredns-74ff55c5b           1         1         1       62m
y56@AA2100083-NB:~$ kubectl get no -A
NAME       STATUS   ROLES                  AGE   VERSION
minikube   Ready    control-plane,master   63m   v1.20.2
y56@AA2100083-NB:~$ kubectl get no
NAME       STATUS   ROLES                  AGE   VERSION
minikube   Ready    control-plane,master   63m   v1.20.2
y56@AA2100083-NB:~$ kubectl get no --all
Error: unknown flag: --all
See 'kubectl get --help' for usage.
y56@AA2100083-NB:~$
```

# [GG] [no permission to pull my own image??!!] Quickstart: Develop on Azure Kubernetes Service (AKS) with Helm
https://docs.microsoft.com/en-us/azure/aks/quickstart-helm
```powershell
# create the Dockfile

# az acr build --image webfrontend:v1 --registry MyHelmACR --file Dockerfile .
az acr build --image webfrontend:v1 --registry kgacrdruiddev2 --file Dockerfile .

git clone https://github.com/Azure/dev-spaces
cd dev-spaces/samples/nodejs/getting-started/webfrontend

# install choco
Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))

# install helm
choco install kubernetes-helm  # reboot win 10, win 10 is BAD~


helm create webfrontend

# Update webfrontend/values.yaml:
##  Replace the loginServer of your registry that you noted in an earlier step, such as myhelmacr.azurecr.io.
##  Change image.repository to <loginServer>/webfrontend
##  Change service.type to LoadBalancer

# Update Update appVersion to v1 in webfrontend/Chart.yaml. 

helm install webfrontend webfrontend/

kubectl get all -A
    default       pod/webfrontend-6d85cfcc65-kqh5n          0/1     ImagePullBackOff   0          11s

PS C:\Users\eugene_wang\dev-spaces\samples\nodejs\getting-started\webfrontend> kubectl describe pod/webfrontend-6d85cfcc65-kqh5n
```

  ```powershell
  Name:         webfrontend-6d85cfcc65-kqh5n
  Namespace:    default
  Priority:     0
  Node:         aks-agentpool-62526533-vmss000002/10.240.0.6
  Start Time:   Wed, 24 Mar 2021 16:02:32 +0800
  Labels:       app.kubernetes.io/instance=webfrontend
                app.kubernetes.io/name=webfrontend
                pod-template-hash=6d85cfcc65
  Annotations:  <none>
  Status:       Pending
  IP:           10.244.0.12
  IPs:
    IP:           10.244.0.12
  Controlled By:  ReplicaSet/webfrontend-6d85cfcc65
  Containers:
    webfrontend:
      Container ID:
      Image:          kgacrdruiddev.azurecr.io/webfrontend:v1
      Image ID:
      Port:           80/TCP
      Host Port:      0/TCP
      State:          Waiting
        Reason:       ImagePullBackOff
      Ready:          False
      Restart Count:  0
      Liveness:       http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
      Readiness:      http-get http://:http/ delay=0s timeout=1s period=10s #success=1 #failure=3
      Environment:    <none>
      Mounts:
        /var/run/secrets/kubernetes.io/serviceaccount from webfrontend-token-bhk9n (ro)
  Conditions:
    Type              Status
    Initialized       True
    Ready             False
    ContainersReady   False
    PodScheduled      True
  Volumes:
    webfrontend-token-bhk9n:
      Type:        Secret (a volume populated by a Secret)
      SecretName:  webfrontend-token-bhk9n
      Optional:    false
  QoS Class:       BestEffort
  Node-Selectors:  <none>
  Tolerations:     node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                  node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
  Events:
    Type     Reason          Age                 From               Message
    ----     ------          ----                ----               -------
    Normal   Scheduled       112s                default-scheduler  Successfully assigned default/webfrontend-6d85cfcc65-kqh5n to aks-agentpool-62526533-vmss000002
    Normal   SandboxChanged  111s                kubelet            Pod sandbox changed, it will be killed and re-created.
    Warning  Failed          65s (x3 over 111s)  kubelet            Failed to pull image "kgacrdruiddev.azurecr.io/webfrontend:v1": rpc error: code = Unknown desc = Error response from daemon: Get https://kgacrdruiddev.azurecr.io/v2/webfrontend/manifests/v1: unauthorized: authentication required, visit https://aka.ms/acr/authorization for more information.
    Warning  Failed          65s (x3 over 111s)  kubelet            Error: ErrImagePull
    Normal   BackOff         27s (x7 over 110s)  kubelet            Back-off pulling image "kgacrdruiddev.azurecr.io/webfrontend:v1"
    Warning  Failed          27s (x7 over 110s)  kubelet            Error: ImagePullBackOff
    Normal   Pulling         14s (x4 over 112s)  kubelet            Pulling image "kgacrdruiddev.azurecr.io/webfrontend:v1"
  ```



# [OK] Quickstart: Deploy an Azure Kubernetes Service cluster using the Azure CLI
```
PS C:\Users\eugene_wang> code azure-vote.yaml  # to create the file
PS C:\Users\eugene_wang> kubectl apply -f azure-vote.yaml
  deployment.apps/azure-vote-back created
  service/azure-vote-back created
  deployment.apps/azure-vote-front created
  service/azure-vote-front created
PS C:\Users\eugene_wang> kubectl get service azure-vote-front --watch
  NAME               TYPE           CLUSTER-IP   EXTERNAL-IP   PORT(S)        AGE
  azure-vote-front   LoadBalancer   10.0.57.71   20.195.53.3   80:30815/TCP   39s
```
20.195.53.3:80 http 
:::success
success
:::

#

