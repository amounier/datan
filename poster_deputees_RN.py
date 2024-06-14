import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("output/RN_deputees_information.csv")

# Get the list of deputy IDs
deputy_ids = df["Deputy ID"].tolist()
first_2_deputees = deputy_ids[:2]

# Set the background color (RGB values)
background_color = np.array([0.075, 0.075, 0.3])  # Dark blue

# Set the figure size
fig_width = 8
fig_height = 8

# Iterate over the deputy IDs
for deputy_id in first_2_deputees:
    # Load the image
    image_path = os.path.join("output/RN_deputees_img", f"{deputy_id}.png")
    image = Image.open(image_path).convert("RGBA")

    # Convert the image to a numpy array
    image_array = np.array(image)

    # Convert grayscale + alpha to RGB + alpha
    if image_array.shape[-1] == 2:
        grayscale = image_array[:, :, 0]
        alpha = image_array[:, :, 1]
        image_array = np.dstack((grayscale, grayscale, grayscale, alpha))

    # Add the background color to the image
    rgb = image_array[:, :, :3]
    rgb = rgb * (1 - background_color) + background_color * 255
    image_array = np.dstack((rgb, image_array[:, :, 3]))

    # Create a new figure
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), facecolor=background_color)

    # Plot the image
    ax.imshow(image_array.astype(np.uint8),alpha=.55)
    # ax.set_title(f"Deputy ID: {deputy_id}", fontsize=16)
    ax.axis("off")

    # Save the image
    plt.savefig(f"output/posters_deputees/poster_{deputy_id}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

print("Poster images created successfully.")