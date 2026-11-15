# Tong Fu academic homepage

English: <https://tongfu0414.github.io/><br>
中文：<https://tongfu0414.github.io/zh/>

A Jekyll academic homepage for Tong Fu (付彤), covering multimodal reasoning, research manuscripts, industry experience, education, and contact information. Red review highlights mark details that require confirmation; they are documented in [the content review list](docs/content-review.md).

## Local development

With Ruby and Bundler installed:

```text
bundle install
bundle exec jekyll serve --host 127.0.0.1
```

To validate a static build:

```text
bundle exec jekyll build --strict_front_matter
python scripts/verify_site.py
```

Edit `about.md` and `zh.md` together. Site identity and navigation live in `_config.yml`; skills and reading resources live in `_data/`. The theme layout and interactions are retained. The MIT license in `LICENSE` applies to the reused theme code; research content retains its respective authorship.
