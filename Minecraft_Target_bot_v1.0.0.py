from turtle import position
import pyautogui
import time
import keyboard
import win32api, win32con

#dimensions of game screen
x=0
y=40
w=1920
h=980

x_crosshair,y_crosshair=(960,533)
# rgb values of the colour you are detecting
# rgb for red (minecraft) 141 34 34(top) 84 21 21(side) 113 28 28(side)  69 16 19 (bottom)
# 233,28,35
r1,g1,b1=(234,28,36)
r2,g2,b2=(187,22,28)
r3,g3,b3=(140,17,21)
r4,g4,b4=(115,14,18)

def detectTarget(spacing):
   global pic
   pic = pyautogui.screenshot(region=(x,y,w,h))
   # pic.save(r"C:\Users\ngnah\OneDrive\Desktop\personal\randoms\code\Python\bots\colour_detector\screenshot.png") --use this to check image
   for x_check in range(x, w, spacing):
      for y_check in range(y, h, spacing):
         r_pixel,g_pixel,b_pixel = pic.getpixel((x_check,y_check))
         if r_pixel in (r1,r2,r3,r4) and g_pixel in (g1,g2,g3,g4) and b_pixel in (b1,b2,b3,b4):
            global x_target 
            x_target = x_check + x 
            global y_target
            y_target = y_check + y #this gives the coords of the target (red)
            return True #this means there is target (red) on the screen


def crosshairCheckRed():
   if r_crosshair in (r1,r2,r3,r4) or g_crosshair in (g1,g2,g3,g4) or b_crosshair in (b1,b2,b3,b4):
      return True
   else:
      return False

def crosshairCheckMargin(margin): #margin in px
   crosshairCheckMargin.margin = margin
   if abs(x_crosshair - x_target) <= margin and abs(y_crosshair - y_target) <= margin: 
      return True
   else:
      return False

def stopAll():
   pyautogui.keyUp("right")
   pyautogui.keyUp("left")
   pyautogui.keyUp("down")
   pyautogui.keyUp("up")


def action(type):
   if type == "shoot_bow":
      pyautogui.keyDown("e")
      time.sleep(1.1)
      pyautogui.keyUp("e")
   if type == "punch":
      pyautogui.press("q")
   if type == "break":
      pyautogui.keyDown("q")
      time.sleep(1)
      pyautogui.keyUp("q")
   if type == "place":
      pyautogui.press("e")

#good settings for
# shoot_bow: some precision (some margin), low speed, high accuracy (low check spacing)
# punch: max precision, high speed, low accuracy
# break: max precision, some speed, low accuracy
# place: max precision, some speed, low accuracy


while keyboard.is_pressed("p") == False:
   detectTarget(20)
   r_crosshair,g_crosshair,b_crosshair=pic.getpixel((x_crosshair,y_crosshair))
   if detectTarget(20) == True:
      # picture = pyautogui.screenshot(region=(x_target-20,y_target-20,40,40))
      # picture.save(r"C:\Users\ngnah\OneDrive\Desktop\personal\randoms\code\Python\bots\colour_detector\screenshot.png")
      if crosshairCheckRed() == True or crosshairCheckMargin(1) == True: #crosshair is either in red or in margin
         stopAll()
         action("punch")
      else:
         if x_crosshair < x_target - crosshairCheckMargin.margin:
            pyautogui.keyUp("left")
            pyautogui.keyDown("right")
         else:
            pyautogui.keyUp("right")
            if x_crosshair > x_target + crosshairCheckMargin.margin:
               pyautogui.keyDown("left")
            else:
               pyautogui.keyUp("left")
         if y_crosshair < y_target - crosshairCheckMargin.margin:
            pyautogui.keyUp("up")
            pyautogui.keyDown("down")
         else:
            pyautogui.keyUp("down")
            if y_crosshair > y_target + crosshairCheckMargin.margin:
               pyautogui.keyDown("up")
            else:
               pyautogui.keyUp("up")
   else:
      stopAll()



# ===============================HOW IT WORKS=======================

# functions

# check if crosshair in red
# check if crosshair in margin
# stop all actions
# action



