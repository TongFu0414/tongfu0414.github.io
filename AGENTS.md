# Tong Fu website guide

This repository is Tong Fu's (付彤) Jekyll/GitHub Pages academic homepage. Its public address is `https://tongfu0414.github.io/`. Keep the existing layout, typography, spacing, themes, and interactions; make content changes with minimal implementation changes.

## Content and evidence

- `about.md` is the English homepage at `/`; `zh.md` is its Chinese counterpart at `/zh/`. Keep their facts, publication states, and review items aligned.
- `_config.yml` controls identity, navigation, contact links, and site metadata. The GitHub account is `TongFu0414`; the contact email is `futong4024@163.com`.
- Tong Fu studied Computer Science and Technology at Taiyuan University of Technology, 2020–2024. Do not describe an application target as a current affiliation.
- QCVS: first author; submitted to ICASSP 2027. CFMS: third author; accepted at PRCV 2026 Main Track. Do not upgrade submission to acceptance or acceptance to publication without evidence.
- Individual paper contributions, final citations, current review status, employment roles and dates, degree title, tools, language scores, and a personal photo need confirmation. Mark uncertain details with `.needs-confirmation`; skills nodes use `needs_confirmation: true`. Explain the uncertainty in text as well as color.
- Do not infer personal engineering contributions from company product descriptions. Keep submission passwords, full transcripts, student/government identifiers, internal material, and unapproved full manuscript files out of the public repository.
- There is no GitHub Activity widget or automatic contribution-chart workflow. Retain only the GitHub profile link.
- The user explicitly requested a fresh independent repository. Do not reattach upstream history or add an upstream remote. Retain the applicable theme/library license notices.

## Structure and presentation

- `_includes/author-profile.html`, `masthead.html`, and `head.html` render identity, navigation, and metadata.
- `_data/skills.yml` supplies the existing interactive skills map; `_data/learning_resources.yml` supplies the existing resource accordions.
- `assets/research/` contains diagrams rendered from the supplied manuscripts. Do not invent benchmark charts or change diagram meaning.
- `_layouts/`, `_sass/`, and `assets/js/` retain the existing theme. Preserve the masthead's `clamp(20rem, 30vw, 28rem)` footprint and author-name typography. Review highlighting is the only added visual treatment.
- `local/` is ignored by Git and excluded from Jekyll. It contains private source archives, temporary figure renders, and local build scripts. `docs/` and `scripts/` are also excluded from the published site.

## Build and validation

Install dependencies with `bundle install`, then run:

```text
bundle exec jekyll build --strict_front_matter
python scripts/verify_site.py
git diff --cached --check
```

When working in the configured Windows environment, Ruby/Bundler run in the Ubuntu WSL distribution. Set `BUNDLE_PATH` to the existing user-local dependency directory before invoking Bundler. Keep `Gemfile.lock` tracked.

When browser preview is available, inspect the English homepage, Chinese page, and 404 page at desktop and mobile widths in both themes. Check navigation, language switching, image previews, research details, review highlights, skills-map controls, and every local asset link. If the preview connection is unavailable, document that limit, continue the build and source/link checks, and do not claim browser or mobile interaction tests passed.

## Publishing

The only deployment target for this task is `TongFu0414/tongfu0414.github.io` on GitHub Pages. Preserve the public repository's audience. Create the first commit only after the Tong Fu content and checks are ready, then verify the remote Pages build and actual site URL.
