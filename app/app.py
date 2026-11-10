"""HTTP-РїСЂРёР»РѕР¶РµРЅРёРµ РґР»СЏ РїСЂРѕРІРµСЂРєРё CI-РєРѕРЅРІРµР№РµСЂР°."""

from flask import Flask, jsonify


def create_app():
    """РЎРѕР·РґР°С‘С‚ Рё РЅР°СЃС‚СЂР°РёРІР°РµС‚ СЌРєР·РµРјРїР»СЏСЂ РїСЂРёР»РѕР¶РµРЅРёСЏ."""
    application = Flask(__name__)

    @application.get("/health")
    def health():
        """Р’РѕР·РІСЂР°С‰Р°РµС‚ СЂРµР·СѓР»СЊС‚Р°С‚ РїСЂРѕРІРµСЂРєРё Р¶РёР·РЅРµСЃРїРѕСЃРѕР±РЅРѕСЃС‚Рё."""
        return jsonify(status="unhealthy")

    @application.get("/")
    def index():
        """Р’РѕР·РІСЂР°С‰Р°РµС‚ СЃРІРµРґРµРЅРёСЏ Рѕ СЃР»СѓР¶Р±Рµ."""
        return jsonify(
            service="devops-ci-app",
            version="1.0.0",
            status="running",
        )

    return application


app = create_app()
