#!/bin/bash

poetry run isort covid_etl/ tests/ && \
poetry run black covid_etl/ tests/ && \
poetry run mypy covid_etl/ tests/
