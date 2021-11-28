<script lang="ts">
import { defineComponent } from 'vue'
import UploadImage from '@/components/home/UploadImage.vue'

export default defineComponent({
  components: {
    UploadImage,
  },

  setup() {
    function handleSelectImage(image: File) {
      console.log(image)
    }
    return {
      handleSelectImage,
    }
  },
})
</script>

<template>
  <div>
    <UploadImage @select="handleSelectImage" />
  </div>
</template>
