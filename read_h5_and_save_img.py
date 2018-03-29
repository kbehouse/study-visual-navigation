import h5py
import matplotlib.pyplot as plt
import numpy as np
from scipy.misc import imsave
from shutil import rmtree
import os


def recreate_dir(tar_dir):
    if os.path.isdir(tar_dir):
        rmtree(tar_dir)
    os.mkdir(tar_dir)


#filename = 'data/bedroom_04.h5'
#filename = 'data/kitchen_02.h5'
# filename = 'data/living_room_08.h5'
filename = 'data/bathroom_02.h5'
f = h5py.File(filename, 'r')


if not os.path.isdir('img'):
    os.mkdir('img')
output_dir = 'img/' + filename[5:-3]
recreate_dir(output_dir)


for i in range(len(f['observation'])):
    save_path = "{}/{:03d}.png".format(output_dir, i)
    print('Save to ' + save_path)
    imsave(save_path, f['observation'][i])