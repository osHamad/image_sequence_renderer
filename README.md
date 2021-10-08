# Image Sequence Renderer
The animation software Krita requires an ffmpeg to render animations as videos. Ffmpeg is no longer available, so animatons can no longer be rendered as videos, but instead as a folder of images. This program converts that folder of images into an mp4 video (AVI is also supported.

## Installation
Python 3.6 or higher

#### Install requirements
`pip install opencv-python`

## Usage
1. Place animation/video frame folder in directory
2. Change `settings.csv` file to match the animation/video settings
3. Run `convert.py`
4. Your frame folder should be converted to a video type file, named as the name specified in `settings.csv`
