<script lang="ts">
import { defineComponent, ref } from 'vue'
import api from '../../api'

function appHeight() {
  const doc = document.documentElement
  doc.style.setProperty('--vh', window.innerHeight * 0.01 + 'px')
}

export default defineComponent({
  components: {},

  setup() {
    const showError = ref(false)

    window.addEventListener('resize', appHeight)
    appHeight()

    async function handleImageSelected(event: InputEvent) {
      showError.value = false

      const image = (event.target as HTMLInputElement).files[0]
      if (!image) {
        showError.value = true
        return
      }

      const formData = new FormData()
      formData.append('image', image)

      try {
        const result = await api.findMatch(formData)
        console.log(result) // TODO: continue here
      } catch (error) {
        showError.value = true
      }
    }

    return {
      handleImageSelected,
      showError,
    }
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

    <p
      v-if="showError"
      class="container__explanation container__explanation--error"
    >
      ⚠️ Hi ha agut un error, torna-ho a intentar ⚠️
    </p>
    <p class="container__explanation">
      Fes una foto a una impressió 3D que vulguis identificar.
    </p>

    <label for="file" class="button">
      Escanejar peça
      <input
        class="button__input"
        type="file"
        id="file"
        name="image"
        accept="image/png, image/jpeg"
        required
        @input="handleImageSelected"
    /></label>

    <!-- <file-upload
      ref="upload"
      v-model="files"
      post-action="/post.method"
      put-action="/put.method"
      @input-file="inputFile"
      @input-filter="inputFilter"
      class="container__button"
    >
      Escanejar peça
    </file-upload> -->
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

    &--error {
      background-color: #e74c3c;
      padding: 0.25rem 1rem;
      border-radius: 0.5rem;
      color: #fff;
    }
  }
}

.button {
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
  position: relative;

  &:hover {
    background: #1e40b0;
  }

  &__input {
    position: absolute;
    top: 0;
    left: 0;
    bottom: 0;
    right: 0;
    opacity: 0;
    pointer-events: none;
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
