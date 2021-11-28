export default <Model[]>[
  {
    name: 'pin',
    stlUrl: './assets/models/pin.stl',
    color: '#3919A4',
  },
  {
    name: 'botella',
    stlUrl: './assets/models/botella.stl',
    color: '#F2EAD9',
  },
  {
    name: 'trofeu',
    stlUrl: './assets/models/trofeu.stl',
    color: '#3919A4',
  },
  {
    name: 'caixa',
    stlUrl: './assets/models/caixa.stl',
    color: '#050505',
  },
  {
    name: 'centrador',
    stlUrl: './assets/models/centrador.stl',
    color: '#050500',
  },
  {
    name: 'monkey',
    stlUrl: './assets/models/monkey.stl',
    color: '#45474A',
  },
  {
    name: 'tub3',
    stlUrl: './assets/models/tub3.stl',
    color: '#0014AD',
  },
  {
    name: 'turbina',
    stlUrl: './assets/models/turbina.stl',
    color: '#149940',
  },
]

export interface Model {
  name: string
  stlUrl: string
  color: string
}
