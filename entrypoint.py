import os
import sys
from datetime import datetime, timezone

name = sys.argv[1] if len(sys.argv) > 1 else "World"

print(f"Hello {name}!")

github_output = os.environ.get("GITHUB_OUTPUT")

if github_output:
    with open(github_output, "a") as f:
        f.write(f"time={datetime.now(timezone.utc).isoformat()}")
