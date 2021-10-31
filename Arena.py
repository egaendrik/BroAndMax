from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import random

x1 = 0
y1 = 0
x2 = 0
y2 = 0

def titikPusat():
    glPointSize(5)
    glColor3f(1, 1, 1)
    glBegin(GL_POINTS)
    glVertex(0, 0)
    glEnd()

def sumbuY():
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex(0, -30)
    glVertex(0, 26)
    glEnd()

def batasAtas():
    glLineWidth(7)
    glBegin(GL_LINE_LOOP)
    glVertex(30, 30)
    glVertex(-30, 30)
    glEnd()

def batasKanan():
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex(30, 30)
    glVertex(30, -30)
    glEnd()

def batasBawah():
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex(30, -30)
    glVertex(-30, -30)
    glEnd()

def batasKiri():
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glVertex(-30, -30)
    glVertex(-30, 30)
    glEnd()

def Box1():
    glPushMatrix()
    glTranslatef(x1,y1,0)
    glColor3f(255, 255, 0)
    glBegin(GL_QUADS)
    glVertex(0, -30)
    glVertex(-4, -30)
    glVertex(-4, -26)
    glVertex(0, -26)
    glEnd()
    glPopMatrix()

def Box2():
    glPushMatrix()
    glTranslatef(x2,y2,0)
    glColor3f(0, 0, 255)
    glBegin(GL_QUADS)
    glVertex(0, -30)
    glVertex(4, -30)
    glVertex(4, -26)
    glVertex(0, -26)
    glEnd()
    glPopMatrix()

def Wall():
    glPushMatrix()
    glTranslatef(x2,y2,0)
    glColor3f(0, 0, 255)
    glLineWidth(2.0)
    glBegin(GL_LINES)
    glVertex(30, 30)
    glVertex(-30, 30)
    glVertex(-30, -30)
    glVertex(30, -30)
    glEnd()
    glPopMatrix()

def Tembok():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(26, -26)
    glVertex(26, -22)
    glVertex(-26, -22)
    glVertex(-26, -26)
    glEnd()
    glPopMatrix()

def Tembok1():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-30, -14)
    glVertex(-4, -14)
    glVertex(-4, -18)
    glVertex(-30, -18)
    glEnd()
    glPopMatrix()

def Tembok2():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-30, -6)
    glVertex(-18, -6)
    glVertex(-18, -10)
    glVertex(-30, -10)
    glEnd()
    glPopMatrix()

def Tembok3():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-14, -6)
    glVertex(20, -6)
    glVertex(20, -10)
    glVertex(-14, -10)
    glEnd()
    glPopMatrix()

def Tembok4():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-26, 2)
    glVertex(0, 2)
    glVertex(0, -2)
    glVertex(-26, -2)
    glEnd()
    glPopMatrix()

def Tembok5():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-2, 10)
    glVertex(10, 10)
    glVertex(10, 6)
    glVertex(-2, 6)
    glEnd()
    glPopMatrix()

def Tembok6():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-30, 10)
    glVertex(-6, 10)
    glVertex(-6, 6)
    glVertex(-30, 6)
    glEnd()
    glPopMatrix()

def Tembok7():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-30, 18)
    glVertex(-22, 18)
    glVertex(-22, 14)
    glVertex(-30, 14)
    glEnd()
    glPopMatrix()

def Tembok8():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-18, 18)
    glVertex(-4, 18)
    glVertex(-4, 14)
    glVertex(-18, 14)
    glEnd()
    glPopMatrix()

def Tembok9():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-26, 26)
    glVertex(-10, 26)
    glVertex(-10, 22)
    glVertex(-26, 22)
    glEnd()
    glPopMatrix()

def Tembok10():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(-6, 26)
    glVertex(0, 26)
    glVertex(0, 22)
    glVertex(-6, 22)
    glEnd()
    glPopMatrix()

def Tembok11():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(4, -14)
    glVertex(30, -14)
    glVertex(30, -18)
    glVertex(4, -18)
    glEnd()
    glPopMatrix()

def Tembok12():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(24, -6)
    glVertex(30, -6)
    glVertex(30, -10)
    glVertex(24, -10)
    glEnd()
    glPopMatrix()

def Tembok13():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(4, 2)
    glVertex(30, 2)
    glVertex(30, -2)
    glVertex(4, -2)
    glEnd()
    glPopMatrix()

def Tembok14():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(14, 10)
    glVertex(20, 10)
    glVertex(20, 6)
    glVertex(14, 6)
    glEnd()
    glPopMatrix()

def Tembok15():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(24, 10)
    glVertex(30, 10)
    glVertex(30, 6)
    glVertex(24, 6)
    glEnd()
    glPopMatrix()

def Tembok16():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(0, 18)
    glVertex(26, 18)
    glVertex(26, 14)
    glVertex(0, 14)
    glEnd()
    glPopMatrix()

def Tembok17():
    glPushMatrix()
    glColor3f(0, 255, 0)
    glBegin(GL_QUADS)
    glVertex(4, 26)
    glVertex(26, 26)
    glVertex(26, 22)
    glVertex(4, 22)
    glEnd()
    glPopMatrix()

def Finish1():
    glPushMatrix()
    glColor3f(255, 0, 0)
    glBegin(GL_QUADS)
    glVertex(-2, 30)
    glVertex(3, 27)
    glVertex(2, 26)
    glVertex(-3, 29)
    glEnd()
    glPopMatrix()

def Finish2():
    glPushMatrix()
    glColor3f(255, 0, 0)
    glBegin(GL_QUADS)
    glVertex(2, 30)
    glVertex(3, 29)
    glVertex(-2, 26)
    glVertex(-3, 27)
    glEnd()
    glPopMatrix()
def input_keyboard(key, x, y):
    global x1, y1, x2, y2
    if key == GLUT_KEY_UP:
        y1 += 2
        y2 += 2
    elif key == GLUT_KEY_DOWN:
        y1 -= 2
        y2 -= 2
    elif key == GLUT_KEY_RIGHT:
        x1 -= 2
        x2 += 2
    elif key == GLUT_KEY_LEFT:
        x1 += 2
        x2 -= 2

def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-30, 30, -30, 30)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    titikPusat()
    batasAtas()
    sumbuY()
    Box1()
    Box2()
    batasAtas()
    batasKanan()
    batasKiri()
    batasBawah()
    Tembok()
    Tembok1()
    Tembok2()
    Tembok3()
    Tembok4()
    Tembok5()
    Tembok6()
    Tembok7()
    Tembok8()
    Tembok9()
    Tembok10()
    Tembok11()
    Tembok12()
    Tembok13()
    Tembok14()
    Tembok15()
    Tembok16()
    Tembok17()
    Finish1()
    Finish2()
    #Wall()
    glutSwapBuffers()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(1,update,0)

def main():
    glutInit(sys.argv) 
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowSize(600, 600)
    glutInitWindowPosition(50, 50)
    glutCreateWindow("YAHAHAHA HAYYUKK")
    glutDisplayFunc(draw)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(50, update, 0)
    glutMainLoop()


main()