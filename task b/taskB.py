from psychopy import visual, event, core, os
import random, glob, util

# Set Size Study - Task B
# Preperation for trial:
# -Drag subject's task a results csv file into 'task b' folder
# -Enter subject's id in Parameters section
# -Enter confederate's id in Parameters section
# -Run
# Output: csv file ex. 'subject_999_confederate_John_task_b_results.csv'
# Matthew Slipenchuk tuf91673@temple.edu (09/2018)

# General Initalization
directory = os.getcwd()
timer = core.Clock()
win = visual.Window(fullscr=True, units='pix', monitor='testMonitor',
        color = [-.9,-.9,-.9])
mouse = event.Mouse()

#-Subject Parameters-------------------------------------------------------------------#
subj_id = '999'
confed_id = '999' 
outputFile = 'subject_' + subj_id + '_confederate_' + confed_id + '_task_b_results.csv'
#--------------------------------------------------------------------------------------#

# Timing Parameters (s)
breakDuration = 300 # 5 min or 600s
choice1Duration = 4.5
choice2Duration = 4.5
postChoice2ScaleDuration = 4.5 
delay1Duration = 5 # Blank display after subject makes item/monetary option decision
delay2Duration = 2 # Blank display after subject chooses specific item/money amount
postChoiceDisplayDuration = 2 # Display subject's choice
interTrialInterval = 1 
tryFasterDuration = 3
selectionOutlineDuration = 1 # Duration the red border appears around chosen choice box

# Game Parameters
itemChoiceAmounts = [3,6,12]
moneyChoiceAmounts = [2,3,4,6]
moneyList = [0.50, 0.75, 1.00, 1.25, 1.50, 1.75]
imageList = util.imageSorter(subj_id + ' task a results.csv') # Sort Images into list
                                                              # from task a data
# GUI Parameters
d = 20; # distance between ui elements
xInner = (d/2 + 160/2) # Center of Inner Right Boxs
xOuter = (d/2 + 160 + d + 160/2) # Center of Outer Right Boxs
y = (160/2 + d + 160/2) # Center of upper Boxs
option1MoneyPosition = (-(d/2 + 156/2),0)
option1ItemPosition = ((d/2 + 156/2),0)
option1MoneyShapeVertices = [(-(d/2 + 156), -156/2), (-(d/2 + 156), 156/2), (-d/2, 156/2), (-d/2, -156/2)]
option1ItemShapeVertices = [((d/2 + 156), -156/2), ((d/2 + 156), 156/2), (d/2, 156/2), (d/2, -156/2)]

# Trial Order Initialization (high pref items, mixed pref items)
highPrefTrials = [1] * 100
lowPrefTrials = [2] * 100
trials = highPrefTrials + lowPrefTrials
random.shuffle(trials)

# ChoosingFor Order Initialization (you items, partner items)
youTrials = [1] * 100
personTrials = [2] * 100
youOrPersonTrials = youTrials + personTrials
random.shuffle(youOrPersonTrials)

# Data Log Arrays Initialization
monetaryOptions = [''] * len(trials)
itemNumberOptions = [''] * len(trials)
choice1Responses = [''] * len(trials)
choice1ReactionTimes = [''] * len(trials)
choice2Responses = [''] * len(trials)
choice2ReactionTimes = [''] * len(trials)
postChoiceSelectedOptionRatings = [''] * len(trials)
postChoiceDecisionRatings = [''] * len(trials)
postChoiceReactionTimes = [''] * len(trials)
trialOptions = [''] * len(trials)
computerResponse = [''] * len(trials)

# Choice 1 GUI Element Initalization #
# Text Boxes
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
personChoosingForTextBox=visual.TextBox(window=win,
                         text=' ',
                         font_size=30,
                         font_color=[1,1,1],
                         size=(1.9,.3),
                         pos=(-.01,.5),
                         grid_horz_justification='center',
                         units='norm',
                         )
# Target Boxes Overlayed Text Boxes
option1MoneyShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=option1MoneyShapeVertices, opacity = 0)
option1ItemsShape = visual.ShapeStim(win, fillColor=[1,1,1],
    vertices=option1ItemShapeVertices, opacity = 0)
