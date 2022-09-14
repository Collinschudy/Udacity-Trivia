import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_
from flask_cors import CORS
import random
from  sqlalchemy.sql.expression import func, select

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


  
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    
    setup_db(app)
    CORS(app)

    

    # CORS Headers
    @app.after_request
    def after_request(response):

        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization,true")
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS")
        return response
   

    """
    @TODO:
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories')
    def get_categories():
        categories = Category.query.order_by(Category.id).all()

        if len(categories) == 0:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'categories': {category.id: category.type for category in categories}
            })

        
    """
    @TODO:
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.

    TEST: At this point, when you start the application
    you should see questions and categories generated,
    ten questions per page and pagination at the bottom of the screen for three pages.
    Clicking on the page numbers should update the questions.
    """

    @app.route('/questions')
    def retrieve_questions():
        all_questions = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, all_questions)

        categories = Category.query.order_by(Category.id).all()

        if len(current_questions) == 0:
            abort(404)
        else:
            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(current_questions),
                'categories': {category.id: category.type for category in categories},
                'current_category': "All"
            })



    """
    @TODO:
    Create an endpoint to DELETE question using a question ID.

    TEST: When you click the trash icon next to a question, the question will be removed.
    This removal will persist in the database and when you refresh the page.
    """ 

    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(question_id):
        try:
            question = Question.query.filter(Question.id == question_id).one_or_none()
            if question is None:
                abort(404)
            else:
                question.delete()
                all_questions = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, all_questions)
                return jsonify({
                    'success': True,
                    'deleted': question.id,
                    'total_questions': len(Question.query.all())
                })
        except:
            abort(422)

    """
    @TODO:
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.

    TEST: When you submit a question on the "Add" tab,
    the form will clear and the question will appear at the end of the last page
    of the questions list in the "List" tab.
    """
    @app.route('/questions', methods=['POST'])
    def create_question():
        body = request.get_json()
        if ('question' in body and 'answer' in body and 'difficulty' in body and 'category' in body):
        

            new_question = body.get("question", None)
            new_answer = body.get("answer", None)
            new_difficulty = body.get("difficulty", None)
            new_category = body.get('category', None)

            try:
                question = Question(question=new_question, answer=new_answer, difficulty=new_difficulty, category=new_category)
                question.insert()

                all_questions = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, all_questions)

                return jsonify(
                    {
                        "success": True,
                        "created": question.id,
                        "questions": current_questions,
                        "total_questions": len(Question.query.all())
                    }
                )

            except:
                abort(422)
        else:
            abort(422)

    """
    @TODO:
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.

    TEST: Search by any phrase. The questions list will update to include
    only question that include that string within their question.
    Try using the word "title" to start.
    """
    @app.route('/questions/search', methods=['POST'])
    def search_questions():
        body = request.get_json()
        search = body.get('searchTerm', None)

        if search:
            searchResults = Question.query.filter(
                Question.question.ilike('%{}%'.format(search))).all()

            current_questions = paginate_questions(request, searchResults)
            
            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(current_questions),
                'current_category': None
            })
            
        


    """
    @TODO:
    Create a GET endpoint to get questions based on category.

    TEST: In the "List" tab / main screen, clicking on one of the
    categories in the left column will cause only questions of that
    category to be shown.
    """
    @app.route('/categories/<int:category_id>/questions')
    def get_questions_by_category(category_id):
        try:
            all_questions = Question.query.filter(or_(
                Question.category == str(category_id), Question.category == " " + str(category_id))).order_by(
                    Question.id).all()
            
            
     
        
            current_questions = paginate_questions(request, all_questions)

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(current_questions),
                'current_category': category_id
            })
        except:
            abort(404)


    """
    @TODO:
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.

    TEST: In the "Play" tab, after a user selects "All" or a category,
    one question at a time is displayed, the user is allowed to answer
    and shown whether they were correct or not.
    """

    @app.route('/quizzes', methods=['POST'])
    def answer_quiz():
        all_category = 0
        try:
            body = request.get_json()
            if ('quiz_category' in body and 'previous_questions' in body):
                quiz_category = body.get('quiz_category')
                previous_questions = body.get('previous_questions')
                category_id = quiz_category['id']
           
            
                if category_id == all_category:
                    unique_questions = Question.query.filter(
                        Question.id.not_in((previous_questions))).all()
                else:
                    unique_questions = Question.query.filter_by(
                        category=category_id).filter(
                            Question.id.not_in((previous_questions))).all()
                if len(unique_questions) > 0:
                    formatted_questions = [random_question.format() for random_question in unique_questions]
                    question = random.choice(formatted_questions)
                # 
                #     random_question = unique_questions[random.randrange(
                #         0, len(unique_questions))].format()
                    # random_question = unique_questions.query.order_by(func.random()).limit(1)
                    # random_question = session.query(unique_questions).order_by(func.rand()).first().format()
                    
                        
                    return jsonify({
                        'success': True,
                        'question': question
                    })
                else:
                    return jsonify({
                            'success': True,
                            'question': None
                        })
            else:
                abort(422)
                    
        except:
            abort(422)

    """
    @TODO:
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Request could not be processed"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource was not found"
        }), 404

    

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Oops! you made an invalid request"
        }), 400

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        }), 500

    


    return app

