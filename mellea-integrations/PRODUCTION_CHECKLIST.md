# Production Checklist: Agentic Framework Integrations Demo Video

**Total Runtime:** 4:30  
**Narration Segments:** 12  
**Key Deadlines:** See below  

---

## Phase 1: Preparation (Do Before Recording)

### A. Narration Audio Generation

- [ ] Install TTS dependencies: `pip install google-cloud-texttospeech` (or ElevenLabs via `pip install requests`)
- [ ] Set up API credentials:
  - **Google Cloud TTS:** `gcloud auth application-default login`
  - **ElevenLabs:** Set `ELEVENLABS_API_KEY` environment variable
- [ ] Run narration generator: `python generate_narration.py`
  - Output: 12 MP3 files in `narration_audio/` folder + `narration_manifest.json`
- [ ] QA narration audio:
  - Listen to each segment; verify speech is clear and pacing matches target durations
  - Total combined narration duration should be ~4:30
  - Adjust speaking rate in `generate_narration.py` if needed (default: 1.0)

### B. Screen Recording Setup (macOS)

- [ ] Install recording software:
  - ScreenFlow (recommended for Mac, paid) OR
  - OBS Studio (free, cross-platform)
  - Quicktime (built-in, basic)
- [ ] Configure display settings:
  - Resolution: 1920×1080 (1080p) minimum
  - Scaling: 100% (no HiDPI blur)
  - Background: Clean desktop or dark wallpaper
- [ ] Prepare code editors:
  - Font size: 14–16pt (readable on video)
  - Theme: Dark (easier to read on video)
  - Suggested: VSCode with Dracula or One Dark Pro theme
- [ ] Prepare terminal:
  - Font size: 14pt
  - Theme: Solarized Dark or similar high-contrast
  - Width: 120 characters (standard)

### C. Demo Code & Data Setup

- [ ] Clone/prepare Mellea repository locally
- [ ] Set up three demo projects:
  - LangChain chain with Mellea validation (product description task)
  - CrewAI crew with two agents (summary + JSON formatting)
  - DSPy program with typed signatures and validation
- [ ] Pre-generate sample outputs for failed validation (first/second attempts)
- [ ] Prepare mock API responses or rate-limit fallback (to ensure consistent timing)
- [ ] Document exact commands to run for each demo (copy-paste ready)

### D. Asset Library Preparation

- [ ] **Logos:** Download high-res versions (400×300px minimum)
  - LangChain logo
  - CrewAI logo
  - DSPy logo
  - Mellea logo
- [ ] **Diagrams/Graphics:**
  - Four-step flow diagram (Generate → Validate → Retry? → Return)
  - Example requirement config (JSON or YAML snippet)
  - Validation metrics graph (optional, for tradeoff section)
- [ ] **B-Roll:** Source royalty-free footage (or use software UI transitions)
  - Agent collaboration diagrams
  - Dashboard metrics visualizations

---

## Phase 2: Screen Recording (Day-of Shooting)

### Shot List with Timing & Instructions

#### **Shot 1: Cold Open Hook (0:00–0:20)**

**Timecode:** 0:00–0:20  
**Narration:** Segment 01 (20s)  
**Action:** Terminal showing LangChain chain validation failure → retry → pass

**Instructions:**
1. Open terminal, dark theme, monospace font 14pt
2. Pre-stage a LangChain chain execution that will fail first time
3. **Record:** Run the chain; show output fails validation (red text/warning)
4. **Record:** Immediate retry; show second attempt passes (green checkmark)
5. **Record:** Show metrics line (e.g., "Validation: PASS, Cost: $0.02, Retries: 1")
6. Keep output visible for 2–3 seconds after narration ends

**Timing:** 20 seconds audio = ~12–15 seconds screen time (narration leads slightly)

---

#### **Shot 2: Framework Logos Transition (0:20–0:35)**

**Timecode:** 0:20–0:35  
**Narration:** Segment 02 opening (first 15s of problem statement)  
**Action:** Three logos fade/slide on screen

**Instructions:**
1. Start with blank dark background
2. LangChain logo slides in from left (0:20)
3. CrewAI logo slides in from center (0:25)
4. DSPy logo slides in from right (0:30)
5. All three hold for 2–3 seconds

**Production:** Use After Effects, Keynote, or OBS overlay; export as video segment to composite later

---

#### **Shot 3: Problem Example (0:35–0:50)**

**Timecode:** 0:35–0:50  
**Narration:** Segment 02 conclusion (last 15s)  
**Action:** Code editor showing bad LLM output

