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

    Output: Elements from the queue: [AA, BB, CC, DD, EE]
    Getting the by peek() method: AA
    Getting the by element() method: AA
    Removing element by remove() method: AA
    Removing element by poll() method: BB
    Size of queue: 3
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
https://docs.feathersjs.com/api/databases/querying.html#sort```
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