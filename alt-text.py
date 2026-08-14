#!/usr/bin/env python3
"""
Alt text for every image on the site, keyed by filename.

Three confidence levels:
  SEEN    — I looked at the actual image file; these should be accurate.
  CONTEXT — derived from the caption, section heading and filename. Very likely
            right, but worth a glance.
  REVIEW  — I could not see the image and the context was thin. These need
            checking. They are listed at the bottom of the build report.

Alt text describes what the image *shows*, not what it is called. It should
make sense read aloud in place of the image. Where a caption already describes
the image, the alt text says something complementary rather than repeating it.
"""

SEEN = {
    "today-4-3.png":
        "A laptop showing the redesigned Stockopedia Today dashboard, with market "
        "charts, research lists and stock movers.",
    "plans-4-3-1.png":
        "The Stockopedia subscription page offering UK, UK and US, or custom "
        "region plans side by side.",
    "process-collage-4-3-1.png":
        "A collage of design references: books including Creativity Inc, Sprint, "
        "Nudge and Drive, alongside double-diamond and diverge-converge diagrams.",
    "process-collage-1.png":
        "A collage of design references: books including Creativity Inc, Sprint, "
        "Nudge and Drive, alongside double-diamond and diverge-converge diagrams.",
    "design-guide-4-3.png":
        "Two pages from the Stockopedia design guide: a core colour palette of "
        "swatch tables, and documentation for breadcrumb and pager components.",
    "m2030-4-3.png":
        "The Manufacture 2030 platform dashboard, showing progress statistics, a "
        "topics list, an activity feed and a members panel.",
    "tut-title-4-3.png":
        "The title illustration for the Wordsmith eBook 'Was Tutankhamen "
        "Killed?', showing a gold death mask flanked by two cartoon detectives.",
    "persona-title-4-3.png":
        "The ideal archetype journey diagram: a quadrant chart with arrows moving "
        "investors from active and discretionary towards passive and systematic.",
    "archetype-journey-title-4-3-1.png":
        "The ideal archetype journey diagram: a quadrant chart with arrows moving "
        "investors from active and discretionary towards passive and systematic.",
    "architypes.png":
        "A quadrant chart of four investor archetypes — Trader, Hunter, Farmer "
        "and Owner — plotted against active-passive and systematic-discretionary "
        "axes, each with a representative investor and playing-card suit.",
    "avg-events-by-persona-type-prev-6m-excluding-novice.png":
        "A bar chart comparing average site events by persona type over six "
        "months, excluding novice investors.",
}

