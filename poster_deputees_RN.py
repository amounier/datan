# -*- coding: utf-8 -*-

import os
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
from matplotlib import font_manager
from unidecode import unidecode

# Read the CSV file into a pandas DataFrame
df = pd.read_csv("output/RN_deputees_information.csv")

# Get the list of deputy IDs
deputy_ids = df["Deputy ID"].tolist()
deputy_names = df["Name"].tolist()
deputy_constituency = df["Constituency_no_code"].tolist()
first_2_deputy_ids = deputy_ids[:2]
first_2_deputy_names = deputy_names[:2]
first_2_deputy_const = deputy_constituency[:2]

# Set the background color (RGB values)
background_color = np.array([0.01, 0.01, 0.25])  # Dark blue

# Set the figure size
fig_width = 8
fig_height = 8

x_pos_text = 0.05
x_pos_cicles = 0.8

big_title = "Mon député RN,\n cette année c'était...".upper()
# font_props = {'family': 'monospace', 'style': 'italic', 'weight': 'bold'}
# Load the "Trial Bold" font
trial_bold_font = font_manager.FontProperties(fname="fonts/Font-Trial-Bold.otf")

# Iterate over the deputy IDs
for deputy_id, deputy_name, deputy_const in zip(first_2_deputy_ids, first_2_deputy_names, first_2_deputy_const):
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

    # Add the big title
    big_title_André = unidecode(f"M. {deputy_name}\n député\n {deputy_const} a voté".upper())
    fig.suptitle(big_title_André, fontsize=46, fontweight='bold', color='white', fontproperties=trial_bold_font, y=0.88)

    # Plot the image
    ax.imshow(image_array.astype(np.uint8),alpha=.55)
    # ax.set_title(f"Deputy ID: {deputy_id}", fontsize=16)
    # Add new lines of text
    nb_votes = 5
    ax.text(x_pos_text, nb_votes*0.1, "Blablablablablabla".upper(), fontsize=32, color="white", transform=ax.transAxes, fontproperties=trial_bold_font)
    ax.scatter(x_pos_cicles, nb_votes*0.1+0.02, s=1800, c="green", marker="o", transform=ax.transAxes, linewidths=1, edgecolors="white")
    ax.text(x_pos_text, nb_votes*0.1-0.1, "Blablablablablabla".upper(), fontsize=32, color="white", transform=ax.transAxes, fontproperties=trial_bold_font)
    ax.scatter(x_pos_cicles, nb_votes*0.1-0.1+0.02, s=1800, c="green", marker="o", transform=ax.transAxes, linewidths=1, edgecolors="white")
    ax.text(x_pos_text, nb_votes*0.1-0.2, "Blablablablablabla".upper(), fontsize=32, color="white", transform=ax.transAxes, fontproperties=trial_bold_font)
    ax.scatter(x_pos_cicles, nb_votes*0.1-0.2+0.02, s=1800, c="green", marker="o", transform=ax.transAxes, linewidths=1, edgecolors="white")
    ax.text(x_pos_text, nb_votes*0.1-0.3, "Blablablablablabla".upper(), fontsize=32, color="white", transform=ax.transAxes, fontproperties=trial_bold_font)
    ax.scatter(x_pos_cicles, nb_votes*0.1-0.3+0.02, s=1800, c="green", marker="o", transform=ax.transAxes, linewidths=1, edgecolors="white")
    ax.text(x_pos_text, nb_votes*0.1-0.4, "Blablablablablabla".upper(), fontsize=32, color="white", transform=ax.transAxes, fontproperties=trial_bold_font)
    ax.scatter(x_pos_cicles, nb_votes*0.1-0.4+0.02, s=1800, c="green", marker="o", transform=ax.transAxes, linewidths=1, edgecolors="white")
    ax.axis("off")

    # Save the image
    plt.savefig(f"output/posters_deputees/poster_{deputy_id}.png", dpi=300, bbox_inches="tight")
    plt.close(fig)

print("Poster images created successfully.")