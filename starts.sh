#!/bin/bash

if [ ! -d "venv" ]; then
    echo "📦 Создаю виртуальное окружение..."
    python3 -m venv venv
fi

echo "📥 Устанавливаю зависимости..."
./venv/bin/pip install flask

echo "🚀 Запускаю проект..."
./venv/bin/python3 main.py