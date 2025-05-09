#!/bin/bash
echo python3 ~/.local/share/life/main.py '$@' > ~/.local/bin/life
chmod +x ~/.local/bin/life
rm -rf ~/.local/share/life
git clone -q https://github.com/ivaaane/life ~/.local/share/life || rm ~/.local/bin/life