CONTEXT = {
    # --- Stockopedia redesign ---------------------------------------------
    "v1-home-edited.png":
        "The homepage of the in-flight redesign, before user testing.",
    "kohana-home-timer.png":
        "The homepage of the live Stockopedia site as it stood before the "
        "redesign.",
    "feature-usage-unique-views.png":
        "A chart of unique views per feature, showing a long tail of features "
        "with very low usage.",
    "redesign-wire-1.png":
        "A wireframe of the proposed site structure, produced at the end of the "
        "design sprint.",
    "desktop-today-1.png":
        "The redesigned Today page on desktop.",
    "desktop-folios.png":
        "The redesigned Folios page on desktop.",
    "reports-laptop.png":
        "A Stockopedia stock report shown on a laptop.",

    # --- Sign up & acquisition --------------------------------------------
    "kohana-plans-1.png":
        "The original subscription plans page, with its complex pricing model.",
    "subscriptions-1.png":
        "A breakdown of subscribers by region.",
    "folio-count-1.png":
        "A chart showing how many portfolios subscribers create.",
    "superfans-1.png":
        "Usage data identifying the most active subscribers.",
    "screen-usage-data-1.png":
        "Usage data for the Screens feature.",
    "1-edited.png": "Design variant one, step one: selecting a plan.",
    "2-edited.png": "Design variant one, step two: selecting investment regions.",
    "3-edited.png": "Design variant one, step three: creating an account.",
    "4-1-edited.png": "Design variant one, step four: entering payment details.",
    "5-edited.png":
        "Design variant one, step five: confirmation and choosing an investor "
        "type.",
    "6-edited.png": "The Stockopedia home page after sign-up is complete.",
    "1-1-edited.png": "Design variant two, step one: selecting a plan.",
    "2-1-edited.png": "Design variant two, step two: creating an account.",
    "3-1-edited.png": "Design variant two, step three: entering payment details.",
    "4-2-edited.png":
        "Design variant two, step four: confirmation and choosing an investor "
        "type.",
    "5-2-edited.png":
        "Design variant two, step five: selecting investment regions.",
    "desktop-plans.png": "The refined subscription plans page on desktop.",
    "ab-test.png": "Results from the A/B test of the two sign-up variants.",

    # --- Design system ----------------------------------------------------
    "colour-palette-1.png":
        "The Stockopedia colour palette, documented as swatch tables with usage "
        "rules.",
    "breadcrumb-pager.png":
        "Design system documentation for the breadcrumb and pager components.",
    "typography-1.png":
        "The Stockopedia type scale, documented with sizes and usage.",
    "global-nav-desktop.png":
        "The global navigation component as designed for desktop.",
    "iphone13-today.png": "The Today page on mobile.",
    "desktop-screens.png": "The Screens page on desktop.",
    "iphone13-screens.png": "The Screens page on mobile.",
    "iphone13-folios.png": "The Folios page on mobile.",
    "kohana-discuss.png":
        "The discussion feature on the original Stockopedia site.",
    "kohona-watchlist.png":
        "The watchlist on the original Stockopedia site.",
    "kohana-valuation-tool.png":
        "The valuation tool on the original Stockopedia site.",
    "kohana-screener-1592246240-e1728317427607.png":
        "The stock screener on the original Stockopedia site.",
    "v1-folio-overview-2872731197-e1728317535980.png":
        "The portfolio overview in the first version of the redesign.",
    "v1-home-3023164958-e1728317543891.png":
        "The home page in the first version of the redesign.",
    "v1-transaction-modal-2503138583-e1728317551408.png":
        "The transaction dialog in the first version of the redesign.",
    "v1-stockchecker-552173400-e1728317561528.png":
        "The StockChecker in the first version of the redesign.",

    # --- M2030 and 2degrees -----------------------------------------------
    "login-tablet.png":
        "The Manufacture 2030 login screen on a tablet, with custom "
        "illustration.",
    "m2030-step-1.png":
        "Manufacture 2030 onboarding, step one: setting up a facility.",
    "m2030-step-2-1.png":
        "Manufacture 2030 onboarding, step two: entering energy spend.",
    "m2030-step-3-1.png":
        "Manufacture 2030 onboarding, step three: selecting efficiency actions.",
    "action-detail-1440-1.png":
        "The detail view for an efficiency action on the Manufacture 2030 "
        "dashboard.",
    "rbs-wireframe.png":
        "A low-fidelity wireframe for a 2degrees community homepage.",
    "rbs-community-1440.png":
        "The finished RBS sustainable community homepage.",
}

# Images I could not see and could not confidently describe from context.
REVIEW = {
    "board-large-edit-141866557-e1728408455418.jpg":
        "A wall of notes and sketches from the design sprint.",
    "img_1965-1406614185-e1728408467562.jpg":
        "The team working together during the design sprint.",
    "img_1980-3175015336-e1728408487396.jpg":
        "The team working together during the design sprint.",
    "img_1994-2739410672-e1728408550975.jpg":
        "The team working together during the design sprint.",
    "screenshot-2024-09-16-at-13.34.11.png":
        "A quantitative scoring table comparing task completion between the live "
        "site and the new wireframe.",
    "investor-mag.png":
        "Stockopedia featured in an investment magazine.",
    "money-week-award.jpg":
        "The MoneyWeek award won by Stockopedia.",
    "gmg-winner.png":
        "An industry award won by Stockopedia.",
    "screen-shot-2014-08-18-at-09.20.34.png":
        "A page from the Wordsmith non-fiction eBook series.",
    "screen-shot-2014-08-18-at-09.21.46.png":
        "A page from the Wordsmith non-fiction eBook series.",
    "screen-shot-2014-08-18-at-09.27.14.png":
        "A page from the Wordsmith non-fiction eBook series.",
    "screen-shot-2014-08-18-at-09.28.28.png":
        "A page from the Wordsmith non-fiction eBook series.",
    "screen-shot-2014-08-18-at-09.48.46.png":
        "A page from the Wordsmith non-fiction eBook series.",
    "screen-shot-2014-08-18-at-09.48.54.png":
        "A page from the Wordsmith non-fiction eBook series.",
    "screen-shot-2014-08-18-at-09.49.06.png":
        "A page from the Wordsmith non-fiction eBook series.",
}

ALT = {**SEEN, **CONTEXT, **REVIEW}
