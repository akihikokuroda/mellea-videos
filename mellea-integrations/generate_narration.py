#!/usr/bin/env python3
"""
Generate narration audio for video script.
Supports: macOS say command, Google Cloud TTS, ElevenLabs API.

Usage: python generate_narration.py [--service say|google|elevenlabs]

--service say          Use macOS say command (free, built-in, no setup)
--service google       Use Google Cloud TTS (requires credentials)
--service elevenlabs   Use ElevenLabs (requires API key)
"""

import os
import sys
import subprocess
from pathlib import Path

# Narration segments with timing metadata
SEGMENTS = [
    {
        "id": "01_hook",
        "timecode": "0:00–0:20",
        "duration_s": 20,
        "text": "You ship an AI agent to production. It works 90% of the time. [pause] The other 10%? Invalid output. Crashed downstream systems. Manual fixes in Slack at 3am.\n\nMellea stops that.",
    },
    {
        "id": "02_problem",
        "timecode": "0:20–0:50",
        "duration_s": 30,
        "text": "Most AI frameworks—LangChain, CrewAI, DSPy—are great at orchestration. But they ship outputs without checking if they're actually good enough for your use case.\n\nYour agent returns something that doesn't meet your requirements. Downstream code breaks. You're back-filling fixes in production.",
    },
    {
        "id": "03_pattern_1",
        "timecode": "0:50–1:00",
        "duration_s": 10,
        "text": "Mellea adds one pattern to every framework. [pause] Generate output. Validate it against your spec. If it fails—retry with feedback. Return the best result.",
    },
    {
        "id": "04_pattern_2",
        "timecode": "1:00–1:20",
        "duration_s": 20,
        "text": "You define what good enough means. A word count range. Required fields. Clarity score. Anything measurable.\n\nMellea wraps your model and handles the rest. Generate, check, retry, done.",
    },
    {
        "id": "05_demo_setup",
        "timecode": "1:45–1:55",
        "duration_s": 10,
        "text": "Product descriptions with Mellea validation.\n\nRequirements: between 50 and 200 words, mention at least two features, include a benefit statement.",
    },
    {
        "id": "06_demo_attempt_1",
        "timecode": "1:55–2:10",
        "duration_s": 15,
        "text": "First try: [pause] 45 words. Too short. Validation fails.",
    },
    {
        "id": "07_demo_attempt_2",
        "timecode": "2:10–2:30",
        "duration_s": 20,
        "text": "Second try: includes features but no benefit. Still fails.\n\nThird try: passes. We got a spec-compliant output in three attempts.",
    },
    {
        "id": "08_demo_results",
        "timecode": "2:30–2:50",
        "duration_s": 20,
        "text": "8 seconds and one extra API call. Bad outputs cost you hours in fixes—this pays for itself.",
    },
    {
        "id": "09_multi_agent",
        "timecode": "2:50–3:10",
        "duration_s": 20,
        "text": "Multi-agent systems? Each agent has its own output spec.\n\nMellea validates each agent independently. Agent A must produce a summary under 100 words. Agent B must format output as JSON.\n\nAgent A passes on first try. Agent B retries once and passes.",
    },
    {
        "id": "10_dspy",
        "timecode": "3:10–3:30",
        "duration_s": 20,
        "text": "DSPy does typed signatures, but no quality guarantees. Mellea adds them.\n\nWe validate the structured output meets our comprehensiveness and clarity thresholds, all within DSPy's type system.",
    },
    {
        "id": "11_tradeoff",
        "timecode": "3:50–4:15",
        "duration_s": 25,
        "text": "Validation adds latency and API cost. Tighter specs mean more retries.\n\nNot every use case. If you're generating casual summaries for an internal dashboard, skip it.\n\nBut if bad output breaks downstream systems or wastes human time? Validation pays for itself.",
    },
    {
        "id": "12_cta",
        "timecode": "4:15–4:30",
        "duration_s": 15,
        "text": "Try it yourself. Head to mellea.ai, grab the framework integration you use—LangChain, CrewAI, or DSPy—and add one validation layer to your next chain.\n\n[pause]\n\nLink in the description.",
    },
]


