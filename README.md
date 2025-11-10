# Sistema de Livros – Versão Básica

## 📄 Descrição  
Este é um sistema web mínimo desenvolvido com Flask. Ele possui apenas duas rotas:  
- `/livros` — lista todos os livros cadastrados (id, título, autor)  
- `/livros/<int:livro_id>` — exibe os dados de um livro específico incluindo id, título, autor  
Se o livro com o `livro_id` solicitado não existir, o sistema retorna um erro 404.

Os dados são mantidos em memória (uma lista de dicionários em Python). O código está contido em um único arquivo `app.py`.

---

## 🛠 Tecnologias utilizadas  
- Python 3.x  
- Flask  
- JSON (formato de resposta para as rotas)  

---

## 📁 Estrutura de arquivos sugerida  
/sistema-livros-basico
│
├─ app.py
├─ requirements.txt (opcional)


---

## ✅ Entrega mínima  
- Arquivo `app.py` com as duas rotas implementadas: `/livros` e `/livros/<int:livro_id>`  
- Tratamento de erro 404 para livro não encontrado  
- Dados de exemplo em memória  

---

## 🔍 Como executar  
1. Clone ou crie o arquivo `app.py` conforme o enunciado.  
2. (Opcional) Crie um `requirements.txt` com `Flask` dentro.  
3. No terminal, instale Flask (se ainda não tiver):  
   ```bash
   pip install flask
   
python app.py
