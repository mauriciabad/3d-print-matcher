<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/logo.png" />
    <SubmitForm />
  </div>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import SubmitForm from "@/components/SubmitForm.vue";

export default defineComponent({
  name: "Home",
  components: {
    SubmitForm,
  },
});
</script>
