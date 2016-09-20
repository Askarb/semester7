source venv/bin/activate
echo '**************************************Run unittest************************************'
./manage.py test quadratic/
echo '*********************************Unittest has finished***********************************'
echo '**********************************Run acceptance tests***********************************'
./manage.py harvest --liveserver localhost:8001 -v 3 --noinput
echo '******************************Acceptance tests has finished******************************'
