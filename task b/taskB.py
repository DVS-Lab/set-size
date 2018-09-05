from psychopy import visual, event, core, os
import random, glob, util

# Task B for Set Size Study
# Matthew Slipenchuk tuf91673@temple.edu (06/2018)

# Input:
# subject's task a results
# -ex: 'name_task_a_results.csv'
# Output:
# .csv file containing subjects results
# -file name indicates if subject is answering for themselves or confederate.
# -'subject_name_task_b_results.csv' contains 90 Trials and
# -'subject_name_confederate_name2_task_b_results.csv' contains 90 trials.

# Parameters
subj_id = 'name here' # ex: 01, 02, ...
confed_id = '' # Leave as '' to indicate no confederate
choice1Duration = 4.5
choice2Duration = 4.5
tryFasterDuration = 3
delay1Duration = 5
choice2Duration = 5
delay2Duration = 2
postChoiceDuration = 2
postChoice2ScaleDuration = 4
interTrialInterval = 1 # Duration in between trials

# Initalization
directory = os.getcwd()
imageList = util.imageSorter('(Subject ID here) task a results.csv') # Place input, subject's task a results here.
timer = core.Clock()
win = visual.Window(fullscr=True, units='pix', monitor='testMonitor',
        color = [-.9,-.9,-.9])
mouse = event.Mouse()
d = 20; ## distance between ui elements

## Trials: 45 presenting high pref images, and 45 presenting low pref images.
## 1 = high preference, 2 = low preference, trial order is randomized.
itemChoiceAmounts = [2,3,4,6,12]
moneyChoiceAmounts = [2,3,4,6]
moneyList = [0.50, 0.75, 1.00, 1.25, 1.50, 1.75]
highPrefTrials = [1] * 45
lowPrefTrials = [2] * 45
trials = highPrefTrials + lowPrefTrials
random.shuffle(trials)

## Lists holding responses and reaction times for each trial
monetaryOptions = [''] * len(trials)
itemNumberOptions = [''] * len(trials)
choice1Responses = [''] * len(trials)
choice1ReactionTimes = [''] * len(trials)
choice2Responses = [''] * len(trials)
choice2ReactionTimes = [''] * len(trials)
postChoiceSnackRatings = [''] * len(trials)
postChoiceDecisionRatings = [''] * len(trials)
postChoiceReactionTimes = [''] * len(trials)
trialOptions = [''] * len(trials)

###################################################################
## Post choice satisfaction Rating Scale
#satisfactionScale = visual.RatingScale(win, name='satisfaction',
#        choices=['1', '2', '3', '4', '5', '6', '7'], pos=[0,0])
###################################################################

# Initializing rating scale
decisionRatingScale = visual.RatingScale(win, name='Decision', choices=['1', '2', '3', '4', '5', '6', '7'], pos=[-500,-200])
snackRatingScale = visual.RatingScale(win, name='Snack', choices=['1', '2', '3', '4', '5', '6', '7'], pos =[500,-200])
decisionRatingTitle=visual.TextBox(window=win,
                         text='How happy are you with your decision?',
                         font_size=40,
                         font_color=[1,1,1],
                         size=(1.9,.3),
                         pos=(-.54,-.3),
                         grid_horz_justification='center',
                         units='norm',
                         )
snackRatingTitle=visual.TextBox(window=win,
                         text='How do you rate this snack?',
                         font_size=40,
                         font_color=[1,1,1],
                         size=(1.9,.3),
                         pos=(.54,-.3),
                         grid_horz_justification='center',
                         units='norm',
                         )


## 1st choice per trial, to be stored in moneytaryOptions[] and itemNumberOptions[] respectively
## Reinitialized every trial to hold the trials randomly selected choices
monetaryAmount = 0
choiceAmount = 0
option1MoneyPosition = (-(d/2 + 156/2),0)
option1ItemPosition = ((d/2 + 156/2),0)
option1MoneyShapeVertices = [(-(d/2 + 156), -156/2), (-(d/2 + 156), 156/2), (-d/2, 156/2), (-d/2, -156/2)]
option1ItemShapeVertices = [((d/2 + 156), -156/2), ((d/2 + 156), 156/2), (d/2, 156/2), (d/2, -156/2)]
## Textboxes for choice 1
option1Money=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=option1MoneyPosition,
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option1Items=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=option1ItemPosition,
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )

## Target Boxes
##  Overlaying these on the textbox stim because visual textboxs do not
##  have the .isPressedIn() method.
## First choice
option1MoneyShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=option1MoneyShapeVertices, opacity = 0)
option1ItemsShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=option1ItemShapeVertices, opacity = 0)
## Second choice
## Top - left to right
option2Pos1Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160+d+160), d+160/2), (-(d/2 + 160+d+160), d+160/2+160), (-(d/2 + 160+d), d+160/2+160), (-(d/2 + 160+d), d+160/2)])
option2Pos2Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160), d+160/2), (-(d/2 + 160), d+160/2+160), (-(d/2), d+160/2+160), (-(d/2), d+160/2)])
option2Pos3Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2), d+160/2), ((d/2), d+160/2+160), ((d/2 + 160), d+160/2+160), ((d/2 + 160), d+160/2)])
option2Pos4Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2 + 160+d), d+160/2), ((d/2 + 160+d), d+160/2+160), ((d/2 + 160+d+160), d+160/2+160), ((d/2 + 160+d+160), d+160/2)])
## Middle
option2Pos5Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160+d+160), -160/2), (-(d/2 + 160+d+160), 160/2), (-(d/2 + 160+d), 160/2), (-(d/2 + 160+d), -160/2)])
option2Pos6Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160), -160/2), (-(d/2 + 160), 160/2), (-(d/2), 160/2), (-(d/2), -160/2)])
option2Pos7Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2), -160/2), ((d/2), 160/2), ((d/2 + 160), 160/2), ((d/2 + 160), -160/2)])
option2Pos8Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2 + 160+d), -160/2), ((d/2 + 160+d), 160/2), ((d/2 + 160+d+160), 160/2), ((d/2 + 160+d+160), -160/2)])
## Bottom
option2Pos9Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160+d+160), -(d+160/2+160)), (-(d/2 + 160+d+160), -(d+160/2)), (-(d/2 + 160+d), -(d+160/2)), (-(d/2 + 160+d), -(d + 160/2 + 160))])
option2Pos10Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160), -(d+160/2+160)), ((-(d/2 + 160)), -(d+160/2)), (-(d/2), -(d+160/2)), (-(d/2), -(d+160/2+160))])
option2Pos11Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2), -(d+160/2+160)), ((d/2), -(d+160/2)), ((d/2 + 160), -(d+160/2)), ((d/2 + 160), -(d+160/2+160))])
option2Pos12Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2 + 160+d), -(d+160/2+160)), ((d/2 + 160+d), -(d+160/2)), ((d/2 + 160+d+160), -(d+160/2)), ((d/2 + 160+d+160), -(d+160/2+160))])

## Coordinates for ImageStims, origin = (0,0)
xInner = (d/2 + 160/2)
xOuter = (d/2 + 160 + d + 160/2)
y = (160/2 + d + 160/2)

## ImageStim - Initialized with placeholder images
## Top - left to right
option2Item1 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xOuter), (y)], size = [156,156])
option2Item2 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xInner), (y)], size = [156,156])
option2Item3 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xInner), (y)], size = [156,156])
option2Item4 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xOuter), (y)], size = [156,156])
## Middle
option2Item5 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xOuter), 0], size = [156,156])
option2Item6 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xInner), 0], size = [156,156])
option2Item7 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xInner), 0], size = [156,156])
option2Item8 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xOuter), 0], size = [156,156])
## Bottom
option2Item9 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xOuter), -(y)], size = [156,156])
option2Item10 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xInner), -(y)], size = [156,156])
option2Item11 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xInner), -(y)], size = [156,156])
option2Item12 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xOuter), -(y)], size = [156,156])
## Subejct's selected image;.
postChoiceItem = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[0,0], size = [156,156])