**Instructions:**
1. Open code editor or terminal
2. Display example of invalid output (e.g., "Great product!" — 8 words when 50 needed)
3. Highlight the problem: text is too short, missing required fields
4. Use red border or arrow annotation to emphasize the issue
5. Hold for 3–4 seconds; then fade to next scene

**Production:** Can be screenshot + annotation, or live editor display

---

#### **Shot 4: Flow Diagram (0:50–1:20)**

**Timecode:** 0:50–1:20  
**Narration:** Segments 03 + 04 (30s total)  
**Action:** Four-step process flow: Generate → Validate → Retry? → Return

**Instructions:**
1. Display flow diagram with labels
2. Animate each box appearing left-to-right as narration mentions it
   - "Generate" appears at 0:55
   - "Validate" appears at 1:00
   - "Retry?" appears at 1:05
   - "Return" appears at 1:10
3. Add color: green for "Return", yellow for "Retry?", neutral for "Generate/Validate"
4. After 1:10, fade in example requirement config (word count, required fields, etc.)

**Production:** Use Keynote, Figma, or OBS with timed overlays; export as video segment

---

#### **Shot 5: Requirement Config (1:10–1:30)**

**Timecode:** 1:10–1:30  
**Narration:** Segment 04 (20s)  
**Action:** Display Mellea validation config

**Instructions:**
1. Show code block or config UI with requirements:
   ```
   word_count: { min: 50, max: 200 }
   required_fields: ["features", "benefit"]
   tone: "professional"
   ```
2. Highlight each requirement as narration mentions it
   - "word count range" → highlight `word_count`
   - "required fields" → highlight `required_fields`
   - "clarity score" → highlight `tone` or similar
3. Fade to next shot

---

#### **Shot 6: LangChain Code (1:30–1:50)**

**Timecode:** 1:30–1:50  
**Narration:** Segment 05 (20s)  
**Action:** Code editor showing LangChain + Mellea integration

**Instructions:**
1. Open code editor with LangChain chain definition
2. Scroll to / highlight the Mellea validator wrapper
3. Use syntax highlighting or color box to isolate Mellea-specific lines
4. Show the requirement definitions side-by-side or as comments
5. Keep visible for full 20 seconds; fade to demo execution

---

#### **Shot 7: Demo Attempt 1 — First Try Fails (1:50–2:10)**

**Timecode:** 1:50–2:10  
**Narration:** Segment 06 (15s) → Segment 07 opening (5s of "second try")  
**Action:** Terminal running LangChain chain; first output fails validation

**Instructions:**
1. Terminal is visible, ready to execute
2. **Record:** Run the chain (or play pre-recorded output)
3. **Show:** Output appears (e.g., "Great product" — 8 words)
4. **Show:** Validation check runs and FAILS (red text, "ERROR: word_count too low")
5. Overlay metric: "Attempt 1: FAILED — 45 words (need 50–200)"
6. Wait 1–2 seconds before moving to next attempt

---

#### **Shot 8: Demo Attempt 2 — Second Try Still Fails (2:10–2:30)**

**Timecode:** 2:10–2:30  
**Narration:** Segment 07 continued (15s)  
**Action:** Terminal showing retry with feedback; second attempt still fails

**Instructions:**
1. **Record:** Retry triggers; model receives feedback ("too short, add feature descriptions")
2. **Show:** Second output appears (longer, includes features, but missing benefit)
3. **Show:** Validation FAILS again (red text, "ERROR: missing benefit statement")
4. Overlay metric: "Attempt 2: FAILED — includes features, no benefit"
5. Pause 1–2 seconds

---

#### **Shot 9: Demo Attempt 3 — Passes (2:30–2:50)**

**Timecode:** 2:30–2:50  
**Narration:** Segment 07 + 08 (~25s)  
**Action:** Third attempt passes validation

**Instructions:**
1. **Record:** Retry with updated feedback
2. **Show:** Third output appears (complete, all requirements met)
3. **Show:** Validation PASSES (green checkmark, "VALIDATED ✓")
4. Overlay metric: "Attempt 3: PASSED — 180 words, all requirements met"
5. **Show:** Summary metrics appear:
   - Total time: 8 seconds
   - Total cost: $0.02
   - API calls: 3
   - Pass rate: 1/3
6. Hold for 2–3 seconds; fade to next section

---

#### **Shot 10: CrewAI Crew Definition (2:50–3:00)**

