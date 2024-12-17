# blog_django
Project Overview 

 This is a Blog Application built using the Django Framework, which allows users to create, manage, and interact with blog posts. The project showcases my skills in web development using Django, Python, and MySQL for database management.

Features 

Create, update, and delete blog posts Organize 
posts by relevant categories 
Commenting system for user interaction 
Home, Contact, and About Us pages 
Admin panel for managing blog posts and categories 

Technologies 

Used Backend: Python, Django
Database: MySQL 
Frontend: HTML, CSS Tools: 
VS Code, Git, and GitHub for version control 

Installation Instructions

Follow these steps to set up and run the project on your local machine:

1.Clone the repository:

git clone
cd

2.Create a virtual environment:

python -m venv venv
source venv/bin/activate # For Linux/macOS
venv\Scripts\activate # For Windows

3.Install dependencies:

pip install -r requirements.txt

4.Configure MySQL Database:

Create a database in MySQL (e.g., blog_db). 
Update the DATABASES setting in your settings.py:
 
DATABASES = {
      'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'blog_db',
            'USER': 'root',
            'PASSWORD': '310704',
            'HOST': 'localhost',
            'PORT': '3306',
            }
        }
        
5.Run database migrations:

python manage.py migrate

6.Create a superuser for admin access:

python manage.py createsuperuser

7.Run the server:

python manage.py runserver

8.Access the project in your browser:
Open http://127.0.0.1:8000/

Project Structure 

arduino Copy code 
├── blog_project/
│ ├── manage.py
│ ├── blog/
│ │ ├── templates/
│ │ │ ├── blog/
│ │ │ │ ├── home.html
│ │ │ │ ├── contact.html
│ │ │ │ ├── about.html
│ │ │ └── base.html
│ │ ├── views.py
│ │ ├── models.py
│ │ ├── urls.py
│ │ └── forms.py
│ ├── static/
│ ├── db.sqlite3
│ ├── requirements.txt

Future Improvements

Implement search functionality for blog posts
Add user profile management 
Allow users to like or share blog posts 
Deploy the project to a cloud platform (e.g., Heroku, AWS)

Contribution 

Contributions are welcome! Feel free to submit issues or pull requests.

Contact

For any inquiries or feedback, please reach out to me at:
Email: jananimalarsoul@gmail.com
