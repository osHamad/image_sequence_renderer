import cv2 as cv
import os
from csv import reader


def to_video(image_sequence, output, filetype, codec, fps):
    for num in image_sequence:

        height, width, layers = num.shape
        size = (width, height)

    out = cv.VideoWriter(f'{output}.{filetype}', cv.VideoWriter_fourcc(*codec), fps, size)

    for i in image_sequence:
        out.write(i)
    out.release()


def main():
    image_sequence = []

    with open('settings.csv') as settings:
        settings = list(reader(settings))

    dir_name = settings[0][1]
    output = settings[1][1]
    fps = int(settings[2][1])
    file_type = settings[3][1]
    codec = settings[4][1]

    # check if the dir with the image sequence exists
    if os.path.isdir(dir_name):
        image_files = os.listdir(dir_name)

        for image in image_files:

            image_sequence.append(cv.imread(f'{dir_name}/{image}'))

        to_video(image_sequence, output, file_type, codec, fps)

    else:
        print('Error: Image directory not found. Ensure that directory is in path.')


if __name__ == '__main__':
    main()
