# ci/cd создание image на гитлабе

# start project docker-compose.yaml


# install pre-commit
    create - .pre-commit-config.yaml
    pip install pre-commit
    pre-commit install(устанавливаем нашу настройку)

# running Celery
    pip install -r requirements.txt
    celery -A shope worker --loglevel=info

# Add fixtures
    python manage.py add_fixtures - применить все фикстуры

# Running docker
    docker compose up -d --build - сборка перед стартом контейнеров
    docker compose up -d - запуск контейнеров (-d для запуска в фоне)
    docker compose down - остановка контейнеров