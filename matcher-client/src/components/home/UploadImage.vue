<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  components: {},

  setup() {
    function appHeight() {
      const doc = document.documentElement
      doc.style.setProperty('--vh', window.innerHeight * 0.01 + 'px')
    }

    window.addEventListener('resize', appHeight)
    appHeight()

    return {}
  },
})
</script>

<template>
  <div class="container">
    <h1 class="container__title">Buscador de peces</h1>

    <div class="container__photos">
      <img src="@/assets/3d-printer.png" alt="" class="image image--printer" />
      <img src="@/assets/take-a-photo.png" alt="" class="image image--photo" />
    </div>

    <div class="container__explanation">
      <p>Fes una foto a una impressió 3D que vulguis identificar.</p>
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
      Escanejar peça
    </file-upload>
  </div>
</template>

<style lang="scss">
.container {
  display: flex;
  align-items: center;
  flex-direction: column;
  justify-content: space-between;
  padding: 1rem;
  max-width: 600px;
  width: 100%;
  box-sizing: border-box;
  margin: 0 auto;
  height: 100vh; /* Fallback for browsers that do not support Custom Properties */
  height: calc(var(--vh, 1vh) * 100);

  &__photos {
    flex-grow: 1;
    justify-content: center;
    display: flex;
    flex-direction: column;
  }

  &__title {
    margin-top: 2rem;
    margin-bottom: 0;
    text-transform: uppercase;
    font-weight: 900;
    font-size: 3rem;
  }

  &__explanation {
    font-size: 1.2rem;
    line-height: 1.6;
    margin: 0 0 1rem;
  }

  &__button {
    text-decoration: none;
    padding: 15px;
    width: 100%;
    box-sizing: border-box;
    font-size: 1.2rem;
    text-transform: uppercase;
    color: white;
    border-radius: 10px;
    background: #2463eb;
    border: 1px solid transparent;
    cursor: pointer;
    font-weight: 500;

    &:hover {
      background: #1e40b0;
    }
  }
}

.image {
  width: 100%;
  max-width: 200px;
  margin: 0 auto;

  &--photo {
    margin-top: -35px;
  }
}
</style>
