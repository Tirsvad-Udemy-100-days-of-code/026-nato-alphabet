# Pembangunan

🌐 [English](Development) · [Dansk](Development-da) · **Bahasa Melayu**

Sediakan projek dahulu ([Pemasangan](Install-ms)). Pilihan tambahan `dev` memasang pytest, ruff, mypy dan import-linter.

## Jalankan ujian

```bash
python -m pytest
```

## Jalankan semakan yang dijalankan oleh CI

```bash
python -m ruff check .
python -m mypy
lint-imports
```

## Bina dokumentasi sumber

```bash
doxygen Doxyfile
```

Buka `build/html/index.html`. Pasang Doxygen dari [doxygen.nl](https://www.doxygen.nl/) atau pengurus pakej anda.

## Susun atur kod

| Folder | Kandungan |
| --- | --- |
| `src/nato_alphabet/domain/` | Peraturan ejaan, tanpa input dan output |
| `src/nato_alphabet/application/` | Kes guna dan portnya |
| `src/nato_alphabet/adapters/` | Pembaca CSV dan konsol |
| `src/nato_alphabet/constants.py` | Semua pemalar program |
| `tests/` | Ujian pytest, mencerminkan `src/` |

Kebergantungan menghala ke dalam: adapter mengenali aplikasi, aplikasi mengenali domain. import-linter menguatkuasakannya.

## Pull request

Satu cabang dan satu pull request bagi setiap milestone; CI mesti hijau. Projek ini mengikut rangka kerja SQA dan QC dalam `framework/`; lihat `docs/` untuk pelan dan rekod semakan.
