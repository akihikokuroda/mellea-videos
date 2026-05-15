# Video Script: Mellea + Agentic Frameworks

**Mode:** demo  
**Target length:** 4:30  
**Source:** https://mellea.ai/blogs/agentic-framework-integrations/  
**One-line thesis:** Mellea adds automatic validation and retries to LangChain, CrewAI, and DSPy so your AI agents produce reliable, spec-compliant outputs without manual fixes.

---

## Cold Open / Hook  (0:00–0:20, ~20s)

[SHOW: terminal running a LangChain chain, output fails validation, retries, and passes]

You ship an AI agent to production. It works 90% of the time. (pause) The other 10%? Invalid output. Crashed downstream systems. Manual fixes in Slack at 3am.

Mellea stops that. (emphasis)

[SHOW: terminal output with validation results—pass/fail status, retry count]

---

## Problem: Unvalidated Outputs Break Prod  (0:20–0:50, ~30s)

[CODE: LangChain example, basic chain without validation]

Most AI frameworks—LangChain, CrewAI, DSPy—are great at orchestration. But they ship outputs without checking if they're actually (slow down) *good enough* for your use case.

[SHOW: example of bad output: too short, missing required fields, wrong format]

Your agent returns something that doesn't meet your requirements. Downstream code breaks. You're back-filling fixes in production.

---

## The Pattern: Instruct, Validate, Repair  (0:50–1:45, ~55s)

[SLIDE or B-ROLL: flow diagram showing four steps]

Mellea adds one pattern to every framework. (pause) Generate output. Validate it against your spec. If it fails—retry with feedback. Return the best result.

[CODE: Mellea validation config in code editor, showing requirements]

You define what "good enough" means. A word count range. Required fields. Clarity score. Anything measurable. (pause) It's just Python.

[CODE: LangChain + Mellea integration, highlight the retry loop]

Mellea wraps your model and handles the rest. Generate, check, retry, done.

[SHOW: terminal output showing three retries, final pass with green checkmark]

---

## Demo: LangChain + Structured Validation  (1:45–2:50, ~1:05)

[SCREEN: code editor with LangChain chain + Mellea validator]

Product descriptions with Mellea validation.

[CODE: highlight the Mellea wrapper and requirement definitions]

Requirements: between 50 and 100 words, mention at least two features, include a benefit statement.

[SHOW: running the chain]

First try: validation fails. Output is too long.

[SHOW: retry with feedback injected into prompt]

Second try: still too long. Validation fails again.

[SHOW: third try passes]

Third try: (emphasis) passes. Mellea returns a spec-compliant output that meets all requirements.

[SHOW: terminal output with timing]

Three attempts in about 5 seconds total. Mellea automated the retry loop so we get a working result without manual intervention.

---

## Beyond Single Chains: Multi-Agent Validation  (2:50–3:50, ~1:00)

[CODE: CrewAI example with two agents]

Multi-agent systems? Each agent has its own output spec.

[SHOW: CrewAI crew definition with Mellea validators on two different agents]

Mellea validates each agent independently. Agent A must produce a summary under 100 words. Agent B must format output as JSON.

[SHOW: both agents running, both validating independently]

Agent A passes on first try. Agent B fails twice, then passes on the third attempt.

[CODE: DSPy example with Mellea validation on a typed signature]

DSPy does typed signatures, but no quality guarantees. Mellea adds them.

[SHOW: DSPy program with Mellea validator, running through examples]

We validate the structured output meets our comprehensiveness and clarity thresholds, all within DSPy's type system.

---

## The Tradeoff: Reliability vs. Latency  (3:50–4:15, ~25s)

[SLIDE or B-ROLL: graph showing cost and latency vs. validation strictness]

Validation adds latency and API cost. Tighter specs mean more retries.

(casual) Not every use case. If you're generating casual summaries for an internal dashboard, skip it.

But if bad output breaks downstream systems or wastes human time? (emphasis) Validation pays for itself.

---

## CTA  (4:15–4:30, ~15s)

[CUT TO: speaker on camera or Mellea website hero]

Try it yourself. Head to mellea.ai, grab the framework integration you use—LangChain, CrewAI, or DSPy—and add one validation layer to your next chain.

(pause)

Link in the description.

---

## Shot List (appendix)

- 0:00 — terminal, dark theme, LangChain chain running, output appears and fails red validation check
- 0:05 — terminal retries, second attempt shows yellow warning, third attempt passes green
- 0:20 — terminal output showing validation pass/fail status and retry count
- 0:30 — code editor with basic LangChain chain (no Mellea)
- 0:35 — example of invalid output: "Great product!" (8 words, should be 50+)
- 0:50 — flow diagram: four boxes left-to-right, "Generate → Validate → Retry? → Return"
- 1:00 — code editor showing Mellea validation config (word count, required fields, clarity thresholds)
- 1:15 — LangChain code with Mellea wrapper highlighted
- 1:30 — terminal execution, first attempt (45 words)
- 1:40 — terminal, second attempt (all features, no benefit)
- 1:50 — terminal, third attempt passes (green checkmark)
- 2:00 — terminal output: "3 attempts, 12 seconds total"
- 2:30 — CrewAI crew definition with two agent tasks
- 2:45 — terminal running both agents, both showing validation status
- 3:10 — DSPy code with typed signature and Mellea validator
- 3:30 — DSPy execution output with validation results
- 3:50 — graph: X-axis "validation strictness", Y-axis "latency / cost", curve showing tradeoff
- 4:15 — speaker on camera or Mellea.ai hero image, CTA slide with link

## Notes for the Editor

- **Suggested music:** minimal, low-energy synth under narration; kick or swell at each successful validation pass (0:05, 1:50, 3:35)
- **Suggested captions:** burn all narration; highlight the word counts and error messages on-screen so viewers see validation failure and recovery without needing sound
- **Color coding:** make passing validations green, failing validations red, in-progress retries yellow—give visual feedback even without reading terminal text
- **Pacing:** each retry cycle (generate → fail → feedback → retry → pass) should feel like progress, not drag; 3–5 seconds per cycle
- **Watch for:** 
  - Dead air in the "first try, fails" section—move briskly through the retry loop
  - Code on screen should be large enough to read from phone; consider code zoom or syntax highlighting overlay
  - Ensure timing is visible in terminal output; add overlay text if terminal text is too small
