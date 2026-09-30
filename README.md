# nhaajtt

Reverse engineer and security researcher. I spend most of my time taking binaries apart to understand how they actually work: unpacking, deobfuscation, protocol and format reversing, and vulnerability research on native code.

- Reverse engineering of native and obfuscated binaries (PE/ELF, packers, VM-based protections)
- Malware analysis and unpacking
- Binary exploitation and vulnerability research
- Windows internals
- Tooling for reverse engineering workflows (scripts, plugins, automation)

I treat CTFs and personal research as a lab: most public work here is proof-of-concept code, analysis notes, and tools built to solve a specific reversing problem, not production software.

Write-ups and analysis notes go to [nhaajtt.github.io](https://nhaajtt.github.io) (RSS available).

## Projects

- [orrery](https://github.com/nhaajtt/orrery) - looks up a GitHub profile and draws its public repositories as planets, plus the Action behind the SVG above.
- [canary-bypass](https://github.com/nhaajtt/canary-bypass) - recovering a stack canary byte by byte from a crash and no-crash oracle.
- [fuzzing-lab](https://github.com/nhaajtt/fuzzing-lab) - a fuzzing harness for cJSON, with a finding reported as [DaveGamble/cJSON#1093](https://github.com/DaveGamble/cJSON/issues/1093).
- [exploit-labs](https://github.com/nhaajtt/exploit-labs) - self-contained stack overflow, ret2libc and SQL injection labs, each with its own target and exploit.
- [re-tools](https://github.com/nhaajtt/re-tools) - small command-line tools: ELF and PE header dumps, entropy scanning, XOR brute-forcing.
- [re-ai-assist](https://github.com/nhaajtt/re-ai-assist) - connects a running Ghidra session to a language model for binary triage.
- [ai-redteam](https://github.com/nhaajtt/ai-redteam) - a red-team harness testing a self-authored assistant against prompt injection and jailbreaks.
- [ctf-writeups](https://github.com/nhaajtt/ctf-writeups) - CTF write-ups with a template and a self-updating index.

## Toolbox

![Ghidra](https://img.shields.io/badge/Ghidra-4B1A1A?style=flat-square)
![IDA Pro](https://img.shields.io/badge/IDA%20Pro-2D2D2D?style=flat-square)
![x64dbg](https://img.shields.io/badge/x64dbg-1E1E1E?style=flat-square)
![radare2](https://img.shields.io/badge/radare2-464646?style=flat-square)
![Frida](https://img.shields.io/badge/Frida-4A9C6D?style=flat-square)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-00599C?style=flat-square&logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![x86/x64 Assembly](https://img.shields.io/badge/x86%2Fx64%20Assembly-333333?style=flat-square)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=flat-square&logo=windows&logoColor=white)

## Activity

![nhaajtt's GitHub stats](https://github-readme-stats.vercel.app/api?username=nhaajtt&show_icons=true&hide_title=true&count_private=true&theme=dark)
![Top languages](https://github-readme-stats.vercel.app/api/top-langs/?username=nhaajtt&layout=compact&hide_border=true&theme=dark)

![Metrics](./github-metrics.svg)

## Orrery

![Public repositories of nhaajtt drawn as planets around the sun](./orrery.svg)

Drawn daily by [Orrery](https://github.com/nhaajtt/orrery), a small GitHub Action I wrote. Each planet is a public repository. There is also a [live version](https://orbit-gh.vercel.app/?u=nhaajtt) where you can look up any username and compare two profiles.
