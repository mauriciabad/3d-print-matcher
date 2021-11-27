export default <Model[]>[
  {
    id: 1,
    name: 'Stanford bunny',
    stlUrl: 'https://ozeki.hu/attachments/16/Stanford_Bunny_sample.stl',
    color: '#ff0000',
  },
  {
    id: 2,
    name: 'Eiffel-tower',
    stlUrl: 'https://ozeki.hu/attachments/116/Eiffel_tower_sample.STL',
    color: '#0000ff',
  },
  {
    id: 3,
    name: 'Menger sponge',
    stlUrl: 'https://ozeki.hu/attachments/116/Menger_sponge_sample.stl',
    color: '#ffffff',
  },
]

interface Model {
  id: number
  name: string
  stlUrl: string
  color: string
}
