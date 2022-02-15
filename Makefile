ifneq (,$(wildcard ./.env))
include .env
export
ENV_FILE_PARAM = --env-file .env

endif

hello:
	echo "hello world"

build:
	docker-compose up --build -d --remove-orphans

up:
	docker-compose up -d

down:
	docker-compose down -v

makemigration:
	docker-compose exec api python3 manage.py makemigrations

migrate:
	docker-compose exec api python3 manage.py migrate

superuser:
	docker-compose exec api python3 manage.py createsuperuser

volume:
	docker inspect estate-src_postgres_data
	
db-estate:
	docker-compose exec postgres-db psql --username=admin --dbname=estate1

show-logs:
	docker-compose logs

test:
	docker-compose exec api pytest -p no:warnings --cov=.

test-html:
	docker-compose exec api pytest -p no:warnings --cov=. --cov-report html

