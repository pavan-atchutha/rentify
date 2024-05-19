# rentify

# House Buying and Selling Application

This Django web application allows users to buy and sell houses. It includes functionalities for listing available houses, viewing house details, adding new houses for sale, and editing existing house listings.

## Features

- User authentication (login and logout)
- List available houses for sale
- View house details
- Add a house for sale
- Edit house details
- Responsive design with Bootstrap

## Technologies Used

- Django
- HTML/CSS
- Bootstrap

## Setup Instructions

To run this project locally on your machine, follow these steps:

### Prerequisites

- Python (3.x recommended)
- Django

### Installation

1. Clone the repository:

   ```bash
   git clone <repository_url>
   cd house-buy-sell

## Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

## Install the dependencies:
pip install -r requirements.txt

## Install the dependencies:
pip install -r requirements.txt

## Apply migrations:
python manage.py migrate

## Create a superuser (admin) account:
python manage.py runserver

## Open your web browser and go to http://127.0.0.1:8000/ to view the app.

### Directory Structure

retify_project/
│
├── retify_app/
│   ├── migrations/
│   ├── templates/
│   │   ├── ├── base.html
│   │   │   └── ...
│   │   └── retify_app/
│   │       ├── house_list.html
│   │       ├── house_detail.html
│   │       ├── sell_house.html
│   │       └── ...
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
│
├── static/
│   ├── css/
│   │   └── styles.css
│   ├── js/
│   │   └── script.js
│   └── ...
│
├── venv/
├── db.sqlite3
├── manage.py
└── README.md





