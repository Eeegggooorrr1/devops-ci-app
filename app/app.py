"""Flask application for the CI pipeline."""

from flask import Flask, jsonify


def create_app():
    """Create and configure the Flask application."""
    application = Flask(__name__)

    @application.get("/health")
    def health():
        """Return the application health status."""
        return jsonify(status="unhealthy")

    @application.get("/")
    def index():
        """Return service information."""
        return jsonify(
            service="devops-ci-app",
            version="1.0.0",
            status="running",
        )

    return application


app = create_app()
