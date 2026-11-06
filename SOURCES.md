# Sources, material boundaries and review

Exam target: **Zertifikat Deutsch / telc Deutsch B1** (general German). This is not DTZ A2–B1, Deutsch-Test für den Beruf B1, or telc Deutsch A2·B1.

Checked: **6 November 2026**.

## Official exam references

- [telc exam overview](https://www.telc.net/en/language-examinations/certificate-exams/german/certificate-german-telc-german-b1/): exam components and timings; free official mock and audio download.
- [Official mock download bundle](https://www.telc.net/fileadmin/user_upload/mock_exams/Deutsch/telc_deutsch_b1.zip): linked by the exam overview. Download from the publisher for personal preparation; extract on your own computer. The site can open your selected local files.
- [Official mock booklet](https://shop.telc.net/media/catalog/product/file/telc_deutsch_b1_zd_uebungstest_1.pdf): standard B1 task types, marking guidance and score thresholds. Publisher booklet, 2020 revised edition; exam format cross-checked with the current overview.
- [telc teaching-material downloads](https://www.telc.net/lehrmaterialien/downloadbereich/): supplementary publisher material. Check the exact exam variant and match audio to its booklet.

The overview specifies a shared 90-minute reading/language-elements block, listening of approximately 30 minutes, 30-minute writing and approximately 15-minute paired speaking after 20 minutes preparation. The mock booklet describes an email task with four guiding points. Its scoring section uses maximums of reading 75, language elements 30, listening 75, writing 45 and speaking 75; written and oral thresholds are separate (135/225 and 45/75). These are reference values for the user-entered mock record, not an automated readiness assessment. Confirm current centre instructions and the booked delivery format.

## Lingolia: supplementary explanations

- [Grammar](https://deutsch.lingolia.com/en/grammar)
- [Vocabulary](https://deutsch.lingolia.com/en/vocabulary)
- [Reading](https://deutsch.lingolia.com/en/reading)
- [Listening](https://deutsch.lingolia.com/en/listening)

The organisational idea is an explanation plus examples and practice, with topic navigation and skill sections. No Lingolia articles, exercise banks, illustrations, audio recordings, private APIs or paid materials are copied into this repository.

## Original material in this project

The 41 library lessons, vocabulary cards, 60 objective exam-format items, email prompts/model responses, speaking cards, study plan and feedback text were authored for this project. They are not official telc questions, have not been difficulty-calibrated, and are not a validated mock examination or CEFR placement test. Browser-generated speech is supplementary and does not reproduce authentic exam audio conditions.

Writing checklists and word counts are self-review aids. They do not automatically judge grammatical quality or award examiner marks. Speaking pages do not activate a microphone, evaluate pronunciation or simulate a responsive conversational partner. Obtain human feedback for productive skills.

The source references inform the exam facts, not permission to republish complete publisher materials. External files stay outside this project; users select their own local copies for personal practice. Do not commit third-party books, answer keys, audio or personal writing. No subscription access controls are bypassed.

## REA inspection and verification

REA repository: [morluto/rea](https://github.com/morluto/rea), used locally at version 6.8.0. REA is an inspection tool, not the website framework or an exam-content source.

1. Static inventory of the previous standalone application completed. REA explicitly reported that the inline JavaScript body was not analysed.
2. Editable JavaScript was extracted to `src/app.js`; the offline build embeds it in `index.html`.
3. REA source inspection was attempted with `--source-path src/app.js`. The analysis stopped with `capability_unavailable`: Linux process ownership inspection required a procps-compatible `ps`, and this execution environment lacks `/proc`. Full source analysis therefore **did not complete**. No process-ownership checks were bypassed.
4. Independent DOM tests exercised navigation, the existing 41 quiz flows, all 60 new answer keys through form events, unanswered/duplicate selections, error review, timers and cleanup, writing saves, daily study marks, mock-score limits, backup validation and reload persistence.
5. Browser visual QA, authentic recording playback and operating-system speech voices were not verified in this environment. DOM tests do not prove visual layout, real-browser media support, pedagogical completeness or exam readiness.

To rerun REA on a suitably configured machine, using your own installation:

```sh
rea analyze-javascript-application /absolute/path/to/deutsch-B1 --source-path src/app.js --detail summary --evidence_output /absolute/path/outside-repository/rea-evidence.json --format json
```

REA needs its documented platform prerequisites; the app itself does not require REA, Node.js or npm.

## Added grammar workbook and interaction update

- Reference for exercise types: [German.net dative prepositions](https://german.net/exercises/prepositions/dative/), inspected 6 November 2026. The reference uses choosing and writing missing prepositions/forms; many further worksheets are restricted. None of its exercise sentences, answers, or paid materials are copied.
- Added 12 original worksheets with 144 questions, including 48 dative-focused items. The first dative sheet explicitly includes the useful construction `an ... vorbei`, which is not an always-dative preposition.
- Changed generated controls from inline event-handler attributes to named, delegated JavaScript event listeners. This removes reliance on inline handler execution in hosting/embedded browser contexts. The reported browser failure was not reproduced in the private authenticated browser; this is a compatibility repair, not a confirmed CSP diagnosis.
- Publisher links now open in the current tab to avoid relying on popup permissions. They still require internet and are not local application pages.
- Added a no-script `START-HERE.html` and rewritten beginner README, with separate Mac/Windows download and extraction steps.
