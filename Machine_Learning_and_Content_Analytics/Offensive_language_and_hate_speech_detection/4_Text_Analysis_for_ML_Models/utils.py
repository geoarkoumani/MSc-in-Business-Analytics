def export_model(model, input_filename):
    import os
    import pickle
    import pathlib
    path = pathlib.Path(__file__).parent.resolve()
    # save the model to disk
    filename = os.path.join(path, input_filename)
    # write model in bytes
    pickle.dump(model, open(filename, 'wb'))

def import_model(input_filename):
    import pickle
    #Load the model
    return pickle.load(open(input_filename, 'rb'))

def export_keras_model(model, input_foldername):
    import os
    import pathlib
    path = pathlib.Path(__file__).parent.resolve()
    # save the model to disk
    filename = os.path.join(path, input_foldername)
    # create the folder which contains the model
    model.save(filename)

def import_keras_model(input_filename):
    import tensorflow as tf
    return tf.keras.models.load_model(input_filename)