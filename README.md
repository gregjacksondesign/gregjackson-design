# gregjackson.design

A static rebuild of the WordPress portfolio, in [Astro](https://astro.build).
Ten pages, no database, no plugins, no monthly fee. Hosting is free; the only
running cost is the domain.

---

## Before it will look right

Two folders are empty, because image files are too large to move through a chat
window. Everything else is done.

1. **Images** → `public/images/` (67 files)
2. **Persona PDFs** → `public/files/` (4 files)

`IMAGE-MANIFEST.md` lists every filename and which page uses it. Get them by
SFTP from WordPress — credentials are under **Settings → Hosting
Configuration** — from `wp-content/uploads/`. Keep the filenames exactly as
listed and every reference resolves with no further edits.

Do this **before 10 September**, when the WordPress plan lapses and the files
become unreachable.

---

## Running it locally

You need [Node.js](https://nodejs.org) 18 or newer.

```bash
npm install     # once
npm run dev     # http://localhost:4321 — reloads as you save
npm run build   # writes the finished site to dist/
npm run preview # serve dist/ to check the real build
```

---

## Deploying to Cloudflare Pages

The site is a folder of static files, so hosting is free and there is no server
to maintain.

**Recommended: connect a Git repository.** Push this folder to GitHub, then in
the Cloudflare dashboard go to **Workers & Pages → Create → Pages → Connect to
Git**, pick the repo, and use:

| Setting | Value |
| --- | --- |
| Framework preset | Astro |
| Build command | `npm run build` |
| Build output directory | `dist` |

Every push then rebuilds the site automatically, and pull requests get their own
preview URL.

**Quicker, no Git:** run `npm run build`, then drag the `dist` folder onto
**Create → Pages → Upload assets**. Fine to start with, but you have to repeat
it by hand for every change.

Either way you get a free `something.pages.dev` address. **Check the site
thoroughly there first** — the WordPress site is still serving until 10
September, so there is no rush and no downtime.

### Pointing the domain at it

Only once you are happy with the `.pages.dev` version:

1. In your Pages project: **Custom domains → Set up a domain**
2. Enter `gregjackson.design`, then repeat for `www.gregjackson.design`

Because Cloudflare already runs your DNS, it adds the records itself. The HTTPS
certificate is issued automatically and takes a few minutes.

---

## How the site is put together

```
src/
  data/projects.js      The seven homepage projects. Edit this to add or reorder.
  layouts/
    Base.astro          Head, fonts, nav, footer — wraps every page.
    CaseStudy.astro     Title, intro and back-link for project pages.
  components/
    Nav.astro           Site navigation, with the underline-on-hover effect.
    Footer.astro
    ProjectCard.astro   Homepage tile: colour, hover wash, scroll reveal.
    Step.astro          A numbered stage in a case study.
    Quote.astro         A customer or colleague quote.
    Figure.astro        An image with optional caption.
    Gallery.astro       Several images in a scroll-snapping strip.
    FileDownload.astro  A downloadable PDF.
  pages/                One file per URL. index.astro is the homepage.
  styles/
    tokens.css          Every colour, size and space. Start here to restyle.
    global.css          Base element styles and shared interactions.
public/
  images/               Drop image files here.
  files/                Drop the persona PDFs here.
```

### Making changes

**Restyling** — `src/styles/tokens.css` holds every colour, type size and
spacing value as a named variable. Changing one there changes it everywhere.

**Editing text** — open the relevant file in `src/pages/` and edit it. It is
HTML with a few components mixed in; if you can read the page, you can edit it.

**Adding a project** — create a new `.astro` file in `src/pages/` (copy an
existing case study as a starting point), then add an entry to
`src/data/projects.js` so it appears on the homepage.

**Adding a nav link** — the `links` array at the top of
`src/components/Nav.astro`.

---

## Decisions worth knowing about

**Fonts are self-hosted.** IBM Plex Sans, Literata and Agbalumo are installed as
npm packages (Fontsource) and bundled at build time. Nothing is requested from
Google, which is faster and avoids the privacy question. All three are
open-licensed, so there is no licence to track.

**URLs match the old site exactly.** `/site-redesign/`, `/about-me/` and the
rest are unchanged, so existing links and anything on your CV keep working.

**The Jetpack slideshow is gone.** Those four design-sprint photos were in a
JavaScript carousel plugin. They are now a scroll-snapping strip that needs no
JavaScript — and shows all four images rather than hiding three.

**Alt text has been written for all 67 images.** Most were derived from
captions, headings and the images themselves, but fifteen were written without
being able to see the file. Those are marked `REVIEW` in `alt-text.py` — worth a
read-through, since your own redesign case study makes a point of accessibility.

**Type is fluid.** Every size uses the same `clamp()` values as the WordPress
theme, so text scales smoothly with the viewport rather than jumping at
breakpoints.

---

## Still to decide

- **The Agbalumo H2s.** Faithfully reproduced. If you want them in Literata to
  match the other headings, change `--font-display` in `tokens.css` to
  `var(--font-serif)` — one line.
- **Commercial detail on the sign-up page.** That case study includes commercial
  figures from an employer. All of it was already public on the original site,
  but a rebuild is a natural moment to decide that deliberately rather than
  carrying it over by default.
- **The M2030 page** is thin compared with the Stockopedia work — three
  paragraphs covering nearly three years. Structurally faithful, but it is where
  more effort would pay off most.
