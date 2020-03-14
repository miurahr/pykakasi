---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---

**Describe the bug**
A clear and concise description of what the bug is.

**Related issue**
(if exist)

**To Reproduce**
Steps to reproduce the behavior:
(example)
1. Prepare test data attached as 'file' in current directory.
2. Run following code with python3.

```
import pykakasi

kakasi = pykakasi.kakasi()
kakasi.setMode("J","K") 
conv = kakasi.getConverter()
conv = kakasi.getConverter()
text2 = conv.do(j2k('私がこの子を助けなきゃいけないってことだよね	'))
print(text2)
ワタシガコノコヲタスケナキゃいけないってことだよね
```

**Expected behavior**
` ワタシガコノコヲタスケナキャイケナイッテコトダヨネ    `

**Environment (please complete the following information):**
 - OS: [e.g. Windows 10, Ubuntu Linux 18.04.01]
 - Python [e.g. 3.6, pypy3.6.9-7.3.0]
 - pykakasi version: [e.g. v0.5b1, commit #123456 on master]

**Test data(please attach in the report):**
A minimum test data to reproduce your problem.

**Additional context**
Add any other context about the problem here.
