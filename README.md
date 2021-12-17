# testjobventoryone

VentoryOne Coding Plan

  In the VentoryOne Plan we calculate the total numbers of catons that is need in Amazon's FBA warehouses from Seller Warehouse.

Getting Started

  To work on the sample code, you'll need to clone project's repository to your local computer. If you haven't, do that first.

Steps to install and run backend on your local machine

    git clone

    1. Create a Python virtual environment for your Django project. This virtual environment allows you to isolate this project and install any packages you need without affecting the system Python installation. At the terminal, type the following command:

    $ virtualenv -p python3.6 venv

    2. Activate the virtual environment:

    $ source venv/bin/activate

    3.Install Python dependencies for this project:

    $ pip install -r requirements.txt

    4.For Database schema:

    $ python manage.py migrate

    5.Create Super User

    $ python manage.py createsupersuer

    6.Start the Django development server:

    $ python manage.py runserver

    7.Open http://127.0.0.1:8000/ in a web browser to view your application.

    8.A url link like "warehouse": "http://127.0.0.1:8000/warehouse/" is apper in your web browser. Output of the given url is given below.
    
    <img width="739" alt="submission" src="https://user-images.githubusercontent.com/91453456/146524610-9a449c2d-8550-4f67-8153-b0a917340bba.png">

