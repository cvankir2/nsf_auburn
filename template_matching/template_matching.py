import cv2 as cv
from matplotlib import pyplot as plt
import math


def find_distance(start, end):
    '''finds distance between two 2D coordinates'''
    distance = math.sqrt(math.pow(start[0]-end[0], 2) +
                         math.pow(start[1]-end[1], 2))
    print('find euclian distance', distance)
    return distance


def find_mmp_pi(altitude):
    ''' returns meters per pixel with altitude (meters) input. this
    function is based on specifications for Raspberry Pi+ Camera v1.3.
    image resoluton is 640x480 pixels, FOC_X = 53.50 & FOC_Y = 41.41'''
    radians = (53.50/2)*math.pi/180
    distance = math.tan(radians)*altitude
    mmp = distance/320
    return mmp


def find_mmp(altitude):
    ''' returns meters per pixel with altitude (meters) input. this
    function is based on specifications for Phantom Camera'''
    radians = (94/2)*math.pi/180
    print('radians', radians)
    distance = altitude * math.tan(radians)
    print('tan(radians)', math.tan(radians))
    print('altitude', altitude)
    print('distance', distance)
    mmp = distance/2500
    print('mmp', mmp)
    return mmp


def find_mps(seconds, altitude, pathStart, pathEnd):
    '''returns speed in meters per second'''

    # loads in timing photos taken from UAV imagery
    img1 = cv.imread(pathStart, cv.IMREAD_GRAYSCALE)
    img2 = cv.imread(pathEnd, cv.IMREAD_GRAYSCALE)

    # creates and saves template from the first photo
    x, y = img1.shape
    print(x, y)
    a, b = int(x*0.3334), int(x*0.6667)
    c, d = int(y*0.3334), int(y*0.6667)
    template = img1[a:b, c:d].copy()
    plt.imsave('template_a_b_c_d.jpg', template)
    midpoint_template = ((a+b)/2, (c+d)/2)

    # this loops through three different methods of determining
    # matching location of the template within second photo and
    # finds an overall average best-fit rectangle midpoint
    avgMidpoint_match = (0, 0)
    methods = ['cv.TM_CCOEFF_NORMED', 'cv.TM_CCORR_NORMED']
    #            'cv.TM_SQDIFF_NORMED']
    w, h = template.shape[::-1]
    for meth in methods:
        img = img2.copy()
        method = eval(meth)
        # Apply template Matching
        res = cv.matchTemplate(img, template, method)
        min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if method == 'cv.TM_SQDIFF_NORMED':
            top_left = min_loc
        else:
            top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        # cv.rectangle takes in args (img,start_point,end_point,color,width)
        cv.rectangle(img, top_left, bottom_right, 255, 10)
        plt.imsave('{0}_template_match.png'.format(meth), img)
        avgMidpoint_match = (avgMidpoint_match[0]+top_left[1]+bottom_right[1],
                             avgMidpoint_match[1]+top_left[0]+bottom_right[0])
    avgMidpoint_match = (avgMidpoint_match[0]/(2*len(methods)),
                         avgMidpoint_match[1]/(2*len(methods)))
    print('avg midpoint match', avgMidpoint_match)
    print('midpoint template', midpoint_template)

    # from coordinates of initial template in first photo and
    # coordinates of template found in second photo, determines
    # the approximate amount of distance traveled
    pixels = find_distance(midpoint_template, avgMidpoint_match)
    meters_per_pixel = find_mmp(altitude)
    return round((pixels*meters_per_pixel)/seconds, 5)


print('meters per second: ', find_mps())
