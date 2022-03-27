source ./venv/bin/activate;

if [ -z "$1" ]; then
		echo "Usage: $0 [command]";
		exit 1;
fi

if [ "$1" = "runserver" ]; then
		python manage.py runserver

elif [ "$1" = "shell" ]; then
		python manage.py shell_plus --ipython

elif [ "$1" = "notebook" ] || [ "$1" = "note" ]; then
		python manage.py shell_plus --notebook

elif [ "$1" = "makemigrations" ]; then
		python manage.py makemigrations

elif [ "$1" = "migrate" ]; then
		python manage.py migrate

elif [ "$1" = "test" ]; then
		python manage.py test

elif [ "$1" = "makemessages" ]; then
		python manage.py makemessages

elif [ "$1" = "compilemessages" ]; then
		python manage.py compilemessages

elif [ "$1" = "check" ]; then
		python manage.py check

elif [ "$1" = "collectstatic" ]; then
		python manage.py collectstatic

elif [ "$1" = "startapp" ]; then
		python manage.py startapp $2

elif [ "$1" = "startproject" ]; then
		python manage.py startproject $2

elif [ "$1" = "help" ]; then
		echo "Usage: $0 [command]";
		echo "Commands:";
		echo "runserver";
		echo "shell";
		echo "makemigrations";
		echo "migrate";
		echo "test";
		echo "makemessages";
		echo "compilemessages";
		echo "check";
		echo "collectstatic";
		echo "startapp";
		echo "startproject";
		echo "help";
		exit 1;

else
		echo "Unknown command: $1";
		exit 1;
fi