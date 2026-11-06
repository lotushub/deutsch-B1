# Klar Deutsch B1 — offline German practice

Original English-language explanations with German examples: 12 lessons, 36 questions, 20 vocabulary cards, a reading text, browser-generated listening and three writing prompts. No account, package installation, build step, external library or database server is required.

## Start without installing anything

1. Download this repository using **Code → Download ZIP** on GitHub.
2. Extract the ZIP to a permanent folder on your computer.
3. Open `index.html` in Chrome, Edge, Firefox or Safari.
4. Bookmark the file. You can disconnect from the internet and continue learning.

You must download and extract the file: GitHub's HTML source view and some attachment previews do not run JavaScript.

## Recommended: a stable local address

If Python 3 is already installed, open a terminal in this folder and run:

- Windows: `py serve.py`
- macOS/Linux: `python3 serve.py`

Then open **http://127.0.0.1:8000** in your browser. The server listens only on your own computer, works without the internet and serves only this project folder. Keep the terminal open; press Ctrl+C to stop. Always use the same address, port and browser profile to keep the same saved progress.

Opening the file directly and opening the localhost address use separate browser storage. Export your progress before switching, then import it at the new address.

## How to learn

Select a section, open a lesson, select an answer and click **Check this answer**. Use **Check answers** after completing the lesson to save its score. Three correct answers mark a lesson mastered. Review vocabulary cards and write a draft in the writing workshop.

## Where your data lives

Course content is embedded in `index.html`. Best scores, vocabulary marks and writing drafts are stored in this browser profile's `localStorage`, under `klar-b1`. Nothing is uploaded to GitHub or any other server. The local Python server only serves files; it does not store your learning progress. Clearing site data or private browsing may erase progress. Direct file storage behavior varies by browser; prefer localhost for a stable origin.

Use **My progress → Export progress** regularly to download a JSON backup. **Import progress** restores that backup and replaces the current browser's saved scores and drafts. Keep backups outside the repository, especially if they contain personal writing. No automatic cross-device sync is included.

## Offline listening

All written lessons and exercises work offline. Listening uses the browser/operating system's speech engine. Install a German **offline** voice in your system's language/speech settings if one is available. Some browser voices require an internet connection; select an offline German voice when offered by your system. A transcript is always available. Speech may be processed by a remote speech provider when an online voice is used; avoid that voice if you want strictly offline audio.

## Files

- `index.html`: complete standalone application, styles, content and logic.
- `serve.py`: optional local-only server using Python's standard library.
- `.gitignore`: keeps progress backups and system files out of Git.
- `README.md`: these instructions.

This is B1-focused practice, not a complete B1 course or official exam. Content is original and not affiliated with Lingolia. There are no analytics or external assets. Do not commit progress backups or private writing.
