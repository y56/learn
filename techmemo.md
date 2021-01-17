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

