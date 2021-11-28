type FindMatchRequest = FormData

type FindMatchResponse = {
  matchImagePath: string
}

export default {
  findMatch: async (data: FindMatchRequest): Promise<FindMatchResponse> => {
    return await fetchAndParseJson('http://localhost:8000', {
      method: 'POST',
      body: data,
    })
  },
}

async function fetchAndParseJson<T extends any>(
  ...args: Parameters<typeof fetch>
): Promise<T> {
  const response = await fetch(...args)
  return await response.json()
}
