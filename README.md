# Hello World Python Action

A simple Hello World GitHub Action written in Python.

## Usage

```yaml
name: Test Python Action

on: [push]

jobs:
  hello:
    runs-on: ubuntu-latest
    steps:
      - name: Run hello world action
        uses: your-username/hello-world-python-action@v1
        with:
          who-to-greet: "Arman"
```
