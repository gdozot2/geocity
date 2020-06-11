#!/bin/bash

echo **************applying entrypoint*******************
while :
do
    echo > /dev/tcp/postgres/5432
    if [[ $? -eq 0 ]]; then
        break
    else
      echo waiting for db...
    fi
    sleep 1
done

cd /code
# rename demo env file
cp -n env.yaml_demo env.yaml
# setup app using the django tools
python3 manage.py migrate
mkdir /code/geomapshark/static/
echo yes | python3 manage.py compilemessages -l fr


python3 manage.py fixturize


exec $@
