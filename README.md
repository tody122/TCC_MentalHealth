# Sistema de Análise de Saúde Mental

Este projeto é um sistema web que utiliza machine learning para análise de saúde mental, integrando um modelo treinado em Python com uma interface web moderna desenvolvida em Vue.js.

## 🚀 Tecnologias Utilizadas

### Backend
- Python
- Flask
- Scikit-learn
- Pandas
- NumPy

### Frontend
- Vue.js 3
- Vue Router
- Pinia (Gerenciamento de Estado)

## 📋 Estrutura do Projeto

```
.
├── Frontend/               # Aplicação Vue.js
│   ├── src/
│   │   ├── pages/        # Componentes de página
│   │   ├── stores/       # Gerenciamento de estado
│   │   └── ...
├── app.py                 # API Flask
├── pipeline_mlp.pkl       # Modelo treinado
├── requirements.txt       # Dependências Python
└── render.yaml           # Configuração do Render
```

## 🔧 Funcionamento do Programa

O sistema funciona da seguinte maneira:

1. **Interface do Usuário**:
   - O usuário acessa a aplicação através de uma interface web moderna
   - Preenche um questionário com perguntas relacionadas à saúde mental
   - Os dados são enviados para o backend através de requisições HTTP

2. **Processamento**:
   - O backend recebe os dados do questionário
   - O modelo de machine learning (`pipeline_mlp.pkl`) processa as respostas
   - Gera uma predição sobre possíveis sintomas de ansiedade ou depressão
   - Calcula a probabilidade e fornece recomendações personalizadas

3. **Resultados**:
   - O frontend recebe e processa os resultados
   - Exibe uma análise detalhada com:
     - Predição final (positiva ou negativa)
     - Grau de gravidade dos sintomas
     - Recomendações personalizadas
     - Sugestões de próximos passos

## 🌐 Hospedagem

O projeto está hospedado em duas plataformas diferentes:

### Frontend (Vercel)
- Interface web hospedada na Vercel
- Configurado através do arquivo `vercel.json`
- Oferece:
  - Deploy automático
  - CDN global
  - SSL gratuito
  - Alta performance

### Backend (Render)
- API Flask hospedada no Render
- Configurado através do `render.yaml`
- Características:
  - Servidor Python dedicado
  - Escalabilidade automática
  - Integração contínua
  - Monitoramento em tempo real

## 🔧 Integração com Render

O projeto está configurado para deploy no Render, uma plataforma de cloud que oferece hospedagem gratuita para aplicações web. A integração foi realizada da seguinte forma:

1. **Configuração do Backend**:
   - O arquivo `render.yaml` define a configuração do serviço
   - O `requirements.txt` lista todas as dependências Python necessárias
   - O `wsgi.py` serve como ponto de entrada para a aplicação Flask

2. **Deploy do Modelo**:
   - O modelo treinado (`pipeline_mlp.pkl`) é versionado e incluído no deploy
   - A API Flask carrega o modelo e disponibiliza endpoints para predição

3. **Integração Frontend-Backend**:
   - O frontend Vue.js se comunica com a API Flask através de requisições HTTP
   - O estado da aplicação é gerenciado pelo Pinia
   - As respostas do modelo são processadas e exibidas na interface

## 🛠️ Instalação e Execução

### Backend

1. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Execute a aplicação:
```bash
python app.py
```

### Frontend

1. Entre no diretório do frontend:
```bash
cd Frontend
```

2. Instale as dependências:
```bash
npm install
```

3. Execute em modo de desenvolvimento:
```bash
npm run dev
```

## 📊 Funcionalidades

- Análise de saúde mental baseada em questionário
- Predição de possíveis sintomas de ansiedade e depressão
- Interface responsiva e amigável
- Recomendações personalizadas baseadas nos resultados

## 🔒 Segurança

- Dados sensíveis são tratados com confidencialidade
- Não há armazenamento permanente de dados pessoais
- Comunicação segura entre frontend e backend
- HTTPS em todas as comunicações

## 🤝 Contribuição

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes. 
