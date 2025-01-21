run-python:
	python fastApiApp/main.py

up:
	docker compose up -d

down:
	docker compose down -v