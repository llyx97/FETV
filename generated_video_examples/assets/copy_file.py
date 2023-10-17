import os, shutil, json

# models = ['cogvideo', 'videofusion', 'text2video-zero', 'gt']
models = ['zeroscope']
vids = {
    'temporal_attribute': {'speed':[491,390,455,574], 'motion_direction':[357,368,374,204], 'event_order':[404,405,407]}, 
    'temporal_major_content': {'actions':[2,6,17,5,256], 'kinetic_motions':[37,149,357,1], 'fluid_motions':[23, 163, 21, 99], 'light_change':[34, 25, 21, 330]},
    'spatial_attribute': {'color':[137,149,157], 'camera_view':[62,122,79,60], 'quantity':[491,272,260,275]}, 
    }

with open('../../fetv_data.json', 'r') as f:
    datas = []
    lines = f.readlines()
    for l in lines:
        datas.append(json.loads(l))
vid_map = {i: d['video_id'] for i,d in enumerate(datas)}


for aspect in vids:
    for catgry in vids[aspect]:
        for model in models:
            tgt_path = os.path.join(aspect, catgry, model)
            src_path = os.path.join(model)
            if not os.path.exists(tgt_path):
                os.makedirs(tgt_path)
            for vid in vids[aspect][catgry]:
                if model=='gt':
                    src_file = os.path.join(src_path, f"{vid_map[vid]}.gif")
                    tgt_file = os.path.join(tgt_path, f"{vid}.gif")
                else:
                    src_file = os.path.join(src_path, f"{vid}.gif")
                    tgt_file = os.path.join(tgt_path, f"{vid}.gif")
                if not os.path.isfile(tgt_file):
                    if not os.path.exists(src_file):
                        print(src_file)
                        continue
                shutil.copy(src_file, tgt_file)