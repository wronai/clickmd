#!/usr/bin/env python3
"""
Log-style colored output example.

Demonstrates how to use clickmd for log-style output with automatic coloring.

Run: python examples/logging.py
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from clickmd import md


def main() -> None:
    md("""
# 📋 Application Log Output

clickmd automatically colors log-style output based on emoji prefixes and keywords.

## Success Messages (Green)

```log
✅ Build completed successfully
✅ All tests passed
✅ Deployment finished
🚀 Application started on port 3000
```

## Warning Messages (Yellow)

```log
⚠️ Deprecated API usage detected
⚠️ Cache miss - fetching from source
🎫 Token expires in 24 hours
📝 Configuration file not found, using defaults
```

## Error Messages (Red)

```log
🛑 Connection refused: localhost:5432
🛑 Authentication failed
❌ Build failed with 3 errors
Error: Module not found
Exception: ValueError
ERR_CONNECTION_REFUSED
```

## Info Messages (Cyan/Gray)

```log
📦 Installing dependencies...
💬 Sending notification...
🔄 Refreshing cache...
→ Processing item 1 of 100
→ Processing item 2 of 100
```

## Progress Messages (Magenta)

```log
📊 Progress: 45% complete
📊 Progress: [████████░░░░░░░░] 50%
```

## Mixed Example

```log
🚀 Starting application...
📦 Loading configuration from config.yaml
✅ Configuration loaded
📦 Connecting to database...
⚠️ Using default connection pool size
✅ Database connected
📊 Progress: Initializing services...
✅ All services ready
🚀 Server listening on http://localhost:3000
```
""")


if __name__ == "__main__":
    main()
