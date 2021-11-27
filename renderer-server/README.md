# Renderer Server

The renderer is used to store `Models` and `Renders` of them, to then be used by the [Matcher](/matcher-server)).

## Entities and types (in typescript)

## Model

```ts
/** 3D model */
interface Model {
  id: number
  stlUrl: string // TODO: Define where this is saved
}
```

## Render

```ts
/** Image representation of a Model */
interface Render {
  id: number
  imageUrl: string // TODO: Define where this is saved
  modelId: number
  camera: {
    orientation: CameraOrientation // TODO: define
    position: CameraPosition // TODO: Define
  }
}
```

## Api documentation

This are the exposed endpoints and how to use them.

You don't need authentication.

### `GET` `/renders`

Get all render files.

#### Response

```ts
type GetRendersResponse = Render[]
```

### `GET` `/model/:id`

Get a model's information by `id`.

#### Response

```ts
type GetModelByIdResponse = Model
```

### `POST` `/model`

Create a new model.

```ts
type CreateModelRequest = Omit<Model, 'id'>
```
