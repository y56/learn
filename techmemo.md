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
`````
