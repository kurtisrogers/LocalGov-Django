# News

The News feature provides newsrooms and articles for council communications.

## Content types

- **Newsroom** — listing page for articles
- **News article** — individual news story

## Newsrooms

A newsroom lists all its articles. You can:

- Feature up to three articles (shown prominently)
- Filter articles by category and year on the listing page

A default newsroom is created by `load_sample_content` at `/news/news/`.

## News articles

Each article has:

- Title, summary, and body
- Published date
- Optional image
- Categories (Topics)
- Featured flag

Article URLs follow the pattern: `/news/<newsroom>/<year>/<slug>/`

## Managing in admin

1. Create or edit a **Newsroom**
2. Add **News articles** and assign to a newsroom
3. Mark articles as **Featured** for prominence
4. Assign **Categories** for filtering
