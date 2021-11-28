<script lang="ts">
import { defineComponent } from 'vue'

function appHeight() {
  const doc = document.documentElement
  doc.style.setProperty('--vh', `${window.innerHeight * 0.01}px`)
}

export default defineComponent({
  setup() {
    window.addEventListener('resize', appHeight)
    appHeight()
  },
})
</script>

<template>
  <router-view />
</template>

<style lang="scss">
#app {
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  font-family: 'Inter', system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI',
    Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
  text-align: center;
  color: #2c3e50;
}
button,
input {
  font: inherit;
}
body {
  margin: 0;
}
</style>
