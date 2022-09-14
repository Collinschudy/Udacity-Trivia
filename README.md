# An Open Source Trivia Game

Udacity is invested in creating bonding experiences for its employees and students. A bunch of team members got the idea to hold trivia on a regular basis and created a webpage to manage the trivia app and play the game, but their API experience is limited and still needs to be built out.

This has led to the building of a seemlessly flexible API experience where users across the web can have a good brain test. Developers can equally make various contribution as it is open source.

## Getting started

Developers who are willing to contribute to this project should have installed Python3, pip, flask and should also download node module for frontend on their local machines.


### Backend

You will need to install some dependencies for your backend, to do this, you have to run `pip install requirements.txt` on your terminal.
To get the application up and running on the backend, you need to run the following command on your git bash:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
export FLASK_DEBUG=true
flask run
```
If you are working from a windows terminal or command prompt, replace the `export` with `SET`.

This application will run on your localhost and port 5000.


### Frontend

To get the frontend running, you will need a dependency. Navigate to the frontend folder from your terminal and run the command below:

```bash
npm install 
```
`it is important to note that you do this only once.` Once the download of the node modules is completed, run the command below:

```bash
npm start
```
This starts the frontend app on the localhost:3000.

### Testing

Make sure you are working from the backend folder. Create your database by running the command below:

```bash
dropdb trivia_test `OR` drop database trivia_test;
createdb trivia_test `OR` create database trivia_test;
```
This creates our database. Inorder to populate it, run the command below:

```bash
psql trivia < trivia.psql>
```
And finally, to get the test app running, you run the command below:

```bash
python test_flaskr.py
```

## API Reference

### Getting Started

1. Base URL: There are various choices of hosting but at the moment, our application is running on the localhost which is `http://127.0.0.1:5000.`

2. Authentication: There is no need for authentication or API keys in our application.

### Endpoints

#### `GET/categories`

This returns all categories which includes their `ids` and `types.`

It is naviated through the URL  `http://127.0.0.1:5000/categories` or `curl http://127.0.0.1:5000/categories`

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```
---
#### `GET/questions`

This returns all questions in the database paginated in 10's in a json object if request was successful. ic contains `id`, `category`, `questionn` and `difficulty.`

It is naviated through the URL  `http://127.0.0.1:5000/questions` from your browser or `curl http://127.0.0.1:5000/questions` from your terminal or postman.
Additionally, you can navigate with page reference using `curl http://127.0.0.1:5000/questions?page=3` this will navigate to the third page.

It appeats in the format below:

```json
{
  "success": true, 
  "questions": [
    {
      "id": 1, 
      "question": " What is the deepest part on Earth?", 
      "answer": " The Mariana Trench", 
      "category": "3", 
      "difficulty": 4
    }, 
    {
      "id": 2, 
      "question": " What movie earned Tom Hanks his third straight Oscar nomination in 1996?", 
      "answer": " Apollo 13", 
      "category": "5", 
      "difficulty": 4
    }, 
    {
      "id": 4, 
      "question": " What actor did author Anne Rice first denounce then praise in the role of her beloved Lestat?", 
      "answer": " Tom Cruise", 
      "category": "5", 
      "difficulty": 4
    }, 
    {
      "id": 5, 
      "question": " Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?", 
      "answer": " Maya Angelou", 
      "category": "4", 
      "difficulty": 2
    }, 
    {
      "id": 6, 
      "question": " What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?", 
      "answer": " Edward Scissorhands", 
      "category": "5", 
      "difficulty": 3
    }, 
    {
      "id": 7, 
      "question": " Which active footballer in 2022 has the most career goals?", 
      "answer": " Cristiano Ronaldo", 
      "category": "6", 
      "difficulty": 2
    }, 
    {
      "id": 8, 
      "question": " In what year the COVID-19 epidemic started?", 
      "answer": " 2020", 
      "category": "4", 
      "difficulty": 2
    }, 
    {
      "id": 9, 
      "question": " What boxer's original name is Cassius Clay?", 
      "answer": " Muhammad Ali", 
      "category": "4", 
      "difficulty": 1
    }, 
    {
      "id": 10, 
      "question": " Which is the only team to play in every soccer World Cup tournament?", 
      "answer": " Brazil", 
      "category": "6", 
      "difficulty": 3
    }, 
    {
      "id": 11, 
      "question": " Which country won the first ever soccer World Cup in 1930?", 
      "answer": " Uruguay", 
      "category": "6", 
      "difficulty": 4
    }
  ], 
  "total_questions": 10, 
  "categories": {
    "1": " Science", 
    "2": " Art", 
    "3": " Geography", 
    "4": " History", 
    "5": " Entertainment", 
    "6": " Sports"
  }, 
  "current_category": "All"
}
```
---

#### `POST /questions`

A new question is created from the newly entered question, answer, category and difficulty. It returns a success message and a formatted page of the added question.

The request will throw an error if a column (ie either of question, answer, category and difficulty) is omitted.