## TextBox - Initialized with placeholder values
option2Money1=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xOuter), (y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money2=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xInner), (y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money3=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xInner), (y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money4=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xOuter), (y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money5=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xOuter), 0),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money6=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xInner), 0),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money7=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xInner), 0),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money8=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xOuter), 0),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money9=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xOuter), -(y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money10=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(-(xInner), -(y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money11=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xInner), -(y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
option2Money12=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=((xOuter), -(y)),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )
postChoiceMoney=visual.TextBox(window=win,
                         text=' ',
                         background_color=[1,1,1],
                         bold=False,
                         italic=False,
                         font_size=21,
                         font_color=[-1,-1,1],
                         size=(156,156),
                         pos=(0, 0),
                         units='pix',
                         grid_horz_justification='center',
                         grid_vert_justification='center',
                         border_color=None,
                         border_stroke_width=4
                         )

# Functions used for draw Option 2 Item/Money Choice Grid (3 colx4 row)
def resetOption2MoneyOptionOutlines():
    option2Pos1Shape.setLineColor(None)
    option2Pos2Shape.setLineColor(None)
    option2Pos3Shape.setLineColor(None)
    option2Pos4Shape.setLineColor(None)
    option2Pos5Shape.setLineColor(None)
    option2Pos6Shape.setLineColor(None)
    option2Pos7Shape.setLineColor(None)
    option2Pos8Shape.setLineColor(None)
    option2Pos9Shape.setLineColor(None)
    option2Pos10Shape.setLineColor(None)
    option2Pos11Shape.setLineColor(None)
    option2Pos12Shape.setLineColor(None)
def drawOption2MoneyTextBoxes():
    option2Money1.draw()
    option2Money2.draw()
    option2Money3.draw()
    option2Money4.draw()
    option2Money5.draw()
    option2Money6.draw()
    option2Money7.draw()
    option2Money8.draw()
    option2Money9.draw()
    option2Money10.draw()
    option2Money11.draw()
    option2Money12.draw()
def drawOption2TargetSquares():
    option2Pos1Shape.draw()
    option2Pos2Shape.draw()
    option2Pos3Shape.draw()
    option2Pos4Shape.draw()
    option2Pos5Shape.draw()
    option2Pos6Shape.draw()
    option2Pos7Shape.draw()
    option2Pos8Shape.draw()
    option2Pos9Shape.draw()
    option2Pos10Shape.draw()
    option2Pos11Shape.draw()
    option2Pos12Shape.draw()
def drawOption2ItemBoxes():
    option2Item1.draw()
    option2Item2.draw()
    option2Item3.draw()
    option2Item4.draw()
    option2Item5.draw()
    option2Item6.draw()
    option2Item7.draw()
    option2Item8.draw()
    option2Item9.draw()
    option2Item10.draw()
    option2Item11.draw()
    option2Item12.draw()
def drawOption2ItemOptionOutlines():
    option2Pos1Shape.setLineColor('red')
    option2Pos2Shape.setLineColor('red')
    option2Pos3Shape.setLineColor('red')
    option2Pos4Shape.setLineColor('red')
    option2Pos5Shape.setLineColor('red')
    option2Pos6Shape.setLineColor('red')
    option2Pos7Shape.setLineColor('red')
    option2Pos8Shape.setLineColor('red')
    option2Pos9Shape.setLineColor('red')
    option2Pos10Shape.setLineColor('red')
    option2Pos11Shape.setLineColor('red')
    option2Pos12Shape.setLineColor('red')

# Main Loop
for i in range(150):
    # Set up all money options to be offered
    numberUniqueMoneyOptions = moneyChoiceAmounts[random.randint(0, len(moneyChoiceAmounts)-1)]
    timesMoneyRepeated = 12 / numberUniqueMoneyOptions
    uniqueMoneyOptions = random.sample(moneyList, numberUniqueMoneyOptions)

    # Create random ordered repeated unique trial pics
    trialMoneyOptions = uniqueMoneyOptions * timesMoneyRepeated
    random.shuffle(trialMoneyOptions)

    # Assign choice 1 textboxes values created above
    monetaryAmount = trialMoneyOptions[0] ## money option displayed in choice 1
    choiceAmount = itemChoiceAmounts[random.randint(0, len(itemChoiceAmounts) - 1)] ## item choice amount displayed in choice 1
    option1Money.setText('$' + str(monetaryAmount))
    option1Items.setText(str(choiceAmount))

    # Randomize Positon of Item and Monetary Choice
    if random.random() < .5: # Item Amount - Right, Money Option - Left
        option1MoneyPosition = (-(d/2 + 156/2),0)
        option1ItemPosition = ((d/2 + 156/2),0)
        option1MoneyShapeVertices = [(-(d/2 + 156), -156/2), (-(d/2 + 156), 156/2), (-d/2, 156/2), (-d/2, -156/2)]
        option1ItemShapeVertices = [((d/2 + 156), -156/2), ((d/2 + 156), 156/2), (d/2, 156/2), (d/2, -156/2)]
    else: # Item Amount - Left, Money Option - Right
        option1MoneyPosition = ((d/2 + 156/2),0)
        option1ItemPosition = (-(d/2 + 156/2),0)
        option1MoneyShapeVertices = [((d/2 + 156), -156/2), ((d/2 + 156), 156/2), (d/2, 156/2), (d/2, -156/2)]
        option1ItemShapeVertices = [(-(d/2 + 156), -156/2), (-(d/2 + 156), 156/2), (-d/2, 156/2), (-d/2, -156/2)]

    # Log Options presented to user
    monetaryOptions[i] = monetaryAmount
    itemNumberOptions[i] = choiceAmount

    # Choice 1 Loop
    timer.reset()
    while timer.getTime() < choice1Duration:
        # Monetary Option Chosen
        if mouse.isPressedIn(option1MoneyShape):
            choice1ReactionTimes[i] = timer.getTime() ## assign reation time
            option1Money.setBorderColor('red')
            option1Money.draw()
            option1Items.draw()
            win.flip()
            core.wait(1) ## Duration of Red outline of subject's selected boxsss
            choice1Responses[i] = monetaryAmount ## assign subject's first choice
            break
        # Choice option Chosen
        elif mouse.isPressedIn(option1ItemsShape):
            choice1ReactionTimes[i] = timer.getTime()
            option1Items.setBorderColor('red')
            option1Items.draw()
            option1Money.draw()
            win.flip()
            core.wait(1)
            choice1Responses[i] = choiceAmount
            break
        option1Money.draw()
        option1MoneyShape.draw()
        option1Items.draw()
        option1ItemsShape.draw()
        win.flip()
    # Reset choice 1 border colors
    option1Money.setBorderColor(None)
    option1Items.setBorderColor(None)
    # Check if subject has not responded
    ## Exit current trial and begin new one if subject did not answer in time
    if choice1Responses[i] == '':
        ## Set all values to None
        choice1Responses[i] = 'None'
        choice1ReactionTimes[i] ='None'
        choice2Responses[i] = 'None'
        choice2ReactionTimes[i] = 'None'
        postChoiceResponses[i] = 'None'
        postChoiceReactionTimes[i] = 'None'
        try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
        ## Show 'try faster' screen
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(tryFasterDuration) # Duration of try faster screen
        continue # Jumps to start of trials for loop, begins a new trial

    # Delay Screen 1: (Blank). JOCN used 5 or 6 second delay
    while timer.getTime() < delay1Duration:
        win.flip()

    # Choice 2
    if choice1Responses[i] == monetaryAmount:
        # Set trialOptions
        trialOptions[i] = uniqueMoneyOptions
        # Set values in the visual stim grid
        option2Money1.setText('$' + str(trialMoneyOptions[0]))
        option2Money2.setText('$' + str(trialMoneyOptions[1]))
        option2Money3.setText('$' + str(trialMoneyOptions[2]))
        option2Money4.setText('$' + str(trialMoneyOptions[3]))
        option2Money5.setText('$' + str(trialMoneyOptions[4]))
        option2Money6.setText('$' + str(trialMoneyOptions[5]))
        option2Money7.setText('$' + str(trialMoneyOptions[6]))
        option2Money8.setText('$' + str(trialMoneyOptions[7]))
        option2Money9.setText('$' + str(trialMoneyOptions[8]))
        option2Money10.setText('$' + str(trialMoneyOptions[9]))
        option2Money11.setText('$' + str(trialMoneyOptions[10]))
        option2Money12.setText('$' + str(trialMoneyOptions[11]))

        # Reset color of ui borders, clear before selection
        resetOption2MoneyOptionOutlines()

        timer.reset()
        while timer.getTime() < choice2Duration:
            ## item1 Chosen
            if mouse.isPressedIn(option2Pos1Shape):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos1Shape.setLineColor('red')
                option2Pos1Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money1.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos2Shape):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos2Shape.setLineColor('red')
                option2Pos2Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money2.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos3Shape):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos3Shape.setLineColor('red')
                option2Pos3Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money3.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos4Shape):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos4Shape.setLineColor('red')
                option2Pos4Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money4.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos5Shape):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos5Shape.setLineColor('red')
                option2Pos5Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money5.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos6Shape):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos6Shape.setLineColor('red')
                option2Pos6Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money6.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos7Shape):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos7Shape.setLineColor('red')
                option2Pos7Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money7.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos8Shape):
                choice2ReactionTimes[i] =  timer.getTime() ## record reaction time
                option2Pos8Shape.setLineColor('red')
                option2Pos8Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money8.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos9Shape):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos9Shape.setLineColor('red')
                option2Pos9Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money9.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos10Shape):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos10Shape.setLineColor('red')
                option2Pos10Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money10.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos11Shape):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos11Shape.setLineColor('red')
                option2Pos11Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money11.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos12Shape):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos12Shape.setLineColor('red')
                option2Pos12Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = option2Money12.getDisplayedText()
                break
            drawOption2MoneyTextBoxes()
            drawOption2TargetSquares()
            win.flip()
    # Subject chose item option
    else:
        # Setup random images to be used based on amount unique images to be shown
        imageType = random.randint(0, 1)
        numberUniquePics = choiceAmount
        timesImageRepeated = 12 / numberUniquePics
        # Check for trial type, 1 or 2, and require images in list than unique pics needed.
        if trials[i] == 1 and numberUniquePics < imageList[imageType]: # Check if trial requires high preference images
            uniquePics = random.sample(imageList[imageType], numberUniquePics)
        else: # Select low preference images
            uniquePics = random.sample(imageList[imageType + 2], numberUniquePics)
        # Assign picture options to trial options array for output
        trialOptions[i] = uniquePics
        # Create random ordered repeated unique trial pics
        trialPics = uniquePics * timesImageRepeated
        random.shuffle(trialPics)

        # Draw red outline around option boxes
        drawOption2ItemOptionOutlines()

        option2Item1.setImage(trialPics[0])
        option2Item2.setImage(trialPics[1])
        option2Item3.setImage(trialPics[2])
        option2Item4.setImage(trialPics[3])
        option2Item5.setImage(trialPics[4])
        option2Item6.setImage(trialPics[5])
        option2Item7.setImage(trialPics[6])
        option2Item8.setImage(trialPics[7])
        option2Item9.setImage(trialPics[8])
        option2Item10.setImage(trialPics[9])
        option2Item11.setImage(trialPics[10])
        option2Item12.setImage(trialPics[11])

        # Collect Subject's Response
        timer.reset()
        while timer.getTime() < choice2Duration:
            ## item1 Chosen
            if mouse.isPressedIn(option2Item1):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos1Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[0]
                break
            elif mouse.isPressedIn(option2Item2):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos2Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[1]
                break
            elif mouse.isPressedIn(option2Item3):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos3Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[2]
                break
            elif mouse.isPressedIn(option2Item4):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos4Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[3]
                break
            elif mouse.isPressedIn(option2Item5):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos5Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[4]
                break
            elif mouse.isPressedIn(option2Item6):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos6Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[5]
                break
            elif mouse.isPressedIn(option2Item7):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos7Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[6]
                break
            elif mouse.isPressedIn(option2Item8):
                choice2ReactionTimes[i] =  timer.getTime() ## record reaction time
                option2Pos8Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[7]
                break
            elif mouse.isPressedIn(option2Item9):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos9Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[8]
                break
            elif mouse.isPressedIn(option2Item10):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos10Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[9]
                break
            elif mouse.isPressedIn(option2Item11):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos11Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[10]
                break
            elif mouse.isPressedIn(option2Item12):
                choice2ReactionTimes[i] = timer.getTime() ## record reaction time
                option2Pos12Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(1)
                choice2Responses[i] = trialPics[11]
                break
            #draw boxes behind
            drawOption2ItemBoxes()
            win.flip()

    # Exit current trial and begin new one if did not answer in time
    if choice2Responses[i] == '':
        choice2Responses[i] = 'None'
        choice2ReactionTimes[i] = 'None'
        postChoiceResponses[i] = 'None'
        postChoiceReactionTimes[i] = 'None'
        try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
        ## Show 'try faster' screen
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(3)
        continue

    # Delay 2. Select 2 or 3 second delay
    timer.reset()
    while timer.getTime() < delay2Duration:
        # print(timer.getTime())
        win.flip()

    # Show Subject's choice
    timer.reset()
    if choice1Responses[i] == monetaryAmount:
        while timer.getTime() < postChoiceDuration: # JOCN duration: 2 seconds
            postChoiceMoney.setText(choice2Responses[i])
            postChoiceMoney.draw()
            win.flip()
            core.wait(3) #
    else:
        while timer.getTime() < postChoiceDuration:
            postChoiceItem.setImage(choice2Responses[i])
            postChoiceItem.draw()
            win.flip()
            core.wait(3)

    decisionRatingScale.reset(); snackRatingScale.reset()
    event.clearEvents()
    timer.reset()
    while timer.getTime() < postChoice2ScaleDuration: # JOCN duration: 3 seconds
        if not decisionRatingScale.noResponse and not snackRatingScale.noResponse:
            postChoiceReactionTimes[i] = timer.getTime()
            postChoiceDecisionRatings[i] = decisionRatingScale.getRating()
            postChoiceSnackRatings[i] = snackRatingScale.getRating()
            decisionRatingTitle.draw()
            snackRatingTitle.draw()
            decisionRatingScale.draw()
            snackRatingScale.draw();
            win.flip()
            core.wait(interTrialInterval)
            break
        decisionRatingTitle.draw()
        snackRatingTitle.draw()
        decisionRatingScale.draw()
        snackRatingScale.draw();
        win.flip()

    if postChoiceResponses[i] == '':
        postChoiceResponses[i] = 'None'
        postChoiceReactionTimes[i] = 'None'
        try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
        ## Show 'try faster' screen
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(3)
    # See Results
    print(trials[i])
    print(monetaryOptions[i])
    print(itemNumberOptions[i])
    print(trialOptions[i])
    print(choice1Responses[i])
    print(choice1ReactionTimes[i])
    print(choice2Responses[i])
    print(choice2ReactionTimes[i])
    print(postChoiceResponses[i])
    print(postChoiceReactionTimes[i])

