# flask-endpoint-test-mocking
Example of how mocking is implemented when calling flask endpoints

## Configuring the application

1. Clone the project:
`$ git clone https://github.com/jhonjairoroa87/flask-endpoint-test-mocking`
2. Install project requirements:
`pip install -r requirements.txt`
3. Add meetup.com key to settings.py file
`MEETUP_API_KEY = "INSERT MEETUP API KEY"`

## Running the application
Run the following command
`python runserver.py`

## Verifying the application is up
Call one of the following url in your browser:
 - http://0.0.0.0:5000/
 - http://0.0.0.0:5000/get_groups

## Testing the application
Run the following command
`nosetests -sv`
