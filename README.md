# Image Sequence Renderer
The animation software Krita requires an ffmpeg to render animations as videos. Ffmpeg is no longer available, so animatons can no longer be rendered as videos, but instead as a folder of images. This program converts that folder of images into an mp4 video (AVI is also supported.

## Installation
Python 3.6 or higher

#### Install requirements
`pip install opencv-python`

## Usage
1. Place animation/video frame folder in directory

![image_1](https://github.com/osHamad/image_sequence_renderer/blob/master/readme_images/image_1.png?raw=true)

2. Change `settings.csv` file to match the animation/video settings

![image_2](https://github.com/osHamad/image_sequence_renderer/blob/master/readme_images/image_2.png?raw=true)

3. Run `convert.py`

![image_3](https://github.com/osHamad/image_sequence_renderer/blob/master/readme_images/image_3.png?raw=true)

4. Your frame folder should be converted to a video type file, named as the name specified in `settings.csv`

![image_4](https://github.com/osHamad/image_sequence_renderer/blob/master/readme_images/image_4.png?raw=true)
