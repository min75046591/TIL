<template>
  <div>
    <p class="greeting">{{ msg }}</p>
  </div>
</template>


<script setup>
import {ref} from 'vue'

const msg = ref('Hello World!')
</script>


<style scoped>
.greeting {
    color: red;
}
</style>