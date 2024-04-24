from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import random

def split_image(image):
    height, width = image.shape
    share1 = np.zeros((height, width), dtype=np.uint8)
    share2 = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            if image[i, j] == 255:
                u1 = random.choice([(0, 1), (1, 0)])
                u2 = u1
            else:
                u1 = random.choice([(1, 0), (0, 1)])
                u2 = (1 - u1[0], 1 - u1[1])
            share1[i, j] = u1[0]
            share2[i, j] = u2[0]
    return share1, share2

def combine_shares(share1, share2):
    height, width = share1.shape
    combined_image = np.zeros((height, width), dtype=np.uint8)
    for i in range(height):
        for j in range(width):
            if share1[i, j] == share2[i, j]:
                combined_image[i, j] = share1[i, j]
            else:
                combined_image[i, j] = 0
    return combined_image

def load_image(file_path):
    image = Image.open(file_path).convert('L')
    return np.array(image)

def show_results(image):
    share1, share2 = split_image(image)
    combined_image = combine_shares(share1, share2)
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 4, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Oryginalny obraz')

    plt.subplot(1, 4, 2)
    plt.imshow(share1, cmap='gray')
    plt.title('Udział 1')

    plt.subplot(1, 4, 3)
    plt.imshow(share2, cmap='gray')
    plt.title('Udział 2')

    plt.subplot(1, 4, 4)
    plt.imshow(combined_image, cmap='gray')
    plt.title('Złożony obraz')

    plt.show()

if __name__ == "__main__":
    image = load_image("test.jpg")
    show_results(image)
