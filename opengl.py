from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
import numpy


def init_fun():
    print('Init')
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, 1, 0.01, 1000)
    gluLookAt(-10000.0, 10.0, 10.0, 0, 0, 0, 0, 1, 0)

    glLightfv(GL_LIGHT0, GL_POSITION, [2.0, 2.0, 2.0])
    glColor3f(1, 1, 1)
    glLoadIdentity()

    glPushMatrix()
    glScale(0.5, 0.5, 0.5)
    glCallList(1)
    glPopMatrix()

    glFlush()


def create_compile_shader(shader_type, source):
    shader = glCreateShader(shader_type)
    glShaderSource(shader, source)
    glCompileShader(shader)
    result = glGetShaderiv(shader, GL_COMPILE_STATUS)

    if result != GL_TRUE:
        raise Exception("Shader compilation failed.")

    return shader


def display_fun():
    print('Load')
    glClear(GL_COLOR_BUFFER_BIT)

    glNewList(1, GL_COMPILE)
    glBegin(GL_TRIANGLES)

    for i in range(5):
        v = []
        for i in range(3):
            x = random.random()
            y = random.random()
            z = random.random()
            v.append([x, y, z])

        m1 = numpy.matrix(v[0])
        m2 = numpy.matrix(v[1])
        m3 = numpy.matrix(v[2])

        norm = numpy.cross(m1 - m2, m3 - m2)

        glNormal3f(norm[0, 0], norm[0, 1], norm[0, 2])

        glVertex3f(m1[0, 0], m1[0, 1], m1[0, 2])
        glVertex3f(m2[0, 0], m2[0, 1], m2[0, 2])
        glVertex3f(m3[0, 0], m3[0, 1], m3[0, 2])


    glEnd()
    glEndList()

    init_fun()


if __name__ == '__main__':
    glutInit()
    glutInitWindowSize(640, 480)
    glutCreateWindow(b"The Cube")
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutDisplayFunc(display_fun)

    # create and compile shaders
    vertex_shader = create_compile_shader(GL_VERTEX_SHADER, """
varying vec3 vPos;
varying vec3 vNormal;

void main(void) {
    vPos = gl_Vertex;
    vNormal = gl_Normal;

    gl_Position = gl_ModelViewProjectionMatrix * gl_Vertex;
}
    """)
    fragment_shader = create_compile_shader(GL_FRAGMENT_SHADER, """
varying vec3 vPos;
varying vec3 vNormal;

void main(void) {
    gl_FragColor = vec4(normalize(vNormal), 1.0);
}
    """)

    # build shader program
    program = glCreateProgram()
    glAttachShader(program, vertex_shader)
    glAttachShader(program, fragment_shader)
    glLinkProgram(program)

    try:
        glUseProgram(program)
    except (GLError, RuntimeError) as err:
        raise RuntimeError(err)

    glutMainLoop()
