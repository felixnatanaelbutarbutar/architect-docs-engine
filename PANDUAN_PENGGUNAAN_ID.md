# Panduan Pemula Architect Docs Engine

Panduan ini menjelaskan cara memakai Architect Docs Engine untuk menyiapkan dan merawat dokumentasi teknis proyek perangkat lunak. Kamu tidak harus sudah punya aplikasi atau mengerti arsitektur perangkat lunak.

## Ringkasnya

Architect Docs Engine adalah **skill untuk AI coding agent**, bukan aplikasi pembuat website dan bukan layanan AI tersendiri. Skill ini memberi agen alur kerja, contoh, aturan, dan pemeriksaan untuk menghasilkan **21 dokumen proyek** yang saling terhubung.

Kamu bisa mulai dari:

- ide kasar yang baru beberapa kalimat;
- brief atau daftar kebutuhan;
- proyek yang sudah punya kode;
- dokumentasi lama yang perlu diperiksa atau diperbarui.

AI agent menulis dan menalar isi dokumennya. Skrip Python yang disertakan hanya membantu memasang skill, memeriksa berkas, tautan, ID, konfigurasi, dan laporan audit. Skrip itu tidak membangun aplikasi dan tidak menggantikan peninjauan manusia.

## Bisa dipakai di Codex?

**Bisa.** Codex mendukung Agent Skills. Skill yang dipasang di dalam proyek berada pada jalur `.agents/skills/`; format skill ini berisi `SKILL.md` beserta referensi, templat, dan skrip pendukung. Dalam Codex CLI atau ekstensi IDE, kamu bisa menyebut skill secara langsung dengan `$architect-docs-engine`. Codex juga dapat memilihnya otomatis ketika permintaanmu cocok dengan deskripsi skill.

