// The seven projects shown on the homepage, in order.
//
// To add a project: add an object here and create the matching page in
// src/pages/. To reorder them, move them in this array. To remove one from the
// homepage without deleting the page, comment it out.
//
// `colour` refers to a tile colour token in tokens.css (blue | sage |
// light-mauve | orange | green | mauve | grey).
//
// `align` controls where the screenshot sits within its coloured tile, matching
// the original site: 'top' | 'center' | 'bottom'.

export const projects = [
  {
    title: 'Stockopedia redesign',
    href: '/site-redesign/',
    description:
      'When I joined Stockopedia, I was tasked with leading the redesign of the application that had been stuck in development for two years without any releases or user feedback.',
    image: '/images/today-4-3.png',
    alt: 'The redesigned Stockopedia dashboard, showing market data and rankings.',
    colour: 'blue',
    align: 'top',
  },
  {
    title: 'Sign up & acquisition',
    href: '/sign-up-and-acquisition/',
    description:
      'Could we increase average revenue per customer with usage based value metrics? Could simplifying the presentation of the plans, pricing structure and customer journey improve conversion rates?',
    image: '/images/plans-4-3-1.png',
    alt: 'Stockopedia subscription plans laid out as a pricing comparison.',
    colour: 'sage',
    align: 'bottom',
  },
  {
    title: 'Establishing a design process',
    href: '/design-process/',
    description:
      'When I joined Stockopedia, ideas went from the CEO to code without validation. My task was to create a repeatable, user-centred design process to consistently ensure high-quality results.',
    image: '/images/process-collage-4-3-1.png',
    alt: 'A collage of design process artefacts: workshop notes, sketches and wireframes.',
    colour: 'light-mauve',
    align: 'top',
  },
  {
    title: 'Stockopedia design system',
    href: '/stockopedia-design-guide/',
    description:
      'I created a design system to unify fragmented UIs across two sites, ensuring consistency, speeding up development, and enhancing the user experience with standardised components and guidelines.',
    image: '/images/design-guide-4-3.png',
    alt: 'Pages from the Stockopedia design guide showing components and colour rules.',
    colour: 'blue',
    align: 'top',
  },
  {
    title: 'Sustainable manufacturing',
    href: '/m2030-and-2degrees/',
    description:
      'I designed the Manufacture 2030 platform from an initial concept (driving corporate sustainability), developing brand guidelines, a component library and creating custom illustrations.',
    image: '/images/m2030-4-3.png',
    alt: 'The Manufacture 2030 platform interface with custom illustration.',
    colour: 'sage',
    align: 'center',
  },
  {
    title: 'Wordsmith, Pearson',
    href: '/wordsmith-non-fiction/',
    description:
      'I was tasked with designing a short non-fiction series that was better than a book. Content was explicitly designed to take advantage of all the extra features an eBook has to offer over a printed one.',
    image: '/images/tut-title-4-3.png',
    alt: 'A title page from the Wordsmith non-fiction eBook series.',
    colour: 'light-mauve',
    align: 'center',
  },
  {
    title: 'Investor personas',
    href: '/personas/',
    description:
      'I created 4 detailed investor personas at Stockopedia based on existing ‘Investor suits’. I utilised user interviews, survey and usage data to ensure they were accurate and representative.',
    image: '/images/persona-title-4-3.png',
    alt: 'Illustrated investor persona cards.',
    colour: 'blue',
    align: 'top',
  },
];
