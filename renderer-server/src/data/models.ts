export default <Model[]>[
  {
    name: 'pin',
    stlUrl: './assets/models/pin.stl',
    color: '#8D7BEF',
  },
  {
    name: 'botella',
    stlUrl: './assets/models/botella.stl',
    color: '#ECDFC6',
  },
  {
    name: 'trofeu',
    stlUrl: './assets/models/trofeu.stl',
    color: '#8D7BEF',
  },
  {
    name: 'caixa',
    stlUrl: './assets/models/caixa.stl',
    color: '#211F18',
  },
  {
    name: 'centrador',
    stlUrl: './assets/models/centrador.stl',
    color: '#211F18',
  },
  {
    name: 'monkey',
    stlUrl: './assets/models/monkey.stl',
    color: '#45474A',
  },
  {
    name: 'tub3',
    stlUrl: './assets/models/tub3.stl',
    color: '#1931CC',
  },
  {
    name: 'turbina',
    stlUrl: './assets/models/turbina.stl',
    color: '#2AE58D',
  },
]

export interface Model {
  name: string
  stlUrl: string
  color: string
}
