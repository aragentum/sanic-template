#!/usr/bin/env bash

until python manage.py migrate; do
  echo "Migration problems, possibly DB server is unavailable"
  sleep 5
done

if [[ "${IS_DEVELOPMENT}" == true ]]; then
  echo "--- DEVELOPMENT MODE ---"
  python manage.py runserver
else
  echo "--- PRODUCTION MODE ---"
  sanic sanic_template.runner.app --host 0.0.0.0 --port 8000 --workers ${SANIC_TEMPLATE_WORKERS:=4}
fi


