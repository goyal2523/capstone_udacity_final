Casting Agency Specifications

The Casting Agency is a company that creates movies and manages actors by assigning them to these movies. As an Executive Producer within the company, you are developing a system to simplify and streamline the process.

Motivation for the Project

The goal of this project is to demonstrate proficiency in using Flask, SQLAlchemy, Auth0, gunicorn, and Heroku to develop and deploy a RESTful API. This project serves as the capstone project for the Udacity Full Stack Nanodegree program.

Getting Started

Installing Dependencies

To get started, you'll need to create virtual environment for Python 3.8. Follow the instructions in the Python documentation to install the latest version of Python for your platform.

Virtual Environment

We recommend using a virtual environment when working with Python projects. This keeps your dependencies separate and organized for each project. Instructions for setting up a virtual environment for your platform can be found in the Python documentation.

PIP Dependencies

Once you have set up your virtual environment, then run the following command:

pip install -r requirements.txt

This command installs all the required packages listed in the requirements.txt file.

Key Dependencies

Flask is a lightweight backend microservices framework used to handle requests and responses.

SQLAlchemy is the Python SQL toolkit and ORM used to manage the lightweight SQLite database. You'll mainly work in app.py and reference models.py.

Flask-CORS is an extension used to handle cross-origin requests from the frontend server.

Running the server
To run the server, execute:

flask run

Project deployed at

--url
To test live APIs the only way right now to do this is curl requests. Add Auth token headers from logins below to test.
OATH login url. There are three logins, JWTs for these appear in the url after successfull login. Those tokens are needed to test the different APIs.


token_executive_producer

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImwxQjBraFFhZDhaMXNNeVdYOVhJSSJ9.eyJpc3MiOiJodHRwczovL2Rldi1sMWE4dXF2bDdjYjV3azI2LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTNmZDU3ZGJlMzBhMTU4YjU1NDRkNmQiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY5ODc1NjQwNywiZXhwIjoxNjk4NzYzNjA3LCJhenAiOiJ5b0RSMkxLT1VBYUtqSklpcG9IM0lZeXlBWGFvOHhzSCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImRlbGV0ZTptb3ZpZXMiLCJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyIsInBhdGNoOmFjdG9ycyIsInBhdGNoOm1vdmllcyIsInBvc3Q6YWN0b3JzIiwicG9zdDptb3ZpZXMiXX0.NqmLaNlxASVEF0dP_bXq67cs9EGGZyCVtbdfj3fvr1y_XGp747I54zInfF2Vu2HUtnk9T2DeYJr5BtitGDF9EGiB01cm0kFZ8LxOmHfGe3RAtJnrPKklHwpFLnQ0BmrlGenZvr6GaOeDgZV52QNcD3R3HCy82TLEGw-lBuuv6_TUvRQXZ0lC0NjqqEu4MeY31FHs-NBf3QmVy9krGz_HTtUlnUM-KB43c-r0irRCFM0xyzrJ-uKiGg9U8r6tdUhvHqdGjkVdjm2-g4HmtzKrNGf3slCq027t3tXSpdXaMYyZdbYNakOY8LsA7Pk4T5mCtUVbr9V43Ymy8vMCPQFb0w


token_casting_assitant

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImwxQjBraFFhZDhaMXNNeVdYOVhJSSJ9.eyJpc3MiOiJodHRwczovL2Rldi1sMWE4dXF2bDdjYjV3azI2LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTQwZmQ5ZDdjNDAzZGRlNmEyMjRlMTciLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY5ODc1ODE4NCwiZXhwIjoxNjk4NzY1Mzg0LCJhenAiOiJ5b0RSMkxLT1VBYUtqSklpcG9IM0lZeXlBWGFvOHhzSCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiXX0.N7JQWtw81DV8jAJ8Q-kttlSLMm6CEj1yUi0K57AwbBvhQs6wbUNgG4nCNn-pIkpuc0BODhEWBWNeFqDbBzavFuThLeq9jT4C3QOG_fV_Ud7FnrVWeb86zkPMZ6b-rUKjJ_94dPhpRH6roK6xhHqBjTnZuXFLZl4L2NGOrSqUd4V_LxMu9EOBYkQCrITCR9ZwWxZn7h8q0Coa-GZBHjwUAVvpgLeX7McTSGPLSa8uyyDUy9KftUr2ZdRZWl7aiSmejBKeNsLqenRxlDhk-1bct9p2zoyKxRl-QpgwBW1cH0AMaMv0eIN5zECRp82DeRC3yRKwoFGbQG75jWh_WV67Mw


