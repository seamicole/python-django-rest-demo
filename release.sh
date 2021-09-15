#!/usr/bin/env bash

# RELEASE SCRIPT: RUNS BEFORE AN APP IS DEPLOYED (TYPICALLY STAGING / PRODUCTION)

echo "RELEASE SCRIPT:"
echo $HEROKU_APP_NAME

if [[ ! $HEROKU_APP_NAME == "drf-demo-backend-staging-pr-"* ]]; then
  echo "Staging / Production app detected, launch release phase (migrate before deploying)"
  python manage.py migrate --no-input
else
  echo "Review App (PR) detected, skip release for faster app creation"
  echo "If you have pushed new migrations after the review app creation, run them manually after deployment:"
  echo "heroku run ./manage.py migrate --app $HEROKU_APP_NAME"
fi
