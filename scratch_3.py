from OpenGL.GL import* #فيها برسم الموديل
from OpenGL.GLUT import*    #
from OpenGL.GLU import *# فيها حاجات جاهزه
import numpy as np
from math import *



def trees():

    glBegin(GL_POLYGON)
    glVertex(1, 1, -1)
    glVertex(-1, 1, -1)
    glVertex(-1, -1, 1)
    glVertex(1, -1, 1)
    glEnd()


def my_polygon():

    glBegin(GL_QUADS)
    glVertex(1, 1, -1)
    glVertex(-1, 1, -1)
    glVertex(-1, 1, 1)
    glVertex(1, 1, 1)
    glEnd()
def sky(x):
    glutSolidSphere(x,100,100)


def myInit():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0, .6, .1, 1)
    glClear((GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT))
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()

    gluPerspective(90,1,0.1,45)
    gluLookAt(5,10,10,
              0,0,0,
              0,1,0)
    #glClearColor(1,1,1,1)


angle=0
x=0
forward=True
def display():


    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    global angle
    global x
    global forward

    glMatrixMode(GL_MODELVIEW)

    # the Road
    glLoadIdentity()
    glScale(1000,0,4)
    glColor3f(0.7, 0.7, 0.7)
    glBegin(GL_POLYGON)
    glVertex(1, 1, -1)
    glVertex(-1, 1, -1)

    glVertex(-1, -1, 1)
    glVertex(1, -1, 1)
    glEnd()


    # polygon on road
    glLoadIdentity()
    glColor3f(1,1,0)
    glScale(4, 0, .5)
    glTranslate(0, 0, -2)
    my_polygon()

    glLoadIdentity()
    glScale(4, 0, .5)
    glTranslate(0, 0, 4)
    my_polygon()

    glLoadIdentity()
    glScale(4, 0, .5)
    glTranslate(-3, 0, -2)
    my_polygon()

    glLoadIdentity()
    glScale(4, 0, .5)
    glTranslate(-3, 0, 4)
    my_polygon()

    glLoadIdentity()
    glScale(4, 0, .5)
    glTranslate(3, 0, 4)
    my_polygon()

    glLoadIdentity()
    glScale(4, 0, .5)
    glTranslate(3, 0, -2)
    my_polygon()

    '''
#traffic
    glLoadIdentity()
    glTranslate(-8,4,-1)
    glScale(.25,2,0)
    glColor3f(0,0,0)
    glBegin(GL_POLYGON)
    glVertex(1,1,0)
    glVertex(-1,1,0)
    glVertex(-1,-1,0)
    glVertex(1,-1,0)
    glEnd()
'''


#the sky
    #glColor3f(.4,.3,.8) #night mood
    glColor3f(0, .2, 1)
    glLoadIdentity()
    glScale(100,1,3)
    glTranslate(0,10,0)
    glBegin(GL_POLYGON)
    glVertex(1, 1, -1)
    glVertex(-1, 1, -1)
    glVertex(-1, -1, 1)
    glVertex(1, -1, 1)
    glEnd()
    glLoadIdentity()







#the Sky
#sun
    glColor3f(1,1,1)#night mode
    glColor3f(.8, .4, 0)
    glLoadIdentity()
    glTranslate(-x*.05+3, 10, 2)
    sky(.25)

#First cloud
   # glColor3f(.7,.7,.7) #night mode
    glColor3f(1, 1, 1)
    glLoadIdentity()
    glTranslate(0+x*.05, 10, 2)
    sky(.45)


    glLoadIdentity()
    glTranslate(.5+x*.05, 10, 2)
    sky(.25)


    glLoadIdentity()
    glTranslate(-0.5+x*.05, 10, 2)
    sky(.25)


#second tree

    glLoadIdentity()
    glColor3f(.4, .3, 0)
    glTranslate(-4, 2, -5)
    glScale(.5, 2, 0)
    trees()

    glLoadIdentity()
    glTranslate(-4.5, 4, -5)
    glColor3f(.4, .6, 0)
    glutSolidSphere(1,100,100)

    glLoadIdentity()
    glTranslate(-3.5, 4, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glTranslate(-3.5, 5, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glTranslate(-4.5, 5, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glTranslate(-4, 6, -5)
    glutSolidSphere(1, 100, 100)

    #third tree
    glLoadIdentity()
    glColor3f(.4, .3, 0)
    glTranslate(2, 2, -5)
    glScale(.5, 2, 0)
    trees()

    glLoadIdentity()
    glTranslate(1.5, 4, -5)
    glColor3f(.4, .6, 0)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glTranslate(2.5, 4, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glTranslate(2.5, 5, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glTranslate(1.5, 5, -5)
    glutSolidSphere(1, 100, 100)

    glLoadIdentity()
    glTranslate(2, 6, -5)
    glutSolidSphere(1, 100, 100)
# المكعب اللى تحت
    glColor3f(0, 0, 0.4)
    glLoadIdentity()
    glTranslate(0+x,+2,0)
    glScale(1,0.25,0.5)
    glutSolidCube(5)

#المكعب اللى فوق
    glColor3f(0, 0, 0.4)
    glLoadIdentity()
    glTranslate(0+x,.25*5+2,0)
    glScale(0.5,.25,.5)
    glutSolidCube(5)

    #glColor3f(0.5, 0.5, 0.5)
    glColor3f(1.0,0,0)
    glLoadIdentity()
    glTranslate(x,0,0)
    glBegin(GL_POLYGON)
    glVertex(1.3, .75+2, 1.3)
    glVertex(1.3, .75+2, -1)
    glVertex(1.3, 1.5+2, -1)
    glVertex(1.3, 1.5+2, 1.3)
    glEnd()

#first wheel
    glLoadIdentity()
    glColor3f(0,0,.9)
    glTranslate(2.5+x,-2.5*.25+2,.5*2.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.15,.5,12,8)
#second wheel
    glLoadIdentity()
    glTranslate(2.5+x, -2.5 * .25+2,- .5 * 2.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.15, .5, 12, 8)
#third wheel
    glLoadIdentity()
    glTranslate(-2.5+x, -2.5 * .25+2, .5 * 2.5)
    glRotate(angle, 0, 0, 1)
    glutWireTorus(0.15, .5, 12, 8)

#forth wheel
    glLoadIdentity()
    glTranslate(-2.5+x, -2.5 * .25+2, -.5 * 2.5)
    glRotate(angle,0,0,1)
    glutWireTorus(0.15, .5, 12, 8)

#first light

    glColor3f(1,1,0)
    glLoadIdentity()
    glTranslate(2.5+x,-.5*2.5*.25+2,-2.5*.25)
    glutWireSphere(.25,100,100)

#second light


    glLoadIdentity()
    glTranslate(2.5+x, -.5*2.5*.25+2, 2.5*.25)
    glutWireSphere(.25, 100, 100)











    if forward:
        x+=.05
        angle -= .1
        if x>10:
            forward=False
    else:
        x-=.05
        angle += .1
        if x<-20:
            forward=True







    glutSwapBuffers()
glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH)# لو استخدمت

glutInitWindowSize(720,1260)
glutCreateWindow(b"Moving Car")
myInit()
glutDisplayFunc(display)
glutIdleFunc(display)
glutMainLoop()

