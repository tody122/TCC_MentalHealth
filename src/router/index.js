import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/Home.vue'
import FormPage from '../pages/FormPage.vue'
import ResultsPage from '../pages/Results.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/formulario',
    name: 'formulario',
    component: FormPage
  },
  {
    path: '/resultados',
    name: 'resultados',
    component: ResultsPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
