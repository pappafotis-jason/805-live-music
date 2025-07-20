# 8:05 LIVE

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)  
[![GitHub issues](https://img.shields.io/github/issues/pappafotis-jason/805-live-music)](https://github.com/pappafotis-jason/805-live-music/issues)  
[![GitHub forks](https://img.shields.io/github/forks/pappafotis-jason/805-live-music)](https://github.com/pappafotis-jason/805-live-music/network)

## Overview
8:05 LIVE is an open-source, community-powered calendar and map for discovering live music events worldwide. Starting as a pilot in Panama City Beach, FL, it empowers musicians, venues, and fans to submit and find gigs effortlessly. Inspired by the frustration of fragmented listings and Sammy Hagar's "It's 8:05, it's time to rock," we're building a decentralized platform—city by city—for the ultimate live music discovery tool.

- **Key Features**: Interactive maps via Leaflet.js and OpenStreetMap, geospatial queries for "shows near me," and easy event submissions.
- **Philosophy**: Decentralized nodes per city, GPLv3-licensed, FOSS-aligned with clean, Pythonic aesthetics (e.g., Linux-like simplicity).
- **Parent Org**: RATlab Records (Rogue Artist Tribe)—decentralized music funding and community.
- **Domain**: [805LiveMusic.com](https://805livemusic.com) (coming soon).

If you're a dev who loves live music and open-source, this is your jam: Fix bugs, add integrations (e.g., Bandsintown), or moderate your local scene!

## Tech Stack
- **Frontend**: Django Templates, Tailwind CSS, HTMX (for light interactivity), Leaflet.js + OpenStreetMap (interactive maps).
- **Backend**: Python + Django, Gunicorn (WSGI server).
- **Database**: PostgreSQL + PostGIS, Django ORM, Redis (caching).
- **Infra/DevOps**: Hostinger VPS (Ubuntu-based hosting), Nginx (web proxy), GitHub Actions (CI/CD).

Optional future: Django Channels (real-time), Celery (background jobs), Alpine.js (light client-side).

## Installation & Setup
### Prerequisites
- Python 3.12+
- PostgreSQL with PostGIS extension
- Redis
- Git
- Hostinger VPS (KVM 2 plan recommended)

### Steps
1. Clone the repo: `git clone https://github.com/pappafotis-jason/805-live-music.git`
2. Install dependencies: `cd 805-live-music && python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`
3. Set up `.env` file: Add DB credentials, Redis URL, etc. (use `env.example` as template).
4. Database: Run `python manage.py makemigrations && python manage.py migrate`
5. Start dev server: `python manage.py runserver` (runs on http://localhost:8000)

For production: Deploy to Hostinger VPS—SSH in, install stack (e.g., PostgreSQL, Redis, Nginx), set up Gunicorn/Nginx services, and point your domain.

## Usage
- Submit events via the form (e.g., venue, date, location).
- Browse the map/calendar for tonight's shows.
- Interactive: Explore events on the Leaflet map with pins, popups, and filters.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We welcome PRs—start with "good first issues"!

## Roadmap
- Phase 1: Panama City Beach pilot (manual inputs, basic map/calendar).
- Phase 2: Multi-city expansion with moderators.
- Phase 3: Integrations (Eventbrite, etc.).
- Phase 4: Alerts, profiles, ticketing.
- Phase 5: Syndication tools.

## License
GNU General Public License v3 (GPLv3). See [LICENSE](LICENSE).

## Get Involved
- Issues/Discussions: Report bugs or suggest features.
- Sponsor: Via GitHub Sponsors or Open Collective.
- Contact: @jasonpappafotis on X or email jason@ratlabrecords.com.

"Check the hands on the clock. It's 8:05, it's time to rock!" -Sammy Hagar 🎸
