import * as THREE from 'three'
import * as THREESTLLoader from 'three-stl-loader'
import { addShadowedLight } from './helper'
const STLLoader = new THREESTLLoader(THREE)

// import models from '../data/models'
// const model = models[0]

let container: HTMLDivElement
let camera: THREE.PerspectiveCamera
let scene: THREE.Scene
let renderer: THREE.WebGLRenderer

init()
render()

function init() {
  container = document.createElement('div')
  document.body.appendChild(container)

  const aspectRatio = window.innerWidth / window.innerHeight
  camera = new THREE.PerspectiveCamera(35, aspectRatio, 1, 15)
  camera.position.set(3, 0, 3)

  camera.lookAt(0, 0, 0)

  scene = new THREE.Scene()
  scene.background = new THREE.Color(0xffffff)

  const loader = new STLLoader()

  loader.load(
    'https://threejs.org/examples/models/stl/ascii/slotted_disk.stl',
    (geometry: any) => {
      const material = new THREE.MeshPhongMaterial({
        color: 0xff5533,
        specular: 0x111111,
        shininess: 200,
      })
      const mesh = new THREE.Mesh(geometry, material)

      mesh.position.set(0, 0, 0)
      mesh.rotation.set(0, 0, 0)
      mesh.scale.set(1, 1, 1)

      mesh.castShadow = true
      mesh.receiveShadow = true

      scene.add(mesh)
      // scene.add(new THREE.BoxHelper(mesh, 0x000000))

      render()
    }
  )

  // Lights
  scene.add(new THREE.HemisphereLight(0x443333, 0x111122))
  addShadowedLight(1, 1, 1, 0xffffff, 1.35, scene)
  addShadowedLight(0.5, 1, -1, 0xffffff, 0.5, scene)

  // renderer
  renderer = new THREE.WebGLRenderer({ antialias: true })
  renderer.setPixelRatio(window.devicePixelRatio)
  renderer.setSize(window.innerWidth, window.innerHeight)
  renderer.outputEncoding = THREE.sRGBEncoding
  renderer.shadowMap.enabled = true

  container.appendChild(renderer.domElement)
}

function render() {
  renderer.render(scene, camera)
}