# what should the process be?
# while button p is not pressed:
#    scan from up to down, left to right
#    at first instance of a red colour, save x and y position of red colour in x and y variables
#    get x and y of crosshair
#       if there is red:
#          if crosshair in red or check if x_crosshair = x_target and y_crosshair = y_target with margin:
#             stop all actions
#             perform action
#          else:
#             if x_crosshair < x_target with margin:
#             stop turning left
#             then turn right
#             else:
#                stop turning right
#                if x_crosshair > x_target with margin:
#                   then turn left 
#                else: 
#                   stop turning left
#          if y_crosshair < y_target with margin:
#             stop turning up
#             then turn down
#          else:
#             stop turning down
#             if y_crosshair > y_target with margin:
#                then turn up:
#             else:
#                stop turning up
#       else:
#          stop all actions

#======================================================================














# def click(x,y):
#    win32api.SetCursorPos((x,y))
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#    time.sleep(0.01) #pauses script for 0.01s
#    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# def walk(duration):
#    pyautogui.keyDown("w")
#    time.sleep(duration)
#    pyautogui.keyUp("w")

# def detectColour():
#    global pic
#    pic = pyautogui.screenshot(region=(x,y,w,h))
#    # pic.save(r"C:\Users\ngnah\OneDrive\Desktop\personal\randoms\code\Python\bots\colour_detector\screenshot.png") --use this to check image
#    for x_check in range(x, w, 110):
#       for y_check in range(y, h, 110):
#          r_pixel,g_pixel,b_pixel = pic.getpixel((x_check,y_check))
#          if r_pixel in (r1,r2,r3,r4) and g_pixel in (g1,g2,g3,g4) and b_pixel in (b1,b2,b3,b4):
#             global x_target 
#             x_target = x_check+x
#             global y_target 
#             y_target = y_check+y
#             # print(x_target, y_target, "red")
#             return True

# def resetKeys_x():
#    pyautogui.keyUp("right")
#    pyautogui.keyUp("left")
# def resetKeys_y():
#    pyautogui.keyUp("down")
#    pyautogui.keyUp("up")


   
# def turnToColour():
#    if x_target < x_crosshair:
#       # print("turning left")
#       pyautogui.keyDown("left")
#    elif x_target > x_crosshair:
#       # print("turning right")
#       pyautogui.keyDown("right")
#    if y_target < y_crosshair:
#       # print("turning up")
#       pyautogui.keyDown("up")
#    elif y_target > y_crosshair:
#       # print("turning down")
#       pyautogui.keyDown("down")
      


# while keyboard.is_pressed("p") == False:
#    resetKeys_y()
#    resetKeys_x()
#    detectColour()
#    r_crosshair,g_crosshair,b_crosshair=pic.getpixel((x_crosshair,y_crosshair))
#    if detectColour() != None: #there is a red block on screen
#       pyautogui.keyDown("Shift")
#       walk(0.1)
#       if r_crosshair not in (r1,r2,r3,r4) or g_crosshair not in (g1,g2,g3,g4) or b_crosshair not in (b1,b2,b3,b4): #when red not in crosshair
#          pyautogui.keyUp("q") #dont break
#          if abs(x_crosshair - x_target) <= 35 or abs(y_crosshair - y_target) <= 35: #if red is close to crosshair on one axis (35px is the margin)
#             # print("at least one is correct")
#             if abs(y_crosshair - y_target) <= 35: 
#                # print("y is correct")
#                resetKeys_y()
#                # print("stopped y")
#             if abs(x_crosshair - x_target) <= 35:
#                # print("x is correct")
#                resetKeys_x()
#                # print("stopped x")
#          if abs(x_crosshair - x_target) <= 35 and abs(y_crosshair - y_target) <= 35: #if red is close to crosshair
#                # print("x and y are correct")
#                resetKeys_y()
#                resetKeys_x()
#                # print("block broken")
#          else: #if red is not close to crosshair
#             # print("none are correct")
#             pyautogui.keyUp("q")
#             turnToColour()
#             # print("changed direction")
#       else: #when block in crosshair
#          pyautogui.keyDown("q")
#          resetKeys_y()
#          resetKeys_x()
#    else: #when no red on screen
#       # print("no red")
#       resetKeys_y()
#       resetKeys_x()
#       pyautogui.keyUp("shift")
#       pyautogui.keyUp("q")
      
#       # picture = pyautogui.screenshot(region=(x_target-20,y_target-20,100,100))
#       # picture.save(r"C:\Users\ngnah\OneDrive\Desktop\personal\randoms\code\Python\bots\colour_detector\screenshot.png")



