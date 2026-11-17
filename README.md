# IBM Full Stack Software Developer Capstone — Best Cars Dealership

A full-stack dealership review application built with Django, React, Express and MongoDB.

## Features
- Django authentication: registration, login and logout
- Dealer directory with state filtering and dealer detail/review API
- Authenticated review submission
- Car make/model catalogue populated from the supplied JSON dataset
- Express/Mongoose API backed by MongoDB
- Review sentiment integration with a neutral fallback when the analyzer is unavailable
- Static About Us and Contact Us pages

## Architecture
- Django API and static pages: `server/` (default port 8000)
- Express/MongoDB API: `server/database/` (port 3030; MongoDB 27017)
- Sentiment service: `server/djangoapp/microservices/` (port 5050)
- React frontend: `server/frontend/`

## Local setup
1. Create and activate a Python virtual environment in `server`.
2. Install the server requirements: `pip install -r requirements.txt`.
3. Start MongoDB and the Express API with `docker compose up --build` from `server/database`.
4. Run Django migrations: `python manage.py makemigrations djangoapp` then `python manage.py migrate`.
5. Seed the car catalogue when the first `/djangoapp/get_cars` request is made.
6. Start Django: `python manage.py runserver`.
7. In `server/frontend`, run `npm install` and `npm start`.

Configure `backend_url` and `sentiment_analyzer_url` in the Django environment as appropriate for your runtime. For Docker deployments, use the service hostname rather than localhost.

## API routes
| Method | Route | Purpose |
|---|---|---|
| POST | `/djangoapp/register` | Create account |
| POST | `/djangoapp/login` | Authenticate |
| POST/GET | `/djangoapp/logout` | End session |
| GET | `/djangoapp/get_dealers/` | List dealers |
| GET | `/djangoapp/get_dealers/<state>` | Filter dealers |
| GET | `/djangoapp/dealer/<id>` | Dealer details |
| GET | `/djangoapp/reviews/dealer/<id>` | Dealer reviews + sentiment |
| GET | `/djangoapp/get_cars` | Car models |
| POST | `/djangoapp/add_review` | Submit authenticated review |

## Project evidence
Evidence command templates are in `evidence/`. Runtime outputs, browser screenshots, successful Actions runs and a public deployment URL must be captured from a real run; they are intentionally not fabricated.
