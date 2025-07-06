---
### Service Applications/README.md

# Service Applications

Small Python service frameworks and utilities.

## 📁 Contents

- **ecommerce/** — Minimal REST API for a shopping cart.  
- **pythonx0/** — Microservice examples using FastAPI.  
- `x0calculator.py` — Console-based calculation service.

## ⚙️ Setup & Usage

1. Install dependencies:
   ```bash
   pip install fastapi uvicorn

2. Run the API:
   ```bash
   -python -m uvicorn pythonx0.asgi:application --reload
   -python -m uvicorn ecommerce.asgi:application --reload
---
