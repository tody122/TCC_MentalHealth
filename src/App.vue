<script setup>
import FooterTCC from './components/FooterTCC.vue'
import Navbar from './components/Navbar.vue'
import ScrollToTop from './components/ScrollToTop.vue'
// O conteúdo do script será movido para um novo componente FormPage.vue
</script>

<template>
  <div class="app-container">
    <ScrollToTop />
    <Navbar />
    <main class="main-content">
    <router-view></router-view>
    </main>
    <FooterTCC />
  </div>
</template>

<style scoped>
.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.main-content {
  margin-top: 80px; /* Espaço para a navbar fixa */
  min-height: calc(100vh - 160px); /* Altura mínima considerando navbar e footer */
}

@media (max-width: 768px) {
  .app-container {
    padding: 0.5rem;
  }

  .main-content {
    margin-top: 70px;
    min-height: calc(100vh - 140px);
  }
}

@media (max-width: 480px) {
  .app-container {
    padding: 0.25rem;
  }
}
</style>
