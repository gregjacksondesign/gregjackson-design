# Handover

Context for continuing this project in Cowork or Claude Code. Read this and
`README.md` first.

---

## What this is

A static rebuild of Greg Jackson's WordPress portfolio (`gregjackson.design`) in
Astro. The WordPress Business plan cost £240/year; this costs nothing to host.

Greg is a designer. The portfolio needs to look like a designer made it, because
that is literally what it is evidence of — the craft of the site is part of the
work being shown. He has strong opinions and should be treated as the design
authority. Push back on his ideas if you have reason to, but do not overrule his
aesthetic judgement.

**The brief was a faithful rebuild, not a redesign.** The original design is
reproduced deliberately, including choices you might otherwise question. Do not
"improve" the visual design unless asked.

---

## Deployment

**Live at https://gregjackson-design.pages.dev** (14 August 2026).

- Repo: `github.com/gregjacksondesign/gregjackson-design`, public, branch `main`.
- Cloudflare Pages, connected to Git. Framework preset Astro, build command
  `npm run build`, output `dist`. `.nvmrc` pins Node 22.
- Every push to `main` rebuilds automatically. Branches get preview URLs.
- **Custom domain is live.** Both `gregjackson.design` and
  `www.gregjackson.design` are attached to the Pages project, Active, with SSL
  issued. Verified serving the static site (including deep links like
  `/experience/`) on 14 August 2026. Cloudflare wrote the DNS records itself —
  the "Complete DNS setup" panel asking for a manual CNAME appeared briefly but
  resolved on its own within a minute or two, so don't rush to add records by
  hand if you ever re-do this.
- WordPress was never on this domain — it lives at
  `gregjacksondesign.wpcomstaging.com`. So going live involved no cutover and no
  downtime; the domain went from resolving to nothing to serving the new site.
- `www` serves the site directly rather than redirecting to the apex, so both
  hostnames return identical content. Canonical tags point at
  `https://gregjackson.design` (from `site` in `astro.config.mjs`), which is what
  tells search engines which one counts. Optional tidying: a Cloudflare redirect
  rule to send `www` → apex with a 301.

Note `astro.config.mjs` sets `site: 'https://gregjackson.design'`, so canonical
URLs on the `.pages.dev` build already point at the real domain. That is correct
and stops the preview being indexed as a duplicate — don't "fix" it.

---

## Where things stand

**Done:**

- All 10 pages built and verified against the WordPress originals, sentence by
  sentence. Zero content lost.
- Design tokens extracted verbatim from the WordPress theme into
  `src/styles/tokens.css`.
- Greg's hand-written CSS ported: nav underline wipe, button fill, project image
  overlay at 0.6, scroll-driven card reveals via `animation-timeline: view()`.
- Alt text written for all 78 images.
- Heading levels normalised so nothing skips; one `h1` per page.
- 108 images and 4 PDFs pulled from WordPress by SFTP and in place.
- Domain re-registered at Namecheap, DNS delegated to Cloudflare (nameservers
  `arushi`/`sergi.ns.cloudflare.com`). Cloudflare zone is empty by design.

**Done in the 14 August session — design system rework:**

