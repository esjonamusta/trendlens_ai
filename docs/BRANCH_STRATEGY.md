# Branch Strategy: GitHub Flow

This project uses **GitHub Flow** for collaborative development. It's a simple, flexible branching model that keeps the main branch production-ready.

## Branch Types

### `main`
- **Purpose:** Production-ready code only
- **Protection:** Requires pull request review and passing CI checks before merge
- **Never commit directly to this branch**

### `feature/*`
- **Purpose:** New features and improvements
- **Naming:** `feature/add-user-auth`, `feature/improve-search`
- **Branches from:** `main`

### `bugfix/*`
- **Purpose:** Bug fixes
- **Naming:** `bugfix/fix-login-error`, `bugfix/handle-edge-case`
- **Branches from:** `main`

### `docs/*` (optional)
- **Purpose:** Documentation updates
- **Naming:** `docs/update-api-guide`, `docs/add-setup-instructions`
- **Branches from:** `main`

## Workflow

### 1. Create a Feature Branch
```bash
git checkout main
git pull origin main
git checkout -b feature/your-feature-name
```

### 2. Make Commits
```bash
git add .
git commit -m "Clear, descriptive commit message"
```

Follow conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, `test:`, etc.

### 3. Push to GitHub
```bash
git push -u origin feature/your-feature-name
```

### 4. Open a Pull Request
- Go to https://github.com/esjonamusta/trendlens_ai
- GitHub will prompt you to create a PR
- Add a descriptive title and description
- Request reviewers
- Ensure CI checks pass

### 5. Code Review & Updates
- Team members review and request changes if needed
- Push additional commits to address feedback
- Commits are automatically added to the PR

### 6. Merge to Main
- Once approved and CI passes, merge the PR
- Delete the feature branch after merging (check the option in GitHub)

### 7. Update Your Local Main
```bash
git checkout main
git pull origin main
```

## Best Practices

- **Keep branches short-lived:** Aim to merge within 1-2 days
- **One feature per branch:** Don't mix multiple features
- **Rebase before merge:** Keep history clean (optional but recommended)
- **Write meaningful PRs:** Good descriptions help reviewers
- **Test locally first:** Run tests before pushing
- **Communicate:** Comment on PRs if review will take time

## Quick Reference

```bash
# Create and switch to a new branch
git checkout -b feature/feature-name

# Push to remote
git push -u origin feature/feature-name

# Delete local branch after merge
git branch -d feature/feature-name

# Delete remote branch
git push origin --delete feature/feature-name
```

## Questions?
See [CONTRIBUTING.md](CONTRIBUTING.md) for more guidelines or reach out to the team.
