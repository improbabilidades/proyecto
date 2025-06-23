import httpx
from httpx_sse import connect_sse
import json


def handle_state_message(data):
    try:
        payload = json.loads(data)
        state = int(payload.get("state"))
        if isinstance(state, int) and state >= 0:
            print(f"Nuevo estado: {state}")
    except (json.JSONDecodeError, TypeError):
        print("Formato de mensaje inválido:", data)


def main():
    url = "https://web.kalouk.xyz/sse/"
    with httpx.Client() as client:
        with connect_sse(client, "GET", url) as event_source:
            for sse in event_source.iter_sse():
                if sse.data:
                    handle_state_message(sse.data)


if __name__ == "__main__":
    main()
