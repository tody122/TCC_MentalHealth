import { defineStore } from 'pinia'

export const useRespostasStore = defineStore('respostas', {
  state: () => ({
    respostas: []
  }),
  actions: {
    adicionarResposta(resposta) {
      this.respostas.push(resposta)
    }
  }
})
