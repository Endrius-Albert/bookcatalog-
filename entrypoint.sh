#!/bin/sh


echo "Aguardando o banco de dados iniciar..."
while ! nc -z $DATABASE_HOST 5432; do
  sleep 1
done

echo "Banco de dados disponível, continuando..."

python manage.py migrate

python manage.py runserver 0.0.0.0:8000