**Timecode:** 2:50–3:00  
**Narration:** Segment 09 opening (10s)  
**Action:** Code editor showing CrewAI crew with two agents

**Instructions:**
1. Open code editor with CrewAI crew definition
2. Show two agent tasks:
   - Agent A: Summarize under 100 words
   - Agent B: Format output as JSON
3. Highlight / zoom to show Mellea validators on each agent
4. Keep visible; narration describes what's happening

---

#### **Shot 11: CrewAI Execution (3:00–3:20)**

**Timecode:** 3:00–3:20  
**Narration:** Segment 09 conclusion (15s) + Segment 10 opening (5s)  
**Action:** Terminal running CrewAI crew; both agents executing with validation

**Instructions:**
1. **Record:** Run crew
2. **Show:** Agent A executes, generates summary, validation passes (green) on first try
3. **Show:** Agent B executes, generates JSON, validation fails on first try (red)
4. **Show:** Agent B retries, output corrected, validation passes (green)
5. Overlay metrics per agent (similar to LangChain demo)
6. Show final crew output: summary + JSON

---

#### **Shot 12: DSPy Program Definition (3:20–3:35)**

**Timecode:** 3:20–3:35  
**Narration:** Segment 10 (15s)  
**Action:** Code editor showing DSPy typed signature + Mellea validator

**Instructions:**
1. Open code editor with DSPy program
2. Show typed signature definition (inputs/outputs)
3. Show Mellea validation rules overlay:
   - Comprehensiveness threshold
   - Clarity threshold
4. Highlight how validation integrates with DSPy type system
5. Fade to execution

---

#### **Shot 13: DSPy Execution (3:35–3:50)**

**Timecode:** 3:35–3:50  
**Narration:** Segment 10 conclusion + Segment 11 opening (15s)  
**Action:** Terminal running DSPy program; validation checks executing

**Instructions:**
1. **Record:** Run DSPy program
2. **Show:** Output generated and validated
3. **Show:** Validation metrics (comprehensiveness score, clarity score)
4. **Show:** Output passes or fails; if fails, retry occurs
5. Display final validated output

---

#### **Shot 14: Tradeoff Graph (3:50–4:15)**

**Timecode:** 3:50–4:15  
**Narration:** Segment 11 (25s)  
**Action:** Graph showing validation strictness vs. latency/cost tradeoff

**Instructions:**
1. Display graph with:
   - X-axis: Validation strictness (low → high)
   - Y-axis: Latency + cost (low → high)
   - Curve showing exponential tradeoff
2. Annotate two zones:
   - "Skip validation" (e.g., casual dashboards)
   - "Strict validation" (e.g., production systems)
3. Highlight the "sweet spot" middle region
4. Optional: overlay use-case examples on the graph

**Production:** Use Keynote, Figma, or static image + narration

---

#### **Shot 15: CTA Slide (4:15–4:30)**

**Timecode:** 4:15–4:30  
**Narration:** Segment 12 (15s)  
**Action:** Speaker on camera or call-to-action slide

**Instructions:**
1. **Option A (Speaker):** Record speaker on camera delivering CTA directly
   - Light background, clear audio
   - Suggest: head-and-shoulders framing, 1080p
2. **Option B (Slide):** Static slide with:
   - Mellea logo
   - Text: "Try it yourself at mellea.ai"
   - Text: "LangChain • CrewAI • DSPy"
   - Text: "Link in the description"
3. Hold for full 15 seconds; fade to black with final logo

---

## Phase 3: Audio Sync & Post-Production

### Narration Audio Files (Pre-Generated)

Stored in `narration_audio/` with manifest:

| Segment | Filename | Duration | Timecode |
|---------|----------|----------|----------|
| 01 | `narration_01_hook.mp3` | 20s | 0:00–0:20 |
| 02 | `narration_02_problem.mp3` | 30s | 0:20–0:50 |
| 03 | `narration_03_pattern_1.mp3` | 10s | 0:50–1:00 |
| 04 | `narration_04_pattern_2.mp3` | 20s | 1:00–1:20 |
| 05 | `narration_05_demo_setup.mp3` | 10s | 1:45–1:55 |
| 06 | `narration_06_demo_attempt_1.mp3` | 15s | 1:55–2:10 |
| 07 | `narration_07_demo_attempt_2.mp3` | 20s | 2:10–2:30 |
| 08 | `narration_08_demo_results.mp3` | 20s | 2:30–2:50 |
| 09 | `narration_09_multi_agent.mp3` | 20s | 2:50–3:10 |
| 10 | `narration_10_dspy.mp3` | 20s | 3:10–3:30 |
| 11 | `narration_11_tradeoff.mp3` | 25s | 3:50–4:15 |
| 12 | `narration_12_cta.mp3` | 15s | 4:15–4:30 |

