#!/bin/bash

cd /Users/Pierre/Library/CloudStorage/GoogleDrive-pierre.granchamp@finamars.com/Mon\ Drive/Finamars/IA/Apps/crewai-local/crewAI/my_crews

git add .
git commit -m "Sync auto $(date '+%Y-%m-%d %H:%M:%S')"
git push origin main