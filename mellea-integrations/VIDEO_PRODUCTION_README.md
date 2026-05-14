# Video Production Workflow: Complete Package

Generated video production materials for the blog post: **"Mellea Meets AI Frameworks: Structured Validation for LangChain, CrewAI, and DSPy"**

---

## 📦 What's Included

This package contains everything needed to produce a professional 4:30 demo video, from script to final export.

### Files Generated

1. **`video-script-agentic-framework-integrations-demo.md`** — 4:30 demo script with:
   - Production cues (camera angles, on-screen graphics)
   - Timing breakdown (15 shots + section timings)
   - Delivery notes (tone, pacing, emphasis)
   - Shot list and editor notes

2. **`narration-segments.txt`** — 12 narration segments extracted from the script:
   - Each segment timestamped and labeled
   - Ready to feed into text-to-speech

3. **`generate_narration.py`** — Python script to auto-generate narration MP3 files:
   - Supports Google Cloud TTS (free tier available)
   - Supports ElevenLabs (premium quality, paid)
   - Outputs 12 MP3 files + manifest JSON with timing metadata
   - No manual voice-over recording needed

4. **`PRODUCTION_CHECKLIST.md`** — Detailed production guide covering:
   - Phase 1: Preparation (TTS setup, screen recording environment)
   - Phase 2: Screen Recording (15 shots with step-by-step instructions)
   - Phase 3: Audio Sync & Post-Production (editing timeline template)
   - Phase 4: QA Checklist (verification before export)
   - Phase 5: Distribution & Metrics (YouTube, social, analytics)

5. **`QUICK_START_VIDEO_PRODUCTION.md`** — Fast-track 3-phase guide:
   - Phase 1: Generate narration (30 min)
   - Phase 2: Record screens (2–3 hours)
   - Phase 3: Edit & export (2–3 hours)
   - Total time: ~5–7 hours start to finish

---

## 🚀 Quick Start (Choose Your Path)

### Path A: I Want the Quick Overview
→ Read **`QUICK_START_VIDEO_PRODUCTION.md`** (5 min)

### Path B: I Want All the Details
→ Read **`PRODUCTION_CHECKLIST.md`** (30 min) then proceed

### Path C: I Want to Start Now
→ Run these commands:

```bash
# 1. Generate narration audio (30 min)
python generate_narration.py
# Output: 12 MP3 files + narration_manifest.json in narration_audio/

# 2. Review the generated audio
open narration_audio/narration_01_hook.mp3

# 3. Follow the shot list to record screens
# → See PRODUCTION_CHECKLIST.md § Phase 2

# 4. Import into your video editor
# → 15 video clips + 12 audio tracks on timeline
```

---

## 🎯 The End Result

**One 4:30 YouTube video featuring:**
- ✅ Professional narration (auto-generated or human)
- ✅ Live screen recordings of all three framework integrations (LangChain, CrewAI, DSPy)
- ✅ Synchronized demo execution showing validation failures and retries
- ✅ Burned-in captions for accessibility
- ✅ Optional background music and transitions
- ✅ Clear CTA pointing viewers to mellea.ai

**Estimated production time:** 5–7 hours (one person, one workday)

---

## 📋 What You Need (Dependencies)

### Software

- **Screen recording:** ScreenFlow (Mac, $30) or OBS Studio (free, all platforms)
- **Video editing:** DaVinci Resolve (free) or Premiere Pro / Final Cut Pro (paid)
- **Python:** 3.8+

### APIs / Credentials

- **Google Cloud TTS:** Free tier (up to 1M characters/month)
  - Requires: Google Cloud account + `gcloud` CLI authenticated
- **OR ElevenLabs TTS:** Paid ($5–100/month depending on usage)
  - Requires: API key

### Time / Effort

- **Narration generation:** 30 min (automated, no manual voice-over needed)
- **Screen recording:** 2–3 hours (read checklist, execute shots sequentially)
- **Editing & export:** 2–3 hours (timeline assembly, sync, captions, export)

---

