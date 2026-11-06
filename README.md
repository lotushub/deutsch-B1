<div align="center">

# Klar Deutsch: telc B1 Preparation

### A focused offline preparation space for Zertifikat Deutsch / telc Deutsch B1.

**28-day study plan · 60 original exam-format items · 41 language lessons**

[Quick start](#start-without-installing-anything) · [Exam preparation](#exam-preparation) · [Offline use](#recommended-a-stable-local-address) · [Backups](#where-your-data-lives) · [Sources & REA](SOURCES.md)

</div>

> **Your target:** standard telc Deutsch B1, starting from A2, with an exam within four weeks. The plan is editable through daily study-time choices. This is a demanding timeline: start with an official mock, prioritise weak areas, and obtain writing/speaking feedback. The app cannot guarantee or predict a pass.

## Exam preparation

| Section | What it does |
| --- | --- |
| Exam home | Exam structure and preparation dashboard |
| Study plan | 28 suggested days; selectable 30/60/90/120-minute study budget; completion tracking |
| Exam practice | 8 original drills, 60 items: reading headings/details/adverts; two connected-text language-element tasks; three true/false listening tasks |
| Exam writing | 4 original four-point emails; 30-minute timer; saved drafts; self-review; original model responses |
| Speaking | All 3 parts: getting acquainted, discussing opinions and planning together; 5 prompt sets and partner cards |
| Mock companion | Open your own downloaded official PDF/audio locally; stage timers; record assessed mock scores |
| My mistakes | Missed items from latest complete drill attempts, with explanations and personal error notes |
| Resources | telc official resources and supplementary Lingolia links, with reuse/offline guidance |
| Language library | Existing 41 lessons / 123 questions; 40 themed vocabulary cards; reading, listening and writing support |

**Official material and original practice are different.** The drill bank is not a calibrated mock exam. Synthetic speech is not authentic exam audio. Writing checklists do not grade language, and speaking cards do not evaluate pronunciation or replace a partner. Use the official mock/recording and assessed writing/speaking for a meaningful benchmark. Consult [SOURCES.md](SOURCES.md) for source links, scoring facts, limitations and REA inspection results.

The original 41 lessons retain their identifiers and browser storage key. Previous progress backups remain importable; new backups also include study days, exam-drill attempts, error notes, exam drafts and mock records.

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

Course content is embedded in `index.html`. Lesson scores, vocabulary marks, writing drafts, study-day ticks, exam-drill results, error notes and mock records are stored in this browser profile's `localStorage`, under `klar-b1`. Nothing is uploaded to GitHub or any other server. The local Python server only serves files; it does not store your learning progress. Clearing site data or private browsing may erase progress. Direct file storage behavior varies by browser; prefer localhost for a stable origin.

Use **My progress → Export progress** regularly to download a JSON backup. **Import progress** restores that backup and replaces the current browser's saved progress, drafts and exam records. Keep backups outside the repository, especially if they contain personal writing. No automatic cross-device sync is included.

## Offline listening

All written lessons and exercises work offline. Listening uses the browser/operating system's speech engine. Install a German **offline** voice in your system's language/speech settings if one is available. Some browser voices require an internet connection; select an offline German voice when offered by your system. A transcript is always available. Speech may be processed by a remote speech provider when an online voice is used; avoid that voice if you want strictly offline audio.

## Files and editing

- `index.html`: built standalone application; open this to study. No build is needed after downloading.
- `src/app.js`: editable content and JavaScript logic.
- `src/template.html`: editable HTML shell and responsive dark CSS.
- `build.py`: embeds the source into the standalone HTML using Python's standard library.
- `serve.py`: optional local-only HTTP server using Python's standard library.
- `SOURCES.md`: official references, material boundaries, REA inspection and verification limits.
- `.gitignore`: excludes progress backups, private drafts and personal study materials.

After editing source files, run `python3 build.py` (macOS/Linux) or `py build.py` (Windows). Commit the rebuilt `index.html` together with the source changes. Node.js, npm and REA are not required to use or rebuild the app.

## Official materials offline

1. Open **Resources** while connected and download the official telc mock bundle from the publisher.
2. Extract it into a folder outside this repository.
3. In **Mock companion**, select the matching PDF and audio files from your computer.
4. Use the official sequence and audio instructions during your rehearsal. Do not pause or reveal answers when simulating the exam.
5. Mark objective tasks using the matching answer key and obtain criterion-based writing/speaking feedback before recording those points.

The site uses local file URLs for selected media; it does not upload their contents. Reselect files after reloading the page. Unsupported media can be opened in your normal PDF/audio application. A record with missing assessed scores is shown as incomplete, not zero or a pass.

## Privacy and offline boundaries

The app has no account, backend database, analytics or remote grading. Ordinary study progress is saved in browser storage. Local PDF/audio selections stay in session memory; the app does not persist those files. External resource links need internet. Browser speech may use an online provider unless a local German voice is installed; real official audio played from a local file works offline when the browser supports its codec.

This independent preparation aid is not affiliated with or endorsed by telc or Lingolia. Do not commit personal data or publisher materials to a public repository. No complete publisher course, paid question bank, official answer key or recording is distributed here.
