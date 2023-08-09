#!/bin/bash

# Set the necessary variables
CONTAINER_NAME="db"
DATABASE_NAME="ckan"
POSTGRES_USER="ckan"
POSTGRES_PASSWORD="your_postgres_password"
BACKUP_DIRECTORY="/path/to/your/backup/directory"
DATE=$(date +%Y%m%d%H%M%S)
MONTH=$(date +%m)
YEAR=$(date +%Y)

# Create the monthly backup directory if it doesn't exist
mkdir -p "$BACKUP_DIRECTORY/monthly/$YEAR-$MONTH"

# Run the backup command
docker exec -e PGPASSWORD=$POSTGRES_PASSWORD $CONTAINER_NAME pg_dump -U $POSTGRES_USER -Fc $DATABASE_NAME > "$BACKUP_DIRECTORY/monthly/$YEAR-$MONTH/ckan_backup_$DATE.dump"

# Compress the dump files into a zip archive
cd "$BACKUP_DIRECTORY/monthly/$YEAR-$MONTH" || exit
zip "backup_${YEAR}-${MONTH}.zip" *.dump

# Remove the original dump files
rm -f *.dump
