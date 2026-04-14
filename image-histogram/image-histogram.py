def image_histogram(image):
    """
    Compute the intensity histogram of a grayscale image.
    """
    # Write code here
    historgram = [0] * 256

    for row in image:
        for pixel in row:
            historgram[pixel] += 1

    return historgram