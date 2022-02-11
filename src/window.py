import glfw
from OpenGL import GL

class Window(object):
    window = None
    resolution: tuple[int, int]
    last_time: float = 0.0
    delta_time: float = 0.0
    fps: int = 0
        
    @staticmethod
    def create_window(width: int, height: int) -> None:
        if not glfw.init():
            raise Exception("Failed to initialize GLFW")

        print("Initialized GLFW")
        
        Window.window = glfw.create_window(width, height, "Bepto Engine", None, None)

        if not Window.window:
            glfw.terminate()
            raise Exception("Failed to create GLFW window")
        
        print("Created GLFW window")

        glfw.make_context_current(Window.window)

        monitor = glfw.get_primary_monitor()
        vidmode = glfw.get_video_mode(monitor)
        mon_width = vidmode.size.width
        mon_height = vidmode.size.height
        pos_x = int((mon_width / 2) - (width / 2))
        pos_y = int((mon_height / 2) - (height / 2))

        glfw.set_window_pos(Window.window, pos_x, pos_y)
        glfw.swap_interval(0) # vsync
        glfw.set_input_mode(Window.window, glfw.RAW_MOUSE_MOTION, glfw.TRUE)
        glfw.set_cursor_pos(Window.window, width / 2, height / 2)
        
        GL.glClearColor(0.3, 0.3, 0.3, 1)
        GL.glEnable(GL.GL_CULL_FACE)
    
    @staticmethod
    def update() -> None:
        glfw.poll_events()

        Window.delta_time = glfw.get_time() - Window.last_time
        Window.last_time = glfw.get_time()
        Window.fps = int(1.0 / Window.delta_time)

        glfw.set_window_title(Window.window, f"Bepto Engine | FPS: {Window.fps}")

    @staticmethod
    def end_frame() -> None:
        glfw.swap_buffers(Window.window)

    @staticmethod
    def cleanup() -> None:
        glfw.terminate()