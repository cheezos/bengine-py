from OpenGL import GL
from bengine.loader import Loader
from bengine.entity import Entity
from bengine.engine import Engine

class Shader:
    def __init__(self, vertex_file: str, fragment_file: str) -> None:
        self._uniforms: dict[str, int] = {}
        self._program: int = Loader.load_shader(vertex_file, fragment_file)
        
        GL.glUseProgram(self._program)
        GL.glEnable(GL.GL_DEPTH_TEST)
        GL.glBlendFunc(GL.GL_SRC_ALPHA, GL.GL_ONE_MINUS_SRC_ALPHA)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_S, GL.GL_REPEAT)
        GL.glTexParameteri(GL.GL_TEXTURE_2D, GL.GL_TEXTURE_WRAP_T, GL.GL_REPEAT)

        self._create_uniform("textureSample")
        self._create_uniform("transformMatrix")
        self._create_uniform("projectionMatrix")
        self._create_uniform("viewMatrix")

    def destroy(self) -> None:
        GL.glUseProgram(0)

    def _update(self, ent: Entity) -> None:
        GL.glUseProgram(self._program)
        GL.glUniform1i(self._get_uniform_location("textureSample"), 0)
        GL.glUniformMatrix4fv(self._get_uniform_location("transformMatrix"), 1, GL.GL_FALSE, ent.transform_matrix)
        GL.glUniformMatrix4fv(self._get_uniform_location("projectionMatrix"), 1, GL.GL_FALSE, Engine.get_camera().projection_matrix)
        GL.glUniformMatrix4fv(self._get_uniform_location("viewMatrix"), 1, GL.GL_FALSE, Engine.get_camera().view_matrix)

    def _create_uniform(self, name: str) -> None:
        uniform_location: int = GL.glGetUniformLocation(self._program, name)
        self._uniforms[name] = uniform_location
    
    def _get_uniform_location(self, name: str) -> int:
        return self._uniforms[name]