# High Preference High Familiarity Arrow
highPrefHighFamArrowVert = [(-0.4 - 1,0.05),(-0.4 - 1,-0.05),(-.2 - 1,-0.05),(-.2 - 1,-0.1),(0 - 1,0),(-.2 - 1,0.1),(-.2 - 1,0.05)]
highPrefHighFameArrow = visual.ShapeStim(win, units='norm', vertices=highPrefHighFamArrowVert, fillColor='white', size=.5, lineColor='white')
highPrefHighFameArrow.setOri(90, '-')
# Mixed Preference High Familiarity Arrows
mixedPrefHighFamleftArrowVert = [(-0.4 - 1,0.05 + .125),(-0.4 - 1,-0.05 + .125),(-.2 - 1,-0.05 + .125),(-.2 - 1,-0.1 + .125),(0 - 1,0 + .125),(-.2 - 1,0.1 + .125),(-.2 - 1,0.05 + .125)]
mixedPrefHighFamLeftArrow = visual.ShapeStim(win,  units='norm', vertices=mixedPrefHighFamleftArrowVert, fillColor='white', size=.5, lineColor='white')
mixedPrefHighFamLeftArrow.setOri(90, '-')
mixedPrefHighFamRightArrowVert = [(-0.4 + 1 + .4,0.05 + .125),(-0.4 + 1 + .4,-0.05 + .125),(-.2 + 1 + .4,-0.05 + .125),(-.2 + 1 + .4,-0.1 + .125),(0 + 1 + .4,0 + .125),(-.2 + 1 + .4,0.1 + .125),(-.2 + 1 + .4,0.05 + .125)]
mixedPrefHighFamRightArrow = visual.ShapeStim(win,  units='norm', vertices=mixedPrefHighFamRightArrowVert, fillColor='white', size=.5, lineColor='white')
mixedPrefHighFamRightArrow.setOri(270, '-')

# Choice 2 GUI Element Initalization #
# TextBoxes - Top - left to right
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
# TextBoxes - Middle - left to right
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
# TextBoxes - Bottom - left to right
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
# Target Boxes overlayed TextBoxes - Top - left to right
option2Pos1Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160+d+160), d+160/2), (-(d/2 + 160+d+160), d+160/2+160), (-(d/2 + 160+d), d+160/2+160), (-(d/2 + 160+d), d+160/2)])
option2Pos2Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160), d+160/2), (-(d/2 + 160), d+160/2+160), (-(d/2), d+160/2+160), (-(d/2), d+160/2)])
option2Pos3Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2), d+160/2), ((d/2), d+160/2+160), ((d/2 + 160), d+160/2+160), ((d/2 + 160), d+160/2)])
option2Pos4Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2 + 160+d), d+160/2), ((d/2 + 160+d), d+160/2+160), ((d/2 + 160+d+160), d+160/2+160), ((d/2 + 160+d+160), d+160/2)])
# Target Boxes overlayed TextBoxes - left to right
option2Pos5Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160+d+160), -160/2), (-(d/2 + 160+d+160), 160/2), (-(d/2 + 160+d), 160/2), (-(d/2 + 160+d), -160/2)])
option2Pos6Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160), -160/2), (-(d/2 + 160), 160/2), (-(d/2), 160/2), (-(d/2), -160/2)])
option2Pos7Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2), -160/2), ((d/2), 160/2), ((d/2 + 160), 160/2), ((d/2 + 160), -160/2)])
option2Pos8Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2 + 160+d), -160/2), ((d/2 + 160+d), 160/2), ((d/2 + 160+d+160), 160/2), ((d/2 + 160+d+160), -160/2)])
# Target Boxes overlayed TextBoxes - Bottom - left to right
option2Pos9Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160+d+160), -(d+160/2+160)), (-(d/2 + 160+d+160), -(d+160/2)), (-(d/2 + 160+d), -(d+160/2)), (-(d/2 + 160+d), -(d + 160/2 + 160))])
option2Pos10Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[(-(d/2 + 160), -(d+160/2+160)), ((-(d/2 + 160)), -(d+160/2)), (-(d/2), -(d+160/2)), (-(d/2), -(d+160/2+160))])
option2Pos11Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2), -(d+160/2+160)), ((d/2), -(d+160/2)), ((d/2 + 160), -(d+160/2)), ((d/2 + 160), -(d+160/2+160))])
option2Pos12Shape = visual.ShapeStim(win, fillColor= None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
    vertices=[((d/2 + 160+d), -(d+160/2+160)), ((d/2 + 160+d), -(d+160/2)), ((d/2 + 160+d+160), -(d+160/2)), ((d/2 + 160+d+160), -(d+160/2+160))])
