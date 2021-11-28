import { fetchAndParseJson } from './helper'
import { FindMatchRequest, FindMatchResponse } from './types'

export default {
  findMatch: async (data: FindMatchRequest): Promise<FindMatchResponse> => {
    // return await fetchAndParseJson('http://localhost:8000', {
    //   method: 'POST',
    //   body: data,
    // })
    return Promise.resolve({
      imageUri: 'https://picsum.photos/600',
      name: `monkey ${Math.random().toFixed(2).slice(2)}`,
      customer: 'Jaimito',
      confidence: 0.95,
    })
  },
}
