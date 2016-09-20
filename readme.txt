cd ~/projects/univer/ # заходим в папку с проектом
virtualenv --no-site-packages --distribute -p /usr/bin/python3 venv

# Активируем виртуальное окружение:
source ./venv/bin/activate
pip install -r requirements_dev.txt # устанавливаем зависимости