You can `POST` a question using `curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"How old was John F. Kennedy when he was assassinated?", "answer":"46 years", "difficulty":"3", "category": "History"}'`

Below is how the reponse will appear if request was successful:

```json
 {
    "success": true,
    "created": 70,
    "questions": [
        {
            "id": 1,
            "question": " What is the deepest part on Earth?",
            "answer": " The Mariana Trench",
            "category": "3",
            "difficulty": 4
        },
        {
            "id": 2,
            "question": " What movie earned Tom Hanks his third straight Oscar nomination in 1996?",
            "answer": " Apollo 13",
            "category": "5",
            "difficulty": 4
        },
        {
            "id": 4,
            "question": " What actor did author Anne Rice first denounce then praise in the role of her beloved Lestat?",
            "answer": " Tom Cruise",
            "category": "5",
            "difficulty": 4
        },
        {
            "id": 5,
            "question": " Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
            "answer": " Maya Angelou",
            "category": "4",
            "difficulty": 2
        },
        {
            "id": 6,
            "question": " What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?",
            "answer": " Edward Scissorhands",
            "category": "5",
            "difficulty": 3
        },
        {
            "id": 7,
            "question": " Which active footballer in 2022 has the most career goals?",
            "answer": " Cristiano Ronaldo",
            "category": "6",
            "difficulty": 2
        },
        {
            "id": 8,
            "question": " In what year the COVID-19 epidemic started?",
            "answer": " 2020",
            "category": "4",
            "difficulty": 2
        },
        {
            "id": 9,
            "question": " What boxer's original name is Cassius Clay?",
            "answer": " Muhammad Ali",
            "category": "4",
            "difficulty": 1
        },
        {
            "id": 10,
            "question": " Which is the only team to play in every soccer World Cup tournament?",
            "answer": " Brazil",
            "category": "6",
            "difficulty": 3
        },
        {
            "id": 11,
            "question": " Which country won the first ever soccer World Cup in 1930?",
            "answer": " Uruguay",
            "category": "6",
            "difficulty": 4
        }
    ],
    "total_questions": 36
}
```
---

#### `GET /categories/{category_id}/questions`

This request if successful, returns a json object of questions based on the category id selected. 

It can be navigated through the URL `curl http://127.0.0.1:5000/categories/3/questions`

Below is how the reponse will appear if request was successful:

```json
{
    "success": true,
    "questions": [
        {
            "id": 5,
            "question": " Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?",
            "answer": " Maya Angelou",
            "category": "4",
            "difficulty": 2
        },
        {
            "id": 8,
            "question": " In what year the COVID-19 epidemic started?",
            "answer": " 2020",
            "category": "4",
            "difficulty": 2
        },
        {
            "id": 9,
            "question": " What boxer's original name is Cassius Clay?",
            "answer": " Muhammad Ali",
            "category": "4",
            "difficulty": 1
        },
        {
            "id": 12,
            "question": " Who invented Peanut Butter?",
            "answer": " George Washington Carver",
            "category": "4",
            "difficulty": 2
        },
        {
            "id": 23,
            "question": " Which dung beetle was worshipped by the ancient Egyptians?",
            "answer": " Scarab",
            "category": "4",
            "difficulty": 4
        },
        {
            "id": 67,
            "question": " How old was John F. Kennedy when he was assassinated?",
            "answer": "46 years",
            "category": "4",
            "difficulty": 3
        }
    ],
    "total_questions": 6,
    "current_category": 4
}
```
---

#### `DELETE /questions/{question_id}`

This request deletes the question whose `question_id` is referenced in the URL and return a success message if true.

It can be navigated through the URL `curl -X DELETE http://127.0.0.1:5000/questions/5` from your terminal.

The success message will be returned in the format below otherwise it throws an error:

```json
{
    "success": true,
    "deleted": 13,
    "total_questions": 35
}
```
---

#### `POST /quizzes`

This request returns a random question from the selected category. 

To achieve this, run `curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"type": "Science", "id": "1"}, }'` or any other category of your choice in your terminal .

For a successful request, the success message is in the format below:

```json
{
    "success": true,
    "question": {
        "id": 20,
        "question": " What is the heaviest organ in the human body?",
        "answer": " The Liver",
        "category": "1",
        "difficulty": 4
    }
}
```

### Error Handling

Error messages are returned when different requests failed for different reasons. These reasons can be represented by different error codes. You can read up [https://www.restapitutorial.com/httpstatuscodes.html](https://www.restapitutorial.com/httpstatuscodes.html).

The error messages are returned as below:
```json
{
    "success": false,
    "error": 404,
    "message": "resource was not found"
}
{
    "success": false,
    "error": 400,
    "message": "Oops! you made an invalid request"
}

{
    "success": false,
    "error": 422,
    "message": "Request could not be processed"
}

{
    "success": false,
    "error": 500,
    "message": "Internal Server Error"
}
```
---

