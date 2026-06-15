from backend.app.services.gemini_service import (
    generate_response
)

response = generate_response(
    "Explain what Python is in 3 lines."
)

print(response)