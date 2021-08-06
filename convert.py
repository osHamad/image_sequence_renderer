import cv2 as cv
import os


def to_video(image_sequence):
    for num in image_sequence:

        height, width, layers = num.shape
        size = (width, height)

    out = cv.VideoWriter('output.mp4', cv.VideoWriter_fourcc(*'mp4v'), 15, size)

    for i in image_sequence:
        out.write(i)
    out.release()


def main():
    # name of the image sequence dir
    dir_name = 'heart_pound'
    image_sequence = []

    # check if the dir with the image sequence exists
    if os.path.isdir(dir_name):
        image_files = os.listdir(dir_name)

        for image in image_files:

            image_sequence.append(cv.imread(f'{dir_name}/{image}'))

        to_video(image_sequence)


    else:
        print('Error: Image directory not found. Ensure that directory is in path.')



if __name__ == '__main__':
    main()
