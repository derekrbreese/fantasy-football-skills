#!/usr/bin/env bash
# Cloud Agent install step for the fantasy-football-skills plugin marketplace.
#
# The repository ships no runtime dependencies: the contract tests in tests/
# use only the Python 3 standard library, which the base image already
# provides. This script provisions the Claude Code CLI so the canonical
# `claude plugin validate` check documented in CONTRIBUTING.md is available.
#
# It is idempotent: re-running installs/updates the CLI and refreshes the
# symlink without accumulating state.
set -euo pipefail

NPM_PREFIX="${HOME}/.npm-global"
mkdir -p "${NPM_PREFIX}"

# Install the Claude Code CLI into a user-owned prefix (the default global
# prefix is not writable without root).
npm config set prefix "${NPM_PREFIX}"
npm install -g @anthropic-ai/claude-code

# Expose the CLI to every shell (interactive or not) via a directory already on
# the default PATH, avoiding shell-profile mutation. Fall back to a profile
# entry if a system symlink cannot be created.
if sudo -n ln -sf "${NPM_PREFIX}/bin/claude" /usr/local/bin/claude 2>/dev/null; then
  echo "Linked claude into /usr/local/bin"
else
  echo "Could not symlink into /usr/local/bin; adding ${NPM_PREFIX}/bin to PATH via ~/.bashrc"
  LINE="export PATH=\"${NPM_PREFIX}/bin:\$PATH\""
  grep -qxF "${LINE}" "${HOME}/.bashrc" 2>/dev/null || echo "${LINE}" >> "${HOME}/.bashrc"
fi

echo "--- Toolchain versions ---"
python3 --version
claude --version
