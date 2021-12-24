import features

def do_it(path = 'input_image/room.jpeg'):
    features.squareify(path)
    features.detectAndFill('input_image/squareified/squareImage.png')
    features.chop('input_image/object_detect/detect.png')
    check = features.checkGreen()
    features.chop('input_image/squareified/squareImage.png')
    return check