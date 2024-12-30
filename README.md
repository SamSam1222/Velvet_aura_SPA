# Velvet Aura Spa APP

Velvet Aura is a Django-based web application designed for a luxurious spa experience. This project includes features for managing spa services, customer bookings, and an enhanced admin interface using the **Jazzmin** theme.

## Features

- **Service Management**: Easily manage and display available spa services.
- **Booking System**: Customers can book services online.
- **Admin Interface**: Customizable admin panel using the **Jazzmin** theme.
- **User-friendly UI**: Simple and elegant design to ensure a smooth user experience.

## Installation

### 1. Clone the Repository
Start by cloning the repository to your local machine:
```bash
git clone https://github.com/your-username/velvet-aura.git
cd velvet-aura
```

### 2. Set Up Virtual Environment
Create and activate a virtual environment:
```bash
python -m venv velvet_aura_env
source velvet_aura_env/bin/activate  # On Windows, use velvet_aura_env\Scripts\activate
```

### 3. Install Dependencies
Install the required Python packages:
``` bash
pip install -r requirements.txt
```

### 4. Set Up the Database
Run migrations to set up the database:
``` bash
python manage.py migrate
```


### 5. Create a Superuser
Create a superuser to access the Django admin:
``` bash
python manage.py createsuperuser

```

### 6. Run the Development Server
Start the Django development server:
``` bash
python manage.py runserver
```

### 5. Admin Interface
The admin interface uses the Jazzmin theme for an enhanced user experience. You can manage the spa's services and bookings by logging in to the admin panel at:
``` bash
http://127.0.0.1:8000/admin/
```

### Project Structure
1. velvet_aura/: Main project folder containing settings and configurations.
2. spa/: Django app that manages the spa's services and bookings.
3. templates/spa/: Contains HTML templates for rendering spa pages.
4. static/spa/: Contains static files like CSS and images.
5. requirements.txt: Lists all Python dependencies for the project.

### Technologies Used
1. Django: Web framework used for backend development.
2. Python: Programming language.
3. Jazzmin: Admin interface theme for Django.
4. SQLite: Default database used for development (you can switch to PostgreSQL or other databases).


### Customizations
1. The admin interface is customized using the Jazzmin theme.
2. You can customize the spa services and booking models in the spa/models.py file.
3. The JAZZMIN_SETTINGS in settings.py can be modified to change the admin interface’s branding.

### Contributing
Feel free to fork the repository and submit pull requests. Contributions are always welcome!


### License
This project is licensed under the MIT License - see the LICENSE file for details.

Contact
For any questions or suggestions, you can reach out via email at samuelemenike4321@gmail.com






