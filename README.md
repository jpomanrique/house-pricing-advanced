# 🏡 House Pricing Advanced  

Projeto de **Machine Learning avançado** para previsão de preços de casas.  
Inclui pipeline completo: pré-processamento, engenharia de features, treinamento de modelos, tuning de hiperparâmetros, API para servir previsões e workflow de CI/CD com GitHub Actions.  

---

## 📂 Estrutura do Repositório  

```
house-pricing-advanced/
│── data/                # datasets (train.csv, test.csv, etc.)
│── notebooks/           # notebooks de EDA, feature engineering e treino
│── src/                 # código principal
│   ├── preprocessing.py
│   ├── train.py
│   ├── evaluate.py
│   ├── tune.py
│   └── api.py
│── models/              # modelos salvos (model.pkl, scaler.pkl, etc.)
│── tests/               # testes unitários (pytest)
│── .github/workflows/   # CI/CD com GitHub Actions
│── requirements.txt     # dependências do projeto
│── Dockerfile           # containerização
│── README.md            # este arquivo
```

---

## ⚙️ Instalação Local (VSCode)

1. Clone o repositório:  
   ```bash
   git clone https://github.com/seu-usuario/house-pricing-advanced.git
   cd house-pricing-advanced
   ```

2. Crie e ative um ambiente virtual:  
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # Linux/Mac
   .venv\Scripts\activate      # Windows
   ```

3. Instale as dependências:  
   ```bash
   pip install -r requirements.txt
   ```

4. Abra no **VSCode**:  
   ```bash
   code .
   ```

---

## 📊 Executando o Projeto

### 🔎 1. Exploração dos Dados
Abra os notebooks dentro de `notebooks/` no **VSCode** (extensão *Jupyter*).  
Exemplo: `notebooks/EDA.ipynb` → contém análise exploratória e visualizações.  

### 🏗️ 2. Treinar o Modelo
```bash
python src/train.py
```
O modelo treinado será salvo em `models/model.pkl`.

### 📈 3. Avaliar o Modelo
```bash
python src/evaluate.py
```

### 🎯 4. Tuning de Hiperparâmetros (Optuna)
```bash
python src/tune.py
```

---

## 🌐 API (FastAPI)

1. Rodar a API localmente:  
   ```bash
   uvicorn src.api:app --reload
   ```

2. Acesse no navegador:  
   - Swagger UI → [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
   - Endpoint de previsão: `POST /predict`  

Exemplo via **curl**:  
```bash
curl -X POST "http://127.0.0.1:8000/predict"      -H "Content-Type: application/json"      -d '{"features": [1200, 3, 2, 1, 2005]}'
```

---

## 🐳 Docker (opcional)

1. Build da imagem:  
   ```bash
   docker build -t house-pricing .
   ```

2. Rodar o container:  
   ```bash
   docker run -p 8000:8000 house-pricing
   ```

Acesse: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## ✅ Testes

Executar todos os testes com **pytest**:  
```bash
pytest tests/
```

---

## 🔄 CI/CD (GitHub Actions)

- O workflow em `.github/workflows/ci.yml` roda automaticamente:  
  - Instala dependências  
  - Executa testes  
  - Valida build  

Basta fazer **push** no repositório que a pipeline será disparada.

---

## 📌 Roadmap

- [x] Estrutura inicial do projeto  
- [x] Treinamento com RandomForest  
- [x] API com FastAPI  
- [x] CI/CD com GitHub Actions  
- [ ] Melhorar feature engineering  
- [ ] Adicionar modelos baseados em deep learning (PyTorch/TF)  
- [ ] Deploy em cloud (AWS/GCP/Azure ou Heroku/Render)  

---

## 👨‍💻 Autor

Projeto criado por **Seu Nome**  
📧 Email: seuemail@example.com  
🔗 GitHub: [@seu-usuario](https://github.com/seu-usuario)  
