###SSH
git clone git@github.com:Askarb/semester7.git ~/PROJECTS/univer <br\>


###Установка окружения на Linux
sudo apt-get install python  python3-dev  python3-setuptools  python3-pip <br\>
sudo pip3 install virtualenv


###Создаем виртуальное окружение для проекта  <br\>
cd ~/PROJECTS/univer/ # заходим в папку с проектом <br\>
virtualenv --no-site-packages --distribute -p /usr/bin/python3 venv # Важно, что мы используем 3-ю версию Python. <br\>


###Активируем виртуальное окружение:
source ./venv/bin/activate <br\>
pip install -r requirements.txt # устанавливаем зависимости


