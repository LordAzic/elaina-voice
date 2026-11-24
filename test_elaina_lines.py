import base64
from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})
ELAINA_VOICE_ID = "voice_go6t98hedtxo"

tests = [
    (
        "smug",
        "brightened pitch, playful lilt, and a subtle vocal smile",
        "Who is the brilliant witch whose ashen hair shines even in the afternoon sun? <short pause> That's right, it's me."
    ),
    (
        "annoyed",
        "flat, clipped, slightly lowered pitch, and dry",
        "<sigh> I'd prefer to be paid to take it off your hands, actually."
    ),
    (
        "banter",
        "breezy, melodic, and lightly detached",
        "If possible, I'd like to make money without working."
    ),
]

for label, style, line in tests:
    interaction = client.interactions.create(
        model="gemini-3.8-flash-tts",
        input=[{
            "type": "user_input",
            "content": [{
                "type": "text",
                "text": line,
                "annotations": [{
                    "type": "speech_metadata",
                    "speaker": "Elaina",
                    "style": style,
                }],
            }],
        }],
        generation_config={
            "speech_config": [{"voice": ELAINA_VOICE_ID}]
        },
    )

    raw_data = interaction.output_audio.data
    audio_bytes = base64.b64decode(raw_data) if isinstance(raw_data, str) else raw_data

    filename = f"elaina_{label}.wav"
    with open(filename, "wb") as f:
        f.write(audio_bytes)
    print(f"Saved {filename}")