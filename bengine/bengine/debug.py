import glfw
from bengine.input import Input
from bengine.config import Config
from OpenGL import GL

class Debug(object):
    @staticmethod
    def update() -> None:
        if not Config.get_debug(): return
        
        if Input.is_action_just_pressed(glfw.KEY_PERIOD):
            Config.set_wireframe(not Config.get_wireframe())
            draw = GL.GL_LINE if Config.get_wireframe() else GL.GL_FILL
            GL.glPolygonMode(GL.GL_FRONT_AND_BACK, draw)