This is a git hook which uses a locally running llama3 to geerate a suggested commit message for your
changes.

Only tested on mac

## Setup

Download and install ollama:
https://ollama.com/download/mac

download llama3
`ollama run llama3`

Symlink the commit hook into any repo you'd like to use it

`ln -s /this/repo/path/prepare-commit-msg /your/repo/path/.git/hooks`


## usage

When you go to commit without a message, a llama3 insstance will be started and will generate a suggested commit message for you.
