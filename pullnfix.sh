#!/bin/bash
git pull origin main
git fetch myorigin
git rebase myorigin/main
git push myorigin main



