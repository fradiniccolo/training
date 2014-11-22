#!/usr/bin/env python
import optparse
import cv2
import numpy
import sys


def get_parameters(filename):
    ext = filename.split('.')[-1]

    if ext == 'mp4':
        with open(filename, 'r') as video:

            #
            # Capture video from file.
            # http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture
            capture = cv2.VideoCapture(video.name)

        #
        # flag:
        #   0 if error occurs.
        #   1 if no error occurs.
        flag, frame = capture.read()

        if flag == 0:
            writer.release()
        else:
            ext = str(video.name).split('.')[-1]
            basename = str(video.name).split('.')[-2]

            #
            # method:
            #    numpy.size(input, axis)
            # parameter:
            #    axis can be
            #    - 0 for y-axis
            #    - 1 for x-axis
            #
            height = numpy.size(frame, 0)
            width = numpy.size(frame, 1)

            # FOURCC Codec: http://www.fourcc.org/codecs.php
            # (*'HFYU') #(*'XVID')
            fourcc = cv2.cv.CV_FOURCC(*'XVID')

            return capture, height, width, fourcc, basename, ext


#
# Extract red channel from video
def extract_red_channel(filename):
    capture, height, width, fourcc, basename, ext = get_parameters(filename)

    #
    # Create object writer with parameters.
    # http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#videowriter
    writer = cv2.VideoWriter(
        filename='RED_{}.{}'.format(basename, ext),
        fourcc=fourcc,
        fps=20,
        frameSize=(width, height),
        isColor=1)

    while writer.isOpened():
        flag, frame = capture.read()

        if flag == 0:
            writer.release()
        else:
            #
            # Set to zero all vector's items.
            red_frame = numpy.zeros((
                frame.shape[0],   # G
                frame.shape[1],   # B
                frame.shape[2]),  # R
                dtype=frame.dtype)
            #
            # Substitute the third red_frame vector
            # with the original third frame vector.
            # Now G and B channels are set to 0.
            red_frame[:,:,2] = frame[:,:,2]

            writer.write(red_frame)

    return "Extraction completed!"


#
# Extract green channel from video
def extract_green_channel(filename):
    capture, height, width, fourcc, basename, ext = get_parameters(filename)

    #
    # Create object writer with parameters.
    # http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#videowriter
    writer = cv2.VideoWriter(
        filename='GREEN_{}.{}'.format(basename, ext),
        fourcc=fourcc,
        fps=20,
        frameSize=(width, height),
        isColor=1)

    while writer.isOpened():
        flag, frame = capture.read()

        if flag == 0:
            writer.release()
        else:
            #
            # Set to zero all vector's items.
            green_frame = numpy.zeros((
                frame.shape[0],    # B
                frame.shape[1],    # G
                frame.shape[2]),   # R
                dtype=frame.dtype)
            #
            # Substitute the second green_frame vector
            # with the original second frame vector.
            # Now R and B channels are set to 0.
            green_frame[:,:,1] = frame[:,:,1]

            writer.write(green_frame)

    return "Extraction completed!"


#
# Extract blue channel from video
def extract_blue_channel(filename):
    capture, height, width, fourcc, basename, ext = get_parameters(filename)

    #
    # Create object writer with parameters.
    # http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#videowriter
    writer = cv2.VideoWriter(
        filename='BLUE_{}.{}'.format(basename, ext),
        fourcc=fourcc,
        fps=20,
        frameSize=(width, height),
        isColor=1)

    while writer.isOpened():
        flag, frame = capture.read()

        if flag == 0:
            writer.release()

        else:
            #
            # Set to zero all vector's items.
            blue_frame = numpy.zeros((
                frame.shape[0],    # B
                frame.shape[1],    # G
                frame.shape[2]),   # R
                dtype=frame.dtype)
            #
            # Substitute the 0 blue_frame vector
            # with the original 0 frame vector.
            # Now G and R channels are set to 0.
            blue_frame[:,:,0] = frame[:,:,0]

            writer.write(blue_frame)

    return "Extraction completed!"


