#!/bin/bash

set -o errexit
set -o nounset


rm -f './celerybeat.pid'
celery -A celery_examples.celery_app beat -l INFO