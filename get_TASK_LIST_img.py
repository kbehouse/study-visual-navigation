from constants import TASK_LIST
import h5py
import cv2
def recreate_dir(tar_dir):
    from shutil import rmtree
    import os
    if os.path.isdir(tar_dir):
        rmtree(tar_dir)
    os.mkdir(tar_dir)

output_dir = 'target_img[TASK_LIST]/'
recreate_dir(output_dir)

# list_of_tasks = TASK_LIST
scene_scopes = TASK_LIST.keys()

for key in scene_scopes:
    h5_filename = 'data/' + key + '.h5'
    f = h5py.File(h5_filename, 'r')
    for obs_id in TASK_LIST[key]:
        img = f['observation'][int(obs_id)]
        save_path = output_dir + "{}-{}.png".format(key, obs_id)
        cv2.imwrite(save_path, img)