RUN = poetry run

.PHONY: dev format test

dev:
	$(RUN) uvicorn src.oak_api.main:app --reload

format:
	$(RUN) black {src,tests}
	$(RUN) isort {src,tests}

test:
	$(RUN) pytest
