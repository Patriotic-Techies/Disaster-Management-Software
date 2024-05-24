UNIFIED RESCUE AGENCY COORDINATION SYSTEM 

Overview

This unified rescue agency coordination Module is designed to enhance communication, aid decision-making, and provide real-time alerts to improve the coordination and response capabilities of rescue agencies during crises.

Features

- **Real-time Communication**: Enables seamless real-time communication between rescue teams.
- **Geolocation Tracking**: Provides accurate location tracking to facilitate effective disaster response.
- **Alerts and Notifications**: Sends instant alerts and notifications to keep all parties informed.
- **User Management**: Manages users and their roles within the system.
- **Data Management**: Handles data related to disaster events, rescue operations, and resource allocation.

## Technologies Used

- **Backend**: Django
- **Frontend**: React Native
- **Database**: MySQL

## Prerequisites

- Python 3.x
- Node.js
- npm or Yarn
- MySQL

## Installation

### Backend (Django)

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/disastermanagement.git
    cd disastermanagement/backend
    ```

2. **Create and activate a virtual environment**:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set up the database**:
    ```sh
    python manage.py migrate
    ```

5. **Create a superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the server**:
    ```sh
    python manage.py runserver
    ```

### Frontend (React Native)

1. **Navigate to the frontend directory**:
    ```sh
    cd ../frontend
    ```

2. **Install the dependencies**:
    ```sh
    npm install
    ```

3. **Run the application**:
    ```sh
    npm start
    ```

### Database (MySQL)

1. **Install MySQL**:
    - For Ubuntu:
      ```sh
      sudo apt-get install mysql-server
      ```
    - For macOS:
      ```sh
      brew install mysql
      ```

2. **Secure the MySQL installation**:
    ```sh
    sudo mysql_secure_installation
    ```

3. **Create a new database and user**:
    ```sh
    mysql -u root -p
    CREATE DATABASE disastermanagement;
    CREATE USER 'dm_user'@'localhost' IDENTIFIED BY 'your_password';
    GRANT ALL PRIVILEGES ON disastermanagement.* TO 'dm_user'@'localhost';
    FLUSH PRIVILEGES;
    EXIT;
    ```

4. **Update the Django settings with the database credentials** in `settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'disastermanagement',
            'USER': 'dm_user',
            'PASSWORD': 'your_password',
            'HOST': 'localhost',
            'PORT': '3306',
        }
    }
    ```

## Usage

1. **Access the Django admin panel**:
    - Navigate to `http://127.0.0.1:8000/admin` and log in with the superuser credentials.

2. **Manage users and roles**:
    - Add rescue teams, assign roles, and manage permissions.

3. **Use the React Native app**:
    - Use the mobile app for real-time communication, location tracking, and receiving alerts.

## Contributing

1. **Fork the repository**.
2. **Create a new branch**:
    ```sh
    git checkout -b feature-name
    ```
3. **Commit your changes**:
    ```sh
    git commit -m 'Add some feature'
    ```
4. **Push to the branch**:
    ```sh
    git push origin feature-name
    ```
5. **Open a pull request**.

## License

This project is licensed under the MIT License.

## Contact

For any questions or issues, please contact [your-email@example.com].

---

This README provides a comprehensive guide to set up and use the Disaster Management Communication Module. Feel free to update it with more details or instructions specific to your implementation.
