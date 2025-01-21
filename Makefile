run-python:
	python fastApiApp/main.py

up:
	docker compose up -d --build

down:
	docker compose down -v