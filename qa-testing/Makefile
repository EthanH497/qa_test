make:
	echo "App running on port 3335..."
	uvicorn app.main:app --host 0.0.0.0 --port 3335 --reload

db:
	docker-compose up

test:
	echo "Running tests..."
	TEST_FLAG=True python3 -m pytest -s -vv --cov=app \
		--cov-report term-missing --pyargs app