#!/bin/bash

set -o errexit
set -o nounset

celery -A celery_examples.celery_app worker -l INFO
