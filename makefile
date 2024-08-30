
docker:
	bash -c "cd backend && poe up"

api:
	bash -c "cd backend && poe start"

ui:
	bash -c "cd frontend && npm start"