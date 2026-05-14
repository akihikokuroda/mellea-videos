# Quick Start: Video Production Workflow

Get your demo video from script to upload in 3 phases.

---

## 🎬 Phase 1: Generate Narration Audio (30 min)

### Step 1: Choose Your TTS Service

**Option A: Google Cloud TTS (recommended)**
```bash
# Install
pip install google-cloud-texttospeech

# Authenticate
gcloud auth application-default login

# Generate
python generate_narration.py
```

**Option B: ElevenLabs (higher quality, paid)**
```bash
# Install
pip install requests

# Set API key
export ELEVENLABS_API_KEY="your_key_here"

# Generate
python generate_narration.py --service elevenlabs
```

### Step 2: Verify Output

```bash
# Check generated files
ls -lh narration_audio/

# Listen to one segment
open narration_audio/narration_01_hook.mp3  # or 'xdg-open' on Linux
```

**Expected output:**
- 12 MP3 files (~500KB–1MB each)
- `narration_manifest.json` (timing metadata)
- Total duration: ~4:30

---

## 🎥 Phase 2: Record Screen Captures (2–3 hours)

### Step 1: Set Up Your Environment

**On macOS:**
```bash
# Download ScreenFlow or use OBS
# Set display to 1920×1080
# Open Terminal, VSCode, etc. in dark theme
```

**Code editor setup (VSCode):**
- Theme: Dracula or One Dark Pro
- Font size: 14pt
- Font: Monaco or Menlo (monospace)

**Terminal setup:**
- Font size: 14pt
- Theme: Solarized Dark
- Width: 120 characters

### Step 2: Follow the Shot List

Open **PRODUCTION_CHECKLIST.md** → **Phase 2: Screen Recording**.

For each shot (15 total):
1. Read the instructions
2. Set up the screen (code, terminal, etc.)
3. Hit record
4. Execute the action (run code, show diagram, etc.)
5. Stop recording
6. Save with clear filename: `shot_01_hook.mp4`, `shot_02_logos.mp4`, etc.

**Timing rule:** Each shot should be 2–5 seconds longer than the narration segment (narration guides you; visuals fill the space).

### Step 3: Organize Output

```bash
mkdir -p video_production/shots
# Save all video clips to this directory
# naming: shot_01_hook.mp4, shot_02_logos.mp4, etc.
```

---

## ✂️ Phase 3: Edit & Export (2–3 hours)

### Step 1: Choose Your Editor

- **Adobe Premiere Pro** (professional, steep learning curve)
- **DaVinci Resolve** (free, powerful, recommended)
- **Final Cut Pro** (Mac-only, fast)
- **CapCut** (free, simple, OK for this scope)

### Step 2: Build Your Timeline

In your editor:

1. **Create new project:** 1920×1080, 30fps
2. **Import media:**
   - All 15 video shots from `video_production/shots/`
   - All 12 narration MP3s from `narration_audio/`
3. **Arrange timeline:**
   - Drag shots onto video track in order (shot_01, shot_02, ..., shot_15)
   - Trim each shot to match narration timing (see PRODUCTION_CHECKLIST.md)
   - Drag narration MP3s onto audio track in order (narration_01, narration_02, ..., narration_12)
4. **Sync audio:** Use timecodes from `narration_manifest.json`
   - Shot 1 (0:00–0:20) → Narration 01 (20s)
   - Shot 2 (0:20–0:35) → Narration 02 (partial, first 15s)
   - etc.

### Step 3: Add Captions

Most editors have auto-captioning:
- DaVinci Resolve: `Edit` → `Captions` → `Auto Transcribe`
- Premiere Pro: `Caption` → `Auto Transcribe`
- CapCut: `Captions` → `Auto Captions`

Then manually correct technical terms:
- "Langchain" → "LangChain"
- "crew A I" → "CrewAI"
- "D S Py" → "DSPy"

### Step 4: Add Music (Optional but Recommended)

