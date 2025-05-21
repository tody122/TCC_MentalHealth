<script setup>
import FooterTCC from './components/FooterTCC.vue'
// O conteúdo do script será movido para um novo componente FormPage.vue
</script>

<template>
  <div class="app-container">
    <router-view></router-view>
    <FooterTCC />
  </div>
</template>

<style scoped>
.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}
</style>
