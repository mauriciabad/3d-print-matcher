import * as THREE from 'three'

export function addShadowedLight(
  x: number,
  y: number,
  z: number,
  color: THREE.ColorRepresentation,
  intensity: number,
  scene: THREE.Scene
) {
  const directionalLight = new THREE.DirectionalLight(color, intensity)
  directionalLight.position.set(x, y, z)
  scene.add(directionalLight)

  directionalLight.castShadow = true

  const d = 1
  directionalLight.shadow.camera.left = -d
  directionalLight.shadow.camera.right = d
  directionalLight.shadow.camera.top = d
  directionalLight.shadow.camera.bottom = -d

  directionalLight.shadow.camera.near = 1
  directionalLight.shadow.camera.far = 4

  directionalLight.shadow.bias = -0.002
}
