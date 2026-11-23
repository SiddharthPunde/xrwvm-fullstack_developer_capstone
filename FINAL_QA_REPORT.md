# Capstone QA Status

**Last verified:** 23 November 2026  
**Repository:** https://github.com/SiddharthPunde/xrwvm-fullstack_developer_capstone

## Verified in GitHub Actions

Workflow run: https://github.com/SiddharthPunde/xrwvm-fullstack_developer_capstone/actions/runs/45112986101

- Python checks: passed.
- React production build: passed.
- Django system checks and migrations: passed.
- Database seed command: created 50 dealership records.
- Assignment API smoke test: `GET /fetchDealers` returned HTTP 200 and 50 records.
- Sentiment compatibility route: `GET /analyze/Fantastic%20services` returned HTTP 200 with positive sentiment.
- Django test suite: 21 tests passed.

## Important scope notes

- Dealership records 15–50 are clearly labelled demo records generated for the assignment's 50-record requirement; they are not claims about real businesses.
- The current successful workflow run verifies the code and API in GitHub Actions, not a public deployment.
- No live deployment URL is currently verified. Do not submit the old CognitiveClass proxy URL copied from another repository.
- The reviewer previously flagged the Task 20 dealer/review screenshot because the review was not fully visible. Retake it only if you intend to recover that point.
- Deployed screenshots for Tasks 25–28 must come from the actual live deployment; existing files should not be represented as verified unless checked against that deployment.
