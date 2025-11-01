# 🌾 FarmTech Agro

### FIAP - Faculdade de Informática e Administração Paulista  
<img width="2385" height="642" alt="image" src="https://github.com/user-attachments/assets/86979b32-ae7f-46a5-ba0e-1ada46f10914" />
**Curso:** Inteligência Artifical e Machine Learning
**Aluno:** Matheus Meissner – RM567080  

---

## 📘 Descrição do Projeto

O **FarmTech Agro** é um sistema de **irrigação inteligente** desenvolvido como parte do projeto **FarmTech Solutions**, com o objetivo de unir tecnologias de **IoT, Banco de Dados e Python**.  

O projeto simula um **ambiente agrícola automatizado** utilizando o **ESP32** na plataforma **Wokwi**, coletando dados de sensores ambientais como umidade, pH e temperatura, armazenando-os no **Oracle Database** e, por fim, exibindo os resultados em uma **dashboard interativa em Python (Streamlit)**.  

O sistema tem como finalidade demonstrar como a automação pode **otimizar o uso de recursos naturais** e auxiliar na **tomada de decisão no campo**, simulando uma fazenda digital conectada.

---

## 🧩 Estrutura de Pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

| Pasta / Arquivo | Descrição |
|------------------|-----------|
| `/wokwi` | Geração dos dados via simulação ESP32. Contém o `README_wokwi.md` com detalhes da simulação e estrutura JSON. |
| `/banco` | Scripts SQL, prints e base de dados utilizados no Oracle. Inclui `create_table_sensores.sql`, `consultas.sql` e `Sensores_Fazenda.csv`. |
| `/ir_alem/dashboard` | Dashboard interativa em Python utilizando Streamlit (etapa opcional "Ir Além"). |
| `README.md` | Documento principal contendo descrição e instruções gerais do projeto. |

---

## 🔧 Como Executar o Projeto

### 🖥️ Pré-requisitos

- **Oracle Database** (versão 21c ou superior)  
- **Python 3.10+**  
- **Bibliotecas:** `streamlit`, `pandas`, `numpy`  
- **Ambiente de simulação:** [Wokwi ESP32](https://wokwi.com/)

### 🚀 Etapas de execução

#### 🧱 1. Criação da Tabela no Oracle

Execute o script `create_table_sensores.sql` no Oracle SQL Developer:

```sql
CREATE TABLE SENSORES (
  UMID NUMBER,
  PH NUMBER,
  N VARCHAR2(10),
  P VARCHAR2(10),
  K VARCHAR2(10),
  CHUVA VARCHAR2(10),
  BOMBA VARCHAR2(10),
  TEMPERATURA NUMBER
);
```
## 📤 2. Importação dos Dados

- Utilize o assistente de importação do SQL Developer.
- Selecione o arquivo Sensores_Fazenda.csv.
- Mapeie as colunas e finalize o processo de carga.

---

## 🔍 3. Validação dos Dados

Rode a consulta:
```
SELECT * FROM SENSORES;
```
Verifique se todos os dados foram importados corretamente.

---

## 📊 4. Dashboard em Python (Ir Além)

Acesse a pasta ir_alem/dashboard

Instale as dependências:
```
pip install -r requirements.txt
```
Execute a aplicação:
```
streamlit run app.py
```
Abra o navegador em:
👉 http://localhost:8501

A dashboard exibirá:

- Umidade e pH em tempo real
- Status da bomba e condição de chuva
- Gráfico histórico de umidade
- Tabela com registros brutos

---

## 🗃 Histórico de Lançamentos
```
Versão	Data	Descrição
1.0.0	01/11/2025	Versão final da entrega FIAP – Banco de Dados
0.9.0	30/10/2025	Adição da dashboard em Streamlit (Ir Além)
0.8.0	28/10/2025	Importação da base CSV e testes no Oracle
0.7.0	25/10/2025	Criação dos scripts SQL e README do banco
0.6.0	22/10/2025	Simulação dos sensores no Wokwi
```

---

## 👨‍💻 Autor

Matheus Meissner
RM567080 – FIAP | Inteligência Artificial e Machine Learning

---

## 🖼️ Evidências do Banco de Dados

<p align="center">
  <img src="prints/estrutura_sensores.png" alt="Estrutura da tabela" width="80%">
</p>

<p align="center">
  <img src="prints/select_sensores.png" alt="Consulta dos dados" width="80%">
</p>

---

## 📜 Licença

Modelo Git FIAP por FIAP está licenciado sob a licença Attribution 4.0 International (CC BY 4.0)
.
Sinta-se à vontade para estudar, adaptar e melhorar este projeto para fins acadêmicos.

---

## 💡 FarmTech Agro – Conectando tecnologia, dados e sustentabilidade no campo.





