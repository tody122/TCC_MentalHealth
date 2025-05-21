import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../pages/Home.vue'
import FormPage from '../pages/FormPage.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomePage
  },
  {
    path: '/form',
    name: 'form',
    component: FormPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
