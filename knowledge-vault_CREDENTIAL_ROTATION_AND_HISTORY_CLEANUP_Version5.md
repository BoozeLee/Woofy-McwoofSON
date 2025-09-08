# Credential Rotation & History Cleanup

## Steps

1. Rotate all secrets/tokens as scheduled or after an exposure.
2. Use tools like git-filter-repo/BFG to scrub secrets from history.
3. Update `.env` files and notify dependent systems.
4. Document each rotation with date & responsible agent.

## Audit Log

- _[YYYY-MM-DD]_ Rotated Gmail/Drive OAuth credentials, removed old tokens – [Agent Name]
- _[YYYY-MM-DD]_ GitHub PATs rotated, `.env` updated – [Agent Name]

---

_Fill in new entries for every credential change or incident._