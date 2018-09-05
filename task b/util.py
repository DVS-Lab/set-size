import os, glob, random, csv
# Returns list containing sorted images
# Index: 0 = highPrefImages, 1 = highPrefHighFamImages, 2 = lowPrefImages, 3 = lowPrefHighFamImages, 4 = highFamImages
# Example Input: 'fgdf task a results.csv'

def imageSorter(ratedImages):
    highPrefImages = []
    lowPrefImages = []
    highFamImages = []
    highPrefHighFamImages = []
    lowPrefHighFamImages = []

    with open(ratedImages) as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        for row in csvReader:
            if int(row[1]) > 4:
                highPrefImages.append(row[0])
                if int(row[2]) > 4:
                    highFamImages.append(row[0])
                    highPrefHighFamImages.append(row[0])
            else:
                lowPrefImages.append(row[0])
                if int(row[2]) > 4:
                    highFamImages.append(row[0])
                    lowPrefHighFamImages.append(row[0])

    sortedImages= []
    sortedImages.append(highPrefImages)
    sortedImages.append(highPrefHighFamImages)
    sortedImages.append(lowPrefImages)
    sortedImages.append(lowPrefHighFamImages)
    sortedImages.append(highFamImages)

    sortedImagesFiltered = filter(None, sortedImages)
    return sortedImagesFiltered
