<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isMenuOpen = ref(false)

const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value
}

const navigateTo = (path) => {
  router.push(path)
  isMenuOpen.value = false
}
</script>

<template>
  <nav class="navbar">
    <div class="navbar-container">
      <div class="navbar-logo" @click="navigateTo('/')">
        <h1>TCC IA</h1>
      </div>

      <div class="navbar-menu" :class="{ 'active': isMenuOpen }">
        <button class="nav-item" @click="navigateTo('/')">Home</button>
        <button class="nav-item" @click="navigateTo('/formulario')">Formulário</button>
        <button class="nav-item" @click="navigateTo('/resultados')">Resultados</button>
      </div>

      <button class="menu-button" @click="toggleMenu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </nav>
</template>

<style scoped>
.navbar {
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
}

.navbar-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.navbar-logo {
  cursor: pointer;
}

.navbar-logo h1 {
  margin: 0;
  font-size: 1.5rem;
  color: #333;
}

.navbar-menu {
  display: flex;
  gap: 1.5rem;
}

.nav-item {
  background: none;
  border: none;
  padding: 0.5rem 1rem;
  font-size: 1rem;
  color: #333;
  cursor: pointer;
  transition: color 0.3s ease;
  font-weight: 500;
}

.nav-item:hover {
  color: #007bff;
  transform: translateY(-2px);
}

.menu-button {
  display: none;
  flex-direction: column;
  gap: 6px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
}

.menu-button span {
  display: block;
  width: 25px;
  height: 2px;
  background-color: #333;
  transition: all 0.3s ease;
}

@media (max-width: 768px) {
  .menu-button {
    display: flex;
  }

  .navbar-menu {
    display: none;
    position: absolute;
    top: 100%;
    left: 0;
    right: 0;
    background-color: #ffffff;
    padding: 1rem;
    flex-direction: column;
    align-items: center;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .navbar-menu.active {
    display: flex;
  }

  .nav-item {
    width: 100%;
    text-align: center;
    padding: 1rem;
  }
}
</style>
