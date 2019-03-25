from psychopy import visual, event, core, os
import random
import glob
import util

# Set Size Study - Task B
# Preperation for trial:
# -Drag subject's task a results csv file into 'task b' folder
# -Enter subject's id in Parameters section
# -Enter partner's id in Parameters section
# -Run
# Output: csv file ex. 'subject_999_partner_998_task_b_results.csv'
# Matthew Slipenchuk tuf91673@temple.edu (09/2018)


# Subject Parameters-------------------------------------------------------------------#
subj_id = '999'
partner_id = '998'
outputFile = 'subject_' + subj_id + '_partner_' + \
    partner_id + '_task_b_results.csv'
# End Subject Parameters---------------------------------------------------------------#


# General Initalization----------------------------------------------------------------#
directory = os.getcwd()
timer = core.Clock()
win = visual.Window(fullscr=True, units='pix', monitor='testMonitor',
                    color=[-.9, -.9, -.9])
mouse = event.Mouse()
# End General Initialization-----------------------------------------------------------#


# Task Parameter Initalization---------------------------------------------------------#
# Timing Parameters (s)
breakDuration = 300  # 5 min or 300s
choice1Duration = 4.5
choice2Duration = 4.5
postChoice2ScaleDuration = 4.5
delay1Duration = 5  # Blank display after subject makes item/monetary option decision
delay2Duration = 2  # Blank display after subject chooses specific item/money amount
postChoiceDisplayDuration = 2  # Display subject's choice
interTrialInterval = 1
tryFasterDuration = 3
# Duration the red border appears around chosen choice box
selectionOutlineDuration = 1
pcSelectionOutlineDuration = 2

# Game Parameters
itemChoiceAmounts = [2, 3, 6, 12]
moneyChoiceAmounts = [2, 3, 4, 6]
moneyList = [0.50, 0.75, 1.00, 1.25, 1.50, 1.75]
imageList = util.imageSorter(
    subj_id + ' task a results.csv')  # Sort Images into list
# from task a data
# Trial Order Initialization
# Indicates who is making decision, type of items (high/mixed), and who
# decision is made for
highPrefTrialsYou = [1] * 30
lowPrefTrialsYou = [2] * 30
pcHighPrefTrialsYou = [3] * 15
pcLowPrefTrialsYou = [4] * 15
highPrefTrialsPartner = [5] * 30
lowPrefTrialsPartner = [6] * 30
pcHighPrefTrialsPartner = [7] * 15
pcLowPrefTrialsPartner = [8] * 15
trials = highPrefTrialsYou + lowPrefTrialsYou + pcHighPrefTrialsYou + pcLowPrefTrialsYou + highPrefTrialsPartner + lowPrefTrialsPartner + pcHighPrefTrialsPartner + pcLowPrefTrialsPartner
random.shuffle(trials)

# ChoosingFor Order Initialization (choosing for yourself or partner)
youOrPersonTrials = [0] * len(trials)  # Values assigned in loop
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
# End Task Parameter Initialization----------------------------------------------------#


# Function Declerations----------------------------------------------------------------#
def resetOption2MoneyOptionOutlines():  # Resets GUI Elements after trial
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

def setOption2MoneyBoxTexts():  # Sets image/money choices in trial
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

def displayResults():  # For debug
    print('trials[' + str(i) + '] = ' + str(trials[i]))
    print('monetaryOptions[' + str(i) + '] = ' + str(monetaryOptions[i]))
    print('itemNumberOptions[' + str(i) + '] = ' + str(itemNumberOptions[i]))
    print('trialOptions[' + str(i) + '] = ' + str(trialOptions[i]))
    print('choice1Responses[' + str(i) + '] = ' + str(choice1Responses[i]))
    print('choice1ReactionTimes[' + str(i) +
          '] = ' + str(choice1ReactionTimes[i]))
    print('choice2Responses[' + str(i) + '] = ' + str(choice2Responses[i]))
    print('choice2ReactionTimes[' + str(i) +
          '] = ' + str(choice2ReactionTimes[i]))
    print('postChoiceDecisionRatings[' + str(i) +
          '] = ' + str(postChoiceDecisionRatings[i]))
    print('postChoiceSelectedOptionRatings[' + str(i) +
          '] = ' + str(postChoiceSelectedOptionRatings[i]))
    print('postChoiceReactionTImes[' + str(i) +
          '] = ' + str(postChoiceReactionTimes[i]))
    print('computerResponse[' + str(i) + '] = ' + str(computerResponse[i]))
