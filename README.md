# Rainaldus

## Cosmere Reading Order

An interactive guide to reading Brandon Sanderson's Cosmere, in `site/`.

- **Star map**: every book arranged by world, with lines showing which books set up which.
- **Reading path**: the recommended order in three phases, with a checklist and an "Up next" pointer.
- **Before you start**: each book lists the books that set it up and flags any you haven't read.
- Connection notes stay hidden until you choose to show them, to avoid spoilers.

Reading progress is saved in the browser.

### Run it locally

The page loads `data.json`, so serve the folder instead of opening the file directly:

```
python3 -m http.server -d site 8000
```

Then open http://localhost:8000.

### Deploy

`.github/workflows/pages.yml` publishes `site/` to GitHub Pages on every push to `main`.
Turn it on once under **Settings → Pages → Source: GitHub Actions**.

### Updating the book data

`site/data.json` is generated from the 17th Shard project's `public/data.json`:

```
python3 scripts/build_data.py path/to/reading-order/public/data.json site/data.json
```

The script flattens the data, repairs broken links and applies the release-date corrections listed at the bottom of the script.
Edit `site/data.json` directly for small fixes.

### Credits

Book data comes from the [17th Shard reading order](https://github.com/17thshard/reading-order) (MIT licence, © 2019 Marvin Rösch).
Notes link to the [Coppermind](https://coppermind.net). This is an unofficial fan project.
