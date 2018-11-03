"""
Invokes the biohazard manager when the biohazard module is run as a script.

Example: python -m biohazard
"""
from biohazard.core.management import run


if __name__ == "__main__":
    run()
