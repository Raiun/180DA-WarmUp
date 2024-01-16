# Histogram and KMeans color calculation based on the example provided by: https://code.likeagirl.io/finding-dominant-colour-on-an-image-b4e075f98097

import cv2
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


def find_histogram(clt):
    """
    create a histogram with k clusters
    :param: clt
    :return:hist
    """
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    hist = hist.astype("float")
    hist /= hist.sum()

    return hist

def plot_colors2(hist, centroids):
    bar = np.zeros((50, 300, 3), dtype="uint8")
    startX = 0

    for (percent, color) in zip(hist, centroids):
        # plot the relative percentage of each cluster
        endX = startX + (percent * 300)
        rgb_color = (int(color[2]), int(color[1]), int(color[0]))
        cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), rgb_color, -1)

        startX = endX

    # return the bar chart
    return bar

###########
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Draw a box on the frame
    box_color = (0, 255, 0)  # Green color in BGR
    box_thickness = 2
    cv2.rectangle(frame, (200, 150), (400, 400), box_color, box_thickness)

    # Display the resulting frame
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Display the resulting frame
    cv2.imshow("Color Tracking", frame)

    # Track only pixels within bounds of the box
    # Convert pixel frames to 2D array
    pixels = frame[170:380, 220:380].reshape((-1, 3))
                                              
    clt = KMeans(n_clusters=3, n_init=1)
    clt.fit(pixels)

    hist = find_histogram(clt)
    bar = plot_colors2(hist, clt.cluster_centers_)

    plt.pause(0.01)
    plt.axis("off")
    plt.imshow(bar)

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()