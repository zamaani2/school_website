# Deploying this Django project to Vercel

Quick steps to deploy:

1. Commit and push this repository to a Git provider (GitHub/GitLab/Bitbucket) connected to Vercel.
2. On Vercel, create a new Project and import this repository.
3. Set Environment Variables in the Vercel Project settings (required at runtime):
   - `DJANGO_SETTINGS_MODULE` = `school_website.production_settings` (already set in `vercel.json` for build)
   - `SECRET_KEY` = (your Django secret key)
   - `DATABASE_URL` = (your production database URL) — or configure an external DB service
   - Any other secrets (e.g., `EMAIL_*`, third-party API keys)
4. Ensure `requirements.txt` includes `vercel-wsgi` (added) so the Vercel Python builder can run the WSGI handler.
5. Optionally, run `python manage.py collectstatic --noinput` during your build or use a storage service (S3) for static files.
6. Deploy and monitor logs from the Vercel dashboard. If you need to update environment variables, edit them in the Project settings.

Notes & troubleshooting:
- This setup uses `api/wsgi.py` (Vercel Serverless Function) and `vercel-wsgi` to run Django's WSGI app.
- For heavy/long-running tasks or full persistent services consider using a platform designed for traditional Django deployments (Render, Railway, Heroku replacement).
