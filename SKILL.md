---
name: doc-craft
description: "Document and paper crafting engine for AI agents. Generates publication-ready academic papers, lab reports, summaries, and technical specs: Times New Roman, pure black text, diagrams, and clean tables."
allowed-tools: Read Write Edit Glob Grep run_command
---

# doc-craft

> Document & Paper Crafting Engine for AI Agents
> Dibuat oleh M. Rifaldo Saputra (Rifaldo-dev)
> Standar pembuatan dokumen resmi, karya tulis akademik, makalah, laporan praktikum, resume materi, dan spesifikasi teknis (.docx) siap cetak tanpa AI slop.

---

## 1. Pemanggilan Skill (Slash Command)

Skill ini dipanggil di Antigravity menggunakan perintah:
> `/doc-craft [instruksi pembuatan dokumen, judul, atau file rujukan]`

### Contoh Penggunaan:
* `/doc-craft buatkan makalah sistem basis data terdistribusi`
* `/doc-craft rangkum materi dari file D:/kuliah/jaringan.pdf dan buat dokumennya`
* `/doc-craft susun laporan praktikum modul 3 basis data`
* `/doc-craft buat dokumen SRS untuk aplikasi kasir minimarket`
* `/doc-craft buat SOP penanganan insiden keamanan server`

Skill ini otomatis mengenali jenis dokumen yang dibutuhkan pengguna (makalah, laporan, resume, atau spesifikasi teknis) tanpa memerlukan perintah terpisah yang membingungkan.

---

## 2. Prinsip Utama (Craftsmanship Standard)

Dokumen yang dihasilkan oleh `doc-craft` harus tampak seperti disusun secara teliti oleh akademisi atau profesional manusia, bukan cetakan generik bot AI:

1. **Intensionalitas**: Setiap bab, paragraf, tabel, dan diagram memiliki alasan keberadaan yang jelas.
2. **Kekayaan Data & Visual**: Wajib menyertakan diagram teknis dan tabel perbandingan, bukan sekadar dinding teks.
3. **Ketegasan Bahasa**: Lugas, objektif, dan berbasis data ilmiah nyata tanpa basa-basi pembuka yang klise.

---

## 3. Tujuh Gerbang Kualitas Mutlak (The Hard Gates)

Seluruh dokumen yang dihasilkan melalui `doc-craft` **WAJIB** memenuhi 7 gerbang kualitas berikut:

### C-01 — Tipografi Konsisten (Times New Roman)
- Menggunakan font **Times New Roman** untuk seluruh elemen teks dokumen.
- Judul Cover: **14 - 16 pt Bold (Kapital)**
- Heading 1 (BAB I, BAB II): **12.5 - 13 pt Bold (Kapital)**
- Heading 2 (Sub-bab): **12 pt Bold**
- Heading 3 (Sub-sub-bab): **11.5 - 12 pt Bold Italic**
- Paragraf: **11.5 - 12 pt Regular**, Rata Kiri-Kanan (*Justify*), spasi 1.15 atau 1.5.

### C-02 — Teks 100% Hitam Murni (Zero Blue Text)
- **DILARANG** memberi warna teks biru navy, ungu, atau abu-abu pudar pada judul, tabel, maupun paragraf.
- Seluruh teks tanpa kecuali berorientasi monokrom hitam: `RGBColor(0, 0, 0)` atau `#000000`.
- Diagram visual tetap mempertahankan warna teknisnya agar mudah dibedakan.

### C-03 — Larangan Karakter Em Dash (`—`)
- **DILARANG KERAS** menggunakan karakter em dash (`—`) di seluruh isi teks dokumen.
- Ganti dengan tanda titik dua (`:`), tanda hubung biasa (`-`), tanda koma (`,`), atau tanda kurung `()`.

### C-04 — Bebas AI Fluff & Buzzwords
- **DILARANG** menggunakan kata klise khas AI seperti:
  * *"secara komprehensif"*, *"revolusioner"*, *"pada lanskap era digital saat ini"*, *"tidak dapat dipungkiri"*, *"penting untuk dicatat bahwa"*, *"tanpa berlama-lama lagi"*.
- Tulisan harus padat, menyertakan definisi ilmiah, formula/rumus, arsitektur, dan perbandingan konkret.

### C-05 — Wajib Diagram Teknis (300 DPI)
- Dokumen dilarang hanya berisi teks panjang monoton.
- Setiap dokumen wajib menyertakan minimal 1-3 visualisasi teknis beresolusi tinggi (300 DPI) yang digenerate menggunakan modul `scripts/diagram_engine.py` (contoh: topologi jaringan, arsitektur sistem, alur proses, atau relasi data).

### C-06 — Format Tabel Standar Ilmiah
- Tabel wajib memiliki garis pembatas tegas, baris *header* berlatar abu-abu muda (`#E0E0E0`) dengan teks tebal hitam, serta bantalan sel (*padding*) proporsional.

### C-07 — Ekspor Langsung ke Microsoft Word (.docx)
- Agen tidak boleh hanya mencetak draf di jendela chat.
- Agen wajib menjalankan generator Python `scripts/docx_engine.py` untuk menghasilkan file `.docx` siap pakai di folder Desktop / Downloads pengguna, lalu membuka lokasinya via Windows Explorer.

---

## 4. Alur Kerja Eksekusi Agen (Workflow)

```
[Trigger /doc-craft] 
       │
       ▼
[1. Ekstraksi Topik & File Acuan] 
       │
       ▼
[2. Baca Profil Pengguna (config.json)] 
       │
       ▼
[3. Susun Struktur Dokumen Baku (Cover s/d Daftar Pustaka)] 
       │
       ▼
[4. Generate Diagram Teknis 300 DPI via Matplotlib] 
       │
       ▼
[5. Kompilasi File .docx (100% Black Text, Times New Roman)] 
       │
       ▼
[6. Simpan ke Desktop & Tampilkan di Windows Explorer]
```

---

## 5. Konfigurasi Profil Pengguna (`config.json`)

Identitas penulis (Nama, NIM, Program Studi, Instansi) otomatis dibaca dari file `config.json` di dalam folder skill:

```json
{
  "author": "M. Rifaldo Saputra",
  "nim": "245720111034",
  "major": "Sistem Informasi",
  "institution": "Universitas / Kampus",
  "default_font": "Times New Roman",
  "auto_open_explorer": true
}
```

Jika pengguna meminta dokumen untuk identitas lain, agen akan menggunakan identitas baru tersebut pada dokumen yang sedang diproses.

---

## 6. Delivery Gate (Pemeriksaan Akhir)

Sebelum menyerahkan file ke pengguna, pastikan seluruh daftar periksa berikut berstatus **PASS**:
- [ ] Apakah seluruh font menggunakan Times New Roman? *(C-01)*
- [ ] Apakah seluruh teks berwarna hitam murni (tidak ada teks biru/abu-abu)? *(C-02)*
- [ ] Apakah seluruh isi teks bebas dari karakter em dash (`—`)? *(C-03)*
- [ ] Apakah teks bebas dari kata-kata klise dan pembuka kosong AI? *(C-04)*
- [ ] Apakah dokumen memuat diagram visual teknis resolusi tinggi (300 DPI)? *(C-05)*
- [ ] Apakah file `.docx` berhasil disimpan dan langsung disorot di Explorer? *(C-07)*
