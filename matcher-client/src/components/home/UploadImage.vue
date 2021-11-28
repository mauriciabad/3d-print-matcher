<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  components: {},

  setup() {
    return {}
  },
})
</script>

<template>
  <div class="container">
    <h1 class="container__title">Benvingut/da!</h1>

    <div class="container__explanation">
      <h3>Com usar la app?</h3>
      <p>
        Utilitza el botó afegir imatge d'una peça 3D per trobar una similitud
        amb la resta de peçes!
      </p>
    </div>

    <file-upload
      ref="upload"
      v-model="files"
      post-action="/post.method"
      put-action="/put.method"
      @input-file="inputFile"
      @input-filter="inputFilter"
      class="container__button"
    >
      Afegir imatge
    </file-upload>
  </div>
</template>

<style lang="scss">
.container {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-between;
  padding: 50px 10px;

  &__title {
    margin-top: 0;
    margin-bottom: 0;
  }

  &__explanation {
    padding: 50px 10px;
  }

  &__button {
    text-decoration: none;
    padding: 15px;
    width: 50%;
    font-size: 20px;
    color: white;
    border-radius: 10px;
    background: #2c3e50;
    border: 1px solid transparent;
    cursor: pointer;

    &:hover {
      box-shadow: 4px 4px #0000008c;
      color: black;
      border: 1px solid #2c3e50;
      background: transparent;

      &:visited {
        color: black;
      }
    }

    &:visited {
      color: white;
    }

    @media (max-width: 900px) {
      width: 80%;
    }
  }
}
</style>
