"""Main entry point for Oracle OIC extension."""

from __future__ import annotations


def app() -> None:
    """Main application entry point."""
    print("Oracle OIC Extension - Main application")

def main() -> None:
    """Main CLI entry point."""
    print("Oracle OIC Extension - Main CLI")

__all__ = ["app", "main"]

if __name__ == "__main__":
    app()