# Determine output file name
if confed_id == '':
    outputFile = 'Subject_' + subj_id + '_task_b_results.csv'
else:
    outputFile = 'Subject_' + subj_id + '_Confederate_' + confed_id + '_task_b_results.csv'

# Write to .csv file with participants name, subj_id, in file name and/or confederate's id, confed_id
f=open( outputFile ,'w')
if len(confed_id) > 0: # Check if there is a confederate
    f.write('Subject: ' + subj_id + ',' + 'Confederate: ' + confed_id + '\n')
f.write('Trial Type, Money Option, Item Option, Trial Options, Choice 1, Choice 1 RT, Choice 2, Choice 2 RT, Decision Rating , Snack Rating, PostChoiceRT\n')
for i in range(90):
    f.write(str(trials[i]) + ',' + str(monetaryOptions[i]) + ',' + str(itemNumberOptions[i]) + ',' + " ".join(map(str,trialOptions[i]))
        + ',' + str(choice1Responses[i]) +','+ str(choice1ReactionTimes[i]) + ',' + str(choice2Responses[i]) + ',' + str(choice2ReactionTimes[i])
        + ',' + str(postChoiceDecisionRatings[i]) + ',' + str(postChoiceSnackRatings[i]) + ',' + str(postChoiceReactionTimes[i]) + "\n")
    # Check results in console
    print(trials[i])
    print(monetaryOptions[i])
    print(itemNumberOptions[i])
    print(trialOptions[i])
    print(choice1Responses[i])
    print(choice1Responses[i])
    print(choice1ReactionTimes[i])
    print(choice2Responses[i])
    print(choice2ReactionTimes[i])
    print(postChoiceResponses[i])
    print(postChoiceReactionTimes[i])
f.close()

win.close()
core.quit()
