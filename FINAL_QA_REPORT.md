# Capstone QA Status

**Last verified:** 23 November 2026  
**Repository:** https://github.com/SiddharthPunde/xrwvm-fullstack_developer_capstone

## Successful end-to-end CI/CD run

Workflow run: https://github.com/SiddharthPunde/xrwvm-fullstack_developer_capstone/actions/runs/45113457158

All four jobs passed:
- Python checks and lint.
- React production build.
- Django system checks, migrations, seed, API smoke tests, and automated tests.
- Docker deployment image build.

Actual checks from the workflow:
- Seed command loaded 50 dealerships from the official IBM capstone sample dataset.
- `GET /fetchDealers` returned HTTP 200 and 50 records.
- `GET /analyze/Fantastic%20services` returned HTTP 200 with positive sentiment.
- Django test suite: 21 tests passed.
- Docker image build: passed.

## Remaining assessment work

- Task 20's existing screenshot was previously rejected because the review was cut off. A replacement screenshot is only needed if recovering that point.
- A Render Blueprint is included in `render.yaml`. It has not yet been deployed, so there is no verified public deployment URL.
- Tasks 25–28 require screenshots from the actual deployed application. Do not claim those are complete until a live deployment has been tested.
- Do not submit the old CognitiveClass proxy URL copied from another repository.
