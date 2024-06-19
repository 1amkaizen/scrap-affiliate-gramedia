# Scrap-affiliate-gramedia

Tools ini untuk mengekstrak judul dan link affiliate dari affiliate gramedia

## Persiapan
Sebelum menjalankan kode harus export dulu email dan password untuk login ke affiliate gramedia nya
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
Judul Produk: Cepat, Praktis, dan Gratis Membuat Website
Link Produk: https://aff.gramedia.com/s/oBFIfnZHVb
---
Judul Produk: Otodidak Desain Website dari Nol
Link Produk: https://aff.gramedia.com/s/ZYhsfxdIPG
---
Judul Produk: Menyelesaikan Website 12 Juta Secara Profesional
Link Produk: https://aff.gramedia.com/s/FgtkGpHTPz
---
Judul Produk: Cara Cepat Membuat Segala Jenis Website
Link Produk: https://aff.gramedia.com/s/IoKtLdCMIa
---
```
