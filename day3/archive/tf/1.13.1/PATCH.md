# Enabling Custom Functions in TensorFlow Lite Converter

1. Look for the path to your lite.py. You can get the path like this.
```
import tensorflow as tf

tf.lite.TFConverter.from_keras_model_file?
```

2. Make a backup of lite.py first in case you need to revert.

3. Edit lite.py to add the change as described by the github changelist (https://github.com/tensorflow/tensorflow/commit/09deaeb03ca4ceb40cf600a337083e2054e65390#diff-51433e291e109194f883fcfc85cd2db3):

    Look for the classmethod, it should be around line 350, add a `custom_objects` parameter:
    ```
      @classmethod
      def from_keras_model_file(cls,
                                ...
                                output_arrays=None,
                                custom_objects=None):

            ...

            keras_model = _keras.models.load_model(model_file, custom_objects)
    ```
    
If you need a reference, you can compare your file with `lite.py`, which has the example changes made.
