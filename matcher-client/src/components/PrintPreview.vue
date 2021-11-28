<script lang="ts">
import { defineComponent, PropType } from 'vue'
import { Print } from '../api/types'
import { MATCH_SERVER_BASE_URL } from '../constants'

export default defineComponent({
  props: {
    value: {
      type: Object as PropType<Print>,
      required: true,
    },
  },

  setup() {
    return {
      MATCH_SERVER_BASE_URL,
    }
  },
})
</script>

<template>
  <div class="print">
    <img
      class="print__image"
      :src="MATCH_SERVER_BASE_URL + value.imageUri"
      alt="Preview of the print"
      intrinsicsize="400 x 400"
    />
    <div class="print__info">
      <h2 class="print__title">{{ value.name }}</h2>
      <p class="print__description">de {{ value.customer }}</p>
    </div>
  </div>
</template>

<style lang="scss" scoped>
.print {
  &__image {
    width: 100%;
    aspect-ratio: 1;
    max-width: 400px;
    border-radius: 1rem;
    background-color: #eee;
    box-shadow: 0px 10px 15px -3px rgba(0, 0, 0, 0.1);
    border: solid 1px #ddd;
  }

  &__title {
    font-size: 2rem;
    font-weight: bold;
    margin-bottom: 0.25rem;
  }

  &__description {
    margin: 0;
  }
}
</style>
