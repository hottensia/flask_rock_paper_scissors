from app import app
import logging
from flask import Flask, jsonify
from flask_cors import CORS
from flask_caching import Cache

logger = logging.getLogger()
formatter = logging.Formatter("%")

logger.setLevel(logging.INFO)

app.url_map.strict_slashes = False

cache = Cache(app)  # Initialize the cache

CORS(app)

app.run(host="127.0.0.1", port=8080, debug=True)