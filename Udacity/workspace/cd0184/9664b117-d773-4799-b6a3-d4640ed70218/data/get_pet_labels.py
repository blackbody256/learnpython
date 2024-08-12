#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Akanga Andrew
# DATE CREATED: 29/07/2024                         
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
      image_dir - The (full) path to the folder of images that are to be
                  classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as pet image filename (string) and 'value' as a 
                    List containing one item - the pet image label (string).
    """
    # Creates an empty dictionary named results_dic
    results_dic = dict()

    # Retrieve the filenames from the specified directory
    filename_list = listdir(image_dir)

    # Processes each filename to extract pet labels
    for filename in filename_list:
        low_pet_image = filename.lower()  # Convert filename to lower case
        word_list_pet_image = low_pet_image.split("_")  # Split by '_'
        pet_name = ""  # Initialize pet_name string

        for word in word_list_pet_image:
            if word.isalpha():  # Check if the word contains only alphabetic characters
                pet_name += word + " "  # Append word with trailing space

        pet_name = pet_name.strip()  # Remove leading/trailing spaces

        # Add to dictionary
        if filename not in results_dic:
            results_dic[filename] = [pet_name]  # Create list with pet_name

    return results_dic