# End Function Declerations------------------------------------------------------------#


# GUI Initalization--------------------------------------------------------------------#
# Position Parameters
d = 20  # distance between ui elements
xInner = (d / 2 + 160 / 2)  # Center of Inner Right Boxs
xOuter = (d / 2 + 160 + d + 160 / 2)  # Center of Outer Right Boxs
y = (160 / 2 + d + 160 / 2)  # Center of upper Boxs
option1MoneyPosition = (-(d / 2 + 156 / 2), 0)
option1ItemPosition = ((d / 2 + 156 / 2), 0)
option1MoneyShapeVertices = [(-(d / 2 + 156), -156 / 2),
                             (-(d / 2 + 156), 156 / 2), (-d / 2, 156 / 2), (-d / 2, -156 / 2)]
option1ItemShapeVertices = [
    ((d / 2 + 156), -156 / 2), ((d / 2 + 156), 156 / 2), (d / 2, 156 / 2), (d / 2, -156 / 2)]

# Choice 1 GUI Element Initalization #
# Text Boxes
option1Money = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False,
                              italic=False, font_size=21, font_color=[-1, -1, 1], size=(156, 156), pos=option1MoneyPosition,
                              units='pix', grid_horz_justification='center', grid_vert_justification='center',
                              border_color=None, border_stroke_width=4)
option1Items = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False,
                              italic=False, font_size=21, font_color=[-1, -1, 1], size=(156, 156), pos=option1ItemPosition,
                              units='pix', grid_horz_justification='center', grid_vert_justification='center',
                              border_color=None, border_stroke_width=4)
personChoosingForTextBox = visual.TextBox(window=win, text=' ', font_size=30, font_color=[1, 1, 1],
                                          size=(1.9, .3), pos=(-.01, .5), grid_horz_justification='center', units='norm')
questionMarkTextBox = visual.TextBox(window=win, text='?', font_size=80, font_color=[1, 1, 1],
                                     size=(1.9, .3), pos=(-.01, -.5), grid_horz_justification='center', units='norm')
# Target Boxes Overlayed Text Boxes
option1MoneyShape = visual.ShapeStim(win, fillColor=[1, 1, 1],
                                     vertices=option1MoneyShapeVertices, opacity=0)
option1ItemsShape = visual.ShapeStim(win, fillColor=[1, 1, 1],
                                     vertices=option1ItemShapeVertices, opacity=0)
# High Preference High Familiarity Arrow
highPrefHighFamArrowVert = [(-0.4 - 1, 0.05), (-0.4 - 1, -0.05), (-.2 - 1, -0.05),
                            (-.2 - 1, -0.1), (0 - 1, 0), (-.2 - 1, 0.1), (-.2 - 1, 0.05)]
highPrefHighFameArrow = visual.ShapeStim(
    win, units='norm', vertices=highPrefHighFamArrowVert, fillColor='white', size=.5, lineColor='white')
highPrefHighFameArrow.setOri(90, '-')
# Mixed Preference High Familiarity Arrows
mixedPrefHighFamleftArrowVert = [(-0.4 - 1, 0.05 + .125), (-0.4 - 1, -0.05 + .125), (-.2 - 1, -0.05 + .125),
                                 (-.2 - 1, -0.1 + .125), (0 - 1, 0 + .125), (-.2 - 1, 0.1 + .125), (-.2 - 1, 0.05 + .125)]
mixedPrefHighFamLeftArrow = visual.ShapeStim(
    win,  units='norm', vertices=mixedPrefHighFamleftArrowVert, fillColor='white', size=.5, lineColor='white')
mixedPrefHighFamLeftArrow.setOri(90, '-')
mixedPrefHighFamRightArrowVert = [(-0.4 + 1 + .4, 0.05 + .125), (-0.4 + 1 + .4, -0.05 + .125), (-.2 + 1 + .4, -0.05 + .125),
                                  (-.2 + 1 + .4, -0.1 + .125), (0 + 1 + .4, 0 + .125), (-.2 + 1 + .4, 0.1 + .125), (-.2 + 1 + .4, 0.05 + .125)]
mixedPrefHighFamRightArrow = visual.ShapeStim(
    win,  units='norm', vertices=mixedPrefHighFamRightArrowVert, fillColor='white', size=.5, lineColor='white')
