source vendor/bin/activate
export CURRENT_ENV=dev
# uvicorn app:app --reload
uvicorn main:app --reload --port 8080