# Item Images - Top - left to right
option2Item1 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xOuter), (y)], size = [156,156])
option2Item2 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xInner), (y)], size = [156,156])
option2Item3 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xInner), (y)], size = [156,156])
option2Item4 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xOuter), (y)], size = [156,156])
# Item Images -  Middle - left to right
option2Item5 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xOuter), 0], size = [156,156])
option2Item6 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xInner), 0], size = [156,156])
option2Item7 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xInner), 0], size = [156,156])
option2Item8 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xOuter), 0], size = [156,156])
# Item Images -  Bottom - left to right
option2Item9 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xOuter), -(y)], size = [156,156])
option2Item10 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[-(xInner), -(y)], size = [156,156])
option2Item11 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xInner), -(y)], size = [156,156])
option2Item12 = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[(xOuter), -(y)], size = [156,156])

# Post Choice 2 GUI Element Initalization #
# Text Box - If money option selected
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
# Item Image - If item option selected
postChoiceItem = visual.ImageStim(win=win, image=imageList[0][0], units='pix', pos=[0,0], size = [156,156])


# Rating Scale GUI Element Initialization # 
# Rating Scales - Decision on Left, Selected Option (money/snack) on right
decisionRatingScale = visual.RatingScale(win, name='Decision', choices=['1', '2', '3', '4', '5', '6', '7'], pos=[-400,-200])
selectedOptionRatingScale = visual.RatingScale(win, name='Selected Option', choices=['1', '2', '3', '4', '5', '6', '7'], pos =[400,-200])
# Text Boxes - Rating Scale Titles 
decisionRatingTitle=visual.TextBox(window=win,
                         text='Decision Rating',
                         font_size=30,
                         font_color=[1,1,1],
                         size=(1.9,.3),
                         pos=(-.51,-.3),
                         grid_horz_justification='center',
                         units='norm',
                         )
selectedOptionRatingTitle=visual.TextBox(window=win,
                         text='Snack Rating',
                         font_size=30,
                         font_color=[1,1,1],
                         size=(1.9,.3),
                         pos=(.52,-.3),
                         grid_horz_justification='center',
                         units='norm',
                         )

# Functions #
def resetOption2MoneyOptionOutlines(): # Resets GUI Elements after trial
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
def drawOption2MoneyTextBoxes(): # Misc. GUI functions for readability
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
def drawOption2TargetBoxes():
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
def setOption2MoneyBoxTexts(): # Sets image/money choices in trial
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
def setOption2ItemImages():
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
def displayResults(): # For debug
    print('trials[' + str(i) + '] = ' +  str(trials[i]))
    print('monetaryOptions[' + str(i) + '] = ' + str(monetaryOptions[i]))
    print('itemNumberOptions[' + str(i) + '] = ' + str(itemNumberOptions[i]))
    print('trialOptions[' + str(i) + '] = ' + str(trialOptions[i]))
    print('choice1Responses[' + str(i) + '] = ' + str(choice1Responses[i]))
    print('choice1ReactionTimes[' + str(i) + '] = ' + str(choice1ReactionTimes[i]))
    print('choice2Responses[' + str(i) + '] = ' + str(choice2Responses[i]))
    print('choice2ReactionTimes[' + str(i) + '] = ' + str(choice2ReactionTimes[i]))
    print('postChoiceDecisionRatings[' + str(i) + '] = ' + str(postChoiceDecisionRatings[i]))
    print('postChoiceSelectedOptionRatings[' + str(i) + '] = ' + str(postChoiceSelectedOptionRatings[i]))
    print('postChoiceReactionTImes[' + str(i) + '] = ' + str(postChoiceReactionTimes[i]))
    print('computerResponse[' + str(i) + '] = ' + str(computerResponse[i]))

