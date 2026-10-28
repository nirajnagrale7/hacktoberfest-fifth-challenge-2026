# Echoes

Echoes is a local-first writing companion for remembering someone or turning a
personal memory into a gentle ghost story. Pick a writing style, share only the
details you choose, and review the result before downloading it.

## Run locally

1. Install [Ollama](https://ollama.com/) and download an open-weight model:

   ```powershell
   ollama pull qwen2.5:3b
   ```

2. In this folder, install the app and start it:

   ```powershell
   python -m pip install -r requirements.txt
   streamlit run app.py
   ```

3. Open the local Streamlit URL, enter a memory, select a writing style, and
   choose **Let the story take shape**.

Ollama must be running locally. The initial model download needs internet; after
that, generation runs on your computer without a hosted AI API.

## Privacy

- The text is sent only to Ollama at `localhost`; Echoes has no cloud service.
- Echoes does not write memories or generated stories to an app database.
- The result stays in the current app session unless you choose to download it.
- The model is asked not to invent personal facts or present fiction as truth.

Use the model output as a draft: edit or discard anything that does not feel
true to you. Echoes is a creative writing tool, not a way to contact someone
who has died.

## Tests

Run the standard-library tests:

```powershell
python -m unittest -v
```

## Why open innovation matters

Memories and family stories are personal. Running an open-weight model locally
keeps those words on the user's own computer instead of sending them to a
hosted AI provider. Once the model is downloaded, the tool works offline with
no per-story API charge. The prompt and model choice can be inspected, adapted,
or replaced.
