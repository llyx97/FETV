# FETV

This repository contains 
- [The **FETV** benchmark for **F**ine-grained **E**valuation of open-domain **T**ext-to-**V**ideo generation](#fetv)
- [Manual evaluation results of text-to-video generation models](#manual_eval)
- [Diagnosis of automatic text-to-video generation metrics](#auto_eval)

<a href='https://arxiv.org/abs/2311.01813'><img src='https://img.shields.io/badge/ArXiv-2311.01813-red'></a>


## <span id="fetv"> FETV Benchmark </span>

### Overview
FETV consist of a diverse set of text prompts, categorized based on three orthogonal aspects: **major content**, **attribute control**, and **prompt complexity**. This enables fine-grained evaluation of T2V generation models.
![](./Figures/categorization.png)

### Data Instances
All FETV data are all available in the file `fetv_data.json`. Each line is a data instance, which is formatted as:
```
{
  "video_id": "1006807024", 
  "prompt": "A mountain stream", 
  "major content": {
       "spatial": ["scenery & natural objects"], 
       "temporal": ["fluid motions"]
     }, 
  "attribute control": {
      "spatial": null, 
      "temporal": null
    }, 
  "prompt complexity": ["simple"], 
  "source": "WebVid", 
  "video_url": "https://ak.picdn.net/shutterstock/videos/1006807024/preview/stock-footage-a-mountain-stream.mp4",
  "unusual type": null
  }
```
**Temporal Major Contents**
![](./Figures/example_temporal_content.png)
**Temporal Attributes to Control**
![](./Figures/example_temporal_attribute.png)
**Spatial Major Contents**
![](./Figures/example_spatial_content.png)
**Spatial Attributes to Control**
![](./Figures/example_spatial_attribute.png)

### Data Fields
* "video_id": The video identifier in the original dataset where the prompt comes from.
* "prompt": The text prompt for text-to-video generation.
* "major content": The major content described in the prompt.
* "attribute control": The attribute that the prompt aims to control.
* "prompt complexity": The complexity of the prompt.
* "source": The original dataset where the prompt comes from, which can be "WebVid", "MSRVTT" or "ours".
* "video_url": The url link of the reference video.
* "unusual type": The type of unusual combination the prompt involves. Only available for data instances with `"source": "ours"`.

### Dataset Statistics
FETV contains 619 text prompts. The data distributions over different categories are as follows (the numbers over categories do not sum up to 619 because a data instance can belong to multiple categories)
![](./Figures/content_attribute_statistics.png)
![](./Figures/complexity_statistics.png)

## <span id="manual_eval"> Manual Evaluation of Text-to-video Generation Models </span>
We evaluate four T2V models, namely CogVideo, Text2Video-zero, ModelScopeT2V and ZeroScope. The generated and ground-truth videos are manually evaluated from four perspectives: **static quality**, **temporal quality**, **overall alignment** and **fine-grained alignment**.

## <span id="auto_eval"> Diagnosis of Automatic Text-to-video Generation Metrics </span>

## License
This dataset is under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.

## Citation
```bibtex
@article{liu2023fetv,
  title   = {FETV: A Benchmark for Fine-Grained Evaluation of Open-Domain Text-to-Video Generation},
  author  = {Yuanxin Liu and Lei Li and Shuhuai Ren and Rundong Gao and Shicheng Li and Sishuo Chen and Xu Sun and Lu Hou},
  year    = {2023},
  journal = {arXiv preprint arXiv: 2311.01813}
}
```
