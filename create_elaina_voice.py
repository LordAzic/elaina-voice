import base64
from google import genai

client = genai.Client(http_options={"api_version": "v1beta"})

voice = client.voices.create(
    store=True,
    voice={
        "model": "gemini-3.8-flash-tts",
        "type": "prompted",
        "display_name": "Elaina (Ashen Witch)",
        "gender": "female",
        "language_code": "en-US",
        "prompted": {
            "input": (
                "A poised young woman around eighteen with a clear, bright mid-high "
                "feminine voice, crisp articulation, and an airy, melodic timbre. "
                "She speaks with an unhurried, lightly cultured cadence that balances "
                "effortless refinement with dry, understated composure."
            )
        },
    },
)

print("SAVE THIS VOICE ID:", voice.id)

if voice.sample_audio and voice.sample_audio.data:
    with open("elaina_audition.wav", "wb") as f:
        f.write(base64.b64decode(voice.sample_audio.data))
    print("Saved elaina_audition.wav!")