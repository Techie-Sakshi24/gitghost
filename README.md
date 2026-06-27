\# 👻 GitGhost



> \*\*Your GitHub profile deserves a better README than "passionate developer who loves to code."\*\*



GitGhost scans your GitHub profile — repos, languages, stars, bio — and generates a cinematic, personality-driven README.md using Claude AI. No templates. No cringe. Just a README that actually sounds like you.



!\[Python](https://img.shields.io/badge/Python-3.8%2B-3776ab?logo=python\&logoColor=white)

!\[Claude AI](https://img.shields.io/badge/Powered%20by-Claude%20AI-orange)

!\[License](https://img.shields.io/badge/License-MIT-green)

!\[Stars](https://img.shields.io/github/stars/Techie-Sakshi24/gitghost?style=social)



\## What it does



GitGhost hits the GitHub API, pulls your real data — top repos, languages, stars, account age, bio — builds a profile summary, and sends it to Claude with a carefully crafted prompt that explicitly bans phrases like "passionate developer", "always learning", and "team player".



The output is a README that reads like a person wrote it.



```bash

$ gitghost Techie-Sakshi24 --style cinematic --preview

```



\## Install



```bash

git clone https://github.com/Techie-Sakshi24/gitghost.git

cd gitghost

pip install -e .

```



\## Setup



You need two things:



\*\*1. Anthropic API key\*\* — get one free at \[console.anthropic.com](https://console.anthropic.com)



```bash

export ANTHROPIC\_API\_KEY=sk-ant-...

```



\*\*2. GitHub token\*\* (optional but recommended — avoids rate limits)



```bash

export GITHUB\_TOKEN=ghp\_...

```



\## Usage



```bash

\# Generate README for any GitHub user

gitghost Techie-Sakshi24



\# Different styles

gitghost Techie-Sakshi24 --style minimal

gitghost Techie-Sakshi24 --style fun

gitghost Techie-Sakshi24 --style professional



\# Save directly to file

gitghost Techie-Sakshi24 -o README.md



\# Preview in terminal

gitghost Techie-Sakshi24 --preview



\# Full example

gitghost Techie-Sakshi24 --style cinematic -o README.md --preview

```



\## Styles



| Style | Vibe |

|---|---|

| `cinematic` | Dramatic, punchy, like a movie trailer for a developer |

| `minimal` | Clean, no fluff, just the essentials |

| `fun` | Witty, jokes welcome, personality first |

| `professional` | Human but polished — resume-ready with a voice |



\---



\## How it works



1\. \*\*GitHub API\*\* — fetches profile, repos, languages, stars, forks, topics

2\. \*\*Profile summary\*\* — builds structured text from raw data

3\. \*\*Claude Sonnet\*\* — generates README with a prompt that enforces personality and bans generic phrases

4\. \*\*Output\*\* — raw markdown, pipe it anywhere or save with `-o`



\## Requirements



\- Python 3.8+

\- Anthropic API key

\- GitHub token (optional)



\## Contributing



PRs welcome. Ideas:



\- \[ ] Auto-commit generated README to your profile repo

\- \[ ] Style presets for specific roles (ML engineer, frontend dev, etc.)

\- \[ ] Regenerate sections individually

\- \[ ] GitHub Actions workflow — auto-update README weekly



\## License



MIT — use it, fork it, build on it.



Made by \[Sakshi Kale](https://github.com/Techie-Sakshi24) · Powered by \[Claude AI](https://anthropic.com)

