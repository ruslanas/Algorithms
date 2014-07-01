from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

import random
from graphics.vector import Vec3

angle = random.randint(0, 90)


def init_fun():
    print('Init')
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(90, 1, 0.01, 1000)
    gluLookAt(-10000.0, 10.0, 10.0, 0, 0, 0, 0, 1, 0)

    glLightfv(GL_LIGHT0, GL_POSITION, [2.0, 2.0, 2.0])
    glLightModeli(GL_LIGHT_MODEL_TWO_SIDE, GL_TRUE)
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
    global angle
    angle += 10
    glClear(GL_COLOR_BUFFER_BIT)

    glNewList(1, GL_COMPILE)
    glBegin(GL_TRIANGLES)

    faces = [
        [Vec3(0, 0, 0), Vec3(1, 0, 0), Vec3(0, 1, 0)],
        [Vec3(0, 1, 0), Vec3(1, 0, 0), Vec3(1, 1, 0)],
        [Vec3(0, 0, 0), Vec3(0, 0, 1), Vec3(0, 1, 0)],
        [Vec3(0, 1, 0), Vec3(0, 0, 1), Vec3(0, 1, 1)],
        [Vec3(0, 0, 1), Vec3(1, 0, 1), Vec3(0, 1, 1)],
        [Vec3(1, 0, 1), Vec3(1, 1, 1), Vec3(0, 1, 1)],
        [Vec3(0, 0, 0), Vec3(1, 0, 0), Vec3(1, 0, 1)],
        [Vec3(0, 0, 1), Vec3(0, 0, 0), Vec3(1, 0, 1)],
    ]

    for face in faces:

        for vertex in face:
            vertex.rotate_x(angle)
            vertex.rotate_y(angle)

        # cross product
        norm = (face[0] - face[1]) ^ (face[0] - face[2])

        glNormal3f(norm.x, norm.y, norm.z)

        glColor3f(1, 0, 0)
        glVertex3f(face[0].x, face[0].y, face[0].z)
        glColor3f(0, 1, 0)
        glVertex3f(face[1].x, face[1].y, face[1].z)
        glColor3f(0, 0, 1)
        glVertex3f(face[2].x, face[2].y, face[2].z)

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
    vec3 light = vec3(0.5, 0.5, 0.5);
    vec3 color = clamp(dot(normalize(vNormal), light), 0.0, 1.0);
    gl_FragColor = vec4(mix(color, vec3(1.0, 0.0, 0.0), 0.5), 1.0);
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