token_casting_director

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6ImwxQjBraFFhZDhaMXNNeVdYOVhJSSJ9.eyJpc3MiOiJodHRwczovL2Rldi1sMWE4dXF2bDdjYjV3azI2LnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2NTQwZmI3MDRhMDc0Yzk1Y2Y5YTA3MWYiLCJhdWQiOiJjYXBzdG9uZSIsImlhdCI6MTY5ODc1NzgwMCwiZXhwIjoxNjk4NzY1MDAwLCJhenAiOiJ5b0RSMkxLT1VBYUtqSklpcG9IM0lZeXlBWGFvOHhzSCIsInNjb3BlIjoiIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9ycyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiXX0.cjqDNB8A0hn8KpYjOko94zMmhOKaWl6-wcQsT-5qKIF37LJiJI_Z9xQTTSYLqXMp10ekrpIfFnOgMe-_5VWc0s7_E-WtIK-8dtzR5J6a0R4_gedhpq01ivlDvBOxXwb15n7CUtKXTaBtBLoMuBJYrT4pD4usCwgqqObeBm5Zr9GxVW7uDyn0OZo6DC-njNsOf8_zH7ELIMKUcXLKv9UmZZPc90ECdRWVH0JS9nz3rU8pQshZJ_EmllSgGLwBx3HZM6BOdroGC2PyAX39SpclPjhDbjJpdWiP9KsCN39vyh8njFb5GkK2-oh_n3xbhQ-xUOQswZ7ELmefpHAkaza71A


Testing
To run the tests, run


python test_app.py
The tests print data returned from the APIs.

The rests also use the Auth token set in env variables and will give an error if the tokens are expired.

API Reference
Error Handling
Errors are returned as JSON objects in the following format:

{
    'success': False,
    'error': 500, 
    'message': 'Internal Server Error'
}

Endpoints
GET '/actors' POST '/actors' PATCH '/actors/<actor_id>' DELETE '/actors/<actor_id>' GET '/movies' POST '/movies' PATCH '/movies/<movie_id>' DELETE '/movies/<movie_id>'

GET '/movies' Fetches list of movies 
Required URL Arguments: None 
Required Data Arguments: None 
Returns: Returns Json data about movies Success Response:

{
   "movies":[
      {
         "release_date":"2023-05-09",
         "title":"Tu Jooth Mai Makkar"
      },
      {
         "release_date":"2020-01-09",
         "title":"Endgame"
      }
   ]
}
GET '/actors' Fetches list of actors 
Required Data Arguments: None 
Returns: Json data about actors
Success Response:

  {
   "actors":[
      {
        "name":"John Deo",
         "age":32,
         "gender":"Male"
         
      }
   ]
}
DELETE '/movies/int:movie_id' Deletes the movie 
Required URL Arguments: movie_id: movie_id_integer 
Required Data Arguments: None 
Returns: deleted movie's ID Success Response:{'success': True}

DELETE '/actors/int:id' Deletes the actor 
Required URL Arguments: id: actor_id 
Required Data Arguments: None 
Returns:the deleted actor's ID Success Response:{'success': True}

POST '/movies' Post a new movie in a database. 
Required URL Arguments: None Required 
Data Arguments: Json data 
Success Response:{'success': True}

POST '/actors' Post a new actor in a database.
Required URL Arguments: None
Required Data Arguments: Json data
Success Response:{'success': True}

PATCH '/movies/int:movie_id' Updates the movie
Required URL Arguments: movie_id: movie_id 
Required Data Arguments: Json data in body to patch
Returns: Json data about the updated movie Success Response:

{
   "movie":{
      "release_date":"2020-09-08",
      "title":"Endgame"
   },
   "success":True
}
PATCH '/actors/int:actor_id' Updates the actor_id of actor 
Required URL Arguments: actor_id: actor_id_integer 
Required Data Arguments: In JSON body add the values to update 
Returns: Json data about the modified actor's ID Success Response:

{
   "actor":{
      "age":29,
      "gender":"M",
      "name":"howard"
   },
   "success":True
}

