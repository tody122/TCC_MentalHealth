<script setup>
import { watch } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

watch(
  () => route.path,
  () => {
    window.scrollTo({
      top: 0,
      behavior: 'smooth'
    })
  }
)
</script>

<template>
  <!-- Componente sem template, apenas lógica -->
</template>