### Editing Timeline (Adobe Premiere / Final Cut / DaVinci Resolve)

1. **Import all video shots** from Phase 2
2. **Arrange on timeline** in sequence (Shot 1, 2, 3, ..., 15)
3. **Add narration audio tracks** — sync to timings above
4. **Adjust video clip duration** to match narration (trim/extend as needed)
5. **Add color correction:** Boost contrast, ensure code is readable
6. **Add captions:** Burn in all narration text + technical terms (LangChain, CrewAI, DSPy)
7. **Add music/ambient track** under narration:
   - Low-energy synth (0:00–3:50)
   - Subtle accent at each validation pass (0:05, 1:50, 3:35)
   - Kick/build at CTA (4:15–4:30)
8. **Add transitions:** Fade between major sections (0.5s cross-dissolve)
9. **Add text overlays:** Metrics, file paths, code highlights as documented in script

---

## Phase 4: QA Checklist

### Audio

- [ ] All 12 narration segments imported correctly
- [ ] No audio dropouts or glitches
- [ ] Narration timing matches video (no sync drift)
- [ ] Audio levels consistent (~-6dB peak, -18dB RMS dialogue)
- [ ] Background noise minimal

### Video

- [ ] All 15 shots in correct order
- [ ] No video glitches, frozen frames, or seek artifacts
- [ ] Terminal and code text readable at 1080p
- [ ] Color grading consistent across shots
- [ ] Metrics/annotations legible

### Sync

- [ ] Narration audio and video start simultaneously at 0:00
- [ ] No A/V desync detected during playback
- [ ] Transitions occur at intended timecodes
- [ ] Demo executions match narration descriptions

### Captions

- [ ] All narration text displayed as burned-in subtitles
- [ ] Technical terms highlighted or styled differently
- [ ] Caption timing synced to audio (not leading/lagging)
- [ ] Code snippets and file paths clearly visible

### Final Export

- [ ] Export at 1920×1080 (1080p H.264)
- [ ] Bitrate: 5–8 Mbps (YouTube quality)
- [ ] Audio: AAC, 128 kbps, stereo
- [ ] Filename: `agentic-framework-integrations-demo.mp4`
- [ ] Duration: 4:30 ± 1 second

---

## Phase 5: Distribution & Next Steps

### YouTube Upload

- [ ] Title: "Mellea: Structured Validation for LangChain, CrewAI, and DSPy"
- [ ] Description: (use /write-technical-blog or extract from blog post)
- [ ] Tags: `mellea`, `langchain`, `crewai`, `dspy`, `ai`, `validation`, `llm`
- [ ] Thumbnail: High-contrast frame from demo (red/green validation check)
- [ ] Playlist: Add to "Framework Integrations" series

### Social Media

- [ ] Tweet thread linking to video + blog post
- [ ] LinkedIn post with key takeaways
- [ ] Slack announcement in #announcements channel

### Metrics Tracking

- [ ] Set up YouTube Analytics dashboard
- [ ] Track: Views, watch time, click-through rate to mellea.ai
- [ ] Goal: Compare against previous demo video performance

---

## Resource Links

- **Narration Generator:** `generate_narration.py` (Python, requires API key)
- **Video Script:** `video-script-agentic-framework-integrations-demo.md`
- **Narration Segments:** `narration-segments.txt`
- **Recording Tools:**
  - ScreenFlow: https://www.screenflow.com
  - OBS Studio: https://obsproject.com
- **TTS Services:**
  - Google Cloud TTS: https://cloud.google.com/text-to-speech
  - ElevenLabs: https://elevenlabs.io
- **Royalty-Free Music:**
  - Epidemic Sound: https://www.epidemicsound.com
  - YouTube Audio Library: https://www.youtube.com/audio
  - Artlist: https://artlist.io

---

## Notes

- **Timing flexibility:** Narration duration is fixed (~4:30), but video clip duration can vary ±2s per shot without noticeable drift
- **Do-over permission:** If a screen recording glitches, just re-record that shot; rest of timeline remains untouched
- **Captioning:** Plan for 2–3 hours of caption timing if doing manually; use auto-captions and correct afterward