#
# Extract red and green channel from video
def extract_red_green_channel(filename):
    capture, height, width, fourcc, basename, ext = get_parameters(filename)

    #
    # Create object writer with parameters.
    # http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#videowriter
    writer = cv2.VideoWriter(
        filename='RG_{}.{}'.format(basename, ext),
        fourcc=fourcc,
        fps=20,
        frameSize=(width, height),
        isColor=1)

    while writer.isOpened():
        flag, frame = capture.read()

        if flag == 0:
            writer.release()

        else:
            #
            # Set to zero all vector's items.
            rg_frame = numpy.zeros((
                frame.shape[0],    # B
                frame.shape[1],    # G
                frame.shape[2]),   # R
                dtype=frame.dtype)
            #
            # Substitute the 0 rg_frame vector
            # with the original 0 frame vector.
            # Now B is set to 0.
            rg_frame[:,:,2] = frame[:,:,2]
            rg_frame[:,:,1] = frame[:,:,1]

            writer.write(rg_frame)

    return "Extraction completed!"


#
# Extract red and blue channel from video
def extract_red_blue_channel(filename):
    capture, height, width, fourcc, basename, ext = get_parameters(filename)

    #
    # Create object writer with parameters.
    # http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#videowriter
    writer = cv2.VideoWriter(
        filename='RB_{}.{}'.format(basename, ext),
        fourcc=fourcc,
        fps=20,
        frameSize=(width, height),
        isColor=1)

    while writer.isOpened():
        flag, frame = capture.read()

        if flag == 0:
            writer.release()

        else:
            #
            # Set to zero all vector's items.
            rb_frame = numpy.zeros((
                frame.shape[0],    # B
                frame.shape[1],    # G
                frame.shape[2]),   # R
                dtype=frame.dtype)
            #
            # Substitute the 0 rg_frame vector
            # with the original 0 frame vector.
            # Now G is set to 0.
            rb_frame[:,:,2] = frame[:,:,2]
            rb_frame[:,:,0] = frame[:,:,0]

            writer.write(rb_frame)

    return "Extraction completed!"


#
# Extract green and blue channel from video
def extract_green_blue_channel(filename):
    capture, height, width, fourcc, basename, ext = get_parameters(filename)

    #
    # Create object writer with parameters.
    # http://docs.opencv.org/modules/highgui/doc/reading_and_writing_images_and_video.html#videowriter
    writer = cv2.VideoWriter(
        filename='GB_{}.{}'.format(basename, ext),
        fourcc=fourcc,
        fps=20,
        frameSize=(width, height),
        isColor=1)

    while writer.isOpened():
        flag, frame = capture.read()

        if flag == 0:
            writer.release()

        else:
            #
            # Set to zero all vector's items.
            gb_frame = numpy.zeros((
                frame.shape[0],    # B
                frame.shape[1],    # G
                frame.shape[2]),   # R
                dtype=frame.dtype)
            #
            # Substitute the 0 rg_frame vector
            # with the original 0 frame vector.
            # Now G is set to 0.
            gb_frame[:,:,1] = frame[:,:,1]
            gb_frame[:,:,0] = frame[:,:,0]

            writer.write(gb_frame)

    return "Extraction completed!"


def Main():
    parser = optparse.OptionParser('usage: python extract_rgb.py [-r] [-g] [-b] [-x] [-y] [-z] <target video>')
    parser.add_option('-r', dest='extract_red_channel', help='extract red channel from video')
    parser.add_option('-g', dest='extract_green_channel', help='extract green channel from video')
    parser.add_option('-b', dest='extract_blue_channel', help='extract blue channel from video')
    parser.add_option('-x', dest='extract_red_green_channel', help='extract red and green channel from video')
    parser.add_option('-y', dest='extract_red_blue_channel', help='extract red and blue channel from video')
    parser.add_option('-z', dest='extract_green_blue_channel', help='extract green and blue channel from video')

    (options, args) = parser.parse_args()

    if options.extract_red_channel:
        print extract_red_channel(options.extract_red_channel)
    elif options.extract_green_channel:
        print extract_green_channel(options.extract_green_channel)
    elif options.extract_blue_channel:
        print extract_blue_channel(options.extract_blue_channel)
    elif options.extract_red_green_channel:
        print extract_red_green_channel(options.extract_red_green_channel)
    elif options.extract_red_blue_channel:
        print extract_red_blue_channel(options.extract_red_blue_channel)
    elif options.extract_green_blue_channel:
        print extract_green_blue_channel(options.extract_green_blue_channel)

    else:
        print parser.usage
        exit(0)

    
if __name__ == '__main__':
    Main()
