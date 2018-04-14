[![CircleCI](https://circleci.com/gh/roselmamendes/pergunte-stackoverflow-cli.svg?style=svg)](https://circleci.com/gh/roselmamendes/pergunte-stackoverflow-cli)

# Pergunte Stackoverflow CLI

Though the terminal search for questions on Stackoverflow.

# Contribution

1. Git clone this repository

2. Run `docker build -t stackoverflow-cli .`

Run tests: `docker run --rm -v "$PWD":/usr/src/app -w /usr/src/app -it stackoverflow-cli python -m unittest`