mixedPrefHighFamRightArrow.setOri(270, '-')

# Choice 2 GUI Element Initalization #
# TextBoxes - Top - left to right
option2Money1 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False,
                               italic=False, font_size=21, font_color=[-1, -1, 1], size=(156, 156), pos=(-(xOuter), (y)),
                               units='pix', grid_horz_justification='center', grid_vert_justification='center',
                               border_color=None, border_stroke_width=4)
option2Money2 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1],
                               bold=False, italic=False, font_size=21, font_color=[-1, -1, 1], size=(156, 156),
                               pos=(-(xInner), (y)), units='pix', grid_horz_justification='center',
                               grid_vert_justification='center', border_color=None, border_stroke_width=4)
option2Money3 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False, italic=False, font_size=21,
                               font_color=[-1, -1, 1], size=(156, 156), pos=((xInner), (y)), units='pix', grid_horz_justification='center',
                               grid_vert_justification='center', border_color=None, border_stroke_width=4)
option2Money4 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False, italic=False, font_size=21,
                               font_color=[-1, -1, 1], size=(156, 156), pos=((xOuter), (y)), units='pix', grid_horz_justification='center',
                               grid_vert_justification='center', border_color=None, border_stroke_width=4)
# TextBoxes - Middle - left to right
option2Money5 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False, italic=False, font_size=21,
                               font_color=[-1, -1, 1], size=(156, 156), pos=(-(xOuter), 0), units='pix', grid_horz_justification='center',
                               grid_vert_justification='center', border_color=None, border_stroke_width=4)
option2Money6 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False, italic=False, font_size=21,
                               font_color=[-1, -1, 1], size=(156, 156), pos=(-(xInner), 0), units='pix', grid_horz_justification='center',
                               grid_vert_justification='center', border_color=None, border_stroke_width=4)
option2Money7 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False, italic=False, font_size=21,
                               font_color=[-1, -1, 1], size=(156, 156), pos=((xInner), 0), units='pix', grid_horz_justification='center',
                               grid_vert_justification='center', border_color=None, border_stroke_width=4)
option2Money8 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False, italic=False, font_size=21,
                               font_color=[-1, -1, 1], size=(156, 156), pos=((xOuter), 0), units='pix', grid_horz_justification='center',
                               grid_vert_justification='center', border_color=None, border_stroke_width=4)
# TextBoxes - Bottom - left to right
option2Money9 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False, italic=False, font_size=21,
                               font_color=[-1, -1, 1], size=(156, 156), pos=(-(xOuter), -(y)), units='pix', grid_horz_justification='center',
                               grid_vert_justification='center', border_color=None, border_stroke_width=4)
option2Money10 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False, italic=False, font_size=21,
                                font_color=[-1, -1, 1], size=(156, 156), pos=(-(xInner), -(y)), units='pix', grid_horz_justification='center',
                                grid_vert_justification='center', border_color=None, border_stroke_width=4)
option2Money11 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False, italic=False, font_size=21,
                                font_color=[-1, -1, 1], size=(156, 156), pos=((xInner), -(y)), units='pix', grid_horz_justification='center',
                                grid_vert_justification='center', border_color=None, border_stroke_width=4)
option2Money12 = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False, italic=False, font_size=21,
                                font_color=[-1, -1, 1], size=(156, 156), pos=((xOuter), -(y)), units='pix', grid_horz_justification='center',
                                grid_vert_justification='center', border_color=None, border_stroke_width=4)
