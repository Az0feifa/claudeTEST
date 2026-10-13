#!/bin/bash
# Local addition (not upstream): installs onetake's Python deps in a fresh Claude Code cloud container.
# playwright pinned to 1.56.0 so it matches the pre-installed chromium-1194 in /opt/pw-browsers
# (newer playwright wants a chromium build that isn't there). ffmpeg and node are already present.
python3 -c "import scipy, matplotlib, fontTools, brotli, cv2" 2>/dev/null && [ "$(pip show playwright 2>/dev/null | sed -n 's/^Version: //p')" = "1.56.0" ] && { echo "onetake deps ok"; exit 0; }
pip install -q "playwright==1.56.0" numpy scipy Pillow matplotlib fonttools brotli opencv-python-headless
python3 -c "import playwright, scipy, matplotlib, fontTools, brotli, cv2" && echo "onetake deps ok"
