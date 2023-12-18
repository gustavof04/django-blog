# 💻 Django Blog

Plataforma para criação de blogs desenvolvida em Django. O sistema e seu banco de dados, por meio de um ambiente Docker, rodam em conjunto através de imagens carregadas em um contêiner. Os blogs são inteiramente gerenciados pelo painel admin do Django.

## 🔧 Tecnologias utilizadas

| Tecnologia | Versão |
| -------- | ------- |
| Python  | 3.11.1 |
| Django | 4.2.5 |
| Docker | 24.0.5 |
| PostgreSQL | 13-alpine |

## Instruções
* No terminal, navegue até a pasta raiz do projeto e execute o seguinte comando para criar um ambiente virtual:
  ```bash
  python -m venv nome_da_virtualenv
  ```
  **Obs.**: A criação de uma virtualenv se faz necessária para evitar erros de importação apontados pela IDE que estiver utilizando. Tais erros não afetam em nada na execução do projeto, já que as dependências são instaladas e executadas em um ambiente Docker ao invés de seu próprio host.

* Rode o comando de acordo com seu sistema para ativar seu ambiente virtual:

  Windows
  ```bash
  .\nome_da_virtualenv\Scripts\activate
  ```

  Linux ou macOS
  ```bash
  source nome_da_virtualenv/bin/activate
  ```

* Na pasta <code>dotenv_files</code>, abra o arquivo <code>.env-example</code>. Ele deve estar desta forma:
   ```bash
  SECRET_KEY="CHANGE-ME"
  
  # 0 False, 1 True
  DEBUG="1"
  
  # Comma Separated values
  ALLOWED_HOSTS="127.0.0.1, localhost"
  
  DB_ENGINE="django.db.backends.postgresql"
  POSTGRES_DB="CHANGE-ME"
  POSTGRES_USER="CHANGE-ME"
  POSTGRES_PASSWORD="CHANGE-ME"
  POSTGRES_HOST="psql"
  POSTGRES_PORT="5432"
   ```
* Renomeie o arquivo de exemplo para <code>.env</code> e troque todos os valores <code>"CHANGE-ME"</code> das variáveis de acordo com sua preferência.

  **Obs.**: Diferentemente das outras variáveis, o valor de uma variável <code>SECRET_KEY</code> deve ser único e imprevisível. Como recomendação, gere uma chave secreta em https://djecrety.ir.

* Com o Docker Desktop ativo, certifique-se de não haver nenhum contêiner ou imagens em execução.

* Ainda na pasta raíz do projeto, execute o seguinte comando:
  ```
  docker compose up --build
  ```

* Vá para http://127.0.0.1:8000/admin.
