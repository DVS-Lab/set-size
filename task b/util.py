import os, glob, random, csv
import pandas as pd
# Returns list containing sorted images
# Index: 0 = highPrefImages, 1 = highPrefHighFamImages, 2 = lowPrefImages, 3 = lowPrefHighFamImages, 4 = highFamImages
# Example Input: 'fgdf task a results.csv'

def imageSorter(ratedImages):
    df=pd.read_csv('103_task_a_results.csv',
               names = ["Image", "Preference", "Familiarity"])

    #FINDING MAX AND MIN
    max_rating = df['Preference'].max()
    min_rating = df['Preference'].min()

    high_pref_fam_images= df.loc[df['Preference'].isin([max_rating]) & df['Familiarity'].isin([4,5,6,7]), 'Image']
    high_pref_fam_images_list = high_pref_fam_images.tolist()
    offset = 1;
    while len(high_pref_fam_images_list) < 12:
        high_pref_fam_images= df.loc[df['Preference'].isin([max_rating]) & df['Familiarity'].isin([4,5,6,7]), 'Image']
        high_pref_fam_images_list += high_pref_fam_images.tolist()

    low_pref_fam_images= df.loc[df['Preference'].isin([min_rating]) & df['Familiarity'].isin([4,5,6,7]), 'Image']
    low_pref_fam_images_list = low_pref_fam_images.tolist()
    offset = 1;
    while len(low_pref_fam_images_list) < 12:
        low_pref_fam_images= df.loc[df['Preference'].isin([min_rating+offset]) & df['Familiarity'].isin([4,5,6,7]), 'Image']
        low_pref_fam_images_list += low_pref_fam_images.tolist()

    images = []
    images.append(high_pref_fam_images_list)
    images.append(low_pref_fam_images_list)

    return images
