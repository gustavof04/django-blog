# 💻 Django Blog

Plataforma para criação de blogs desenvolvida em Django. O sistema e seu banco de dados, por meio do Docker, rodam em conjunto através de imagens carregadas em um contêiner. Os blogs são inteiramente gerenciados pelo painel admin do Django.

> Status do Projeto: ✔️ (concluído)

## 🔧 Tecnologias utilizadas

| Tecnologia | Versão |
| -------- | ------- |
| Python  | 3.11.1 |
| Django | 4.2.5 |
| Docker | 24.0.5 |
| PostgreSQL | 13-alpine |

## ⚙️ Instruções para a virtualenv (opcional)
A criação de uma virtualenv para o Django Blog é recomendada para evitar erros de importação apontados pela IDE que estiver utilizando. Entretanto, tais erros não afetam em nada na execução do projeto, pois a venv e suas dependências serão criadas e executadas em um ambiente Docker após o build de forma automática. Se não for seu caso, pule para o tópico <code>📂 Instruções para .env</code>.

* No terminal, navegue até a pasta raiz do projeto e execute o seguinte comando para criar um ambiente virtual:
  ```bash
  python -m venv nome_da_virtualenv
  ```

* Rode o comando de acordo com seu sistema para ativar seu ambiente virtual:

  Windows
  ```bash
  .\nome_da_virtualenv\Scripts\activate
  ```

  Linux ou macOS
  ```bash
  source nome_da_virtualenv/bin/activate
  ```

* Com o ambiente virtual ativado, execute os dois seguintes comandos:
  ```bash
  cd djangoapp
  pip install -r requirements.txt
  ```

* Volte para a pasta raíz:
  ```bash
  cd ..
  ```

## 📂 Instruções para o .env
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

  > **Obs.**: Diferente de outras variáveis, o valor de <code>SECRET_KEY</code> deve ser único e imprevisível. Como recomendação, gere uma chave secreta em https://djecrety.ir.

## 🐋 Instruções para o Docker
* Com o Docker Desktop ativo e em segundo plano, certifique-se de não haver nenhum contêiner ou imagens em execução.

* Ainda na pasta raíz do projeto (a que possui os arquivos Dockerfile e docker-compose.yml), execute o seguinte comando:
  ```
  docker compose up --build
  ```

* Crie um superusuário para utilizar no admin com o seguinte comando:
  ```bash
  docker-compose run --rm djangoapp python manage.py createsuperuser
  ```

## 🤔 Como criar meu blog?
1. Vá para http://127.0.0.1:8000/admin e faça login com o superusuário que você criou.

![image](https://github.com/gustavof04/django-blog/assets/127045694/bc56484a-2365-43b8-bcf5-6f17d7937684)

</br>

2. Você verá este painel contendo todas as models do sistema no bloco à esquerda. Clique na model <code>Setup</code> do app <code>SITE_SETUP</code>.

![image](https://github.com/gustavof04/django-blog/assets/127045694/e83de2dc-867c-4080-bccf-137ea8c2b04a)

</br>

3. Configure a base do seu blog da forma que desejar e salve após terminar.

![image](https://github.com/gustavof04/django-blog/assets/127045694/6eaa1e9f-806a-48f2-89ee-ba5e7a5bafca)

</br>

4. Vá para http://127.0.0.1:8000 e veja que o seu blog está renderizando as informações salvas no admin.

![image](https://github.com/gustavof04/django-blog/assets/127045694/71890b22-44ac-43f3-b912-b9a3db4cc5d5)

</br>

5. Um blog não é um blog sem posts. Volte para o admin e vá para a model <code>Posts</code> do app <code>BLOG</code>. Adicione seu post modificando-o da forma que preferir e salve-o após terminar.

![image](https://github.com/gustavof04/django-blog/assets/127045694/01f1cfed-4fe7-4d51-89f1-ecbf13c51b19)
> OBS.: Não esqueça de marcar o campo <code>Is published</code> para todo post que você adicionar, caso contrário o post não será exibido no seu blog.  

</br>

6. Volte para http://127.0.0.1:8000 e veja as mudanças.

Página inicial exibindo nosso post em um postcard            |  Página do post
:-------------------------:|:-------------------------:
![image](https://github.com/gustavof04/django-blog/assets/127045694/4495596a-8fac-422f-a9aa-6ab2d9353df7) | ![image](https://github.com/gustavof04/django-blog/assets/127045694/eb928ec0-eb42-4494-bbab-169fc8ba9bfc)

</br>

O Django Blog possui outras features para explorar, como:
 * **Tags** e **categorias** para os posts;
 * Model <code>Page</code> para criar uma página independente;
 * Campo <code>MENU LINKS</code> em <code>Setup</code> para exibir um menu de atalhos no seu blog.
