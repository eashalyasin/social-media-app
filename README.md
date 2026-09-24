# Social Media App

A full-stack social networking application with a **Next.js + TypeScript** frontend and a **Python** backend API. Users can browse public profiles, follow and unfollow each other, send and manage friend requests, and explore followers, following, and friends lists from a single tabbed screen.

**Live demo:** [social-media-app-ten-eta.vercel.app](https://social-media-app-ten-eta.vercel.app)

> **About the `[TODO]` markers:** anything tagged **[TODO]** below could not be confirmed from the repository when this README was drafted (backend internals, environment variable names, exact run commands). Replace each one with the real value, then delete this note.

---

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Architecture Overview](#architecture-overview)
- [Feature Deep Dive: Followers / Following / Friends Screen](#feature-deep-dive-followers--following--friends-screen)
- [API Reference](#api-reference)
- [Getting Started](#getting-started)
- [Environment Variables](#environment-variables)
- [Testing](#testing)
- [Deployment](#deployment)
- [Development History](#development-history)
- [Known Limitations](#known-limitations)
- [Contributing](#contributing)
- [License](#license)

---

## Features

### Profiles
- Public profile pages showing avatar, display name, `@username`, and live **follower / following / friend** counts.
- Posts shown on the profile, filtered by what the viewer is allowed to see. **[TODO: confirm visibility rules]**
- Profile counts refresh automatically when a follow or friend action happens elsewhere on the page, with no manual reload.

### Follow System
- One-way **Follow / Unfollow** between users.
- Follower and following counts update instantly after each action.

### Friend System
- Two-way friendships built on friend requests:
  - **Add friend** sends a request and the button changes to **Pending**.
  - Clicking **Pending** cancels the outgoing request.
  - **Unfriend** removes an existing friendship, protected by a confirmation dialog.
- **[TODO]** Describe the flow for accepting or declining incoming requests, if implemented.

### Followers / Following / Friends Screen
- One modal with three tabs (**Followers**, **Following**, **Friends**) instead of three separate popups.
- Every row has a context-aware relationship button (see the [deep dive](#feature-deep-dive-followers--following--friends-screen)).
- Each tab loads once and is cached, so switching tabs never refetches.

### Authentication
- The app is used as an authenticated experience (the list screen is only reachable from inside the logged-in app). 

---

## Tech Stack

| Layer | Technology | Notes |
|-------|------------|-------|
| Frontend framework | **Next.js** (React) | Inferred from the `.next/` entry in `.gitignore` and the Vercel deployment |
| Language | **TypeScript** | Components are `.tsx`; the `@/` import alias is used |
| HTTP client | **Axios** (likely) | API responses are consumed as `res.data`. **[TODO: confirm]** |
| Backend | **Python** | `venv/`, `__pycache__/` and `*.egg-info/` are ignored. **[TODO: confirm framework, e.g. FastAPI]** |
| Database | **pgadmin** | |
| CI | **GitHub Actions** | Workflows live in `.github/workflows/` |
| Frontend hosting | **Vercel** | |
| Backend hosting | **[TODO]** | |

---

## Project Structure

```
social-media-app/
├── .github/
│   └── workflows/           # GitHub Actions workflows [TODO: describe what they run]
├── backend/                 # Python API [TODO: document modules/routers/models]
├── frontend/                # Next.js application
│   └── src/
│       ├── components/
│       │   ├── FollowListModal.tsx   # Tabbed followers/following/friends modal
│       │   └── ProfileView.tsx       # Profile page (stats, posts, relationship button)
│       └── lib/
│           └── api.ts                # API client (e.g. profileAPI)
├── .gitattributes
├── .gitignore
└── README.md
```

The repository is a **monorepo**: `frontend/` and `backend/` are developed, installed, and run independently.

---

## Architecture Overview

```
┌────────────────────┐      HTTPS / JSON      ┌────────────────────┐
│  Next.js frontend  │ ─────────────────────▶ │   Python backend   │ ──▶  Database
│  (Vercel)          │ ◀───────────────────── │   REST API         │      [TODO]
└────────────────────┘                        └────────────────────┘
```

- **All network calls go through `frontend/src/lib/api.ts`**, which groups requests into namespaces such as `profileAPI` (`getPublicProfile`, `getFollowers`, `getFollowing`, `getFriends`). Components never build URLs by hand.
- **State is local and optimistic.** When a user follows, unfollows, or changes a friendship, the UI updates immediately and stays consistent with the server on the next fetch. This is the convention used across the app.
- **`ProfileView` owns the profile's counts**, and child components report changes upward through callbacks so stats never go stale.

---

## Feature Deep Dive: Followers / Following / Friends Screen

### Component contract

`FollowListModal` is a single component that owns all three tabs.

| Prop | Type | Purpose |
|------|------|---------|
| `userId` | `string` | Whose lists to display |
| `currentUserId` | `string` | The logged-in viewer, used to compute relationships |
| `initialType` | `'followers' \| 'following' \| 'friends'` | Which tab opens first |
| `onClose` | `() => void` | Closes the modal |
| `onRelationshipChanged` | `() => void` | Fires after any follow/friend action so the parent can refresh counts |

The three stat buttons on the profile header (Followers, Following, Friends) all open this same modal, each with a different `initialType`.

### Relationship button per row

The modal fetches the **viewer's own** following, friends, and outgoing-request lists once, then derives a state for every row:

| Viewer's relationship to the row's user | What is shown | On click |
|------------------------------------------|---------------|----------|
| Stranger | **Follow** (primary) plus a small add-friend icon | Follow, or send friend request |
| Following | **Following** | Unfollow |
| Request sent | **Pending** | Cancel the request |
| Friends | Green **Friends** pill that becomes red **Unfriend** on hover | Unfriend, after a confirm dialog |
| The viewer themself | No button | n/a |

### Behavior details
- **Per-tab caching:** each list is fetched the first time its tab is opened and reused afterward.
- **Instant feedback:** follow, unfollow, add friend, cancel, and unfriend all update local state immediately.
- **Live list edits:** unfriending someone while viewing **your own** Friends tab removes their row right away.
- **Count sync:** every action calls `onRelationshipChanged`. In `ProfileView` this triggers `refreshCounts`, which re-requests the public profile and the friends list to update the header stats behind the modal.
- **Navigation:** clicking a row (not the button) opens that user's profile and closes the modal.

---

## API Reference

Endpoints confirmed from the frontend work:

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/users/{user_id}/followers` | Users who follow `user_id` |
| `GET` | `/users/{user_id}/following` | Users that `user_id` follows |
| `GET` | `/users/{user_id}/friends` | Confirmed friends of `user_id` |

Additional notes:
- The backend supports `skip` and `limit` query parameters for pagination. The frontend does not use them yet.
- **[TODO]** Document the remaining endpoints: authentication, public profile, follow/unfollow, friend request send/cancel/accept/decline, unfriend, and posts.
- **[TODO]** If the backend exposes interactive docs (FastAPI serves them at `/docs`), link them here.

---

## Getting Started

### Prerequisites

- **Node.js** (LTS) and **npm**
- **Python** 3.x **[TODO: minimum version]**
- **[TODO: database]** installed or available as a hosted service
- **Git**

### 1. Clone the repository

```bash
git clone https://github.com/eashalyasin/social-media-app.git
cd social-media-app
```

### 2. Run the backend

```bash
cd backend

# Create and activate a virtual environment
python -m venv venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# macOS / Linux
source venv/bin/activate

# Install dependencies  [TODO: confirm requirements file name]
pip install -r requirements.txt
```

Create a `.env` file in `backend/` (see [Environment Variables](#environment-variables)), then start the server:

```bash
# [TODO: replace with the real start command, e.g. uvicorn main:app --reload]
```

### 3. Run the frontend

```bash
cd frontend
npm install
npm run dev
```

Open the URL printed in the terminal (typically <http://localhost:3000>).

To verify a production build:

```bash
npm run build
```

---

## Environment Variables

`.env`, `.env.local`, and `.env.*.local` are git-ignored, so secrets never reach the repository. Create them locally.

**Backend (`backend/.env`)** **[TODO: replace with real variable names]**

```env
DATABASE_URL=
SECRET_KEY=
```

**Frontend (`frontend/.env.local`)** **[TODO: confirm variable name]**

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

---

## Testing

### Manual test checklist: Followers / Following / Friends screen

- [ ] Clicking **Followers** on a profile opens the modal on the Followers tab, showing avatar, name, and `@username` for each user.
- [ ] Switching to **Following** loads that list once; returning to Followers does not refetch.
- [ ] The **Friends** tab loads correctly (this used to return a 404 before the `/users/{user_id}/friends` route was added).
- [ ] A stranger row shows **Follow** plus an add-friend icon.
- [ ] Clicking **Follow** flips the button to **Following** instantly, with no reload.
- [ ] Clicking add-friend changes the button to **Pending**, and clicking it again cancels the request.
- [ ] A friend row shows a green **Friends** pill that turns red **Unfriend** on hover, and unfriending asks for confirmation first.
- [ ] Unfriending from your own Friends tab removes the row immediately.
- [ ] Your own row (if it appears) shows no relationship button.
- [ ] Any follow/friend action silently refreshes the counts on the profile page behind the modal.
- [ ] Clicking a row (not its button) navigates to that user's profile and closes the modal.

### Automated tests

**[TODO]** Add the commands for backend and frontend tests, and describe what the CI workflow in `.github/workflows/` runs.

---

## Deployment

- **Frontend:** deployed on **Vercel** at [social-media-app-ten-eta.vercel.app](https://social-media-app-ten-eta.vercel.app). Set the Vercel project's root directory to `frontend/` and provide the frontend environment variables in the project settings.
- **Backend:** **[TODO: hosting provider, start command, and required environment variables]**
- **CI:** GitHub Actions workflows in `.github/workflows/`. **[TODO: describe triggers and jobs]**

---

## Development History

The project has been built up in focused tasks, which is reflected in the commit history (60+ commits on `main`):

- **Task 1:** fixed `src/lib/api.ts` so `profileAPI.getFollowers`, `getFollowing`, and `getFriends` call the real `/users/...` routes, and added the backend `/users/{user_id}/friends` route.
- **Task 2:** rewrote `FollowListModal.tsx` into a single tabbed modal with per-row relationship buttons, and updated `ProfileView.tsx` to pass `userId`, `currentUserId`, and `initialType`, and to refresh counts when relationships change.

---

## Known Limitations

- The followers/following/friends lists load in a single request each. There is no infinite scroll or "load more", even though the backend supports `skip` and `limit`.
- The list endpoints appear to respond without authentication. Confirm this is intended, since friend and follower lists can be sensitive.
- No open-source license is currently included in the repository.

---

## Contributing

1. Fork the repository and create a feature branch: `git checkout -b feature/your-feature`
2. Make your changes and verify the frontend builds: `cd frontend && npm run build`
3. Commit with a clear message, for example `Task N: short description of the change`
4. Push your branch and open a pull request against `main`

---

## License

No license file is currently present. Add a `LICENSE` file (for example MIT) to state how others may use this code.

---

## Author

Built by [@eashalyasin](https://github.com/eashalyasin).
