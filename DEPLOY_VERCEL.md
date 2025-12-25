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

Build error you may see:

```
No solution found when resolving dependencies:
   Because vercel-wsgi was not found in the package registry and your
   project depends on vercel-wsgi, we can conclude that your project's
   requirements are unsatisfiable.
```

How to resolve the above:
- Remove `vercel-wsgi` from `requirements.txt` (done in this repo). This lets Vercel install remaining deps.
- If you need the `vercel-wsgi` adapter, supply it from source (git) in `requirements.txt`, for example:

```
# Example (replace with the correct repository/url if you have one)
# git+https://github.com/<owner>/vercel-wsgi.git@main#egg=vercel-wsgi
```

- Alternatively, implement a small WSGI-to-Vercel adapter in `api/wsgi.py` (avoids external package). If you'd like, I can add a self-contained adapter implementation into `api/wsgi.py` and reconfigure `vercel.json` accordingly.

