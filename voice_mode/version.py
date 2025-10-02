"""Enhanced version detection for voice mode."""

import os
import subprocess
from pathlib import Path
from typing import Optional

from .__version__ import __version__ as base_version


def get_git_commit_hash(short: bool = True) -> Optional[str]:
    """Get the current git commit hash."""
    try:
        # Get the directory where this file is located
        module_dir = Path(__file__).parent
        
        # Run git rev-parse to get commit hash
        cmd = ["git", "rev-parse", "--short", "HEAD"] if short else ["git", "rev-parse", "HEAD"]
        result = subprocess.run(
            cmd,
            cwd=module_dir,
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def is_git_repository() -> bool:
    """Check if we're running from a git repository."""
    try:
        module_dir = Path(__file__).parent
        # Check if .git directory exists in parent directories
        current = module_dir
        while current != current.parent:
            if (current / ".git").exists():
                return True
            current = current.parent
        return False
    except Exception:
        return False


def get_version() -> str:
    """Get the version string, including dev suffix if running from git."""
    # Start with base version
    version = base_version
    
    # Check if we're in a git repository
    if is_git_repository():
        commit = get_git_commit_hash()
        if commit:
            # Check if we have uncommitted changes
            try:
                module_dir = Path(__file__).parent
                result = subprocess.run(
                    ["git", "status", "--porcelain"],
                    cwd=module_dir,
                    capture_output=True,
                    text=True
                )
                has_changes = bool(result.stdout.strip())
                
                # Format: 2.16.0-dev.abc1234 or 2.16.0-dev.abc1234-dirty
                version = f"{base_version}-dev.{commit}"
                if has_changes:
                    version += "-dirty"
                    
            except Exception:
                # Fallback to just commit if status check fails
                version = f"{base_version}-dev.{commit}"
    
    return version


# Export the enhanced version
__version__ = get_version()