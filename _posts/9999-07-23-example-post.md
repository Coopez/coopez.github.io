---
title: "Example blog post (delete me)"
date: 9999-07-23
excerpt: "A template post showing how the blog cards work. Delete this once you write a real one."
# thumbnail: /images/posts/my-image.png   # optional; create images/posts/ and drop a file there
published: false   # kept as a template, hidden from the site. Set to true (and give a real date) to publish.
---

This is an example post so you can see the blog card format. Delete it once you
have a real one to show.

**How posts work:**

- Put each post in `_posts/`, named `YYYY-MM-DD-slug.md` (the date drives the
  order). To keep a draft hidden, set `published: false` in its front matter.
- The card on the [Blog page](/year-archive/) uses this post's `title`, `date`,
  `excerpt`, and optional `thumbnail`.
- Add `thumbnail: /images/posts/xxx.png` to the front matter to give the card an
  image (make an `images/posts/` folder and drop the file there). Without one,
  the card is text-only.
- Everything below the front matter is normal Markdown.
