# Matcher Server

The matcher is used to find a match of an image in the list of `Models` avilable in the [Renderer server](/renderer-server)).

## Entities and types (in typescript)

### Match

```ts
/** Match */
interface Match {
  modelId: number
  imageUrl: string
  confidence: number // From 0 to 1
}
```

## Api documentation

This are the exposed endpoints and how to use them.

You don't need authentication.

### `GET` `/match`

Find the best matching model by an image.

#### Request

```ts
type GetMatchRequest = {
  imageUrl: string
}
```

#### Response

```ts
type GetMatchResponse = Match
```
