<template>
  <footer class="footer-tcc">
    <div class="footer-content">
      <strong>Análise de Problemas Mentais Baseado em Dados Comportamentais</strong> — 2025<br>
      Desenvolvido por Pedro Henrique Todineyb Santos, Rafael Ramos do Rosário, Kauan da Silva<br>
      Facens — Faculdade de Engenharia de Sorocaba<br>
      Engenharia da Computação<br>
      Orientador: Prof. Allan Marconato Marum<br>
      <span class="footer-disclaimer">
        Este sistema não substitui avaliação profissional. Procure um especialista em caso de necessidade.
      </span>
      <br>
      <span>© 2025 Todos os direitos reservados.</span>
    </div>
  </footer>
</template>

<style scoped>
.footer-tcc {
  width: 100vw;
  background: #f0f2f5;
  color: #222;
  padding: 2rem 1rem 1.2rem 1rem;
  text-align: center;
  font-size: 1rem;
  margin-top: 3rem;
  border-top: 1px solid #e0e0e0;
  position: relative;
  left: 50%;
  right: 50%;
  margin-left: -50vw;
  margin-right: -50vw;
  box-sizing: border-box;
}
.footer-content {
  line-height: 1.6;
  width: 100%;
  padding: 0;
}
.footer-disclaimer {
  display: block;
  color: #666;
  font-size: 0.98rem;
  margin: 1rem 0 0.5rem 0;
}
@media (max-width: 600px) {
  .footer-content {
    font-size: 0.95rem;
    padding: 0 0.5rem;
  }
}
</style>
