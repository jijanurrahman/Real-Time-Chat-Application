# Real Time Chat Applicaton using Django Framework with User Profiles, Live Chat, and Following System
## Author
- [Jijanur Rahman](https://jijanurrahman.netlify.app)
## Description
This project is a feature-rich social networking platform built with Django, offering functionalities like user authentication,
user profiles, live chat, and a following system. The platform allows users to sign up, log in, and manage their profiles,
including updating profile pictures, professional details, and social links. Users can search for profiles, follow/unfollow
other users, and engage in real-time messaging with file sharing.

## Key Features

- **User Authentication:** Secure signup and login with email and password.
  
- **Profile Management:** Editable user profiles with support for uploading profile pictures and adding personal details.
  
- **Search Functionality:** Search for users by username or email.
  
- **Follow System:** Follow/unfollow other users with real-time updates on follower counts.
  
- **Live Chat:** Real-time messaging with support for text and file sharing.
   
- **Message Inbox:** Organized view of sent and received messages.
  
- **Responsive Design:** Mobile-friendly UI for all pages.

## Lessons Learned
This project is perfect for learning Django and implementing core functionalities required in modern social platform

## How It Works

- **Authentication:** Users sign up with a unique username, email, and password. On successful login, users are redirected to their personalized home page.

- **Profile Management:** Users can update their profile details, including social media links and profile pictures.

- **Following System:** Users can follow or unfollow others directly from search results or profile pages.

- **Live Chat:** Enables real-time communication between users, with options for text and file attachments.

- **Logout:** Logs the user out securely, redirecting them to the authentication page.

 ## Prerequisites

- **Python:** Make sure Python 3.10 is installed on your system.

- **Django:** Install Django, which is required to run the project.
```bash
  pip install django
```
- **Database:** The project uses Django's default SQLite database, so no external database setup is needed unless you want to configure another one.

## 🔗 Project Demo
[![YouTube](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAYAAABzenr0AAABJklEQVR4Ae2WpVaFQRSFcaeS4QVwIjTiLbgk7D1w9xeg4FQcOu6acHeXtNnDmsFd7in/WetLI+f7dbYDAFEsAUvgoeAQ5k5iSQFpIH1kkMyQFXJMTsgpwTuc6jlHes2M3qNP71mge7g76DLNg8gygZ1QckGmuSdZJ7Azq8RDCSQTCJGgBCoFBWqVQLegQJcSmPnWIr9oICMXcIr4C4FJJbD9rUX+NtzX+CIQlfVbgS0lcP4jAVNt/UCA7acCZ0oAPxfQdXMLFNUBvpHflvgbAVM7h0B6zrfeD3kB+Ucg/xLKf4biPyLJX3GH9GFUogRSBQUSTSBZEwskQpFs1USyl6E0gRSRJtJPhsnci1B69oVQeqzXzOo9+kmj3juBeDw2BkSxBCyBO+9s03HRLVCoAAAAAElFTkSuQmCC)](https://youtu.be/B2QjFlOGWIA?si=4jghcI1Gk4x166tj)


## Steps to Run the Project

**Set Up a Virtual Environment (Optional but Recommended):** It's a good practice to use a virtual environment to manage dependencies.

- Install virtualenv (if you don't have it):
```bash
  pip install virtualenv
```
- Create a virtual environment:
```bash
  python -m venv venv
```
- Activate the virtual environment:
```bash
  .\venv\Scripts\activate
```
- On macOS/Linux:
```bash
  source venv/bin/activate
```

**Apply Migrations:**
- Run migrations to set up the database schema:
```bash
  python manage.py migrate
```
**Create a Superuser (Optional):** If you want to access the Django admin panel or manage user profiles, create a superuser account:
```bash
python manage.py createsuperuser
```
**Run the Development Server:**
- Start the Django development server:
```bash
python manage.py runserver
```
**Access the Project:**

- Open your browser and go to http://127.0.0.1:8000/ to access the project.

- If you created a superuser, you can access the Django admin panel at http://127.0.0.1:8000/admin/ using the credentials you created.
