from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def myinit():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1,1,1,1)
    glClear(GL_COLOR_BUFFER_BIT)
    # glOrtho(-10,10,-10,10,-10,10)
    gluPerspective(60,1,0.1,50)
    gluLookAt(10,10,10,0,0,0,0,1,0)
############################################################################
def draw1():
    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0,0,0)
    glLineWidth(2)
    glTranslate(1,0,0)
    glScale(3,.25,3)
    glutSolidCube(1)
    glPopAttrib()
    glPopMatrix()

    # glLoadIdentity()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0,0,0)
    glTranslate(-.25,0,-3.25)
    glScale(3,2.5,.5)
    glutWireCube(1)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0)
    glTranslate(-.31, -1.5, 1.20)
    glScale(1, 5, 1)
    glutWireCube(.5)
    glPopAttrib()
    glPopMatrix()

    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0)
    glTranslate(2.20, -1.5, 1.20)
    glScale(1, 5, 1)
    glutWireCube(.5)
    glPopAttrib()
    glPopMatrix()


    glPushMatrix()
    glPushAttrib(GL_ALL_ATTRIB_BITS)
    glColor(0, 0, 0)
    glTranslate(1.75, -1.5, -2.20)
    glScale(1, 3.8, 1)
    glutWireCube(.5)
    glPopAttrib()
    glPopMatrix()



def main():
    glMatrixMode(GL_PROJECTION)
    glClearColor(1, 1, 1, 1)
    glClear(GL_COLOR_BUFFER_BIT)

    glColor3f(1,1,0)
    draw1()

    glTranslate(-5,5,0)
    draw1()
    glLoadIdentity()

    glFlush()





###########################
glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
glutInitWindowSize(600,700)
glutCreateWindow(b"chair")
glutDisplayFunc(main)
# glutIdleFunc(draw)
myinit()
glutMainLoop()




