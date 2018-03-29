import h5py
import matplotlib.pyplot as plt
import numpy as np


def save_with_index(f_name, np_ary):
    with open(f_name, 'w') as f:
        for ind, data in enumerate(np_ary):
            f.write("{:4d}: {}\n".format(ind,data))

filename = 'data/bathroom_02.h5'

#filename = 'data/bedroom_04.h5'
f = h5py.File(filename, 'r')


print("-START--------datasetNames---------")
datasetNames = [n for n in f.keys()]
for n in datasetNames:
    print(n)
print("---------datasetNames--------END-")

print("f['graph'].shape="+str(f['graph'].shape))
print("f['location'].shape="+str(f['location'].shape))
print("f['observation'].shape="+str(f['observation'].shape))
print("f['resnet_feature'].shape="+str(f['resnet_feature'].shape))
print("f['rotation'].shape="+str(f['rotation'].shape))
print("f['shortest_path_distance'].shape="+str(f['shortest_path_distance'].shape))
'''
f['graph'].shape=(180, 4)
f['location'].shape=(180, 2)
f['observation'].shape=(180, 300, 400, 3)
f['resnet_feature'].shape=(180, 10, 2048)
f['rotation'].shape=(180,)
f['shortest_path_distance'].shape=(180, 180)

'''

print("type(f['resnet_feature'])="+ str(type(f['resnet_feature'])) )

#--------------Save resnet_feature-----------#
# out_ary = np.squeeze(f['resnet_feature'][3])
# # print("out_ary.shape="+str(out_ary.shape))
# for i in range(len(f['resnet_feature'][3])):
#     out_name = "f[resnet_feature][003][{:02d}].out".format(i)
#     np.savetxt(out_name,f['resnet_feature'][3][i])

out_ary = np.squeeze(f['resnet_feature'][3])
# print("out_ary.shape="+str(out_ary.shape))
for i in range(len(f['resnet_feature'][3])):
    out_name = "keras_f[resnet_feature][003][{:02d}].out".format(i)
    np.savetxt(out_name,f['resnet_feature'][3][i])

#--------------Save shortest_path_distance-----------#
# np.savetxt("f['shortest_path_distance'][64].out",f['shortest_path_distance'][64])
# np.savetxt("f['graph'].out",f['graph'],fmt='%03d')
save_with_index("f['shortest_path_distance'][161].out", f['shortest_path_distance'][161])
save_with_index("f['graph'].out", f['graph'])

print("f['location'][134] = " + str(f['location'][134]) )
print("f['rotation'][134] = " + str(f['rotation'][134]) )

print("Show image of f['observation'][134] " )

# print("-START--------f['location'] & f['rotation']-------")
# for  i in range(180):
# 	print("f['location'][{}]={}, f['rotation'][{}]={}".format(i, f['location'][i], i, f['rotation'][i]))
# print("---------f['location'] & f['rotation']--------END-")


# print("-START--------f['graph']-------")
# for  i in range(180):
# 	print("f['graph'][{}]={}".format(i, f['graph'][i]) )
# print("---------f['graph'] --------END-")

# print("-START--------f['shortest_path_distance']-------")
# for  i in range(180):
# 	print("f['shortest_path_distance'][{}]={}".format(i, f['shortest_path_distance'][i]) )
# print("---------f['shortest_path_distance'] --------END-")


print(f['location'][134])
print(f['rotation'][134])
img = np.array(f['observation'][134])

# plt.imshow(img)
# plt.show()


