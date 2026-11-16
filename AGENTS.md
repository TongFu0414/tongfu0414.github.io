# Tong Fu website guide

This repository is Tong Fu's (付彤) Jekyll/GitHub Pages academic homepage. Its public address is `https://tongfu0414.github.io/`. Keep the existing layout, typography, spacing, themes, and interactions; make content changes with minimal implementation changes.

## Content and evidence

- `about.md` is the English homepage at `/`; `zh.md` is its Chinese counterpart at `/zh/`. Keep their facts, publication states, and review items aligned.
- `_config.yml` controls identity, navigation, contact links, and site metadata. The GitHub account is `TongFu0414`; the contact email is `futong0414@163.com`, matching the current user-designated CV.
- The user's application PDF is the sole canonical CV. The public `assets/CV_TongFu.pdf` must be an unchanged copy of it; do not create an alternative website CV.
- Use the user-provided `images/me.jpg` avatar with the reference theme's circular treatment. The user states the profile location is Hangzhou. The WeChat contact opens the existing modal and displays `Ft_Be_admitted_to` as text.
- The sidebar names Taiyuan University of Technology (211) and says Tong Fu is seeking MPhil opportunities for Fall 2027. Avoid replacing this with a research-keyword/applicant tagline. School-name parentheses display `211`, not an abbreviation.
- Tong Fu studied Computer Science and Technology at Taiyuan University of Technology, 2020–2024. Do not describe an application target as a current affiliation.
- The latest canonical CV, updated during this work on 2026-11-15, states QCVS is under review at ICASSP 2027 with co-first authorship; these entries are no longer highlighted in that CV. CFMS is accepted at PRCV 2026 Main Track and Tong Fu is third author. Do not upgrade review to acceptance or acceptance to publication without evidence.
- The user authorizes removing experience review highlighting after checking local materials, without another review gate. Roles, dates and Hangzhou locations agree between the current canonical CV and the supplied work-experience draft; display them normally. Describe product/data requirements, model evaluation and human review conservatively, without turning company capabilities into personal algorithm-development claims or adding unsubstantiated metrics. Source consistency is not an independent employer verification.
- The updated education line is B.Eng. in Computer Science without a review highlight. The user requested removal of red review text from the research/publications sections, the introductory explanation of red highlighting, and the paper author/status/link reminders. Keep unresolved paper details in internal notes instead of restoring those public notices.
- Keep both paper citations in the same author/title/venue/status format. Use the current CV's co-first-author marker for QCVS; do not invent its complete author list, a DOI, a public manuscript link, or an individual contribution statement.
- On 2026-11-16, the user explicitly authorized publishing both supplied manuscripts unchanged at `assets/papers/QCVS.pdf` and `assets/papers/CFMS.pdf`. The user subsequently changed paper-title destinations to the corresponding project overview figures: the CV links to `/zh/#qcvs-overview` and `/zh/#cfms-overview`; each homepage language links its publication titles to its own `#qcvs-overview` and `#cfms-overview` figures. This authorization does not include submission screenshots or access credentials.
- Encode an asterisk inside inline superscript tags as `&#42;`. A literal asterisk can start Markdown emphasis and swallow the closing superscript tag. Check generated superscripts contain only their marker and venue emphasis contains only the venue.
- The user authorizes drafting the skills map around large language models without asking for confirmation of basic tools. Include Python, PyTorch, Git and related logically grouped skills; show TOEFL Certificate under English. Do not add scores, dates, proficiency ratings or certificate downloads that were not provided. Skills nodes should not carry confirmation labels.
- Do not infer personal engineering contributions from company product descriptions. Keep submission passwords, full transcripts, student/government identifiers, internal material, and unapproved full manuscript files out of the public repository.
- The user authorizes public certificate evidence links in the reference template's `[Evidence]` style. `assets/evidence/` contains six cropped, correctly oriented, redacted and flattened PDF copies for the five awards/certifications and comprehensive evaluation rank. Preserve the source originals privately; never replace these public copies with unredacted originals. Ranking evidence supports comprehensive evaluation only; the engineer-program certificate is coursework completion, not a degree certificate.
- There is no GitHub Activity widget or automatic contribution-chart workflow. Retain only the GitHub profile link.
- The user explicitly requested a fresh independent repository. Do not reattach upstream history or add an upstream remote. Retain the applicable theme/library license notices.

## Structure and presentation

- `_includes/author-profile.html`, `masthead.html`, and `head.html` render identity, navigation, and metadata.
- `_data/skills.yml` supplies the existing interactive skills map. `_data/learning_resources.yml` contains all 27 entries from the reference homepage's Foundations group, copied at the user's request. Label this section and its navigation link `Inspiring Articles` / `受启发的文章`; retain one fully expanded, ungrouped list with two cards per row.
- The masthead places the official Taiyuan University of Technology and Hikvision wordmarks in the reference logo position. Experience entries reuse the reference `experience-logos.html` include and organization/location, date, bold role/degree, and focus lines. Institution artwork and source URLs are recorded in `_data/experience_logos.yml`.
- `assets/research/` contains diagrams rendered from the supplied manuscripts. Do not invent benchmark charts or change diagram meaning.
- `_layouts/`, `_sass/`, and `assets/js/` retain the existing theme. Preserve the masthead's `clamp(20rem, 30vw, 28rem)` footprint, author-name typography, and original experience styles. The dual wordmark, text-based WeChat modal, and expanded two-column resource list are user-requested presentation changes.
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

After each requested change is complete and checked, commit and push it to the repository. The user explicitly requests pushing every time; no additional confirmation is needed.

The only deployment target for this task is `TongFu0414/tongfu0414.github.io` on GitHub Pages. Preserve the public repository's audience. Create the first commit only after the Tong Fu content and checks are ready, then verify the remote Pages build and actual site URL.
