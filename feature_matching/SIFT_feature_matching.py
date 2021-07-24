#!/usr/bin/env python3

import sys
import os
import cv2
import matplotlib.pyplot as plt


def compare_two(path_a, path_b):
    '''this method returns a 'percent match' statistic for two images through
    feature matching, given the path to each image. the images compared can be
    rotationally and/or scale variant, as this method is implemented through
    SIFT. the 'percent match' statistic is computed as the ratio of deemed
    'good matches' to the total number of extracted features.'''

    print('A')

    # reads in the two images
    img1 = cv2.imread(path_a, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(path_b, cv2.IMREAD_GRAYSCALE)

    # shows the two images that are read in
    plt.imshow(img1, cmap='gray')
    plt.show()
    plt.imshow(img2, cmap='gray')
    plt.show()

    # initiates the SIFT detector
    sift = cv2.SIFT_create()

    # finds the keypoints and descriptors
    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    # FLANN parameters
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm=FLANN_INDEX_KDTREE, trees=5)
    search_params = dict(checks=50)   # or pass empty dictionary
    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    # for use in determining the final test statistic
    total = len(matches)
    match = 0

    # need to draw only good matches, so create a mask
    matches_mask = [[0, 0] for i in range(len(matches))]

    # ratio test as per Lowe's paper, set at 0.7 - rejects almost all false
    # matches while losing only a minimal percentage of true matches
    for i, (m, n) in enumerate(matches):
        if m.distance < 0.7*n.distance:
            matches_mask[i] = [1, 0]
            match += 1

    # sets parameters and draws an image representation of the feature matches
    # between the two images
    draw_params = dict(matchColor=(0, 255, 0),
                       singlePointColor=(255, 0, 0),
                       matchesMask=matches_mask,
                       flags=cv2.DrawMatchesFlags_DEFAULT)
    img3 = cv2.drawMatchesKnn(img1, kp1, img2, kp2, matches,
                              None, **draw_params)
    plt.imshow(img3), plt.show()

    # saves the new image in the current folder with a name corresponding to
    # the input images names and data about the final output match
    name1 = (path_a.split('/')[-1]).split('.')[0]
    name2 = (path_b.split('/')[-1]).split('.')[0]
    plt.imsave('{0}_{1}_{2}_{3}_{4}.png'.format(name1, name2, match, total,
               round(match/total, 4)), img3)

    # prints data about the strength  between the two images
    print('  - good matches:', match)
    print('  - total features:', total)
    print('  - percentage:', round(match/total, 4))

    # returns the match statistic to two decimal places
    return round(match/total, 2)


def get_ls(path):
    '''returns a list of the naames of the .tif files in a folder'''
    temp = os.getcwd()
    os.chdir(path)
    files = os.popen('ls')
    os.chdir(temp)
    files = list(filter(lambda s: s[-4:] == '.tif',
                 map(lambda s: s.strip(), files)))
    return files


def __init__():
    print('b')
    args = sys.argv[1:]
    print(compare_two(args[0], args[1]))


if __name__ == '__init__':
    __init__()
