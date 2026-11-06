<div align="center">

# Klar Deutsch: Your Offline German B1 Library

### Grammar, vocabulary, reading, listening and writing — in one local site.

**41 lessons · 123 interactive questions · 40 vocabulary cards · No account required**

[Quick start](#start-without-installing-anything) · [Course contents](#course-contents) · [Local server](#recommended-a-stable-local-address) · [Progress & backups](#where-your-data-lives) · [Offline listening](#offline-listening)

</div>

> **Offline first:** download this repository, extract it, and open `index.html`. All written lessons and exercises run on your computer. Listening depends on the German speech voices available on your device.

A dark learning interface with a topic-based structure, search, explanatory feedback, themed vocabulary cards and mixed practice. Original B1-focused content with core grammar revision; not affiliated with Lingolia and not a reproduction of its course or paid exercises.

## Course contents

| Section | Included |
| --- | --- |
| Grammar | 28 lessons across tenses, verbs, nouns/articles, pronouns, adjectives, adverbs, prepositions and sentence structure |
| Vocabulary | 40 word cards across 7 themes, plus 3 guides on dates/times, confusing words and everyday expressions |
| Reading | 4 texts: a new city, a repair request, workplace arrangements and a community garden |
| Listening | 4 messages: an appointment change, a train announcement, a course enquiry and weekend plans |
| Writing school | 2 lessons: punctuation/capitalisation and formal email structure |
| Writing workshop | 3 writing prompts, self-review checklist, saved drafts and text download |
| Mixed practice | 10 randomly selected grammar/vocabulary questions per review, with explanations and links back to lessons |
| Contents | Searchable index of every lesson |
| My progress | Best lesson scores, mastery tracking and JSON backup/import |

Existing progress from the previous 12-lesson version remains compatible: the first 12 lesson identifiers and the browser storage key are unchanged. Added lessons begin uncompleted.

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
