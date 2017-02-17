# Convolutional Neural Network

# Importing Keras libraries and packages
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense 

# Initialising the CNN
classifier = Sequential()

# Step 1 - Convolution
classifier.add(Convolution2D(32, 3, 3, input_shape = (64, 64, 3), activation = 'relu')) # Flip for Theano backend

# Step 2 - Max Pooling 
classifier.add(MaxPooling2D(pool_size = (2, 2))) # Dividing the convo layer by 2

# Adding 2nd Convolutional Layer & Max Pooling to improve test-set accuracy 
classifier.add(Convolution2D(32, 3, 3, activation = 'relu')) # Dont need input_shape
classifier.add(MaxPooling2D(pool_size = (2, 2))) # Dividing the convo layer by 2

# Step 3 - Flattening features into linear starting layer of neurons
classifier.add(Flatten())

# Step 4 - Full Connection (Classic ANN)
classifier.add(Dense(output_dim = 128, activation = 'relu')) # How to choose output_dim?
classifier.add(Dense(output_dim = 1, activation = 'sigmoid')) #Use softmax func for multi-class classification 

# Compiling the CNN (Choosing gradient descent model, categorical_crossentropy if multi-class)
classifier.compile(optimizer = 'adam', loss = 'binary_crossentropy', metrics = ['accuracy']) 

# Fitting CNN to layer - what do all of these do?
from keras.preprocessing.image import ImageDataGenerator 
train_datagen = ImageDataGenerator(rescale=1./255, shear_range=0.2, zoom_range=0.2, horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory('dataset/training_set', target_size=(64, 64), batch_size=32, class_mode='binary')
test_set = test_datagen.flow_from_directory('dataset/test_set', target_size=(64, 64), batch_size=32, class_mode='binary') # Resizing the images
classifier.fit_generator(training_set, samples_per_epoch = 8000, nb_epoch=25, validation_data = test_set, nb_val_samples=2000)

# But whats actually really going on here??
