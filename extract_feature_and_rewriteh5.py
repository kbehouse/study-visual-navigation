from resnet50 import ResNet50
from keras.preprocessing import image
from imagenet_utils import preprocess_input
import numpy as np
import h5py

h5_name = 'data/bathroom_02.h5'

model = ResNet50(weights='imagenet', include_top=False)
def get_feature(img_path):
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    features = model.predict(x)

    return features

f = h5py.File(h5_name, 'r+')
feature_ary = []

img_dir_name = 'img/' + h5_name[5:-3]
for i in range(len(f['observation'])):
    img_path = "{}/{:03d}.png".format(img_dir_name, i)
    print("Extract feature from -> " + img_path)
    feature = get_feature(img_path)
    feature = np.array(feature)
    # print('feature.shape='+ str(feature.shape))
    # feature.squeeze()
    feature = feature[0,0,:,:]
    # print('feature.shape='+ str(feature.shape))
    feature_ary.append(feature)

feature_ary = np.array(feature_ary)
print('feature_ary.shape='+ str(feature_ary.shape))

#-------------Rewrite h5 file------------#

# data =  f['resnet_feature']
# data[...] = feature_ary

del f['resnet_feature']
dset = f.create_dataset('resnet_feature', data=feature_ary)
f.close()