def generate_with_macos_say(segments, output_dir="narration_audio"):
    """Generate MP3 files using macOS say command (built-in, no API required)."""
    os.makedirs(output_dir, exist_ok=True)

    # Check if ffmpeg is available (needed to convert AIFF to MP3)
    try:
        subprocess.run(["ffmpeg", "-version"], capture_output=True, check=True)
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("ffmpeg not found. Install with: brew install ffmpeg")
        return False

    manifest = []

    for segment in segments:
        # Clean up brackets for speech
        text = segment["text"].replace("[pause]", " ").replace("[emphasis]", " ")

        segment_id = segment["id"]
        aiff_file = os.path.join(output_dir, f"narration_{segment_id}.aiff")
        mp3_file = os.path.join(output_dir, f"narration_{segment_id}.mp3")

        print(f"Generating {segment_id}...", end=" ")

        try:
            # Step 1: Generate AIFF using macOS say command
            subprocess.run(
                ["say", "-o", aiff_file, text],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            # Step 2: Convert AIFF to MP3 using ffmpeg
            subprocess.run(
                ["ffmpeg", "-i", aiff_file, "-q:a", "5", "-codec:a", "libmp3lame", mp3_file],
                check=True,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )

            # Clean up AIFF (optional, keep for now)
            # os.remove(aiff_file)

            mp3_size = os.path.getsize(mp3_file)
            print(f"✓ ({mp3_size} bytes)")

            manifest.append({
                "segment_id": segment_id,
                "timecode": segment["timecode"],
                "duration_s": segment["duration_s"],
                "filename": f"narration_{segment_id}.mp3",
                "filepath": mp3_file,
            })

        except subprocess.CalledProcessError as e:
            print(f"✗ Error: {e}")
        except Exception as e:
            print(f"✗ Error: {e}")

    return manifest if manifest else False


def generate_with_google_tts(segments, output_dir="narration_audio"):
    """Generate MP3 files using Google Cloud Text-to-Speech."""
    try:
        from google.cloud import texttospeech
    except ImportError:
        print("Google Cloud TTS not installed. Install with:")
        print("  pip install google-cloud-texttospeech")
        return False

    os.makedirs(output_dir, exist_ok=True)
    client = texttospeech.TextToSpeechClient()

    manifest = []

    for segment in segments:
        # Clean up brackets for TTS
        text = segment["text"].replace("[pause]", " ").replace("[emphasis]", " ")

        synthesis_input = texttospeech.SynthesisInput(text=text)

        voice = texttospeech.VoiceSelectionParams(
            language_code="en-US",
            name="en-US-Neural2-C",  # Professional male voice
            ssml_gender=texttospeech.SsmlVoiceGender.MALE,
        )

        audio_config = texttospeech.AudioConfig(
            audio_encoding=texttospeech.AudioEncoding.MP3,
            speaking_rate=1.0,  # Adjust for pacing
        )

        print(f"Generating {segment['id']}...", end=" ")

        try:
            response = client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config,
            )

            filename = f"narration_{segment['id']}.mp3"
            filepath = os.path.join(output_dir, filename)

            with open(filepath, "wb") as out:
                out.write(response.audio_content)

            print(f"✓ ({os.path.getsize(filepath)} bytes)")

            manifest.append({
                "segment_id": segment["id"],
                "timecode": segment["timecode"],
                "duration_s": segment["duration_s"],
                "filename": filename,
                "filepath": filepath,
            })
        except Exception as e:
            print(f"✗ Error: {e}")

    return manifest


def generate_with_elevenlabs(segments, output_dir="narration_audio", api_key=None):
    """Generate MP3 files using ElevenLabs API."""
    try:
        import requests
    except ImportError:
        print("requests library not installed. Install with: pip install requests")
        return False

    if not api_key:
        api_key = os.getenv("ELEVENLABS_API_KEY")
        if not api_key:
            print("ElevenLabs API key not found. Set ELEVENLABS_API_KEY environment variable.")
            return False

    os.makedirs(output_dir, exist_ok=True)

    # ElevenLabs endpoint
    url = "https://api.elevenlabs.io/v1/text-to-speech"
    headers = {"xi-api-key": api_key, "Content-Type": "application/json"}

    # Use a professional voice ID (example: Adam)
    voice_id = "pNInz6obpgDQGcFmaJgB"

    manifest = []

    for segment in segments:
        # Clean up brackets for TTS
        text = segment["text"].replace("[pause]", " ").replace("[emphasis]", " ")

        payload = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.75,
            },
        }

        print(f"Generating {segment['id']}...", end=" ")

        try:
            response = requests.post(f"{url}/{voice_id}", json=payload, headers=headers)

            if response.status_code == 200:
                filename = f"narration_{segment['id']}.mp3"
                filepath = os.path.join(output_dir, filename)

                with open(filepath, "wb") as out:
                    out.write(response.content)

                print(f"✓ ({os.path.getsize(filepath)} bytes)")

                manifest.append({
                    "segment_id": segment["id"],
                    "timecode": segment["timecode"],
                    "duration_s": segment["duration_s"],
                    "filename": filename,
                    "filepath": filepath,
                })
            else:
                print(f"✗ HTTP {response.status_code}: {response.text}")
        except Exception as e:
            print(f"✗ Error: {e}")

    return manifest


def save_manifest(manifest, output_dir="narration_audio"):
    """Save manifest JSON for post-production workflow."""
    import json

    manifest_path = os.path.join(output_dir, "narration_manifest.json")
    with open(manifest_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"\nManifest saved to {manifest_path}")
    return manifest_path


def main():
    service = "say"  # Default to macOS say (easiest, no setup)

    if "--service" in sys.argv:
        idx = sys.argv.index("--service")
        if idx + 1 < len(sys.argv):
            service = sys.argv[idx + 1]

    print(f"Generating narration with {service} TTS...")
    print(f"Total segments: {len(SEGMENTS)}")
    print()

    if service == "say":
        manifest = generate_with_macos_say(SEGMENTS)
    elif service == "elevenlabs":
        manifest = generate_with_elevenlabs(SEGMENTS)
    elif service == "google":
        manifest = generate_with_google_tts(SEGMENTS)
    else:
        print(f"Unknown service: {service}")
        print("Supported: say (macOS), google, elevenlabs")
        return 1

    if manifest:
        save_manifest(manifest)
        print(f"\n✓ Generated {len(manifest)} audio files")
        print(f"Output directory: narration_audio/")
        return 0
    else:
        print("\n✗ No files generated. Check API keys or ffmpeg installation.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
