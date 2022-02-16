from OpenGL import GL
from bengine.entity import Entity
from bengine.model import Model
from bengine.texture import Texture
from bengine.shader import Shader

class MeshInstance(Entity):
    def __init__(self, model_path: str, **kwargs) -> None:
        __name__ = "MeshInstance"
        super().__init__(**kwargs)

        self._model: Model = Model(model_path)
        self._texture: Texture = Texture("base.png")
        self._shader: Shader = Shader("unlit_vertex.glsl", "unlit_fragment.glsl")        
    
    def _process(self, delta_time: float) -> None:
        super()._process(delta_time)

        self._shader._update(self)
        self._texture._update()
        self._model._update()

        GL.glUseProgram(0)

    def destroy(self) -> None:
        self._model.destroy()
        self._texture.destroy()
        self._shader.destroy()