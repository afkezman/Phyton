# Diabetes Application

This is a Flask-based web application designed to help users manage and understand diabetes. The application provides various features including tracking blood sugar levels, managing medication, and offering educational resources.

## Project Structure

```
diabetes-app
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   ├── static
│   │   ├── css
│   │   └── js
│   └── templates
│       └── base.html
├── tests
│   ├── __init__.py
│   └── test_routes.py
├── requirements.txt
├── config.py
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/diabetes-app.git
   cd diabetes-app
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Set the environment variable for Flask:
   ```
   export FLASK_APP=app
   ```

2. Run the application:
   ```
   flask run
   ```

3. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Features

- User authentication and profile management
- Blood sugar level tracking
- Medication management
- Educational resources and tips for managing diabetes

## Testing

To run the tests, ensure your virtual environment is activated and run:
```
pytest
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.