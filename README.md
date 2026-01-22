# BlogFast — Minimal, Bold, Fast Reading

A modern, animated blogging web application focused on many short posts, fast reading, and a smooth, minimal user experience with a bold black and yellow theme.

## Tech Stack
- Backend: Django (Python)
- Frontend: Django Templates (HTML), Tailwind CSS (CDN), Alpine.js (CDN)
- Rich Text: CKEditor (django-ckeditor)
- Database: Django ORM (SQLite by default)

## Features
- Blogger (staff): custom dashboard for create/edit/delete, publish/unpublish, attach images, live likes/comments via lightweight polling.
- Reader: browse published posts, previews, Read More, like, instant comments (no moderation).
- Animations: subtle fade-in, hover transitions.

## Quickstart

### Local Development

### 1) Create venv and install deps
```bash
python3 -m venv /home/isaac/Desktop/blogfast/.venv
source /home/isaac/Desktop/blogfast/.venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

### 2) Migrate and run
```bash
cd /home/isaac/Desktop/blogfast
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### 3) Usage
- Visit: http://127.0.0.1:8000/ for public blog list.
- Visit: http://127.0.0.1:8000/dashboard/ (login as staff) to manage posts.
- Upload images via dashboard forms; CKEditor uploader stores files under `media/uploads/`.

## Settings
- Templates: `templates/`
- Static: `static/`
- Media: `media/`
- CKEditor: `ckeditor/` URLs included.

## Scalability
- Add tags/categories: new model + filters.
- Search: simple title/content search view.
- Pagination: Django pagination or infinite scroll via HTMX/Alpine.
- SEO: add meta tags, sitemaps.
- Multi-bloggers: multiple staff users.
- Newsletter: integrate a mail provider API.

## Notes
- For Tailwind customization beyond defaults, switch to compiled Tailwind (CLI or `django-tailwind`). CDN is used here to keep JS minimal and setup light.
- Likes are simple counters (no dedupe); comments are public and instant (no moderation).

## Production Deployment

### Azure App Service
See [DEPLOYMENT.md](DEPLOYMENT.md) for complete Azure deployment guide with:
- **Azure SQL Database** (recommended)
- **Azure Database for PostgreSQL** (alternative)
- Environment configuration
- Step-by-step commands

The app is production-ready with:
- Environment-based configuration
- PostgreSQL & Azure SQL support
- WhiteNoise for static files
- Gunicorn for WSGI server
- Security settings for HTTPS