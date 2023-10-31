import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        setup_db(self.app)

        self.token_executive_producer = 'Bearer ' + os.environ['token_executive_producer']
        self.token_casting_assitant = 'Bearer ' + os.environ['token_casting_assitant']
        self.token_casting_director = 'Bearer ' + os.environ['token_casting_director']

        self.headers = {'Content-Type': 'application/json', 'Authorization': self.token_executive_producer}

        self.header_casting_assistant = {'Content-Type': 'application/json', 'Authorization': self.token_casting_assitant}

        self.header_casting_director = {'Content-Type': 'application/json', 'Authorization': self.token_casting_director}

        self.new_movie = {"title": "Titanic Test", "release_date": "2006-05-05"}
        self.new_actor = {"name": "Priyanka", "age": 25, "gender": "male"}
        self.patch_movie = {"title": "Titanic Test 1", "release_date": "2006-05-06"}
        self.patch_actor = {"name": "Priyanka", "age": 25, "gender": "female"}
        self.error_age = {"age": "twenty five"}
        self.error_gender = {"gender": "femal"}
        self.error_date = {"release_date": "12345"}

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass


    def test_get_movies(self):
        res = self.client().get("/movies", headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["movies"]))

    def test_get_actors(self):
        res = self.client().get("/actors", headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["actors"]))

    def test_post_movies(self):
        res = self.client().post("/movies", headers=self.headers, json=self.new_movie)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_post_actors(self):
        res = self.client().post("/actors", headers=self.headers, json=self.new_actor)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_patch_movies(self):
        res = self.client().patch("/movies/1", headers=self.headers, json=self.patch_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    
    def test_patch_actors(self):
        res = self.client().patch("/actors/1", headers=self.headers, json=self.patch_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_patch_movies(self):
        res = self.client().patch("/movies/1", headers=self.headers, json=self.patch_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    
    def test_patch_actors(self):
        res = self.client().patch("/actors/1", headers=self.headers, json=self.patch_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_delete_movies(self):
        res = self.client().delete("/movies/1", headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    
    def test_delete_actors(self):
        res = self.client().delete("/actors/1", headers=self.headers)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_422_if_actor_age_not_integer(self):
        res = self.client().post("/actors", headers=self.headers, json=self.error_age)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_422_if_actor_gender_not_maleOrfemale(self):
        res = self.client().post("/actors", headers=self.headers, json=self.error_gender)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_422_if_movie_releasedate_is_gibberish(self):
        res = self.client().post("/movies", headers=self.headers, json=self.error_date)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")

    def test_404_if_movie_not_found_patch(self):
        res = self.client().patch("/movies/100", headers=self.headers, json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not Found")

    def test_404_if_movie_not_found_delete(self):
        res = self.client().delete("/movies/100", headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not Found")

    def test_404_if_actor_not_found_patch(self):
        res = self.client().patch("/actors/100", headers=self.headers, json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not Found")

    def test_404_if_actor_not_found_delete(self):
        res = self.client().delete("/actors/100", headers=self.headers)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "Not Found")

    def test_get_movies_casting_assistant(self):
        res = self.client().get("/movies", headers=self.header_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["movies"]))

    def test_get_actors_casting_assistant(self):
        res = self.client().get("/actors", headers=self.header_casting_assistant)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(len(data["actors"]))

    def test_patch_actors_casting_assistant_acess_error(self):
        res = self.client().patch("/actors/1", headers=self.header_casting_assistant, json=self.patch_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "You dont have access for this action")

    def test_patch_movies_casting_assistant_acess_error(self):
        res = self.client().patch("/movies/1", headers=self.header_casting_assistant, json=self.patch_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "You dont have access for this action")

    def test_patch_actors_casting_director(self):
        res = self.client().patch("/actors/1", headers=self.header_casting_director, json=self.patch_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_patch_movies_casting_director(self):
        res = self.client().patch("/movies/1", headers=self.header_casting_director, json=self.patch_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)

    def test_delete_actors_casting_director_acess_error(self):
        res = self.client().delete("/actors/1", headers=self.header_casting_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "You dont have access for this action")
    
    def test_delete_movies_casting_director_acess_error(self):
        res = self.client().delete("/movies/1", headers=self.header_casting_director)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "You dont have access for this action")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