## 📝 Detailed File Descriptions

### 1. Video Script (`video-script-agentic-framework-integrations-demo.md`)

**What:** Complete shootable script for a 4:30 demo video

**Includes:**
- Cold open hook (0:00–0:20): Problem frame — AI agents fail in production
- Problem context (0:20–0:50): Why frameworks don't validate
- Pattern explanation (0:50–1:45): Four-step validation cycle
- LangChain demo (1:45–2:50): Live product description example with retries
- Multi-agent section (2:50–3:50): CrewAI + DSPy validation
- Tradeoff discussion (3:50–4:15): When to use validation
- CTA (4:15–4:30): Call viewers to mellea.ai

**Format:** Markdown with production cues:
- `[SHOW: terminal running ...]` — visual/screen cue
- `[CODE: highlight ...]` — code editor cue
- `(pause)`, `(emphasis)`, `(casual)` — delivery notes
- Timings: `(0:00–0:20, ~20s)` — section duration budgets

---

### 2. Narration Segments (`narration-segments.txt`)

**What:** 12 individual narration blocks extracted and timestamped

**Format:** Plain text, one segment per section

**Usage:** 
- Feed into TTS API via `generate_narration.py`
- Or read aloud yourself and record audio

---

### 3. Narration Generator (`generate_narration.py`)

**What:** Python script to synthesize all narration audio automatically

**Supports:**
- Google Cloud Text-to-Speech (default)
- ElevenLabs API (premium quality)

**Output:**
- 12 MP3 files (one per narration segment)
- `narration_manifest.json` — timings + filenames for easy timeline import

**Usage:**
```bash
# Google Cloud (default, free tier)
python generate_narration.py

# ElevenLabs (high quality, requires API key)
python generate_narration.py --service elevenlabs
```

---

### 4. Production Checklist (`PRODUCTION_CHECKLIST.md`)

**What:** Complete production workflow from pre-production through distribution

**Sections:**
- **Phase 1 (Preparation):** TTS setup, screen recording environment, demo code prep
- **Phase 2 (Recording):** 15 shots with detailed step-by-step instructions
  - Each shot has: timecode, narration segment, action description, key instructions
  - Examples: terminal recording, code editor display, flow diagram, metrics overlay
- **Phase 3 (Post-Production):** Timeline assembly, audio sync, captions, color correction
- **Phase 4 (QA):** Verification checklist before final export
- **Phase 5 (Distribution):** YouTube upload, social media, analytics

**Shot List Summary:**
1. Cold open (terminal demo) — 0:00–0:20
2. Framework logos — 0:20–0:35
3. Problem example — 0:35–0:50
4. Flow diagram — 0:50–1:20
5. Requirement config — 1:10–1:30
6. LangChain code — 1:30–1:50
7. Demo attempt 1 (fails) — 1:50–2:10
8. Demo attempt 2 (fails) — 2:10–2:30
9. Demo attempt 3 (passes) — 2:30–2:50
10. CrewAI crew definition — 2:50–3:00
11. CrewAI execution — 3:00–3:20
12. DSPy program definition — 3:20–3:35
13. DSPy execution — 3:35–3:50
14. Tradeoff graph — 3:50–4:15
15. CTA slide — 4:15–4:30

---

### 5. Quick Start Guide (`QUICK_START_VIDEO_PRODUCTION.md`)

**What:** Abbreviated 3-phase workflow for quick orientation

**Includes:**
- Copy-paste commands for narration generation
- Numbered steps for each phase
- Troubleshooting section
- Timeline overview (5–7 hours total)

---

## 🎬 Workflow Overview

