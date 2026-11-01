# Nhaajt

<p align="center">
  <img width="160" src="https://github.com/nhaajtt.png" alt="Nhaajt" />
</p>

<p align="center"><sub><em>
Student, still learning, and very happy about it.<br />
I like taking things apart to see how they work: a binary, a network, a bricked Spotify Car Thing.<br />
Right now I'm learning two things properly: running things in the cloud, and reading them back in assembly.<br />
Most of what's here is me learning in public, so expect rough edges and a lot of notes.
</em></sub></p>

<p align="center">
  <a href="https://www.nhaajt.com"><b>nhaajt.com</b></a> ·
  <a href="https://lab.nhaajt.com">lab</a> ·
  <a href="https://nhaajtt.github.io">notes</a> ·
  <a href="mailto:nhaajt.work@gmail.com">nhaajt.work@gmail.com</a>
</p>

---

## Now

cloud & infrastructure<br>
﹂**a two-server homelab I run and break myself**<br>
&nbsp;&nbsp;&nbsp;&nbsp;﹂Linux and Docker, container health checks, CPU / memory / temperature graphs over 24 h<br>
&nbsp;&nbsp;&nbsp;&nbsp;﹂locked down by default: firewall allow-lists, alerts on failed SSH logins and on any newly opened port<br>
&nbsp;&nbsp;&nbsp;&nbsp;﹂a desk device that can reach exactly one port on one server, nothing else ([carthing-desk-hub](https://github.com/nhaajtt/carthing-desk-hub))<br>
﹂**a real-time multiplayer backend on Cloudflare Workers** ([chess rooms](https://github.com/nhaajtt/chess-in-the-margins/tree/main/server))<br>
&nbsp;&nbsp;&nbsp;&nbsp;﹂one Durable Object per room, hibernating WebSockets, every move re-checked on the server<br>
&nbsp;&nbsp;&nbsp;&nbsp;﹂per-IP rate limits, an origin allow-list, socket caps, rooms that clean themselves up after a day<br>
&nbsp;&nbsp;&nbsp;&nbsp;﹂strict CSP and HSTS in front, tests for the abuse cases behind<br>
﹂**CI/CD I can trust**: tests on every push, CodeQL, actions pinned to commit SHAs, read-only tokens<br>
﹂**next**: Terraform for all of the above, then AWS (Cloud Practitioner → Solutions Architect Associate)

reverse engineering<br>
﹂**x86/x64 assembly and C**: learning to read what the compiler actually wrote<br>
﹂**Ghidra and x64dbg**: stepping through programs until they make sense<br>
﹂**CTFs and crackmes**: solving them, then writing down how (first notes coming to [nhaajtt.github.io](https://nhaajtt.github.io))<br>
﹂**fuzzing**: found and reported a stack overflow in cJSON ([#1093](https://github.com/DaveGamble/cJSON/issues/1093))<br>
﹂**malware analysis basics**: unpacking samples inside a throwaway VM, carefully

---

## Learning path

| | Cloud & infrastructure | Reverse engineering |
|---|---|---|
| **done** | two-server homelab: Docker, monitoring, security alerts · real-time backend on Durable Objects · hardened CI (pinned actions, CodeQL) | fuzzed cJSON and reported a stack overflow ([cJSON#1093](https://github.com/DaveGamble/cJSON/issues/1093)) |
| **now** | zero-trust networking with Tailscale ACLs · least-privilege containers · observability | x86/x64 assembly · Ghidra and x64dbg · CTFs and crackmes |
| **next** | Terraform · AWS Cloud Practitioner → Solutions Architect Associate · Kubernetes basics | unpacking · malware analysis basics in a lab VM |

---

## Things I made

<table>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/nhaajtt/chess-in-the-margins"><b>chess-in-the-margins</b></a><br />
      <sub>Chess drawn in ballpoint, every piece a creature. Own chess engine, online rooms on Cloudflare · <a href="https://chess.nhaajt.com">play it</a></sub><br />
      <img src="https://img.shields.io/static/v1?style=for-the-badge&label=focus&message=durable%20objects%20%7C%20websockets&labelColor=f97316&color=111827" alt="focus cloudflare websockets" /><br />
      <img src="https://img.shields.io/github/stars/nhaajtt/chess-in-the-margins?style=flat-square&label=stars&color=f59e0b" alt="stars" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/nhaajtt/orrery"><b>orrery</b></a><br />
      <sub>Any GitHub profile drawn as planets, plus a GitHub Action that redraws it daily · <a href="https://orrery.nhaajt.com">try it</a></sub><br />
      <img src="https://img.shields.io/static/v1?style=for-the-badge&label=focus&message=github%20actions%20%7C%20svg&labelColor=0ea5e9&color=111827" alt="focus github actions svg" /><br />
      <img src="https://img.shields.io/github/stars/nhaajtt/orrery?style=flat-square&label=stars&color=f59e0b" alt="stars" />
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <a href="https://github.com/nhaajtt/carthing-desk-hub"><b>carthing-desk-hub</b></a><br />
      <sub>A bricked Spotify Car Thing brought back as a desk hub: markets, news, weather, server health</sub><br />
      <img src="https://img.shields.io/static/v1?style=for-the-badge&label=focus&message=homelab%20%7C%20monitoring&labelColor=22c55e&color=111827" alt="focus hardware self-hosting" /><br />
      <img src="https://img.shields.io/github/stars/nhaajtt/carthing-desk-hub?style=flat-square&label=stars&color=f59e0b" alt="stars" />
    </td>
    <td width="50%" valign="top">
      <a href="https://github.com/nhaajtt/shiftdrop"><b>shiftdrop</b></a><br />
      <sub>Shift + drag any file for a wheel of actions: convert, compress, sign, share. Offline, Windows · <a href="https://shiftdrop.nhaajt.com">site</a></sub><br />
      <img src="https://img.shields.io/static/v1?style=for-the-badge&label=focus&message=windows%20%7C%20desktop&labelColor=a855f7&color=111827" alt="focus windows desktop" /><br />
      <img src="https://img.shields.io/github/stars/nhaajtt/shiftdrop?style=flat-square&label=stars&color=f59e0b" alt="stars" />
    </td>
  </tr>
</table>

More experiments, finished and unfinished, live on [lab.nhaajt.com](https://lab.nhaajt.com).

---

## Tiếng Việt

Mình đang đi học và tự học thêm hai hướng mình mê nhất: **cloud engineering** và **reverse engineering**. Mình tự dựng và vận hành homelab hai server ở nhà, viết backend thời gian thực trên Cloudflare, và làm hạ tầng theo kiểu “không tin gì mặc định”.
Mình thích tháo tung mọi thứ ra xem bên trong chạy thế nào, từ một file chương trình, một hệ thống mạng, đến cái Spotify Car Thing đã "chết".
Những gì ở đây là mình học công khai: có cái xong, có cái còn dở, nhưng cái nào cũng là một bài học.
Nếu bạn cũng đang học, cứ nhắn mình, học chung vui hơn.

---

## Say hi

Learning buddies, CTF teammates, homelab tips, or a "you got this wrong": all welcome.<br>
📫 [nhaajt.work@gmail.com](mailto:nhaajt.work@gmail.com)
