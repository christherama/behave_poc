SHELL: /bin/sh

start:
	docker-compose up -d

test:
	docker run --rm -it "behave_poc_api" /bin/bash -ci "python manage.py behave"