export async function fetchAndParseJson<T extends any>(
  ...args: Parameters<typeof fetch>
): Promise<T> {
  const response = await fetch(...args)
  return await response.json()
}
