# Sonido del video: paleta sintética de onetake (scripts/sfx_palette.py), tiempos leídos de events.json (__events del comp).
import os, sys, json
sys.path.insert(0, os.path.expanduser("~/.claude/skills/onetake/scripts"))
from sfx_palette import Score, air, glass, wood, sub, bubble
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ev = json.load(open(os.path.join(HERE, "events.json")))
s = Score(dur=15.0, T60=1.0); place = s.place
at = lambda k: [e for e in ev if e["kind"] == k]
PENTA = [349, 392, 440, 523, 587, 698, 784, 880, 1047, 1175, 1397, 1568, 1760]   # F pentatonic, climbing

tap = at("tap")[0]["t"]
place(wood(240, 0.08), tap, 0.30, -0.4, 0.2); place(glass(698, 1.0, 0.6), tap + 0.02, 0.16, -0.4, 0.5)      # the idea lights
roll, hit = at("roll")[0]["t"], at("hit")[0]["t"]
place(air(hit - roll, 160, 900, 1.1, 0.95), roll, 0.30, -0.5, 0.3, pan_to=-0.1)                             # the roll
place(wood(200, 0.12), hit, 0.40, -0.1, 0.25)                                                             # the knock
place(wood(170, 0.14), at("land-copy")[0]["t"], 0.36, -0.05, 0.25)
t_reel = at("land-reel")[0]["t"]; place(wood(140, 0.16), t_reel, 0.40, 0.0, 0.25); place(sub(64, 0.6), t_reel, 0.30, 0.0, 0.3)
place(bubble(420, 0.24), at("play")[0]["t"], 0.22, 0.05, 0.3)                                             # play; then the rest is quiet
bz = at("buzz")[0]["t"]
for k in range(4): place(wood(95, 0.05), bz + k * 0.045, 0.22, 0.1, 0.1)                                  # the buzz
for i, e in enumerate(at("land-like")):                                                                  # the likes run, climbing
    place(wood(210 + i * 12, 0.08), e["t"], 0.26, 0.2, 0.2); place(glass(PENTA[i], 0.6, 0.7), e["t"] + 0.01, 0.12, 0.2, 0.45)
L = at("land-letter")
for i, e in enumerate(L):                                                                                # the name, still climbing
    place(wood(260 + i * 10, 0.09), e["t"], 0.30, 0.35, 0.2); place(glass(PENTA[7 + i], 0.7, 0.6), e["t"] + 0.01, 0.13, 0.35, 0.5)
done = L[-1]["t"]
place(sub(50, 1.2), done + 0.02, 0.50, 0.3, 0.45); place(glass(698, 1.6, 0.35), done + 0.04, 0.12, 0.3, 0.7); place(glass(880, 1.6, 0.3), done + 0.06, 0.09, 0.3, 0.7)
pull = at("pull")[0]["t"]; place(air(1.2, 1800, 220, 1.2, 0.4), pull, 0.30, 0.3, 0.6, pan_to=0.0)             # the camera pulls out
place(air(0.5, 300, 1600, 1.3, 0.6), at("sub")[0]["t"], 0.16, 0.0, 0.5)
place(glass(523, 1.4, 0.5), at("hola")[0]["t"], 0.12, 0.2, 0.6)
t2 = at("tap2")[0]["t"]; place(wood(240, 0.08), t2, 0.26, -0.5, 0.2); place(glass(698, 1.4, 0.5), t2 + 0.02, 0.14, -0.5, 0.6)
s.write(os.path.join(HERE, "sfx.wav"))
print("sfx.wav ok")
