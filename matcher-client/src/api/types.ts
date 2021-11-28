export interface Print {
  imageUri: string
  name: string
  customer: string
  confidence: number
}

export type FindMatchRequest = FormData
export type FindMatchResponse = Print
