#!/bin/bash

docker exec postgres \
pg_dump -U admin appdb \
> backup_$(date +%F).sql

# Daily PostgreSQL backup using pg_dump.
# Can be automated using cron.