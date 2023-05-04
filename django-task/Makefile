all:
	@echo "make start - Запуск контейнеров."
	@echo "make stop - Выключение контейнера."
	@echo "make createsuperuser - Создание суперпользователя."
start:
	docker-compose up --build
stop:
	docker-compose down
createsuperuser:
	docker-compose exec django python manage.py createsuperuser
