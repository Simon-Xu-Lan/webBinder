from pathlib import Path


AUTH_DIR = Path("auth")
AUTH_FILE = AUTH_DIR / "auth.json"


def save_session(context):
    AUTH_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    context.storage_state(
        path=str(AUTH_FILE)
    )

    print(
        f"Authentication session saved to: {AUTH_FILE}"
    )