from psychopy import visual, core, event, gui, data, sound, logging
import sys
import os
import glob
import csv
import datetime
import random

# Path to working directory
directory = os.getcwd()

# Get subjID
subjDlg=gui.Dlg(title="JOCN paper- rate items")
subjDlg.addField('Enter Subject ID: ')
subjDlg.show()
subj_id=subjDlg.data[0]

if len(subj_id)<1: # Make sure participant entered name
    core.quit()

# Initialzing Window, insruction, and thank you screens
win = visual.Window(fullscr=True, size=[1100, 800], units='pix', monitor='testMonitor', color = [-.9,-.9,-.9])
instruction_screen = visual.TextStim(win, text="""Rate how much you prefer the items by clicking on the rating line.
                                     \nPress \'Enter\' or click the button below the line to move on to the next item.
                                     \nThe rating is from: \n  1 (little to no preference)\n  to 7 (very high preference).
                                      \n Press any key to start""")
thank_you_screen = visual.TextStim(win, text="""Thank you for choosing!""")

# Show instruction screen
event.clearEvents()
instruction_screen.draw()
win.flip()

# Lets participant quit at any time by pressing escape button
if 'escape' in event.waitKeys():
    core.quit()

# Initialize image list
imageList = [os.path.join(directory, image) for image in
                 glob.glob('images/*.jpg')]
# Randomize order of images
random.shuffle(imageList)

# Initializing response list same size as imageList
ratings = [''] * len(imageList)
familiarity = [''] * len(imageList)

# Initializing rating scale
ratingScale = visual.RatingScale(win, name='Preference', choices=['1', '2', '3', '4', '5', '6', '7'], pos=[-500,-200])
familiarityScale = visual.RatingScale(win, name='familiarity', choices=['1', '2', '3', '4', '5', '6', '7'], pos =[500,-200])
ratingTitle=visual.TextBox(window=win, 
                         text='Preference',
                         font_size=40,
                         font_color=[1,1,1], 
                         size=(1.9,.3),
                         pos=(-.54,-.3), 
                         grid_horz_justification='center',
                         units='norm',
                         )
familiarityTitle=visual.TextBox(window=win, 
                         text='familiarity',
                         font_size=40,
                         font_color=[1,1,1], 
                         size=(1.9,.3),
                         pos=(.54,-.3), 
                         grid_horz_justification='center',
                         units='norm',
                         )

# Main Loop
for image in imageList:
    # The size parameter rescales images.
    # Stretch can be mitigated by cropping images to a resolution that would scale to the specified one bellow.
    myItem = visual.ImageStim(win=win, image=image, units='pix', pos=[0, 200], size = [300,300])
    ratingScale.reset(); familiarityScale.reset()  # reset between repeated uses of the same scale
    ratingScale.setDescription('Preference')
    familiarityScale.setDescription('Familiarity')
    event.clearEvents()
    while ratingScale.noResponse or familiarityScale.noResponse:
        myItem.draw()
        ratingScale.draw()
        familiarityScale.draw()
        ratingTitle.draw()
        familiarityTitle.draw()
        win.flip()
        if event.getKeys(['escape']):
            core.quit()
    ''' Additional pause after both ratings:
    myItem.draw()
    ratingScale.draw()
    familiarityScale.draw()
    ratingTitle.draw()
    familiarityTitle.draw()
    win.flip(); core.wait(0.35) # Brief pause
    '''
    # assigns response to corresponding image
    ratings[imageList.index(image)] = ratingScale.getRating()
    familiarity[imageList.index(image)] = familiarityScale.getRating()
    
    win.flip()
    core.wait(0.35)  # brief pause, slightly smoother for the subject



# Write to .csv file with participants name, subj_id, in file name
f=open( subj_id + ' task a results.csv','w')
for i in range(0,len(imageList)):
    # Remove filepath from imageList[i] string
    picName = os.path.relpath(imageList[i], '..\..\JOCN\task a\images\\') #..\..\JOCN\task a\images\
    f.write(picName +','+ratings[i]+','+familiarity[i]+"\n")
f.close()

# Thank participant
thank_you_screen.draw()
win.flip()
core.wait(1.5)
