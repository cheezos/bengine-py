import numpy as np
from bengine.loader import Loader

class OBJLoader(object):
    @staticmethod
    def load(model_path: str) -> np.ndarray:
        v = []
        vt = []
        vn = []
        vertices = []
        
        with open(Loader.get_resource(model_path), "r") as f:
            line = f.readline()
            
            while line:
                first_space = line.find(" ")
                flag = line[0:first_space]
                
                if flag == "mtllib":
                    # ignore the material flag
                    pass
                elif flag == "v":
                    # vertex
                    line = line.replace("v ", "")
                    line = line.split(" ")
                    l = [float(x) for x in line]
                    v.append(l)
                elif flag == "vt":
                    line = line.replace("vt ", "")
                    line = line.split(" ")
                    l = [float(x) for x in line]
                    vt.append(l)
                elif flag == "vn":
                    line = line.replace("vn ", "")
                    line = line.split(" ")
                    l = [float(x) for x in line]
                    vn.append(l)
                elif flag == "f":
                    line = line.replace("f ", "")
                    line = line.replace("\n", "")
                    line = line.split(" ")
                    verts = []
                    texts = []
                    norms = []
                    
                    for _v in line:
                        l = _v.split("/")
                        position = int(l[0]) - 1
                        verts.append(v[position])
                        texture = int(l[1]) - 1
                        texts.append(vt[texture])
                        normal = int(l[2]) - 1
                        norms.append(vn[normal])
                    
                    tri_in_face = len(line) - 2
                    vertex_order = []
                    
                    for _i in range(tri_in_face):
                        vertex_order.append(0)
                        vertex_order.append(_i + 1)
                        vertex_order.append(_i + 2)
                    
                    for _i in vertex_order:
                        for _x in verts[_i]:
                            vertices.append(_x)
                        
                        for _x in texts[_i]:
                            vertices.append(_x)
                        
                        for _x in norms[_i]:
                            vertices.append(_x)
                
                line = f.readline()
        
        vertices = np.array(vertices, dtype=np.float32)
        return vertices