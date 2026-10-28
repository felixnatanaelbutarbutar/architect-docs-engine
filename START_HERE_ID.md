# Panduan Architect Docs Engine

Repository ini sekarang berisi reusable Agent Skill `architect-docs-engine`, skrip pemeriksaan lokal, template, dan contoh proyek fiktif. `ANTIGRAVITY_BUILD_PROMPT.md` disimpan sebagai brief build sumber; README root menjelaskan instalasi dan pemakaian secara lengkap.

## Validasi yang sudah dijalankan

- Suite lokal: 29 tes dijalankan, 27 lulus, 2 tes symlink dilewati karena pembuatan symlink dibatasi Windows pada lingkungan ini.
- Contoh proyek fiktif: 4 tes lulus.
- Skill, config, dan audit struktur 21 dokumen: lulus pemeriksaan mekanis.
- Traceability: 14 ID terdefinisi, 0 dangling, 0 duplikat.
- Audit dokumen berstatus `BLOCKED` untuk kesiapan rilis karena 23 pernyataan unresolved masih memerlukan bukti; pemeriksaan mekanis dokumen tetap lulus. Kesiapan produksi diblokir sampai keputusan autentikasi, penyimpanan/retensi, transport, dan operasi ditetapkan.

## Pasang di workspace proyek

Dari root repository, pratinjau lalu pasang ke folder proyek yang sudah ada:

```powershell
python .agents/skills/architect-docs-engine/scripts/install.py --scope workspace --target ..\nama-proyek --dry-run
python .agents/skills/architect-docs-engine/scripts/install.py --scope workspace --target ..\nama-proyek
```

Buka proyek tersebut di Antigravity. Minta agen memakai `architect-docs-engine` untuk menginspeksi codebase dan menghasilkan suite dokumentasi penuh. Slash command `/architect-docs-engine` tersedia hanya pada surface yang mendukung pemanggilan manual.

```text
Gunakan architect-docs-engine untuk menginspeksi codebase dan membuat 21 dokumen di /docs. Bedakan bukti dari usulan, jangan mengarang fitur, pertahankan dokumen yang sudah ditulis manusia, lalu audit traceability dan laporkan keputusan yang belum terjawab.
```

## Periksa secara lokal

Jalankan dari root repository:

```powershell
python -m unittest discover -s tests -v
python -m unittest discover -s examples/sample-project/src -v
python .agents/skills/architect-docs-engine/scripts/cli.py validate-skill
python .agents/skills/architect-docs-engine/scripts/cli.py validate-config --project .\examples\sample-project
python .agents/skills/architect-docs-engine/scripts/cli.py audit --project .\examples\sample-project
python .agents/skills/architect-docs-engine/scripts/cli.py traceability --project .\examples\sample-project
```

## Siapkan publikasi sendiri

Periksa file dan identitas Git terlebih dahulu. Repository belum dipublikasikan dan belum memiliki remote yang dikonfigurasi. Setelah membuat repository GitHub dan memastikan `origin` belum ada, tambahkan remote milikmu lalu push branch yang sudah ditinjau. Jangan menyertakan data rahasia atau data perusahaan.

## Perbedaan README

- `README.md` di root repository ini menjelaskan skill yang dapat digunakan ulang.
- `examples/sample-project/docs/README.md` adalah contoh indeks dokumentasi proyek target.
- Pada proyek nyata, hasilnya berada di `<proyek>/docs/README.md`.

Prinsip utama: **fakta harus punya bukti; keputusan yang belum diketahui ditulis sebagai unresolved, bukan ditebak.**
