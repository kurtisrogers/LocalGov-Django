# Getting started

## Requirements

- Python 3.12+
- pip

## Installation

```bash
git clone https://github.com/kurtisrogers/LocalGov-Django.git
cd LocalGov-Django
pip install -r requirements.txt
python manage.py migrate
python manage.py load_sample_content
python manage.py createsuperuser  # optional
python manage.py runserver
```

Visit [http://localhost:8000](http://localhost:8000) for the demo site.

## Admin

Content is managed via Django admin at `/admin/`. All content types are registered with prepopulated slug fields and inline editing where appropriate.

## Sample content

The `load_sample_content` management command creates:

- Site configuration and navigation menus
- Example services (waste, council tax, housing)
- A schools directory with facets
- A guide and step-by-step process
- News articles and an event
- A subsite and alert banner

Run it again safely — it uses `get_or_create` so existing content is preserved.

## Environment

For production, set at minimum:

- `SECRET_KEY` — use a secure random value
- `DEBUG=False`
- `ALLOWED_HOSTS` — your domain(s)
- A production database (PostgreSQL recommended)

## Next steps

- [Features](features/index.md) — technical feature documentation
- [Theme](theme.md) — LocalGov Base styling
- [Testing](testing.md) — unit and BDD tests
