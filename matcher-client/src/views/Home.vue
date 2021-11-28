<script lang="ts">
import { defineComponent, ref } from 'vue'
import api from '../api'
import { Print } from '../api/types'
import PrintPreview from '../components/PrintPreview.vue'

export default defineComponent({
  components: { PrintPreview },

  setup() {
    const showError = ref(false)
    const showLoading = ref(false)
    const print = ref<Print | null>(null)

    async function handleImageSelected(event: InputEvent) {
      clearScreen()
      showLoading.value = true

      const image = (event.target as HTMLInputElement).files?.[0]
      if (!image) {
        showError.value = true
        showLoading.value = false
        return
      }

      const formData = new FormData()
      formData.append('file', image)

      try {
        print.value = await api.findMatch(formData)
      } catch (error) {
        showError.value = true
        showLoading.value = false
      }
      showLoading.value = false
    }

    function clearScreen() {
      showError.value = false
      print.value = null
    }

    return {
      handleImageSelected,
      showError,
      print,
      showLoading,
    }
  },
})
</script>

<template>
  <div class="container">
    <h1 class="container__title">
      <template v-if="print">Peça més semblant</template>
      <template v-else>Buscador de peces</template>
    </h1>

    <div v-if="print" class="container__print">
      <print-preview :value="print" />
    </div>
    <div v-else class="container__photos">
      <img src="@/assets/3d-printer.png" alt="" class="image image--printer" />
      <img src="@/assets/take-a-photo.png" alt="" class="image image--photo" />
    </div>

    <p
      v-if="showLoading"
      class="container__explanation container__explanation--loading"
    >
      Loading...
    </p>
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
      <template v-if="print">Torna a escanejar</template>
      <template v-else>Escanejar peça</template>

      <input
        class="button__input"
        type="file"
        id="file"
        name="image"
        accept="image/png, image/jpeg"
        required
        @input="handleImageSelected"
    /></label>
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

  &__photos,
  &__print {
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
    &--loading {
      background-color: #3498db;
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