Download royalty-free music:
- YouTube Audio Library (free): https://www.youtube.com/audio_library
- Epidemic Sound ($10/mo): https://www.epidemicsound.com
- Artlist ($15/mo): https://artlist.io

Search for: "minimal synth" or "tech ambient" (1–2 minutes, ~70BPM)

- Drag music to audio track 2 (below narration)
- Reduce volume to **–12dB** (so narration sits on top)
- Boost volume at CTA section (4:15–4:30) to **–6dB**

### Step 5: Add Transitions

Between major sections, add **0.5s cross-dissolve:**
- After shot 2 (logos) → shot 3
- After shot 5 (config) → shot 6
- After shot 9 (demo 3) → shot 10
- After shot 14 (graph) → shot 15

### Step 6: Export

**Export settings:**
- Format: H.264 (MP4)
- Resolution: 1920×1080
- Bitrate: 5–8 Mbps
- Audio: AAC 128 kbps, stereo
- Filename: `agentic-framework-integrations-demo.mp4`

**Typical file size:** 40–80 MB for a 4:30 video

---

## 📊 Timeline Overview

| Phase | Task | Duration | Files |
|-------|------|----------|-------|
| 1 | Generate narration | 30 min | 12×MP3 + JSON |
| 2 | Record screens | 2–3 hrs | 15×MP4 |
| 3 | Edit + export | 2–3 hrs | 1×MP4 (final) |
| **Total** | **Start to finish** | **5–7 hrs** | |

---

## 🚀 Next Steps After Export

### Upload to YouTube

1. Go to [youtube.com/upload](https://www.youtube.com/upload)
2. Select `agentic-framework-integrations-demo.mp4`
3. Fill in metadata:
   - **Title:** "Mellea: Structured Validation for LangChain, CrewAI, and DSPy"
   - **Description:** (Copy from blog post or write 2–3 sentences)
   - **Tags:** `mellea`, `langchain`, `crewai`, `dspy`, `ai`, `validation`, `llm`
   - **Thumbnail:** Select a frame with visible validation (green checkmark)
4. Set visibility: Public or Unlisted (to share with team first)
5. Schedule publish or publish immediately

### Share on Social Media

- **Tweet:** Link to YouTube + call out all three frameworks
- **LinkedIn:** Paste YouTube link + write a thread on the problem + solution
- **Slack:** Post in #announcements channel

### Update Blog Post

Add an embedded YouTube player above or below the blog post text:
```markdown
## Watch the Demo

<iframe width="560" height="315" src="https://www.youtube.com/embed/VIDEO_ID" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
```

---

## 🔧 Troubleshooting

### Narration Generator Fails

**Error: "Google credentials not found"**
```bash
gcloud auth application-default login
# Restart terminal, try again
```

**Error: "ElevenLabs API key not set"**
```bash
export ELEVENLABS_API_KEY="sk-..."
echo $ELEVENLABS_API_KEY  # Verify it's set
python generate_narration.py --service elevenlabs
```

### Screen Recording Issues

**Text too small:** Increase font size to 16pt before recording

**Terminal output hard to read:** Add 2–3 seconds of pause after each command executes

**Video glitchy:** Re-record just that one shot; rest of timeline unaffected

### Audio Sync Problems

**Narration leading (audio starts before visuals):** Slide audio clip later on timeline (+0.2s)

**Narration lagging (audio after visuals):** Slide audio clip earlier (–0.2s)

**Narration duration doesn't match video:** Edit the video clip to match narration (use timecodes in manifest)

---

## Resources

- **Generator script:** `generate_narration.py`
- **Production checklist:** `PRODUCTION_CHECKLIST.md` (detailed shot-by-shot guide)
- **Video script:** `video-script-agentic-framework-integrations-demo.md`
- **Narration manifest:** `narration_audio/narration_manifest.json` (after running generator)

---

**Ready to start?** Run `python generate_narration.py` now. ✨
