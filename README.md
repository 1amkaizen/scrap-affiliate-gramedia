# Scrap-affiliate-gramedia

Tools ini untuk mengekstrak judul dan link produk affiliate dari [affiliate.gramedia.com/affiliate-link/generate-link](https://aff.gramedia.com/s/MrHMDcJDbt) dan menyimpannya ke dalam file txt

## Persiapan
Sebelum menjalankan kode harus export dulu email dan password untuk login ke [affiliate gramedia](https://aff.gramedia.com/s/MrHMDcJDbt) nya
```bash
export EMAIL="youremail@gmail.com"
export PASSWORD="yourpassword"
```
## Penggunaan
Untuk menjalankannya gunakan perintah ini

```bash
python3 main.py
```

Jika ada ini berarti login berhsil
```bash
Opened login page.
Entered email and password.
Clicked login button.
Login successful, current URL: https://affiliate.gramedia.com/dashboard
```

Tampilannya akan sperti ini
```bash
Opened login page.
Entered email and password.
Clicked login button.
Login successful, current URL: https://affiliate.gramedia.com/dashboard
Mengambil data: 100%|████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:31<00:00,  3.17baris/s]
---

