# FETV

**FETV** is a benchmark for **F**ine-grained **E**valuation of open-domain **T**ext-to-**V**ideo generation

## Overview
FETV consist of a diverse set of text prompts, categorized based on three orthogonal aspects: major content, attribute control, and prompt complexity.
![](./Figures/categorization.png)

## Data Statistics
FETV contains 619 text prompts. The data distributions over different categories are as follows
![](./Figures/content_attribute_statistics.eps)

## Data Format
All FETV data are all available in the file `fetv_data.json`. Each line is a data instance, which is formatted as:
```
{
  "video_id": 1006807024, 
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
  "video_url": "https://ak.picdn.net/shutterstock/videos/1006807024/preview/stock-footage-a-mountain-stream.mp4"
  }
```

## License
This dataset is under [CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/) license.
