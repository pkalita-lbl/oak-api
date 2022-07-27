RUN = poetry run

.PHONY: dev format test

dev:
	$(RUN) uvicorn src.oak_api.main:app --reload

lint:
	$(RUN) flake8 src/ tests/

format:
	$(RUN) black {src,tests}
	$(RUN) isort {src,tests}

test:
	$(RUN) pytest
