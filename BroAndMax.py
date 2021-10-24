from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import sys
import random

# Variabel awal tranlasi
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

# Untuk membuat sumbu X


def sumbuX():
    glBegin(GL_LINE_LOOP)
    glVertex(-30, 0)
    glVertex(30, 0)
    glEnd()

# Untuk membuat sumbu Y


def sumbuY():
    glBegin(GL_LINE_LOOP)
    glVertex(0, -30)
    glVertex(0, 30)
    glEnd()

# Untuk membuat objek


def Box1():
    glPushMatrix()
    glTranslatef(x1,y1,0)
    glColor3f(255, 0, 0)
    glBegin(GL_QUADS)
    glVertex(0, 0)
    glVertex(0, 2)
    glVertex(2, 2)
    glVertex(2, 0)
    glEnd()
    glPopMatrix()

def Box2():
    glPushMatrix()
    glTranslatef(x2,y2,0)
    glColor3f(0, 0, 255)
    glBegin(GL_QUADS)
    glVertex(0, 0)
    glVertex(0, 2)
    glVertex(-2, 2)
    glVertex(-2, 0)
    glEnd()
    glPopMatrix()

def input_keyboard(key, x, y):
    global x1, y1, x2, y2
    if key == GLUT_KEY_UP:
        y1 += 2
        y2 += 2
        print("Tombol Atas ditekan ", "x : ", x2, " y : ", y2)
    elif key == GLUT_KEY_DOWN:
        y1 -= 2
        y2 -= 2
        print("Tombol Bawah ditekan ", "x : ", x2, " y : ", y2)
    elif key == GLUT_KEY_RIGHT:
        x1 -= 2
        x2 += 2
        print("Tombol Kanan ditekan ", "x : ", x2, " y : ", y2)
    elif key == GLUT_KEY_LEFT:
        x1 += 2
        x2 -= 2
        print("Tombol Kiri ditekan ", "x : ", x2, " y : ", y2)

# Untuk menampung dan menggambar semua objek


def draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-30, 30, -30, 30)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    titikPusat()
    #sumbuX()
    sumbuY()
    Box1()
    Box2()
    glutSwapBuffers()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():  # fungsi utama
    glutInit(sys.argv)  # membuat inisialisasi
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)  # pemberian warna
    # menentukan panjang dan lebar dari jendela yang menampilkan gambar
    glutInitWindowSize(600, 600)
    # menentukan posisi jendela gambar pada layar komputer
    glutInitWindowPosition(50, 50)
    # membuat nama jendela
    glutCreateWindow("BRO AND MAX")
    glutDisplayFunc(draw)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(50, update, 0)
    glutMainLoop()  # menjalankan program


main()  # Memanggil fungsi utama