# Target Boxes overlayed TextBoxes - Top - left to right
option2Pos1Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                    vertices=[(-(d / 2 + 160 + d + 160), d + 160 / 2), (-(d / 2 + 160 + d + 160), d + 160 / 2 + 160), (-(d / 2 + 160 + d), d + 160 / 2 + 160), (-(d / 2 + 160 + d), d + 160 / 2)])
option2Pos2Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                    vertices=[(-(d / 2 + 160), d + 160 / 2), (-(d / 2 + 160), d + 160 / 2 + 160), (-(d / 2), d + 160 / 2 + 160), (-(d / 2), d + 160 / 2)])
option2Pos3Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                    vertices=[((d / 2), d + 160 / 2), ((d / 2), d + 160 / 2 + 160), ((d / 2 + 160), d + 160 / 2 + 160), ((d / 2 + 160), d + 160 / 2)])
option2Pos4Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                    vertices=[((d / 2 + 160 + d), d + 160 / 2), ((d / 2 + 160 + d), d + 160 / 2 + 160), ((d / 2 + 160 + d + 160), d + 160 / 2 + 160), ((d / 2 + 160 + d + 160), d + 160 / 2)])
# Target Boxes overlayed TextBoxes - left to right
option2Pos5Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                    vertices=[(-(d / 2 + 160 + d + 160), -160 / 2), (-(d / 2 + 160 + d + 160), 160 / 2), (-(d / 2 + 160 + d), 160 / 2), (-(d / 2 + 160 + d), -160 / 2)])
option2Pos6Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                    vertices=[(-(d / 2 + 160), -160 / 2), (-(d / 2 + 160), 160 / 2), (-(d / 2), 160 / 2), (-(d / 2), -160 / 2)])
option2Pos7Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                    vertices=[((d / 2), -160 / 2), ((d / 2), 160 / 2), ((d / 2 + 160), 160 / 2), ((d / 2 + 160), -160 / 2)])
option2Pos8Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                    vertices=[((d / 2 + 160 + d), -160 / 2), ((d / 2 + 160 + d), 160 / 2), ((d / 2 + 160 + d + 160), 160 / 2), ((d / 2 + 160 + d + 160), -160 / 2)])
# Target Boxes overlayed TextBoxes - Bottom - left to right
option2Pos9Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                    vertices=[(-(d / 2 + 160 + d + 160), -(d + 160 / 2 + 160)), (-(d / 2 + 160 + d + 160), -(d + 160 / 2)), (-(d / 2 + 160 + d), -(d + 160 / 2)), (-(d / 2 + 160 + d), -(d + 160 / 2 + 160))])
option2Pos10Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                     vertices=[(-(d / 2 + 160), -(d + 160 / 2 + 160)), ((-(d / 2 + 160)), -(d + 160 / 2)), (-(d / 2), -(d + 160 / 2)), (-(d / 2), -(d + 160 / 2 + 160))])
option2Pos11Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                     vertices=[((d / 2), -(d + 160 / 2 + 160)), ((d / 2), -(d + 160 / 2)), ((d / 2 + 160), -(d + 160 / 2)), ((d / 2 + 160), -(d + 160 / 2 + 160))])
option2Pos12Shape = visual.ShapeStim(win, fillColor=None, lineWidth=4, lineColor='red', lineColorSpace='rgb',
                                     vertices=[((d / 2 + 160 + d), -(d + 160 / 2 + 160)), ((d / 2 + 160 + d), -(d + 160 / 2)), ((d / 2 + 160 + d + 160), -(d + 160 / 2)), ((d / 2 + 160 + d + 160), -(d + 160 / 2 + 160))])
# Item Images - Top - left to right
option2Item1 = visual.ImageStim(win=win, image=imageList[0][
                                0], units='pix', pos=[-(xOuter), (y)], size=[156, 156])
option2Item2 = visual.ImageStim(win=win, image=imageList[0][
                                0], units='pix', pos=[-(xInner), (y)], size=[156, 156])
option2Item3 = visual.ImageStim(win=win, image=imageList[0][
                                0], units='pix', pos=[(xInner), (y)], size=[156, 156])
option2Item4 = visual.ImageStim(win=win, image=imageList[0][
                                0], units='pix', pos=[(xOuter), (y)], size=[156, 156])
# Item Images -  Middle - left to right
option2Item5 = visual.ImageStim(win=win, image=imageList[0][
                                0], units='pix', pos=[-(xOuter), 0], size=[156, 156])
option2Item6 = visual.ImageStim(win=win, image=imageList[0][
                                0], units='pix', pos=[-(xInner), 0], size=[156, 156])
option2Item7 = visual.ImageStim(win=win, image=imageList[0][
                                0], units='pix', pos=[(xInner), 0], size=[156, 156])
option2Item8 = visual.ImageStim(win=win, image=imageList[0][
                                0], units='pix', pos=[(xOuter), 0], size=[156, 156])
# Item Images -  Bottom - left to right
option2Item9 = visual.ImageStim(win=win, image=imageList[0][
                                0], units='pix', pos=[-(xOuter), -(y)], size=[156, 156])
option2Item10 = visual.ImageStim(win=win, image=imageList[0][
                                 0], units='pix', pos=[-(xInner), -(y)], size=[156, 156])
