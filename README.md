# MachineLearning_Classification_and_Regression_Repo
this is a school project data analytics. We were Required to gather two kinds of datasets, Classification and Regression. Did an EDA on them and made a Machine Learning Model to be used in the Web App.

# INSTRUCTIONS To start the web app

Open a terminal and navigate to the project directory.

OPEN the file "LINK TO REGRESSION" pdf file and download the zip file. 

After Downloading, Extract to first 'mlproject' folder.

THIS IS DUE TO THE MODEL FILE BEING TO HEAVY

2. Activate the virtual environment:

    ```bash
    pipenv shell
    ```

5. Update and sync dependencies:

    ```bash
    pipenv update
    pipenv sync
    ```

6. In pgAdmin, create a database with appropriate settings.

7. Back in the project, update the database name and password in your settings.py

8. Run migrations:

    ```bash
    python manage.py makemigrations
    python manage.py migrate
    ```

9. Import geoplot dataset (if applicable):

    ```bash
    python manage.py import_pizza_data
    ```

10. Run the development server:

    ```bash
    python manage.py runserver
    ```
