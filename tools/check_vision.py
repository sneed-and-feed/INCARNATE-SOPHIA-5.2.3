import os
from google import genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("SOPHIA_API_KEY") or os.getenv("GOOGLE_AI_KEY") or os.getenv("GOOGLE_API_KEY")

if not api_key:
    print("❌ [ERROR] No API Key found in Environment.")
else:
    client = genai.Client(api_key=api_key)

    print("--- [OCULAR DIAGNOSTIC] AVAILABLE MODELS ---")
    try:
        for m in client.models.list():
            actions = getattr(m, 'supported_actions', [])
            if 'generateContent' in actions:
                print(f"👁️  {m.name}")
    except Exception as e:
        print(f"❌ CONNECTION FAILED: {e}")