option2Item11 = visual.ImageStim(win=win, image=imageList[0][
                                 0], units='pix', pos=[(xInner), -(y)], size=[156, 156])
option2Item12 = visual.ImageStim(win=win, image=imageList[0][
                                 0], units='pix', pos=[(xOuter), -(y)], size=[156, 156])

# Post Choice 2 GUI Element Initalization #
# Text Box - If money option selected
postChoiceMoney = visual.TextBox(window=win, text=' ', background_color=[1, 1, 1], bold=False, italic=False,
                                 font_size=21, font_color=[-1, -1, 1], size=(156, 156), pos=(0, 0), units='pix', grid_horz_justification='center',
                                 grid_vert_justification='center', border_color=None, border_stroke_width=4)
# Item Image - If item option selected
postChoiceItem = visual.ImageStim(win=win, image=imageList[0][
                                  0], units='pix', pos=[0, 0], size=[156, 156])

# Rating Scale GUI Element Initialization #
# Rating Scales - Decision on Left, Selected Option (money/snack) on right
decisionRatingScale = visual.RatingScale(win, name='Decision', choices=[
                                         '1', '2', '3', '4', '5', '6', '7'], pos=[-400, -200])
selectedOptionRatingScale = visual.RatingScale(win, name='Selected Option', choices=[
                                               '1', '2', '3', '4', '5', '6', '7'], pos=[400, -200])
# Text Boxes - Rating Scale Titles
decisionRatingTitle = visual.TextBox(window=win,text='Decision Rating',font_size=30,font_color=[1, 1, 1],
    size=(1.9, .3),pos=(-.51, -.3),grid_horz_justification='center',units='norm')
selectedOptionRatingTitle = visual.TextBox(window=win,text='Snack Rating',font_size=30,font_color=[1, 1, 1],
    size=(1.9, .3),pos=(.52, -.3),grid_horz_justification='center',units='norm')
# End GUI Initialization---------------------------------------------------------------#


