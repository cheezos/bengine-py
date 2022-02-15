import glfw
from OpenGL import GL
import numpy as np
import pyrr

class Window(object):
    _window: glfw._GLFWwindow | None = None
    _title: str = "Bepto Engine"
    _size: tuple[int, int]
    _last_time: float = 0.0
    _delta_time: float = 0.0
    _fps: int = 0
        
    @staticmethod
    def create_window(title: str, width: int, height: int) -> None:
        if not glfw.init():
            raise Exception("Failed to initialize GLFW")

        print("Initialized GLFW")

        maximize = False

        if width == 0 or height == 0:
            width = 1280
            height = 720
            maximize = True
        
        Window._window = glfw.create_window(width, height, title, None, None)

        if not Window._window:
            glfw.terminate()
            raise Exception("Failed to create GLFW window")
        
        print("Created GLFW window")

        glfw.make_context_current(Window._window)

        monitor = glfw.get_primary_monitor()
        vidmode = glfw.get_video_mode(monitor)
        mon_width = vidmode.size.width
        mon_height = vidmode.size.height
        pos_x = int((mon_width / 2) - (width / 2))
        pos_y = int((mon_height / 2) - (height / 2))

        glfw.swap_interval(0) # vsync
        glfw.set_window_attrib(Window._window, glfw.RESIZABLE, glfw.TRUE) # resizable

        glfw.set_window_pos(Window._window, pos_x, pos_y)
        glfw.set_input_mode(Window._window, glfw.RAW_MOUSE_MOTION, glfw.TRUE)
        glfw.set_cursor_pos(Window._window, width / 2, height / 2)
        glfw.show_window(Window._window)
        
        GL.glEnable(GL.GL_CULL_FACE)

        if maximize:
            glfw.maximize_window(Window._window)

        glfw.set_framebuffer_size_callback(Window._window, lambda _, w, h : Window._resize_callback(w, h))

        Window._title = title
        Window._size = (width, height)
        Window._ready = True
    
    @staticmethod
    def update() -> None:
        glfw.swap_buffers(Window._window)
        glfw.poll_events()

        GL.glClearColor(0.1, 0.1, 0.1, 1)
        GL.glClear(int(GL.GL_COLOR_BUFFER_BIT) | int(GL.GL_DEPTH_BUFFER_BIT))

        Window._delta_time = glfw.get_time() - Window._last_time
        Window._last_time = glfw.get_time()
        Window._fps = int(1.0 / Window._delta_time)

        glfw.set_window_title(Window._window, f"{Window._title} | FPS: {Window._fps}")

    @staticmethod
    def cleanup() -> None:
        glfw.terminate()
        Window._window = None

    @staticmethod
    def _resize_callback(width: int, height: int) -> None:
        GL.glViewport(0, 0, width, height)
        Window._size = (width, height)

    @staticmethod
    def get_window() -> glfw._GLFWwindow | None:
        return Window._window

    @staticmethod
    def get_title() -> str:
        return Window._title
    
    @staticmethod
    def get_size() -> tuple[int, int]:
        return Window._size

    @staticmethod
    def get_fps() -> int:
        return Window._fps

    @staticmethod
    def get_delta_time() -> float:
        return Window._delta_time