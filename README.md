# Klar Deutsch — start here

A German learning site for preparing for **Zertifikat Deutsch / telc Deutsch B1**.

You do **not** need to be a programmer. You do **not** need to install Python, Node.js, npm, REA, or a database to use it.

## Option 1: use the private website

1. Open [your private study site](https://klar-deutsch-b1-study-preview.bhuchungchungnga.chatgpt.site).
2. If asked, choose **Continue with ChatGPT** and use the same ChatGPT account that owns the site.
3. Start with **Exam home**. Choose **Study plan** for daily tasks or **Grammar practice** for the new question worksheets.

This option needs internet. Your learning progress is saved in that browser, not synced between devices.

## Option 2: run it on your computer — no installation

### Step 1: download the site

1. Open [the GitHub repository](https://github.com/lotushub/deutsch-B1).
2. Find the green **Code** button above the file list.
3. Click **Code**, then click **Download ZIP**.
4. Wait for the download to finish. It will usually be in your **Downloads** folder.

**Important:** clicking `index.html` on GitHub shows its source code. Download the ZIP first.

### Step 2: extract the ZIP

**On a Mac:**

1. Open **Finder → Downloads**.
2. Double-click the downloaded `.zip` file.
3. A folder appears, usually called `deutsch-B1-main`.
4. Move this folder to **Documents** so you can easily find it again.

**On Windows:**

1. Open **File Explorer → Downloads**.
2. Right-click the downloaded `.zip` file.
3. Choose **Extract All**, then **Extract**.
4. Move the extracted folder to **Documents**.

Do not run the site from inside the ZIP. Open the extracted folder.

### Step 3: open the learning site

1. Open the extracted folder.
2. Find **START-HERE.html** and double-click it.
3. Click **Open my German learning site** on the page that appears.
4. You should see the dark **Klar Deutsch** site and its exam dashboard.

You can also double-click **index.html** directly. If your computer opens a text editor or shows code, right-click `index.html`, choose **Open With**, and select **Chrome**, **Edge**, **Firefox**, or **Safari**.

Some systems hide the `.html` ending. The file may appear as `index` with the type **HTML document**.

### Step 4: study

1. Choose **Grammar practice** in the menu.
2. Open a worksheet, for example **Dative 1**.
3. Select an answer, then click **Check this answer** for feedback.
4. Complete all 12 questions and click **Check worksheet** to save the result.
5. Try **Type the answer** when you want a harder version.
6. Use **Retry missed questions** to review mistakes.

The workbook has **144 original questions** across 12 worksheets, including **48 dative-focused questions**. The language library also has 41 lessons / 291 questions, and exam practice has 60 original items.

### Step 5: use it without internet

After downloading and extracting, the lessons, worksheets, writing prompts, study plan and answer feedback work without internet. Keep the extracted folder on your computer.

These parts are different:

- Links to telc, Lingolia and German.net need internet. They are optional resources, not offline pages.
- Browser-generated listening needs an installed offline German voice. Some voices require internet.
- Official telc PDF/audio files can work offline after you download them. See below.

## Save and back up your progress

Progress is automatically saved in your **browser storage**, on this computer and in this browser profile. There is no separate database to install.

To make a backup:

1. Choose **My progress** in the site menu.
2. Click **Export progress**.
3. Keep the downloaded `klar-progress-...json` file somewhere safe.

To restore a backup:

1. Open the site and go to **My progress**.
2. Find **Import progress** and choose your saved `.json` backup.
3. Confirm that you want to replace the current progress.

Export before updating, moving folders, changing browsers, clearing browsing data, or switching between the private website and your local copy. Private/incognito browsing may delete progress when closed. Browser storage for directly opened files varies; keep backups regularly.

## Get official telc audio and PDFs for offline use

1. While online, choose **Resources** in the site.
2. Open the official telc exam page and download the free mock test and matching audio.
3. Extract that download, just as you extracted this site.
4. Return to **Mock companion** in Klar Deutsch.
5. Click the file selector and select the PDF/audio files from your computer.
6. You can now use those selected local files offline. Reselect them after reopening the site.

The site does not upload your files. You can also open the PDF and audio in your normal computer applications. Follow the official recording's instructions for a timed rehearsal.

## If something does not work

| Problem | Try this |
| --- | --- |
| A menu button does nothing | Make sure you have downloaded the latest ZIP. Open the extracted `index.html` in a normal browser, not a GitHub source page, attachment preview, or text editor. |
| The private website shows an old version | Refresh it. On Mac press **Command + Shift + R**; on Windows press **Ctrl + Shift + R**. |
| A telc, Lingolia or German.net link does not load | Connect to the internet. External publishers may require an account for some materials. |
| I see code instead of the site | Right-click `index.html` → **Open With** → your web browser. |
| The site is blank | Extract the ZIP first and open `index.html`. If necessary, try another browser with JavaScript enabled. |
| No answer is marked | Choose/type an answer first, then use **Check this answer**. For a saved worksheet score, answer every question. |
| Audio does not play | Use the transcript, install an offline German voice through your system settings, or play the downloaded official audio in your usual audio player. |
| My progress is missing | Open the same file/location in the same browser profile, or import your latest backup. |

## Optional: a stable local web address

**Skip this section if double-clicking works.** It is useful if your browser does not reliably save progress for local files. Python 3 must already be installed.

**Mac:** open Terminal, type `cd ` (including the space), drag the extracted site folder into Terminal, then press Return. Run:

```sh
python3 serve.py
```

**Windows:** open the extracted folder, click the File Explorer address bar, type `cmd`, then press Enter. Run:

```bat
py serve.py
```

Then open **http://127.0.0.1:8000** in your browser. Keep the Terminal/Command Prompt window open while studying. Press **Ctrl + C** in that window to stop the server. It works without internet and listens only on your computer. Always use the same address and port for the same saved progress.

If the command is not found, use the double-click method above; you do not have to install Python. If the port is busy, close another copy of the local server and try again.

## How to update later

1. Export your progress from the version you are currently using.
2. Download and extract the new ZIP from GitHub.
3. Open the new version's `index.html`.
4. Import your progress backup.
5. Keep the old folder until you have confirmed your progress is restored.

Do not put your progress backups, personal writing or downloaded publisher books/audio into the public GitHub repository.

## Inside each grammar lesson

Every grammar lesson now has **9 questions** (previously 3). Before the questions, read **How this topic works**: three steps, explained examples and a common mistake. The 28 grammar lessons provide 252 questions in total. The separate workbook provides another 144 questions.

Old three-question scores remain labelled as earlier-edition results until you complete the expanded lesson. Export/import still works.

## What is included

- 28-day suggested study plan with selectable daily study budget.
- 12 grammar worksheets / 144 original questions, with answer choices, typed answers and mistake review.
- 41 language lessons / 291 questions and 40 themed vocabulary cards.
- 60 original objective exam-format items.
- Four timed email tasks with model responses, and speaking prompts for all three parts.
- Local official-mock PDF/audio companion, assessed-score records and progress backup/import.

The app does not predict a pass, automatically assess writing or speaking, or replace an official mock and human feedback. From A2, four weeks is a demanding timeline. Use your baseline results to prioritise.

## For someone editing the code (optional)

- `index.html`: ready-to-use offline site; you do not need to build it after downloading.
- `START-HERE.html`: beginner start page.
- `src/app.js`: editable lessons, exercises and application code.
- `src/template.html`: page layout and styling.
- `build.py`: rebuilds `index.html` after source edits, using Python 3 only.
- `serve.py`: optional local server.
- [SOURCES.md](SOURCES.md): source references, material boundaries and verification limits.

After editing the source, run `python3 build.py` (Mac/Linux) or `py build.py` (Windows), then commit the rebuilt HTML with its sources. The application has no npm dependencies. REA was used as an inspection tool during development, not as a runtime requirement.

This independent site is not affiliated with or endorsed by telc, Lingolia or German.net. The practice material is original; publisher exercise banks and recordings are not redistributed.