# Main Loop #
for i in range(len(trials)):
    
    if i == 50 | i == 100 | i == 150:
            while timer.getTime() < breakDuration:
                win.flip()
    
    # Set Up Money Option Choices & Unique Options #
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
    
    # Setup random images to be used based on amount unique images to be shown
    numberUniquePics = choiceAmount
    timesImageRepeated = 12 / numberUniquePics
    
    # Check for trial type, 1 or 2, and require images in list than unique pics needed.
    if trials[i] == 1: # Check if trial requires high preference images
        uniquePics = random.sample(imageList[1], numberUniquePics)
    else: # Select mixed preference images
        uniquePics = random.sample(imageList[4], numberUniquePics)
    
    # Assign picture options to trial options array for output
    trialOptions[i] = uniquePics
    
    # Create random ordered repeated unique trial pics
    trialPics = uniquePics * timesImageRepeated
    random.shuffle(trialPics)

    # Randomize Positon of Item and Monetary Choice
    if random.random() < .5: # Item Amount - Right, Money Option - Left
        option1MoneyPosition = (-(d/2 + 156/2),0)
        option1ItemPosition = ((d/2 + 156/2),0)
        option1MoneyShapeVertices = [(-(d/2 + 156), -156/2), (-(d/2 + 156), 156/2), (-d/2, 156/2), (-d/2, -156/2)]
        option1ItemShapeVertices = [((d/2 + 156), -156/2), ((d/2 + 156), 156/2), (d/2, 156/2), (d/2, -156/2)]
        option1Money.setPosition(option1MoneyPosition)
        option1Items.setPosition(option1ItemPosition)
        option1MoneyShape.setVertices(option1MoneyShapeVertices)
        option1ItemsShape.setVertices(option1ItemShapeVertices)
    else: # Item Amount - Left, Money Option - Right
        option1MoneyPosition = ((d/2 + 156/2),0)
        option1ItemPosition = (-(d/2 + 156/2),0)
        option1MoneyShapeVertices = [((d/2 + 156), -156/2), ((d/2 + 156), 156/2), (d/2, 156/2), (d/2, -156/2)]
        option1ItemShapeVertices = [(-(d/2 + 156), -156/2), (-(d/2 + 156), 156/2), (-d/2, 156/2), (-d/2, -156/2)]
        option1Money.setPosition(option1MoneyPosition)
        option1Items.setPosition(option1ItemPosition)
        option1MoneyShape.setVertices(option1MoneyShapeVertices)
        option1ItemsShape.setVertices(option1ItemShapeVertices)
    
    # Determine Partner Type (Person or PC)
    if youOrPersonTrials[i] == 1:
        personChoosingFor = 'You'
        personChoosingForTextBox.setText(personChoosingFor)
    else:
        personChoosingFor = 'Partner'
        personChoosingForTextBox.setText(personChoosingFor)
    
    # Set computer response to default value and log options presented to subject
    computerResponse[i] = 0 # Will switch to 1 during trial if no response from subject
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
            personChoosingForTextBox.draw()
            # Display Respective Arrow(s)
            if trials[i] == 1: # High Preference High Familiarity Images Trial
                highPrefHighFameArrow.draw()
            else: # Mixed Preference High Familiarity Images Trial
                mixedPrefHighFamLeftArrow.draw()
                mixedPrefHighFamRightArrow.draw()
            win.flip()
            core.wait(selectionOutlineDuration) # Display border around selected option
            choice1Responses[i] = monetaryAmount # Log response
            break
        
        # Choice option Chosen
        elif mouse.isPressedIn(option1ItemsShape):
            choice1ReactionTimes[i] = timer.getTime()
            option1Items.setBorderColor('red')
            option1Items.draw()
            option1Money.draw()
            personChoosingForTextBox.draw()
            if trials[i] == 1:
                highPrefHighFameArrow.draw()
            else:
                mixedPrefHighFamLeftArrow.draw()
                mixedPrefHighFamRightArrow.draw()
            win.flip()
            core.wait(selectionOutlineDuration)
            choice1Responses[i] = choiceAmount
            break
        
        if trials[i] == 1:
            highPrefHighFameArrow.draw()
        else:
            mixedPrefHighFamLeftArrow.draw()
            mixedPrefHighFamRightArrow.draw()
        personChoosingForTextBox.draw()
        option1Money.draw()
        option1MoneyShape.draw()
        option1Items.draw()
        option1ItemsShape.draw()
        win.flip()
    
    # GUI - Reset choice 1 border colors # 
    option1Money.setBorderColor(None)
    option1Items.setBorderColor(None)
    
    # Subject Response Check - Selects random responses if no response given
    if choice1Responses[i] == '':
        computerResponse[i] = 1 # Indicate Computer Response is True
        if random.random() < .5: # Randomly Select Option 1,2
            choice1Responses[i] = choiceAmount
            choice2Responses[i] = trialPics[random.randint(0,11)]
        else:
            choice1Responses[i] = monetaryAmount
            choice2Responses[i] = trialMoneyOptions[random.randint(0,11)]
        choice1ReactionTimes[i] ='n/a'
        choice2ReactionTimes[i] = 'n/a'
        postChoiceDecisionRatings[i] = random.randint(1,7) # Ranomly Select Ratings
        postChoiceSelectedOptionRatings[i] = random.randint(1,7)
        postChoiceReactionTimes[i] = 'n/a'
        try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(tryFasterDuration) 
        displayResults()
        continue # Starts a new trial

    # Delay Screen 1 #
    while timer.getTime() < delay1Duration:
        win.flip()

    # Choice 2 #
    # Money Option Chosen
    if choice1Responses[i] == monetaryAmount:
        # Update Rating Scale Text 
        selectedOptionRatingTitle.setText('Money Rating')
        
        # Log unique monetary amounts presented
        trialOptions[i] = uniqueMoneyOptions
        
        # Set values in the text box grid
        setOption2MoneyBoxTexts()

        # Reset color of ui borders, clear before selection
        resetOption2MoneyOptionOutlines()
        
        # Subject Response Collection Loop
        timer.reset()
        while timer.getTime() < choice2Duration:
            ## item1 Chosen
            if mouse.isPressedIn(option2Pos1Shape):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos1Shape.setLineColor('red')
                option2Pos1Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money1.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos2Shape):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos2Shape.setLineColor('red')
                option2Pos2Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money2.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos3Shape):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos3Shape.setLineColor('red')
                option2Pos3Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money3.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos4Shape):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos4Shape.setLineColor('red')
                option2Pos4Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money4.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos5Shape):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos5Shape.setLineColor('red')
                option2Pos5Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money5.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos6Shape):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos6Shape.setLineColor('red')
                option2Pos6Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money6.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos7Shape):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos7Shape.setLineColor('red')
                option2Pos7Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money7.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos8Shape):
                choice2ReactionTimes[i] =  timer.getTime() 
                option2Pos8Shape.setLineColor('red')
                option2Pos8Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money8.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos9Shape):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos9Shape.setLineColor('red')
                option2Pos9Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money9.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos10Shape):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos10Shape.setLineColor('red')
                option2Pos10Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money10.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos11Shape):
                choice2ReactionTimes[i] = timer.getTime()
                option2Pos11Shape.setLineColor('red')
                option2Pos11Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money11.getDisplayedText()
                break
            elif mouse.isPressedIn(option2Pos12Shape):
                choice2ReactionTimes[i] = timer.getTime()
                option2Pos12Shape.setLineColor('red')
                option2Pos12Shape.draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = option2Money12.getDisplayedText()
                break
            
            drawOption2MoneyTextBoxes()
            drawOption2TargetBoxes()
            win.flip()
    # Item Option Chosen
    else:
        # Update Rating Scale Text 
        selectedOptionRatingTitle.setText('Snack Rating')
        
        # Draw red outline around option boxes
        drawOption2ItemOptionOutlines()
        
        # Set values in the image grid
        setOption2ItemImages()
        
        # Subject Response Collection Loop
        timer.reset()
        while timer.getTime() < choice2Duration:
            if mouse.isPressedIn(option2Item1):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos1Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[0]
                break
            elif mouse.isPressedIn(option2Item2):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos2Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[1]
                computerResponse[i] == 0
                break
            elif mouse.isPressedIn(option2Item3):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos3Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[2]
                break
            elif mouse.isPressedIn(option2Item4):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos4Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[3]
                break
            elif mouse.isPressedIn(option2Item5):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos5Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[4]
                break
            elif mouse.isPressedIn(option2Item6):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos6Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[5]
                break
            elif mouse.isPressedIn(option2Item7):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos7Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[6]
                break
            elif mouse.isPressedIn(option2Item8):
                choice2ReactionTimes[i] =  timer.getTime() 
                option2Pos8Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[7]
                break
            elif mouse.isPressedIn(option2Item9):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos9Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[8]
                break
            elif mouse.isPressedIn(option2Item10):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos10Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[9]
                break
            elif mouse.isPressedIn(option2Item11):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos11Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[10]
                break
            elif mouse.isPressedIn(option2Item12):
                choice2ReactionTimes[i] = timer.getTime() 
                option2Pos12Shape.draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice2Responses[i] = trialPics[11]
                break
            
            drawOption2ItemBoxes()
            win.flip()

    # Subject Response Check - Selects random responses if no response given
    if choice2Responses[i] == '':
        computerResponse[i] = 1
        if choice1Responses[i] == choiceAmount:
            choice2Responses[i] = trialPics[random.randint(0,11)]
        else:
            choice2Responses[i] = trialMoneyOptions[random.randint(0,11)]
        choice2ReactionTimes[i] = 'n/a'
        postChoiceDecisionRatings[i] = random.randint(1,7)
        postChoiceSelectedOptionRatings[i] = random.randint(1,7)
        postChoiceReactionTimes[i] = 'n/a'
        try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
        ## Show 'try faster' screen
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(tryFasterDuration)
        # See Results
        displayResults()
        continue
    
    # Delay 2. Select 2 or 3 second delay
    timer.reset()
    while timer.getTime() < delay2Duration:
        # print(timer.getTime())
        win.flip()
    
    # Show Subject's choice
    timer.reset()
    if choice1Responses[i] == monetaryAmount:
        while timer.getTime() < postChoiceDisplayDuration: 
            postChoiceMoney.setText(choice2Responses[i])
            postChoiceMoney.draw()
            win.flip()
            core.wait(postChoiceDisplayDuration) 
    else:
        while timer.getTime() < postChoiceDisplayDuration:
            postChoiceItem.setImage(choice2Responses[i])
            postChoiceItem.draw()
            win.flip()
            core.wait(postChoiceDisplayDuration)
    
    # Get Post Choice Ratings (Decision Rating and Snack/Money Rating)
    decisionRatingScale.reset(); selectedOptionRatingScale.reset()
    event.clearEvents()
    timer.reset()
    while timer.getTime() < postChoice2ScaleDuration: # JOCN duration: 3 seconds
        if not decisionRatingScale.noResponse and not selectedOptionRatingScale.noResponse:
            postChoiceReactionTimes[i] = timer.getTime()
            postChoiceDecisionRatings[i] = decisionRatingScale.getRating()
            postChoiceSelectedOptionRatings[i] = selectedOptionRatingScale.getRating()
            decisionRatingTitle.draw()
            selectedOptionRatingTitle.draw()
            decisionRatingScale.draw()
            selectedOptionRatingScale.draw();
            win.flip()
            core.wait(interTrialInterval)
            break
        decisionRatingTitle.draw()
        selectedOptionRatingTitle.draw()
        decisionRatingScale.draw()
        selectedOptionRatingScale.draw();
        win.flip()
    
    # Subject Response Check - Selects random responses if no response given
    if postChoiceDecisionRatings[i] == '' or postChoiceSelectedOptionRatings[i] == '':
        computerResponse[i] = 1
        postChoiceDecisionRatings[i] = random.randint(1,7)
        postChoiceSelectedOptionRatings[i] = random.randint(1,7)
        postChoiceReactionTimes[i] = 'n/a'
        try_faster_screen = visual.TextStim(win, text='Please make a faster decision next round!')
        ## Show 'try faster' screen
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(tryFasterDuration)
        displayResults()
        continue
    
    displayResults()

# Write to .csv file with participants name, subj_id, in file name and/or confederate's id, confed_id
f=open( outputFile ,'w')
if len(confed_id) > 0: # Check if there is a confederate
    f.write('Subject: ' + subj_id + ',' + 'Confederate: ' + confed_id + '\n')
f.write('Trial Type, Money Option, Item Option, Trial Options, Choice 1, Choice 1 RT, Choice 2, Choice 2 RT, Decision Rating , Selected Option Rating, PostChoiceRT, Computer Response, Choosing For\n')
for i in range(len(trials)):
    f.write(str(trials[i]) + ',' + str(monetaryOptions[i]) + ',' + str(itemNumberOptions[i]) + ',' + " ".join(map(str,trialOptions[i]))
        + ',' + str(choice1Responses[i]) +','+ str(choice1ReactionTimes[i]) + ',' + str(choice2Responses[i]) + ',' + str(choice2ReactionTimes[i])
        + ',' + str(postChoiceDecisionRatings[i]) + ',' + str(postChoiceSelectedOptionRatings[i]) + ',' + str(postChoiceReactionTimes[i]) + ',' + str(computerResponse[i]) + "\n"
        + ',' + str(youOrPersonTrials[i]) + "\n")
f.close()

win.close()
core.quit()
