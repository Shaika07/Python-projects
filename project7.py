import pyautogui
o="No"
while o=="No":
    o=pyautogui.confirm('Have you clicked inside text box where you want to write ?', buttons=['Yes','No'])
for i in range(1, 50):
    pyautogui.write('i love you afreen',interval=0.2)
    pyautogui.press('enter')
