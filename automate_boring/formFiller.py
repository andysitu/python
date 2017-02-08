#! python3
# formFiller.py - Automatically fills the form.

import pyautogui, time

# Set mouse to the coordinates
nameField = (663, 225)
submitButton = (672, 830)
submitButtonColor = (75, 141, 249)
submitAnotherLink = (760, 224)

formData = [{'name': 'Alice', 'fear': 'eavesdroppers', 'source': 'wand',
             'robocop': 4, 'comments': 'Tell Bob I said hi.'},
            {'name': 'Bob', 'fear': 'bees', 'source': 'amulet', 'robocope': 4,
             'comments': 'n/a'},
            {'name': 'Carol', 'fear': 'puppets', 'source': 'crystal ball',
             'robocop': 1, 'comments': 'Please take the puppets out of the break room.'},
            {'name': 'Alex Murphy', 'fear': 'ED-209', 'source': 'money',
             'robocop': 5, 'comments': 'Protect the innocent. Serve the public trust. Uphold the law.'},
            ]

pyautogui.PAUSE = 0.5

for person in formData:
    #Give the user a chance to kill the script.
    print('>>> 4 Seconds pause to let user press ctrl-C <<<')
    time.sleep(5)

    # Wait until the form page has loaded.
    While not pyautogui.pixelMatchesColor(submitButton[0], submitButton[1],
                                          submitButtonColor):
        time.sleep(0.5)

    print('Enter %s info' % (person['name']))
    pyautogui.click(nameField[0], nameField[1])

    # Fill out the Name field.
    pyautogui.typewrite(person['name'] + '\t')

    # Fill out the Greatest Fear(s) field.
    pyautogui.typewrite(person['fear']+ '\t')

    # Filll out the source of Wizard Powers field.
    if person['source'] == 'wand':
        pyautogui.typewriter(['down', '\t'])
    elif person['source'] =='amulet':
        pyautogui.typewriter(['down', 'down', '\t'])
    elif person['source'] == 'crystal ball':
        pyautogui.typewriter(['down', 'down', 'down', '\t'])
    elif person['source'] == 'money':
        pyautogui.typewriter(['down', 'down', 'down', 'down', '\t'])

    # Fill out the RobotCop field.
    if person['robocop'] == 1:
        pyautogui.typewrite([' ', '\t'])
    elif person['robocop'] == 2:
        pyautogui.typewrite(['right', '\t'])
    elif person['robocop'] == 3:
        pyautogui.typewrite(['right', 'right', '\t'])
    elif person['robocop'] == 4:
        pyautogui.typewrite(['right', 'right', 'right', '\t'])
    elif person['robocop'] == 5:
        pyautogui.typewrite(['right', 'right', 'right', 'right', '\t'])

    # Fill out the Additonal Comments field
    pyautogui.typewrite(person['comments'] + '\t')

    # Click submit.
    pyautogui.press('enter')

    # Wait until pae form ahs loaded.
    print('Clicked Submit.')
    time.sleep(5)

    # Click the Submit another response link
    pyautogui.click(submitAnotherLink[0], submitAnotherLink[1])
