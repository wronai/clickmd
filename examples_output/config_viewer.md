# Application settings
app:
  name: MyApp
  version: 1.0.0
  debug: true

# Database
database:
  host: localhost
  port: 5432
  name: myapp_db

# Features
features:
  - authentication
  - logging
  - caching
```


## JSON Configuration


```json
{
  "name": "my-project",
  "version": "1.0.0",
  "scripts": {
    "build": "webpack --mode production",
    "test": "jest --coverage"
  },
  "dependencies": {
    "react": "^18.0.0",
    "typescript": "^5.0.0"
  }
}
```


## TOML Configuration


```toml
[project]
name= "clickmd"
version= "1.5.0"
description= "Markdown for CLI"

[project.optional-dependencies]
click= ["click>=8.0"]
rich= ["rich>=13.0"]

[tool.pytest]
testpaths= ["tests"]
```


## Environment Variables

```
┌──────────┬───────────────────────────────────────────────────────┐
│Variable  │Value                                                  │
├──────────┼───────────────────────────────────────────────────────┤
│PATH      │/home/tom/.cargo/bin:/home/tom/.local/bin:/usr/loc...  │
│HOME      │/home/tom                                              │
│USER      │tom                                                    │
│SHELL     │/bin/bash                                              │
│TERM      │                                                       │
└──────────┴───────────────────────────────────────────────────────┘
```

## Config Diff

```diff
--- config.old.yaml
+++ config.new.yaml
@@ -1,3 +1,4 @@
 database:
-  host: localhost
+  host: db.example.com
   port: 5432
+  ssl: true
```

## Config Structure

```
config/
├── app/
│   ├── name: MyApp
│   └── version: 1.0.0
├── database/
│   ├── connection/
│   │   ├── host: localhost
│   │   └── port: 5432
│   └── pool/
│       ├── min: 5
│       └── max: 20
└── logging/
    ├── level: INFO
    └── file: /var/log/app.log
```
