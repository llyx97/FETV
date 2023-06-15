# FETV

**FETV** is a benchmark for **F**ine-grained **E**valuation of open-domain **T**ext-to-**V**ideo generation

## Overview
FETV consist of a diverse set of text prompts, categorized based on three orthogonal aspects: major content, attribute control, and prompt complexity.
![](./Figures/categorization.png)

## Dataset Structure
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

## License
This dataset is under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.
