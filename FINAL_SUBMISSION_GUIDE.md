# Capstone Resubmission Checklist

Repository: https://github.com/SiddharthPunde/xrwvm-fullstack_developer_capstone

## Corrections now in the repository

| Task | Correction | Status |
|---|---|---|
| 1 | README now uses the destination repository name and identifies the project and author. | Updated |
| 3 | About page includes a Best Cars Dealership description. | Updated |
| 4 | Contact page already contains both CSS links and active Contact Us navigation. | Checked |
| 9 | Seeder now creates 50 records; CI verified `GET /fetchDealers` returns HTTP 200 and 50 records. | Verified in CI |
| 16 | Added the required `/analyze/<text>` compatibility route; CI verified positive sentiment for “Fantastic services”. | Verified in CI |
| 23 | GitHub Actions pipeline runs Python checks, a React production build, Django checks, API smoke tests, and the test suite. | Successful run |

## Evidence links

- README: https://github.com/SiddharthPunde/xrwvm-fullstack_developer_capstone/blob/main/README.md
- About page: https://github.com/SiddharthPunde/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/About.html
- Contact page: https://github.com/SiddharthPunde/xrwvm-fullstack_developer_capstone/blob/main/server/frontend/static/Contact.html
- CI run: https://github.com/SiddharthPunde/xrwvm-fullstack_developer_capstone/actions/runs/45112986101

## Remaining user actions

1. Task 20: reviewer said the dealer review was cut off. One replacement screenshot is needed only if recovering that point.
2. Task 24: deploy the app in an environment you can access and record its real public URL.
3. Tasks 25–28: capture the four required screens from that live URL. Do not reuse screenshots or URLs from another user's environment.

The old CognitiveClass proxy URL in earlier notes belongs to a different repository/environment and is not verified for this submission. Do not submit it.
