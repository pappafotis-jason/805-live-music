# 8:05 LIVE

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)  
[![GitHub issues](https://img.shields.io/github/issues/pappafotis-jason/805-live-music)](https://github.com/pappafotis-jason/805-live-music/issues)  
[![GitHub forks](https://img.shields.io/github/forks/pappafotis-jason/805-live-music)](https://github.com/pappafotis-jason/805-live-music/network)

## Overview
8:05 LIVE is an open-source, community-powered calendar and map for discovering live music events worldwide. Starting as a pilot in Panama City Beach, FL, it empowers musicians, venues, and fans to submit and find gigs effortlessly. Inspired by the frustration of fragmented listings and Sammy Hagar's "It's 8:05, it's time to rock," we're building a decentralized platform—city by city—for the ultimate live music discovery tool.

- **Key Features**: Interactive Google Maps with custom pins, real-time updates via Socket.IO, geospatial queries for "shows near me," and easy event submissions.
- **Philosophy**: Decentralized nodes per city, GPLv3-licensed, FOSS-aligned with clean aesthetics (e.g., Material Design).
- **Parent Org**: RATlab Records (Rogue Artist Tribe)—decentralized music funding and community.
- **Domain**: [805LiveMusic.com](https://805livemusic.com).

If you're a dev who loves live music, this is your jam: Fix bugs, add integrations (e.g., Bandsintown), or moderate your local scene!

## Tech Stack
- **Frontend**: React + Next.js, Tailwind CSS, @react-google-maps/api, React Hook Form, next-intl (i18n), Framer Motion (optional).
- **Backend**: Node.js + Express, Socket.IO, Auth.js.
- **Database**: PostgreSQL + PostGIS, Prisma ORM, Redis (caching/real-time).
- **Infra/DevOps**: GCP (hosting), Vercel (frontend), GitHub Actions (CI/CD).

## Installation & Setup
### Prerequisites
- Node.js v18+
- PostgreSQL with PostGIS extension
- Google Maps API key (from GCP)
- Redis (optional for dev)

### Steps
1. Clone the repo: `git clone https://github.com/pappafotis-jason/805-live-music.git`
2. Install dependencies: `cd 805-live-music && npm install`
3. Set up `.env` file (copy from `.env.example`): Add DB URL, Google Maps key, etc.
4. Database: Run `npx prisma migrate dev` to set up schema.
5. Start dev server: `npm run dev` (runs on http://localhost:3000)

For production: Deploy backend to GCP Cloud Run, frontend to Vercel.

## Usage
- Submit events via the form (e.g., venue, date, location).
- Browse the map/calendar for tonight's shows.
- Real-time: New submissions update live for connected users.

## Contributing
See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines. We welcome PRs—start with "good first issues"!

## Roadmap
- Phase 1: Panama City Beach, FL, USA pilot (manual inputs, basic map/calendar).
- Phase 2: Multi-city expansion with moderators.
- Phase 3: Integrations (Eventbrite, etc.).
- Phase 4: Alerts, profiles, ticketing.
- Phase 5: Syndication tools.

## License
GNU General Public License v3 (GPLv3). See [LICENSE](LICENSE).

## Get Involved
- Issues/Discussions: Report bugs or suggest features.
- Sponsor: Via GitHub Sponsors or Open Collective.
- Contact: @pappafotis-jason on X or email jason@ratlabrecords.com.

Let's rock at 8:05! 🎸
