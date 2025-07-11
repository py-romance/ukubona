import os, subprocess

# Prompt user for GitHub info
GH_USER = input("GitHub Username: ")
GH_TOKEN = input("GitHub Token: ")
GH_REPO = input("GitHub Repo: ")
BRANCH = "main"

# Set up directories
dirs = [
    "umubonaboneza/css",
    "umubonaboneza/js",
    "umubonaboneza/md"
]

# File contents
files = {
    "index.html": """<!DOCTYPE html>
<html lang='en'>
<head>
  <meta charset='UTF-8' />
  <meta name='viewport' content='width=device-width, initial-scale=1.0' />
  <title>Coen Recursion Engine</title>
  <link rel='stylesheet' href='umubonaboneza/css/main.css' />
</head>
<body>
  <div class='cosmos'>
    <div id='pentagon'>
      <div class='glyph' id='glyph-origin' data-glyph='🌊'></div>
      <div class='glyph' id='glyph-rules' data-glyph='❤️'></div>
      <div class='glyph' id='glyph-recursion' data-glyph='🔁'></div>
      <div class='glyph' id='glyph-splicing' data-glyph='🎭'></div>
      <div class='glyph' id='glyph-illusion' data-glyph='🤖'></div>
    </div>
    <div id='details' class='hidden'></div>
  </div>
  <script src='umubonaboneza/js/main.js'></script>
</body>
</html>""",

    "umubonaboneza/css/main.css": """body {
  margin: 0;
  padding: 0;
  background: radial-gradient(#000010, #000000);
  overflow: hidden;
  font-family: 'Georgia', serif;
  color: #fff;
}
.cosmos {
  position: relative;
  width: 100vw;
  height: 100vh;
}
#pentagon {
  position: absolute;
  width: 60vmin;
  height: 60vmin;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
}
.glyph {
  position: absolute;
  font-size: 3rem;
  cursor: pointer;
  transition: transform 0.4s ease, text-shadow 0.4s ease;
  animation: pulse 3s infinite;
}
.glyph:hover {
  transform: scale(1.8);
  text-shadow: 0 0 15px #fff, 0 0 30px #fff;
}
#glyph-origin     { top: 0%;   left: 50%; transform: translate(-50%, -50%); }
#glyph-rules      { top: 30%;  left: 90%; transform: translate(-50%, -50%); }
#glyph-recursion  { top: 80%;  left: 70%; transform: translate(-50%, -50%); }
#glyph-splicing   { top: 80%;  left: 30%; transform: translate(-50%, -50%); }
#glyph-illusion   { top: 30%;  left: 10%; transform: translate(-50%, -50%); }
@keyframes pulse {
  0%   { opacity: 0.8; transform: scale(1); }
  50%  { opacity: 1; transform: scale(1.1); }
  100% { opacity: 0.8; transform: scale(1); }
}
#details {
  position: absolute;
  bottom: 2rem;
  left: 50%;
  transform: translateX(-50%);
  width: 90%;
  max-height: 40%;
  overflow-y: auto;
  padding: 1rem;
  background: rgba(0, 0, 0, 0.85);
  border: 1px solid #fff;
  border-radius: 1rem;
  font-size: 1rem;
  display: none;
}
#details.visible {
  display: block;
}""",

    "umubonaboneza/js/main.js": """const glyphs = {
  'glyph-origin': \`🌊 Sea (Origins)...\`,
  'glyph-rules': \`❤️ Love (Rules)...\`,
  'glyph-recursion': \`🔁 Recursion (Games)...\`,
  'glyph-splicing': \`🎭 Theater (Splicing)...\`,
  'glyph-illusion': \`🤖 Illusion (Broadcast)...\`
};
document.querySelectorAll('.glyph').forEach(glyph => {
  glyph.innerText = glyph.getAttribute('data-glyph');
  glyph.addEventListener('click', () => {
    const content = glyphs[glyph.id];
    const details = document.getElementById('details');
    details.innerHTML = content;
    details.classList.add('visible');
  });
});""",

    "umubonaboneza/md/README.md": """# Coen Recursion Engine  

🌊 ❤️ 🔁 🎭 🤖  

A mythic UI simulator grounded in five glyphs:  
Each glyph opens a narrative based in recursive logic from Coen Brothers' filmography.  

## Glyphs & Meaning

- �� **Sea (Origins)** — Llewyn Davis’ return to the alley: recursion as ontology  
- ❤️ **Love (Rules)** — Larry Gopnik and the covenant of absurdity  
- 🔁 **Recursion (Games)** — Fargo’s loop of crime and grace  
- 🎭 **Theater (Splicing)** — Barton Fink and genre collapse  
- 🤖 **Illusion (Broadcast)** — Chigurh’s coin and fate’s fakery  

## Architecture

- `setup.sh` calls `origins.py`
- `origins.py` generates HTML/CSS/JS
- Glyph engine = symbolic recursion UI

## Intent

This is not a site. It is a ritual.
It renders the illusion of agency within a stage already written.
Yet the glyphs respond.  
Which means... it listens.
""",

    "render.yaml": """services:
  - type: web
    name: ukubona-glyphs
    env: static
    staticPublishPath: .
"""
}

# Create directories
for d in dirs:
    os.makedirs(d, exist_ok=True)

# Write files
for path, content in files.items():
    with open(path, 'w') as f:
        f.write(content)

# Initialize and push to GitHub
print("🔧 Initializing git...")
subprocess.run(["git", "init"])
subprocess.run(["git", "checkout", "-b", BRANCH])
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", "🌱 Initial commit from origins.py"])
subprocess.run(["git", "remote", "remove", "origin"], stderr=subprocess.DEVNULL)
subprocess.run(["git", "remote", "add", "origin", f"https://{GH_USER}:{GH_TOKEN}@github.com/{GH_USER}/{GH_REPO}.git"])
subprocess.run(["git", "push", "-u", "origin", BRANCH])

print(f"✅ Pushed to https://github.com/{GH_USER}/{GH_REPO}")
