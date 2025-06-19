import os
import logging
from flask import Flask
from flask_restful import Resource, Api

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = Flask(__name__)
api = Api(app)


class Greeting(Resource):
    def get(self):
        logger.info("Greeting endpoint called")
        return "Telethon Music is Up & Running!"


api.add_resource(Greeting, '/')

def main() -> None:
    port = int(os.environ.get("PORT", 8080))
    logger.info("Starting server on port %s", port)
    app.run(host="0.0.0.0", port=port)


if __name__ == "__main__":
    main()
