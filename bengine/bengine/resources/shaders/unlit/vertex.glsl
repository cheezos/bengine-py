#version 430 core

in vec3 position;
in vec2 textureCoord;
out vec2 fragTextureCoord;
uniform mat4 transformMatrix;
uniform mat4 projectionMatrix;
uniform mat4 viewMatrix;

void main() {
    gl_Position = projectionMatrix * viewMatrix * transformMatrix * vec4(position, 1.0);
    fragTextureCoord = textureCoord;
}