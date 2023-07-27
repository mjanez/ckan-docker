#!/bin/bash

# Set the necessary variables
CONTAINER_NAME="db"
DATABASE_NAME="ckan"
POSTGRES_USER="ckan"
POSTGRES_PASSWORD="your_postgres_password"
BACKUP_DIRECTORY="/path/to/your/backup/directory"
DATE=$(date +%Y%m%d%H%M%S)

# Run the backup command
docker exec -e PGPASSWORD=$POSTGRES_PASSWORD $CONTAINER_NAME pg_dump -U $POSTGRES_USER -Fc $DATABASE_NAME > $BACKUP_DIRECTORY/ckan_backup_$DATE.dump