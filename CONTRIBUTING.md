# Contributing to 8:05 LIVE

Thanks for your interest in contributing to 8:05 LIVE! We're building a decentralized live music discovery app, and your help—as a dev, musician, or fan—will make it rock harder. Follow these guidelines to keep things smooth.

## How to Contribute
1. **Fork the Repo**: Click "Fork" on GitHub to create your copy.
2. **Clone Locally**: `git clone https://github.com/yourusername/805-live-music.git`
3. **Create a Branch**: `git checkout -b feature/your-feature` (use descriptive names like "fix-map-zoom" or "add-sms-alerts").
4. **Make Changes**: Follow the tech stack (Django frontend templates, Python backend). Add tests if applicable.
5. **Commit**: Use clear messages, e.g., "Add event submission view with validation".
6. **Push**: `git push origin feature/your-feature`
7. **Open a Pull Request (PR)**: From your fork, create a PR to the main repo. Reference any issues (e.g., "Fixes #5").

## Code Standards
- **Style**: Follow PEP 8; use Black for formatting and Flake8 for linting (setup via `pip install -r requirements-dev.txt` and run `black .`).
- **Tests**: Add unit tests with Django's TestCase or pytest for new features.
- **Commits**: Conventional Commits encouraged (e.g., "feat: add map clustering").
- **Accessibility**: Ensure UI is mobile-friendly and i18n-ready.

## Good First Issues
Look for labels like "good first issue" or "help wanted" in Issues. Start small: Docs updates, bug fixes, or UI tweaks.

## Roles
- **Moderators**: Interested in curating a city instance? Mention in your PR or open an issue.
- **Ideas**: Use Discussions for feature brainstorming.

## Code of Conduct
See [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md). Be kind and inclusive!

Questions? Open an issue or ping @jasonpappafotis on X.