```
┌─ VIDEO SCRIPT ──────────────────────────────────────────────────────────┐
│ video-script-agentic-framework-integrations-demo.md                     │
│ (4:30 demo with 15 shots, production cues, timings)                    │
└────────────────────────────┬────────────────────────────────────────────┘
                             │
        ┌────────────────────┴────────────────────┐
        │                                         │
        ▼                                         ▼
   ┌─────────────────────┐              ┌──────────────────────────┐
   │ NARRATION GENERATOR │              │ SCREEN RECORDING PHASE   │
   │ generate_narration.py                │ (Manual, ~2–3 hrs)      │
   │ (Automated, 30 min) │              │                          │
   │                     │              │ Follow PRODUCTION_       │
   │ Output:             │              │ CHECKLIST.md § Phase 2   │
   │ • 12 MP3 files      │              │                          │
   │ • Manifest JSON     │              │ Output:                  │
   └──────────┬──────────┘              │ • 15 video clips         │
              │                         │ • Named shot_01 through  │
              │                         │   shot_15               │
              │                         └──────────┬──────────────┘
              │                                    │
              └────────────────┬───────────────────┘
                               │
                    ┌──────────▼──────────┐
                    │  EDITING PHASE      │
                    │  (DaVinci/Premiere) │
                    │  (~2–3 hrs)         │
                    │                     │
                    │ 1. Import video     │
                    │    clips            │
                    │ 2. Arrange on       │
                    │    timeline         │
                    │ 3. Import narration │
                    │    MP3s & sync      │
                    │ 4. Add captions     │
                    │ 5. Add music        │
                    │ 6. Color correct    │
                    │ 7. Export 1080p     │
                    │    H.264            │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  FINAL VIDEO (MP4)  │
                    │ agentic-framework-  │
                    │ integrations-demo   │
                    │ .mp4                │
                    │ (~4:30, 40–80 MB)   │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
   ┌─────────────┐      ┌─────────────┐      ┌───────────────┐
   │   YouTube   │      │  LinkedIn   │      │   Twitter     │
   │   Upload    │      │   Post      │      │   Thread      │
   └─────────────┘      └─────────────┘      └───────────────┘
```

---

## ✅ Verification Checklist

Before starting, verify you have:

- [ ] Python 3.8+ installed
- [ ] Google Cloud SDK or ElevenLabs account with API key
- [ ] Video recording software (ScreenFlow, OBS, or similar)
- [ ] Video editing software (DaVinci Resolve recommended, free)
- [ ] 2–3 hours of uninterrupted time
- [ ] Demo code ready to run (LangChain, CrewAI, DSPy examples)

---

## 📞 Support & Troubleshooting

**Q: Do I need to record my own voice?**
A: No. `generate_narration.py` auto-generates professional narration using TTS. You can record a voice-over if you prefer, but it's not required.

**Q: What if my Google Cloud TTS sounds robotic?**
A: Try ElevenLabs (`--service elevenlabs`). It uses advanced neural voices that sound more natural, though it costs ~$5–25/month.

**Q: Can I use this for multiple videos?**
A: Yes! The script, checklist, and generator are reusable. Just update the narration segments and shot list for each new video.

**Q: How long does screen recording take?**
A: ~2–3 hours for all 15 shots. Most time is setup; actual recording is quick once you know what to capture.

**Q: Can I edit the script before generating narration?**
A: Yes. Edit `narration-segments.txt` or the script directly, then re-run `generate_narration.py`. It will generate new MP3s.

---

## 🎓 Learning Resources

- **Video Production Basics:** https://www.youtube.com/results?search_query=premiere+pro+tutorial
- **DaVinci Resolve Guide:** https://www.davinciresolveuniversity.com
- **Google Cloud TTS Docs:** https://cloud.google.com/text-to-speech/docs
- **ElevenLabs API:** https://elevenlabs.io/docs/api

---

## 📌 Next Steps

**Ready to start?**

1. **Choose your quick-start path** (A, B, or C above)
2. **Run the narration generator:** `python generate_narration.py`
3. **Follow the production checklist** for screen recording and editing
4. **Export and upload to YouTube**

**Questions?** Refer to PRODUCTION_CHECKLIST.md (detailed) or QUICK_START_VIDEO_PRODUCTION.md (abbreviated).

---

**Created:** 2026-05-13  
**Video duration:** 4:30  
**Estimated production time:** 5–7 hours  
**Status:** Ready to produce ✅
