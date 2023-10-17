from PIL import Image
import os
import moviepy.editor as mp
from tqdm import tqdm

models = ['videofusion']
vids = [390,455,491,574,357,368,374,204,404,405,407,2,5,6,17,256,1,37,149,357,23,163,21,99,21,34,25,330,137,149,157,62,122,60,491,272,260,275,79]

def crop_gif_files(src_path, tgt_path):
    for filename in tqdm(os.listdir(src_path)):
        vid = filename.replace('.gif', '')
        if not int(vid) in vids:
            continue
        if filename.endswith('.gif'):
            clip = mp.VideoFileClip(os.path.join(src_path, filename))
            # clip = clip.resize(0.5)
            clip.write_gif(os.path.join(tgt_path, filename))

for model in models:
    tgt_path = f'{model}_crop'
    if not os.path.exists(tgt_path):
        os.makedirs(tgt_path)
    crop_gif_files(src_path=model, tgt_path=tgt_path)