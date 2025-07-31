# Database Migrations

This directory contains Alembic migration files for managing database schema changes.

## Directory Structure

```
migrations/
├── env.py              # Alembic environment configuration
├── script.py.mako      # Template for new migration files
└── versions/           # Migration revision files
```

## Usage

The migrations are managed via the Makefile commands:

```bash
# Create a new migration
make revision

# Apply migrations
make migrate

# Rollback last migration
make rollback
```

## Notes

- Migration files are auto-generated based on model changes
- Each migration has an upgrade() and downgrade() function
- Always review generated migrations before applying
