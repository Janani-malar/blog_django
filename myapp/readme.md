Django Blog Project
Project Overview
This is a Blog Application built using the Django Framework, which allows users to create, manage, and interact with blog posts. The project showcases my skills in web development using Django, Python, and MySQL for database management.

Features
Create, update, and delete blog posts
Organize posts by relevant categories
Commenting system for user interaction
Home, Contact, and About Us pages
Admin panel for managing blog posts and categories
Technologies Used
Backend: Python, Django
Database: MySQL
Frontend: HTML, CSS
Tools: VS Code, Git, and GitHub for version control
Installation Instructions
Follow these steps to set up and run the project on your local machine:

Clone the repository:

bash
Copy code
git clone <repo-link>  
cd <project-directory>  
Create a virtual environment:

bash
Copy code
python -m venv venv  
source venv/bin/activate  # For Linux/macOS  
venv\Scripts\activate     # For Windows  
Install dependencies:

bash
Copy code
pip install -r requirements.txt  
Configure MySQL Database:

Create a database in MySQL (e.g., blog_db).
Update the DATABASES setting in your settings.py:
python
Copy code
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
Run database migrations:

bash
Copy code
python manage.py migrate  
Create a superuser for admin access:

bash
Copy code
python manage.py createsuperuser  
Run the server:

bash
Copy code
python manage.py runserver  
Access the project in your browser:
Open http://127.0.0.1:8000/

Project Structure
arduino
Copy code
├── blog_project/  
│   ├── manage.py  
│   ├── blog/  
│   │   ├── templates/  
│   │   │   ├── blog/  
│   │   │   │   ├── home.html  
│   │   │   │   ├── contact.html  
│   │   │   │   ├── about.html  
│   │   │   └── base.html  
│   │   ├── views.py  
│   │   ├── models.py  
│   │   ├── urls.py  
│   │   └── forms.py  
│   ├── static/  
│   ├── db.sqlite3  
│   ├── requirements.txt  
Screenshots
(Include relevant screenshots here, such as the homepage, blog post detail page, category view, and admin panel.)

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

