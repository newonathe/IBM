# Supabase Setup

1. Create a Supabase project.
2. In the Supabase SQL editor, run [`supabase/schema.sql`](C:/Users/ethan/Downloads/Internships/Internship%20Companies/IBM/supabase/schema.sql).
3. In Supabase Authentication settings, enable Email auth.
4. Add your GitHub Pages URL to the allowed redirect URLs and site URL.
5. Copy your project URL and anon key into [`assets/supabase-config.js`](C:/Users/ethan/Downloads/Internships/Internship%20Companies/IBM/assets/supabase-config.js).
6. Redeploy the site.

What this enables:

- Supabase email/password sign-up and sign-in
- Cloud-synced lesson progress by part
- Cloud-synced IDE workspace state
- Per-user row-level security on profiles, progress, and workspace data

What still works without Supabase:

- Full public access
- Guest mode
- Local browser saves
- The lesson split-view IDE and full IDE page
