# 💻 Django Blog

A platform for creating blogs developed in Django. The system and its database run together through Docker images loaded in a container. The user has the administrator role and the blogs are entirely managed by the Django admin panel.

> Project Status: ✔️ (completed)

## 🔧 Technologies Used

| Technology | Version |
| -------- | ------- |
| Python  | 3.11.1 |
| Django | 4.2.5 |
| Docker | 24.0.5 |
| Docker Desktop | 4.22.0 |
| PostgreSQL | 13-alpine |

## ⚙️ Instructions for virtualenv (optional)
Creating a virtualenv for the Django Blog is recommended to avoid import errors pointed out by the IDE you are using. However, these errors do not affect the execution of the project, as the venv and its dependencies will be created and executed in a Docker environment automatically after the build. If this does not apply to you, skip to the section <code>📂 Instructions for .env</code>.

* In the terminal, navigate to the project's root folder and run the following command to create a virtual environment:
  ```bash
  python -m venv name_of_virtualenv
  ```

* Run the command according to your system to activate your virtual environment:

  **Windows**
  ```bash
  .\name_of_virtualenv\Scripts\activate
  ```

  **Linux or macOS**
  ```bash
  source name_of_virtualenv/bin/activate
  ```

* With the virtual environment activated, run the following two commands:
  ```bash
  cd djangoapp
  pip install -r requirements.txt
  ```

* Return to the root folder:
  ```bash
  cd ..
  ```

## 📂 Instructions for .env
* In the <code>dotenv_files</code> folder, open the <code>.env-example</code> file. It should look like this:
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
* Rename the example file to <code>.env</code> and change all <code>"CHANGE-ME"</code> values of the variables according to your preference.

  > **Note**: Unlike other variables, the value of <code>SECRET_KEY</code> must be unique and unpredictable. As a recommendation, generate a secret key at https://djecrety.ir.

## 🐋 Instructions for Docker
* Download and install <a href="https://www.docker.com/products/docker-desktop/" target="_blank">Docker Desktop</a> if you don't have it on your machine.

* With Docker Desktop active and running in the background, ensure that there are no containers or images running.

* Still in the project's root folder (the one containing the <code>Dockerfile</code> and <code>docker-compose.yml</code> files), run the following command:
  ```
  docker compose up --build
  ```

* Create a superuser to use in the admin with the following command:
  ```bash
  docker-compose run --rm djangoapp python manage.py createsuperuser
  ```

## 🤔 How to create my blog?
1. Go to http://127.0.0.1:8000/admin and log in with the superuser you created.

![image](https://github.com/gustavof04/django-blog/assets/127045694/bc56484a-2365-43b8-bcf5-6f17d7937684)

</br>

2. You will see this panel containing all the system models in the block on the left. Click on the <code>Setup</code> model of the <code>SITE_SETUP</code> app.

![image](https://github.com/gustavof04/django-blog/assets/127045694/e83de2dc-867c-4080-bccf-137ea8c2b04a)

</br>

3. Configure the base of your blog as you wish and save it after finishing.

![image](https://github.com/gustavof04/django-blog/assets/127045694/6eaa1e9f-806a-48f2-89ee-ba5e7a5bafca)

</br>

4. Go to http://127.0.0.1:8000 and see that your blog is rendering the information saved in the admin.

![image](https://github.com/gustavof04/django-blog/assets/127045694/71890b22-44ac-43f3-b912-b9a3db4cc5d5)

</br>

5. A blog is not a blog without posts. Go back to the admin and go to the <code>Posts</code> model of the <code>BLOG</code> app. Add your post, modifying it as you prefer, and save it after finishing.

![image](https://github.com/gustavof04/django-blog/assets/127045694/01f1cfed-4fe7-4d51-89f1-ecbf13c51b19)
> NOTE: Don't forget to check the <code>Is published</code> field for every post you add; otherwise, the post will not be displayed on your blog.  

</br>

6. Go back to http://127.0.0.1:8000 and see the changes.

Homepage displaying our post in a card            |  Post page
:-------------------------:|:-------------------------:
![image](https://github.com/gustavof04/django-blog/assets/127045694/4495596a-8fac-422f-a9aa-6ab2d9353df7) | ![image](https://github.com/gustavof04/django-blog/assets/127045694/eb928ec0-eb42-4494-bbab-169fc8ba9bfc)

</br>

## Bonus

The Django Blog has other features to explore, such as:
 * **Tags** and **categories** fields for posts;
 * <code>MENU LINKS</code> field in <code>Setup</code> to display a shortcut menu on your blog.
 * <code>Page</code> model to create an independent page.
