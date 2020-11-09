#!/usr/bin/env bash
# sleep 1
# if [ $(mysql -h $MYSQL_HOST -u $MYSQL_USER -p$MYSQL_PASSWORD $MYSQL_DATABASE -bse "SELECT COUNT(*) FROM information_schema.tables WHERE table_schema='$MYSQL_DATABASE';") -gt 0 ] ; then
#   echo -e "No need to run migrations"
# else
#   python migrate.py db init && python migrate.py db migrate && python migrate.py db upgrade
#   echo -e "database successfully created"
# fi

export FLASK_ENV=development
export FLASK_APP=run.py
# python3 -m pip install pyidm --user
flask run --host=0.0.0.0 --port=9999
