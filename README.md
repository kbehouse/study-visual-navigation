## Study icra2017-visual-navigation

This repo is forked from [https://github.com/zfw1226/icra2017-visual-navigation](https://github.com/zfw1226/icra2017-visual-navigation), please read the original repo first.


## Install and download data 

Install requirement packages

```bash
pip install -r requirements.txt
```

Download *.h5 in data/
```bash
./data/download_scene_dumps.sh
```

## Study 

Know h5 file (By [Minda](https://github.com/Minda93/) )

```bash
python read_h5.py
```

Save one scene all imgaes (By [Minda](https://github.com/Minda93/) )
```bash
python read_h5_and_save_all.py
```

Know what the target task image, and save to target_img[TASK_LIST]/ diretctory

```bash
python get_TASK_LIST_img.py
```

You could play scene first, and log image to  keyboard_agent_save/ directory, use keyboard [up, down, right, left] and use [q] to quit, [r] to restart 
```bash 
python keyboard_agent.py
```

## Extract feature and generate resnet_feature 

Decompress the h5 file save save images to img/ directory (choose scene by ***filename*** variable)

```bash
python read_h5_and_save_img.py
```

Extract features and rewrite to h5 file
(Resnet50 from https://github.com/fchollet/deep-learning-models)
```bash
python extract_feature_and_rewriteh5.py
```

## Train model and test model

Train and save model to checkpoints
(The train scene is from constants.py ***TASK_LIST***)
```bash
python train.py
```

Test the model and save image to evaluate_img/ directory
```bash
python evaluate.py
```

## Acknowledgements
[Yuke Zhu](http://web.stanford.edu/~yukez/)


## License
MIT
