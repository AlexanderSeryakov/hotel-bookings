DC = docker compose


runserver:
	${DC} up --remove-orphans -d --build
down:
	${DC} down
connect-app:
	${DC} exec backend sh