- **Spacing rebuilt as one system.** The WordPress 25px scale, and an interim
  `--s-*` scale, are both gone. Now two tiers in `tokens.css`: fixed insets
  (`--space-4` … `--space-48`, in rem, on a 4px grid — Greg's working scale) and
  three fluid layout tokens (`--gap-block` 32→80, `--gap-inner` 24→48,
  `--page-gutter` 20→72) that interpolate between 375px and 1440px. Read the
  comments there before adding anything.
- **Fixed a real bug:** structural spacing used `padding-block`, so adjacent
  blocks each contributed their own and padding doesn't collapse — gaps between
  Experience roles were 250px instead of 80px. All structural spacing is now
  single-direction (`.x + .x { margin-top }`).
- **Breakpoints consolidated to two**, `48rem` and `64rem`, all `min-width`, all
  rem. Documented at the top of `tokens.css`. Was five values in a mix of px and
  rem, min- and max-width.
- **Nav:** LinkedIn is now the `[in]` mark rather than a text label — it's an
  outbound link, and four text labels wouldn't fit one row at 375px. Tap targets
  raised from ~26px to ~50px. Header is sticky from `48rem` up.
- **Case-study steps** now use the `.tag`/`.meta-row` label-column layout, and
  step titles render as dark serif at h3 size (they were 64px red Agbalumo).
- **Blockquotes** are filled panels at body size, measured off the original.
- Production build verified clean: 10 pages, one `h1` each, no heading skips, no
  dead tokens in the built CSS.

**Not done:**

- Greg has not yet reviewed most pages visually.
- Mobile header is not sticky. Making it so needs the header compacted first —
  hiding the `gregjackson.design` wordmark and dropping the nav to 14px gets
  logo and nav onto one row at 375px (~326px of ~335px available) and the header
  to ~62px. That's two visual changes, so it's Greg's call.

---

## Follow-up: image weight

**Not urgent, but do it before the link goes to anyone who matters.**

`public/images` is **56MB across 108 files** — 15 over 1MB, largest 5.2MB
(`board-large-edit-141866557-e1728408455418.jpg`). The design-sprint gallery on
`/site-redesign/` alone pulls roughly 16MB in one go, on the page a hiring
manager is most likely to read properly. `loading="lazy"` softens this but
doesn't fix it.

Resizing to sensible dimensions and converting to WebP should get the total under
about 5MB with no visible quality loss. Nothing is broken as-is — Cloudflare
Pages' per-file limit is 25MB and every file is well inside it.

Note `IMAGE-MANIFEST.md` is **stale**: it claims "12 of 75 images are in place,
63 still to add" with every box unticked. That is wrong — all 108 images and all
4 PDFs are present on disk. The doc was never updated after the SFTP pull.

---

## Resolved — WordPress renewal

**No longer urgent.** WordPress's dashboard gave conflicting renewal dates
on 12 August (Active Upgrades said 13 August 2026; billing history and a
"My Home" banner both pointed to 10 September 2026 instead — never fully
reconciled). Greg sidestepped the ambiguity by removing the payment method
on file, so the plan can no longer auto-renew and will simply lapse when
its current paid term ends (around 10 September 2026, per the "expires in
X days" figure, which is now what the dashboard shows with no card
attached). All images and PDFs have already been retrieved into this
project, so there's nothing to lose when it lapses.

---

## Known issues and gotchas

**Heading levels vs. visual size are deliberately decoupled.** On the original,
inner page titles were `h2` — which in this design means red Agbalumo display
face. Semantically a page title should be `h1`. So `CaseStudy.astro` renders
`<h1 class="type-h2">`: correct outline, original appearance. The `.type-h1`
through `.type-h4` utilities in `global.css` exist for this. **If you change a
heading's level, carry the `type-` class across or the design will break.** This
already caused one regression.

**`h2` is the site's signature.** Display face (Agbalumo), brick red
(`#b6463b`), forced. It is unusual and intentional.

**All headings are weight 400, and `strong` is also weight 400.** Deliberate,
from the original. Do not "fix" this.

**Images are flat in `public/images/`,** not in WordPress's year/month folders.
Filenames match the originals so references resolve.

**Fonts come from npm (Fontsource), not Google.** IBM Plex Sans, Literata,
Agbalumo — all OFL, all self-hosted at build time. Do not add a Google Fonts
link.

**URLs deliberately match the old site** (`/site-redesign/`, `/about-me/`, etc.)
so existing links and CV references keep working. Do not rename routes.

---

## Open questions for Greg

1. **The Agbalumo `h2`s.** Three type families do headline work across two
   registers, and Agbalumo is the outlier. Faithfully reproduced. Switching
   `--font-display` to `var(--font-serif)` in `tokens.css` is a one-line change.
   His call, and he has not made it yet.

2. **Commercial detail on `/sign-up-and-acquisition/`.** That case study includes
   commercial figures from an employer. All of it was already public on the
   original site, but whether it stays is a deliberate decision for Greg rather
   than an assumption to carry forward.

3. **`/m2030-and-2degrees/` is thin** — around 200 words covering nearly three
   years of work, versus 1,700 for the Stockopedia redesign. Structurally
   faithful, but the weakest page and where effort would pay off most.

4. **Fifteen images have alt text written without seeing the file** — the design
   sprint photos and the Wordsmith screenshots. Marked `REVIEW` in `alt-text.py`.
   Worth checking, especially as his redesign case study makes a point of
   accessibility.

5. **Two `>`-only paragraphs on About me** were dropped as artefacts. He may want
   them back.

---

## Next steps, in order

1. **Greg reviews every page** against the original at
   `gregjacksondesign.wpcomstaging.com` while the WordPress plan is still live.
   He is the only one who can judge fidelity — he has already caught one bug this
   way.
2. **Fix whatever he finds.**
3. **Put it in Git and deploy to Cloudflare Pages** (settings in `README.md`).
   Test thoroughly on the free `.pages.dev` URL.
4. **Only then** point `gregjackson.design` at it via Custom domains. Cloudflare
   adds the DNS records automatically since it already runs the zone.
5. Add `www.gregjackson.design` as well.

---

## Verifying changes

There is a habit worth keeping from the build: **check the output, do not assume
it worked.** Every bug found so far was found by comparing built HTML against the
original rather than trusting the code. `npm run build`, then parse `dist/` and
check counts, heading order, alt text and links.
