#version 430 core

in vec2 fragTextureCoord;
out vec4 fragColour;
uniform sampler2D textureSample;

void main() {
    fragColour = texture(textureSample, fragTextureCoord);
}