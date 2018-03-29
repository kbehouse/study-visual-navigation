import h5py
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imsave

#filename = 'data/bathroom_02.h5'
#filename = 'data/bedroom_04.h5'
#filename = 'data/kitchen_02.h5'
def recreate_dir(tar_dir):
    from shutil import rmtree
    import os
    if os.path.isdir(tar_dir):
        rmtree(tar_dir)
    os.mkdir(tar_dir)

# filename = 'data/living_room_08.h5'
filename = 'data/bathroom_02.h5'
f = h5py.File(filename, 'r')

datasetNames = [n for n in f.keys()]
for n in datasetNames:
	print(n)

print(f['graph'].shape)
print(f['location'].shape)
print(f['observation'].shape)
print(f['resnet_feature'].shape)
print(f['rotation'].shape)
print(f['shortest_path_distance'].shape)
'''
f['graph'].shape=(180, 4)
f['location'].shape=(180, 2)
f['observation'].shape=(180, 300, 400, 3)
f['resnet_feature'].shape=(180, 10, 2048)
f['rotation'].shape=(180,)
f['shortest_path_distance'].shape=(180, 180)
f['location'][134] = [0.5 3.5]
f['rotation'][134] = 180
'''
# for i in range(len(f['location'])):
#     if(f['location'][i][0] == 9.0 and f['location'][i][1] == 3.0 and f['rotation'][i] == 0):
#         img = np.array(f['observation'][i])        
#         plt.imshow(img)
#         plt.show()

print(filename[5:-3])

output_dir = 'img/' + filename[5:-3]
recreate_dir(output_dir)

print("Output Directory: " + output_dir)

print("f['location'].shape={}".format( f['location'].shape))
print("len(f['location'])={}".format( len(f['location'])) )
for i in range(len(f['location'])):
    img = np.array(f['observation'][i])
    # fig = plt.figure()
    # plt.imshow(img)
    save_path = "{}/[{:03d}]_x{:04.2f}_y{:04.2f}_r{:03d}.png".format(output_dir, i, f['location'][i][0], f['location'][i][1], f['rotation'][i])
    print('Save to ' + save_path)
    imsave(save_path, img)
    # fig.savefig('img/'+filename[5:-3]+'/x'+str(f['location'][i][0])+'_y'+str(f['location'][i][1])+'_r'+str(f['rotation'][i])+'.png', dpi=fig.dpi)