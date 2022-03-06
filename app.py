from flask import Flask
from flask_restx import Resource, Api, fields, reqparse

app = Flask(__name__)
api = Api(app, version="1.0", title="Calculation API", description="Various calculation utilities")


answer = api.model('Answer', {
    'answer': fields.Integer
})
num_parser = reqparse.RequestParser()
num_parser.add_argument('number1', type=int, location='args', help='First number to be multiplied')
num_parser.add_argument('number2', type=int, location='args', help='Second number to be multiplied')

@api.route('/multiply')
class Multiply(Resource):
    @api.response(200, 'Success', answer)
    @api.expect(num_parser)
    def get(self):
        '''
        Multiply 2 numbers
        '''
        args = num_parser.parse_args()
        return {'answer': args['number1']*args['number2']}

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5014, debug=True, ssl_context='adhoc')