# Main Loop----------------------------------------------------------------------------#
for i in range(len(trials)):
    # Check if break needed before trial starts
    if i == 45 | i == 90 | i == 135:
        timer.reset()
        while timer.getTime() < breakDuration:
            win.flip()

    # Set Up Money Option Choices & Unique Options #
    numberUniqueMoneyOptions = moneyChoiceAmounts[
        random.randint(0, len(moneyChoiceAmounts) - 1)]
    timesMoneyRepeated = 12 / numberUniqueMoneyOptions
    uniqueMoneyOptions = random.sample(moneyList, numberUniqueMoneyOptions)

    # Create random ordered repeated unique trial pics
    trialMoneyOptions = uniqueMoneyOptions * timesMoneyRepeated
    random.shuffle(trialMoneyOptions)

    # Assign choice 1 textboxes values created above
    monetaryAmount = trialMoneyOptions[0]  # money option displayed in choice 1
    # item choice amount displayed in choice 1
    choiceAmount = itemChoiceAmounts[
        random.randint(0, len(itemChoiceAmounts) - 1)]
    option1Money.setText('$' + str(monetaryAmount))
    option1Items.setText(str(choiceAmount))

    # Setup random images to be used based on amount unique images to be shown
    numberUniquePics = choiceAmount
    timesImageRepeated = 12 / numberUniquePics

    # Check for trial type, 1 or 2, and require images in list than unique
    # pics needed.
    if trials[i] == 1:  # Check if trial requires high preference images
        uniquePics = random.sample(imageList[1], numberUniquePics)
    else:  # Select mixed preference images
        lowUniquePics = random.sample(imageList[3], numberUniquePics-1)
        highUniquePic = random.sample(imageList[3], 1)
        uniquePics = lowUniquePics + highUniquePic
        #uniquePics = random.sample(imageList[4], numberUniquePics)

    # Assign picture options to trial options array for output
    trialOptions[i] = uniquePics

    # Create random ordered repeated unique trial pics
    trialPics = uniquePics * timesImageRepeated
    random.shuffle(trialPics)

    # Randomize Positon of Item and Monetary Choice
    if random.random() < .5:  # Item Amount - Right, Money Option - Left
        option1MoneyPosition = (-(d / 2 + 156 / 2), 0)
        option1ItemPosition = ((d / 2 + 156 / 2), 0)
        option1MoneyShapeVertices = [
            (-(d / 2 + 156), -156 / 2), (-(d / 2 + 156), 156 / 2), (-d / 2, 156 / 2), (-d / 2, -156 / 2)]
        option1ItemShapeVertices = [
            ((d / 2 + 156), -156 / 2), ((d / 2 + 156), 156 / 2), (d / 2, 156 / 2), (d / 2, -156 / 2)]
        option1Money.setPosition(option1MoneyPosition)
        option1Items.setPosition(option1ItemPosition)
        option1MoneyShape.setVertices(option1MoneyShapeVertices)
        option1ItemsShape.setVertices(option1ItemShapeVertices)
    else:  # Item Amount - Left, Money Option - Right
        option1MoneyPosition = ((d / 2 + 156 / 2), 0)
        option1ItemPosition = (-(d / 2 + 156 / 2), 0)
        option1MoneyShapeVertices = [
            ((d / 2 + 156), -156 / 2), ((d / 2 + 156), 156 / 2), (d / 2, 156 / 2), (d / 2, -156 / 2)]
        option1ItemShapeVertices = [
            (-(d / 2 + 156), -156 / 2), (-(d / 2 + 156), 156 / 2), (-d / 2, 156 / 2), (-d / 2, -156 / 2)]
        option1Money.setPosition(option1MoneyPosition)
        option1Items.setPosition(option1ItemPosition)
        option1MoneyShape.setVertices(option1MoneyShapeVertices)
        option1ItemsShape.setVertices(option1ItemShapeVertices)

    # Determine Partner Type (You or Partner)
    if trials[i] < 5:
        youOrPersonTrials[i] = 1
        personChoosingFor = 'You'
        personChoosingForTextBox.setText(personChoosingFor)
    else:
        youOrPersonTrials[i] = 2
        personChoosingFor = 'Partner'
        personChoosingForTextBox.setText(personChoosingFor)

    # Set computer response to default value and log options presented to
    # subject
    if trials[i] in [1, 2, 5, 6]:
        # Will switch to 1 during trial if no response from subject
        computerResponse[i] = 0
    else:
        computerResponse[i] = 1  # Set to 1 for PC response trial types
    monetaryOptions[i] = monetaryAmount
    itemNumberOptions[i] = choiceAmount

    # Choice 1 Loop
    timer.reset()
    while timer.getTime() < choice1Duration:
        if trials[i] in [1, 2, 5, 6]:  # Check if current trial is a player response trial
            # Player Choice--------------------------------------------------#
            if mouse.isPressedIn(option1MoneyShape):  # Monetary Option Chosen
                # assign reaction time
                choice1ReactionTimes[i] = timer.getTime()
                option1Money.setBorderColor('red')
                option1Money.draw()
                option1Items.draw()
                personChoosingForTextBox.draw()
                # Display Respective Arrow(s)
                if trials[i] in [1, 5]:
                    highPrefHighFameArrow.draw()
                elif trials[i] in [2, 6]:
                    mixedPrefHighFamLeftArrow.draw()
                    mixedPrefHighFamRightArrow.draw()
                win.flip()
                # Display border around selected option
                core.wait(selectionOutlineDuration)
                choice1Responses[i] = monetaryAmount  # Log response
                break
            elif mouse.isPressedIn(option1ItemsShape):  # Choice option Chosen
                choice1ReactionTimes[i] = timer.getTime()
                option1Items.setBorderColor('red')
                option1Items.draw()
                option1Money.draw()
                personChoosingForTextBox.draw()
                # Display Respective Arrow(s)
                if trials[i] in [1, 5]:
                    highPrefHighFameArrow.draw()
                elif trials[i] in [2, 6]:
                    mixedPrefHighFamLeftArrow.draw()
                    mixedPrefHighFamRightArrow.draw()
                win.flip()
                core.wait(selectionOutlineDuration)
                choice1Responses[i] = choiceAmount
                break
            # End Player Choice------------------------------------------------#
        else:
            # PC Choice--------------------------------------------------------#
            if random.random() < .5:
                # assign reaction time
                choice1ReactionTimes[i] = timer.getTime()
                option1Money.setBorderColor('red')
                option1Money.draw()
                option1Items.draw()
                option1ItemsShape.draw()
                option1MoneyShape.draw()
                personChoosingForTextBox.draw()
                # Display Question Mark indicating PC is choosing this trial
                questionMarkTextBox.draw()
                win.flip()
                # Display border around selected option
                core.wait(pcSelectionOutlineDuration)
                choice1Responses[i] = monetaryAmount  # Log response
                break
            else:
                choice1ReactionTimes[i] = timer.getTime()
                option1Items.setBorderColor('red')
                option1Items.draw()
                option1Money.draw()
                option1ItemsShape.draw()
                option1MoneyShape.draw()
                personChoosingForTextBox.draw()
                # Display Question Mark indicating PC is choosing this trial
                questionMarkTextBox.draw()
                win.flip()
                core.wait(pcSelectionOutlineDuration)
                choice1Responses[i] = choiceAmount
                break
            break
            # End PC Choice----------------------------------------------------#
        if trials[i] in [1, 5]:
            highPrefHighFameArrow.draw()
        elif trials[i] in [2, 6]:
            mixedPrefHighFamLeftArrow.draw()
            mixedPrefHighFamRightArrow.draw()
        else:  # PC Response trial type
            questionMarkTextBox.draw()
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
        computerResponse[i] = 1  # Indicate Computer Response is True
        if random.random() < .5:  # Randomly Select Option 1,2
            choice1Responses[i] = choiceAmount
            choice2Responses[i] = trialPics[random.randint(0, 11)]
        else:
            choice1Responses[i] = monetaryAmount
            choice2Responses[i] = trialMoneyOptions[random.randint(0, 11)]
        choice1ReactionTimes[i] = 'n/a'
        choice2ReactionTimes[i] = 'n/a'
        postChoiceDecisionRatings[i] = random.randint(
            1, 7)  # Ranomly Select Ratings
        postChoiceSelectedOptionRatings[i] = random.randint(1, 7)
        postChoiceReactionTimes[i] = 'n/a'
        try_faster_screen = visual.TextStim(
            win, text='Please make a faster decision next round!')
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(tryFasterDuration)
        displayResults()
        continue  # Starts a new trial

    # Delay Screen 1 #
    while timer.getTime() < delay1Duration:
        win.flip()

    # Choice 2 Loop
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
            if trials[i] in [1, 2, 5, 6]:  # Check if current trial is a player response trial
                # Player Choice--------------------------------------------------#
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
                    choice2ReactionTimes[i] = timer.getTime()
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
                # End Player Choice----------------------------------------------#
            else:
                # PC Choice------------------------------------------------------#
                choice2ReactionTimes[i] = timer.getTime()
                # Randomly choose optioon2Pos_ shape and option2Money_ textbox
                pcChoice = random.choice([(option2Pos1Shape, option2Money1),
                                          (option2Pos2Shape, option2Money2), (
                                              option2Pos3Shape, option2Money3),
                                          (option2Pos4Shape, option2Money4), (
                                              option2Pos5Shape, option2Money5),
                                          (option2Pos6Shape, option2Money6), (
                                              option2Pos7Shape, option2Money7),
                                          (option2Pos8Shape, option2Money8), (
                                              option2Pos9Shape, option2Money9),
                                          (option2Pos10Shape, option2Money10), (
                                              option2Pos11Shape, option2Money11),
                                          (option2Pos12Shape, option2Money12)])
                pcChoice[0].setLineColor('red')
                pcChoice[0].draw()
                drawOption2MoneyTextBoxes()
                win.flip()
                core.wait(pcSelectionOutlineDuration)
                choice2Responses[i] = pcChoice[1].getDisplayedText()
                break
                # End PC Choice----------------------------------------------------#
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
        # TO DO: add check if it is a pcLowPrefTrials or pcHighPrefTrials, and generate random choice
        #  between all boxes, look for 1/12 chance for each choice.
        timer.reset()
        while timer.getTime() < choice2Duration:
            if trials[i] in [1, 2, 5, 6]:  # Check if current trial is a player response trial
                # Player Choice--------------------------------------------------#
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
                    choice2ReactionTimes[i] = timer.getTime()
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
                # End Player Choice----------------------------------------------#
            else:
                # PC Choice------------------------------------------------------#
                choice2ReactionTimes[i] = timer.getTime()
                # randomly choose optioon2Pos_ shape and corresponding trialPic
                # index
                pcChoice = random.choice([(option2Pos1Shape, 0),
                                          (option2Pos2Shape, 1),
                                          (option2Pos3Shape, 2),
                                          (option2Pos4Shape, 3),
                                          (option2Pos5Shape, 4),
                                          (option2Pos6Shape, 5),
                                          (option2Pos7Shape, 6),
                                          (option2Pos8Shape, 7),
                                          (option2Pos9Shape, 8),
                                          (option2Pos10Shape, 9),
                                          (option2Pos11Shape, 10),
                                          (option2Pos12Shape, 11)])
                pcChoice[0].draw()
                drawOption2ItemBoxes()
                win.flip()
                core.wait(pcSelectionOutlineDuration)
                choice2Responses[i] = trialPics[pcChoice[1]]
                break
                # End PC Choice----------------------------------------------------#
            drawOption2ItemBoxes()
            win.flip()

    # Subject Response Check - Selects random responses if no response given
    if choice2Responses[i] == '':
        computerResponse[i] = 1
        if choice1Responses[i] == choiceAmount:
            choice2Responses[i] = trialPics[random.randint(0, 11)]
        else:
            choice2Responses[i] = trialMoneyOptions[random.randint(0, 11)]
        choice2ReactionTimes[i] = 'n/a'
        postChoiceDecisionRatings[i] = random.randint(1, 7)
        postChoiceSelectedOptionRatings[i] = random.randint(1, 7)
        postChoiceReactionTimes[i] = 'n/a'
        try_faster_screen = visual.TextStim(
            win, text='Please make a faster decision next round!')
        # Show 'try faster' screen
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
    decisionRatingScale.reset()
    selectedOptionRatingScale.reset()
    event.clearEvents()
    timer.reset()
    #if trials[i] in [1, 2, 5, 6]:
    while timer.getTime() < postChoice2ScaleDuration:  # JOCN duration: 3 seconds
        if not decisionRatingScale.noResponse and not selectedOptionRatingScale.noResponse:
            postChoiceReactionTimes[i] = timer.getTime()
            postChoiceDecisionRatings[i] = decisionRatingScale.getRating()
            postChoiceSelectedOptionRatings[
                i] = selectedOptionRatingScale.getRating()
            decisionRatingTitle.draw()
            selectedOptionRatingTitle.draw()
            decisionRatingScale.draw()
            selectedOptionRatingScale.draw()
            win.flip()
            core.wait(interTrialInterval)
            break
        decisionRatingTitle.draw()
        selectedOptionRatingTitle.draw()
        decisionRatingScale.draw()
        selectedOptionRatingScale.draw()
        win.flip()
    #else:  # Executes if PC response trial
    #    postChoiceDecisionRatings[i] = "n/a"
    #    postChoiceSelectedOptionRatings[i] = "n/a"

    # Subject Response Check - Selects random responses if no response given
    if postChoiceDecisionRatings[i] == '' or postChoiceSelectedOptionRatings[i] == '':
        computerResponse[i] = 1
        postChoiceDecisionRatings[i] = random.randint(1, 7)
        postChoiceSelectedOptionRatings[i] = random.randint(1, 7)
        postChoiceReactionTimes[i] = 'n/a'
        try_faster_screen = visual.TextStim(
            win, text='Please make a faster decision next round!')
        # Show 'try faster' screen
        event.clearEvents()
        try_faster_screen.draw()
        win.flip()
        core.wait(tryFasterDuration)
        displayResults()
        continue

    displayResults()
# End Main Loop------------------------------------------------------------------------#

# Write to .csv file with participants name, subj_id, in file name and/or
# confederate's id, confed_id
f = open(outputFile, 'w')
f.write('Trial Type, Money Option, Item Option, Trial Options, Choice 1, Choice 1 RT, Choice 2, Choice 2 RT, Decision Rating , Selected Option Rating, PostChoiceRT, Computer Response, Choosing For\n')
for i in range(len(trials)):
    f.write(str(trials[i]) + ',' + str(monetaryOptions[i]) + ',' + str(itemNumberOptions[i]) + ',' + " ".join(map(str, trialOptions[i]))
            + ',' + str(choice1Responses[i]) + ',' + str(choice1ReactionTimes[i]) + ',' + str(choice2Responses[i]) + ',' + str(choice2ReactionTimes[i])
            + ',' + str(postChoiceDecisionRatings[i]) + ',' + str(postChoiceSelectedOptionRatings[i]) + ',' + str(postChoiceReactionTimes[i]) + ',' + str(computerResponse[i])
            + ',' + str(youOrPersonTrials[i]) + "\n")
f.close()

win.close()
core.quit()
