
============================================================
clickmd Logger Examples
============================================================

# Basic Logger Usage


```log
→ Starting process...
```


```log
✅ Build completed successfully
```


```log
⚠️ Cache miss - fetching from source
```


```log
🛑 Connection refused
```


----------------------------------------

# Action Logging


```log
🚀 Evolution mode activated
```


```log
🤖 Using OpenRouter provider
```


```log
🔨 Generating code to ./output
```


```log
🧪 Running test suite
```


```log
💾 Saving contract.ai.json
```


```log
✅ All tasks completed
```


----------------------------------------

# Progress & Steps


```log
📊 Installing: 25% (25/100)
```


```log
📊 Building: 50% (50/100)
```


```log
📊 Testing: 75% (75/100)
```


```log
📊 Complete: 100% (100/100)
```


```log
[1/5] Initialize project
```


```log
[2/5] Generate contract
```


```log
[3/5] Generate code
```


```log
[4/5] Run tests
```


```log
[5/5] Deploy
```


----------------------------------------

# Exception Handling


```log
🛑 ZeroDivisionError: division by zero
```


```log
🛑 ValueError: Invalid configuration: missing 'port' field
```


```log
  Traceback (most recent call last):
```


```log
    File "/home/tom/github/wronai/contract/clickmd/examples/logger_usage.py", line 81, in exception_handling
```


```log
      raise ValueError("Invalid configuration: missing 'port' field")
```


```log
  ValueError: Invalid configuration: missing 'port' field
```


----------------------------------------

# Grouped Output (Sections)


```log
→ This is separate
```


```log
→ Each line is its own block
```


## With Section


```log
🚀 Starting build...
→ Compiling TypeScript
→ Bundling assets
→ Optimizing images
✅ Build complete!
```


----------------------------------------

# LLM Logging


```log
🤖 LLM selected: openrouter
```


```log
→ Model: qwen/qwen-2.5-coder-32b-instruct
```


```log
📋 Attempt 1/3 (contract generation)
```


```log
📋 Attempt 2/3 (contract generation)
```


```log
→ Provider: openrouter
```


```log
→ Model: qwen-2.5-coder
```


```log
→ Temperature: 0.7
```


----------------------------------------

## Generation Status


```log
🚀 Starting generation...
```


```log
→ Loading contract.ai.json
```


```log
✅ Contract loaded
```


## Generated Files

| File | Size | Status |
|------|------|--------|
| server.ts | 2.4 KB | ✅ |
| package.json | 0.8 KB | ✅ |
| tsconfig.json | 0.3 KB | ✅ |


```log
✅ Generation complete!
```


----------------------------------------

# 🧬 Evolution Mode


```log
→ Prompt: Create a todo app
→ Output: ./output
→ Engine: Python Native
```


## Contract Generation


```log
🤖 LLM selected: openrouter
```


```log
→ Model: nvidia/nemotron-3-nano-30b-a3b:free
```


```log
📋 Attempt 1/3 (contract generation)
```


```log
✅ Contract generated successfully in 1 attempt(s)
```


## Code Generation


```log
🔨 Generating code to ./output
→ Framework: express (typescript)
→ Entities: 1
🤖 Using LLM for code generation...
✅ LLM generated 3 files
```


## Testing


```log
✅ Health check passed
✅ CRUD tests passed
⚠️ 1 test skipped (optional feature)
```


## ✅ Evolution Complete


```log
✅ All tasks finished successfully!
```

