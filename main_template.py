from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

class UppercaseText(Resource):

    def get(self):
        """
        This method responds to the GET request for this endpoint and returns the data in uppercase.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be converted to uppercase
        responses:
            200:
                description: A successful GET request
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The text in uppercase
        """
        text = request.args.get('text')

        # return jsonify({"text": text.upper()})
        return {"text": text.upper()}, 200


class TransformText(Resource):
    def get(self):
        """
        Transform the input text by duplication and optional capitalization.
        ---
        tags:
        - Text Processing
        parameters:
            - name: text
              in: query
              type: string
              required: true
              description: The text to be transformed
            - name: duplication_factor
              in: query
              type: integer
              required: false
              description: Number of times to repeat the text
            - name: capitalization
              in: query
              type: string
              required: false
              enum: [UPPER, LOWER, None]
              description: Capitalization style of the text
        responses:
            200:
                description: Successfully transformed text
                content:
                    application/json:
                      schema:
                        type: object
                        properties:
                            text:
                                type: string
                                description: The transformed text
        """
        text = request.args.get('text')
        if not text:
            return {"error": "Missing required parameter 'text'"}, 400

        duplication_factor = request.args.get('duplication_factor', default=1, type=int)
        capitalization = request.args.get('capitalization', default='None')

        # Validate capitalization input
        if capitalization not in ('UPPER', 'LOWER', 'None'):
            return {'error': 'Invalid capitalization value'}, 400

        # Apply capitalization if specified
        if capitalization == "UPPER":
            text = text.upper()
        elif capitalization == "LOWER":
            text = text.lower()

        # Duplicate the text
        transformed_text = text * duplication_factor

        return {"transformed_text": transformed_text}, 200

# Register Endpoints
api.add_resource(UppercaseText, "/uppercase")
api.add_resource(TransformText, "/transform")


if __name__ == "__main__":
    app.run(debug=True)