Panduan resmi: [membuat dan memakai Skills di OpenAI Learn](https://learn.chatgpt.com/docs/build-skills) dan [pengaturan kustomisasi Codex](https://learn.chatgpt.com/docs/customization/overview).

### Cara paling mudah untuk Codex: pasang di proyek

Pemasangan workspace membuat skill tersedia saat Codex membuka proyek tujuan. Folder target harus sudah dibuat sebelum installer dijalankan.

1. Unduh atau clone repository ini.
2. Buat folder untuk proyek yang ingin didokumentasikan.
3. Jalankan installer dengan opsi **--scope workspace** dan arahkan **--target** ke folder proyek.
4. Buka **folder proyek tujuan** di Codex.
5. Minta Codex memakai skill ini. Di Codex CLI atau IDE, kamu bisa menulis `$architect-docs-engine` di awal permintaan.

Contoh untuk Windows PowerShell:

~~~powershell
git clone https://github.com/felixnatanaelbutarbutar/architect-docs-engine.git
New-Item -ItemType Directory -Force -Path "C:\Proyek\ide-aplikasi"
Set-Location .\architect-docs-engine

# Lihat dulu tujuan pemasangannya; perintah ini belum memasang apa pun.
python .agents/skills/architect-docs-engine/scripts/install.py --scope workspace --target "C:\Proyek\ide-aplikasi" --dry-run

# Setelah tujuannya benar, pasang skill.
python .agents/skills/architect-docs-engine/scripts/install.py --scope workspace --target "C:\Proyek\ide-aplikasi"
~~~

Setelah itu, buka `C:\Proyek\ide-aplikasi` sebagai proyek di Codex. Folder skill akan berada di:

~~~text
C:\Proyek\ide-aplikasi\.agents\skills\architect-docs-engine\
~~~

Jika ingin memakai skill secara global di Codex, dokumentasi Codex menggunakan folder `$HOME/.agents/skills/`. Salin **seluruh** folder `architect-docs-engine` ke sana. Opsi installer `--scope global` pada repository ini ditujukan untuk Antigravity, jadi jangan gunakan opsi itu untuk memasang skill global Codex. Untuk pemula, pemasangan workspace di atas lebih mudah dilihat dan dikelola.

## Bagaimana kalau proyeknya baru berupa ide kasar?

Tetap bisa. Kamu tidak perlu menebak teknologi, membuat diagram lebih dulu, atau mengisi formulir konfigurasi. Mulailah dengan menjelaskan hal yang sudah kamu tahu, misalnya:

> Saya ingin membuat aplikasi untuk membantu pemilik kos mencatat kamar, penghuni, dan pembayaran bulanan. Pengguna utamanya pemilik kos. Saya belum menentukan apakah aplikasinya web atau mobile, cara pembayaran, teknologi, atau tempat penyimpanan data.

Agent akan memakai informasi itu sebagai brief awal. Bagian yang belum diketahui seharusnya ditulis sebagai **Proposed** (usulan yang perlu disetujui) atau **Unresolved** (belum terjawab), bukan dipresentasikan sebagai keputusan atau fakta. Karena belum ada kode, dokumen yang menyatakan stack, API, dan operasi harus jelas menyebut usulan atau hal yang belum ditentukan.

Hasilnya bisa menjadi dasar diskusi dan perencanaan, tetapi 21 dokumen tidak berarti aplikasinya sudah dibuat, aman, siap dirilis, atau sudah memenuhi aturan hukum.

### Contoh permintaan untuk menghasilkan semua dokumen

Salin teks ini ke Codex setelah skill tersedia. Ganti bagian contoh dengan idemu sendiri.

~~~text
$architect-docs-engine

Saya baru punya ide kasar: aplikasi untuk membantu pemilik kos mencatat kamar,
penghuni, dan pembayaran bulanan. Pengguna utamanya pemilik kos. Saya belum
menentukan platform, teknologi, metode pembayaran, atau penyimpanan data.

Bantu saya menyusun dokumentasi awal lengkap. Tulis dalam Bahasa Indonesia yang
mudah dipahami. Buat seluruh 21 dokumen di folder docs/ proyek ini. Mulai dengan
merangkum ide dan batas cakupannya. Jangan membuat atau mengubah kode aplikasi.
Jangan mengarang teknologi, fitur, API, data yang sudah tersimpan, hasil tes,
infrastruktur yang sudah berjalan, atau persetujuan yang belum saya berikan.
Tandai fakta, usulan, hal yang belum terjawab, dan bagian yang tidak berlaku
secara jelas. Jangan berhenti hanya karena ada pertanyaan yang belum terjawab;
catat pertanyaannya agar dokumen lain yang sudah bisa dibuat tetap selesai.

Untuk UI/UX, utamakan alur yang jelas, tampilan yang sesuai kebutuhan produk,
warna dan ikon yang punya alasan, konsistensi jarak dan tipografi, aksesibilitas,
serta tampilan yang sudah ditinjau. Jangan memakai popup/modal sebagai tempat
formulir utama; gunakan halaman atau formulir langsung di dalam halaman, kecuali
ada alasan produk yang jelas dan dijelaskan.

Untuk keamanan, buat model ancaman dan daftar verifikasi yang sesuai dengan
informasi yang tersedia. Bahas autentikasi, izin akses per data, penyalahgunaan
bot, pembatasan permintaan dan biaya, validasi masukan, perlindungan data dan
rahasia, serta risiko AI/alat otomatis jika memang digunakan. Pisahkan kontrol
yang baru diusulkan dari kontrol yang benar-benar sudah diterapkan.

Setelah menulis dokumen, periksa kelengkapan dan hubungan antar dokumen. Laporkan
file yang dibuat, keputusan yang masih perlu saya jawab, risiko utama, dan
pemeriksaan yang belum bisa dilakukan karena aplikasi atau buktinya belum ada.
~~~

Untuk proyek yang sudah punya kode, ubah bagian pembuka menjadi: **“Periksa brief, kode, tes, konfigurasi, dan dokumentasi proyek ini sebelum menulis. Gunakan bukti yang benar-benar ditemukan.”** Skill dirancang untuk menginspeksi proyek secara lokal dan tidak menjalankan kode proyek saat pemindaian.

## Arti 21 dokumen

Semua berkas berikut dibuat di `docs/` secara bawaan. Beberapa bagian boleh menyatakan belum diketahui atau tidak berlaku dengan alasan teknis yang jelas.

| No. | Berkas | Penjelasan sederhana |
|---:|---|---|
| 1 | README.md | Pintu masuk dokumentasi: gambaran proyek, status, peta, istilah, dan daftar dokumen. |
| 2 | PRD.md | Masalah pengguna, tujuan, kebutuhan, batas cakupan, dan pertanyaan produk. |
| 3 | TECH_STACK.md | Teknologi yang sudah terbukti ada dan pilihan teknologi yang masih berupa usulan. |
| 4 | DECISIONS.md | Catatan keputusan penting, alasan, alternatif, status, dan kapan keputusan ditinjau ulang. |
| 5 | DATA_MODEL.md | Jenis data, hubungan antar data, masa simpan, dan penghapusan. |
| 6 | VALIDATION_RULES.md | Aturan yang membuat masukan dan proses bisnis dianggap sah atau ditolak. |
| 7 | API_CONTRACT.md | Kontrak API atau antarmuka lain, jika proyek memilikinya; jika belum, catat statusnya. |
| 8 | UI.md | Arah visual: warna, tipografi, tata letak, komponen, ikon, dan cara meninjau tampilannya. |
| 9 | UX.md | Perjalanan pengguna, keadaan layar, formulir, pesan kesalahan, pemulihan, dan aksesibilitas. |
| 10 | AGENTS.md | Petunjuk kerja bagi AI agent atau pengembang yang akan membantu proyek. |
| 11 | PROMPTS.md | Pola prompt dan cara mengevaluasi AI proyek, jika memang ada fitur AI. |
| 12 | SECURITY.md | Aset, pihak yang terlibat, batas kepercayaan, ancaman, perlindungan, pengujian, dan risiko tersisa. |
| 13 | SEED.md | Cara menyiapkan data contoh/fixture dengan aman dan berulang. |
| 14 | IMPLEMENTATION.md | Tahapan pekerjaan, ketergantungan, pemeriksaan, dan cara membatalkan perubahan. |
| 15 | TESTING.md | Strategi tes dan bukti tes yang benar-benar sudah atau belum dijalankan. |
| 16 | ACCEPTANCE.md | Kriteria yang harus dipenuhi agar fitur atau proyek dapat diterima. |
| 17 | TRACEABILITY.md | Hubungan kebutuhan dengan keputusan, data, UI/API, dan tes terkait. |
| 18 | OPERATIONS.md | Menjalankan, mengonfigurasi, memantau, memulihkan, dan menangani insiden. |
| 19 | AUDIT.md | Aturan untuk menilai mutu dokumentasi dan arti status audit. |
| 20 | _AUDIT_REPORT.md | Hasil audit terbaru, bukti, temuan, dan tindakan perbaikan. |
| 21 | _CHANGELOG.md | Riwayat perubahan dokumentasi proyek. |

## Apakah skill ini membuat proyek jadi aman?

Skill ini membantu AI **memikirkan risiko, mendokumentasikan kontrol, dan merencanakan verifikasi**. Skill tidak otomatis memasang firewall, memperbaiki kode aplikasi, menghentikan bot, melakukan pentest, atau menjamin aplikasi tidak dapat diretas. Keamanan bergantung pada implementasi, konfigurasi layanan, proses operasi, dan pengujian nyata.

Untuk produk web/API, minta agen menilai hal yang relevan, seperti:

- login dan pemulihan akun, tetapi juga izin untuk **setiap objek/data** agar pengguna tidak bisa membaca atau mengubah milik orang lain;
- pemeriksaan izin di server, bukan hanya menyembunyikan tombol di UI;
- validasi masukan, pengelolaan sesi, rahasia, unggahan berkas, dan data pribadi;
- bot, spam, brute force, pembatasan laju, batas ukuran/biaya, dan pencegahan kehabisan sumber daya;
- pencatatan aktivitas yang berguna tanpa mencatat kata sandi, token, atau data pribadi berlebihan;
- pencadangan, pemulihan, pemantauan, pembaruan dependensi, serta respons insiden;
- untuk agentic AI: prompt injection, keluaran model yang tidak tepercaya, penyalahgunaan alat, akses minimum, persetujuan tindakan berisiko, dan batas biaya.

Jangan menganggap tulisan “aman” di dokumen sebagai bukti bahwa kontrol sudah bekerja. Minta bukti implementasi dan pengujian untuk tiap kontrol penting. Jangan masukkan kata sandi, token, kunci API, data pelanggan, atau rahasia lain ke prompt maupun dokumentasi.

## Tentang tampilan yang terasa seperti buatan AI

Panduan UI/UX-nya memang mengarahkan agen agar tidak sekadar menempelkan warna, ikon, kartu, gradasi, atau pola layout generik. Pilihan visual harus punya alasan berdasarkan produk, pengguna, tugas, aksesibilitas, dan konteks merek. Konsistensi warna, tipografi, jarak, keadaan kosong/error/loading, serta peninjauan tampilan juga dibahas.

Formulir utama seharusnya tampil sebagai halaman atau bagian langsung di halaman. Popup/modal tidak dijadikan pilihan otomatis untuk formulir biasa; penggunaannya perlu alasan yang sesuai alur produk. Karena proyek yang hanya berupa ide belum memiliki layar nyata, dokumen UI/UX pada tahap itu adalah **rencana**, bukan bukti desain yang sudah jadi. Minta peninjauan ulang setelah ada implementasi dan tampilan yang bisa dilihat.

## Cara memeriksa hasil

Setelah agen selesai, baca dokumen dengan urutan praktis: docs/README.md, docs/PRD.md, docs/SECURITY.md, docs/UI.md, docs/UX.md, docs/DECISIONS.md, lalu laporan audit dan traceability. Koreksi setiap usulan yang tidak cocok sebelum menganggapnya sebagai keputusan proyek.

Kamu juga dapat menjalankan pemeriksaan lokal dari root proyek target:

~~~powershell
python .agents/skills/architect-docs-engine/scripts/cli.py validate-skill
python .agents/skills/architect-docs-engine/scripts/cli.py audit --project .
python .agents/skills/architect-docs-engine/scripts/cli.py traceability --project .
~~~

Jika proyek memiliki `architect-docs.config.json`, periksa juga konfigurasinya:

~~~powershell
python .agents/skills/architect-docs-engine/scripts/cli.py validate-config --project .
~~~

Pemeriksaan tersebut memastikan hal-hal mekanis seperti berkas, tautan, ID, dan struktur. Hasil **BLOCKED** dapat berarti dokumen sudah lengkap secara mekanis, tetapi masih ada keputusan atau bukti yang belum tersedia untuk menyatakan proyek siap dirilis. Itu bukan otomatis berarti program pemeriksanya rusak. Baca temuan dan alasan statusnya.

## Memakai di Google Antigravity

Pemasangan workspace sama seperti contoh Codex. Buka proyek tujuan di Antigravity, lalu minta agen memakai skill ini. `/architect-docs-engine` dapat dipakai pada permukaan Antigravity yang mendukung pemanggilan skill secara langsung.

Installer juga menyediakan pemasangan global khusus Antigravity:

~~~powershell
python .agents/skills/architect-docs-engine/scripts/install.py --scope global --dry-run
python .agents/skills/architect-docs-engine/scripts/install.py --scope global
~~~

Lokasi global Antigravity: `~/.gemini/config/skills/architect-docs-engine/`. Jika installer memberi tahu bahwa pemasangan berbeda sudah ada, tinjau dulu; jangan langsung menggantinya. Opsi `--force` membuat salinan cadangan sebelum mengganti pemasangan yang berbeda.

## Masalah yang umum

| Masalah | Yang bisa dicoba |
|---|---|
| Codex tidak menemukan skill | Pastikan folder lengkap ada di `.agents/skills/architect-docs-engine/` di root proyek yang sedang dibuka. Sebut `$architect-docs-engine` secara langsung di Codex CLI/IDE. Jika baru memasang dan belum muncul, muat ulang atau mulai ulang Codex. |
| Installer mengatakan folder target tidak ada | Buat folder proyek terlebih dahulu, lalu jalankan installer lagi. `--target` harus menunjuk ke folder yang sudah ada. |
| Installer menemukan pemasangan berbeda | Periksa berkas yang ada. Jangan gunakan `--force` sebelum memahami perubahan; jika diteruskan, installer membuat cadangan bertanggal. |
| Agen meminta banyak keputusan | Minta ia melanjutkan dokumen yang bisa dikerjakan dan mencatat sisanya sebagai `Unresolved` atau `Proposed`, bukan mengarang jawaban. |
| Semua dokumen ada, tetapi audit belum siap | Buka `_AUDIT_REPORT.md` dan selesaikan bukti, keputusan, atau pemetaan yang disebutkan. Jumlah 21 berkas saja tidak cukup untuk kesiapan rilis. |
| Isi dokumen terlalu umum atau terasa seperti AI | Berikan konteks pengguna, tugas utama, batasan nyata, contoh merek/produk, dan keputusan yang sudah dibuat. Minta alasan untuk tiap usulan dan minta agen menghapus bagian generik yang tidak didukung bukti. |

## Istilah singkat[[]()]()

- **Skill**: petunjuk kerja dan bahan pendukung yang dipakai AI agent untuk tugas tertentu.
- **Workspace**: folder proyek yang sedang dibuka di Codex atau Antigravity.
- **Bukti**: hal yang dapat ditunjukkan dari brief, keputusan pengguna, kode, konfigurasi, tes, atau sumber yang diperiksa.
- **Proposed**: usulan yang belum disetujui.
- **Unresolved**: pertanyaan atau keputusan penting yang belum terjawab.
- **Audit**: pemeriksaan konsistensi dan kelengkapan; bukan sertifikasi keamanan.

## Tautan

- [Repository GitHub](https://github.com/felixnatanaelbutarbutar/architect-docs-engine)
- [README utama](README.md)
- [Spesifikasi Agent Skills](https://agentskills.io/specification)
- [OpenAI Learn: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI Learn: Codex customization](https://learn.chatgpt.com/docs/customization/overview)

