import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login  # Import the login function from login.py
from tqdm import tqdm  # Import tqdm untuk progress bar

def perform_login(driver, email, password):
    try:
        # Login
        login(driver, email, password)
    except Exception as e:
        print('Terjadi kesalahan saat login:', str(e))
        raise  # Propagate the exception

def set_rows_per_page(driver):
    try:
        # Temukan dan klik dropdown untuk membuka opsi jumlah baris per halaman
        rows_per_page_dropdown = driver.find_element(By.XPATH, "//div[@aria-label='Rows per page']")
        rows_per_page_dropdown.click()
        
        # Tunggu hingga opsi muncul
        wait = WebDriverWait(driver, 10)
        option_100 = wait.until(EC.presence_of_element_located((By.XPATH, "//li[contains(text(),'100')]")))
        
        # Klik opsi dengan nilai 100
        option_100.click()
    except Exception as e:
        print(f'Terjadi kesalahan saat mengatur jumlah baris per halaman: {str(e)}')

def scrape_product_page(driver, output_file):
    try:
        # Akses halaman produk langsung
        product_page_url = 'https://affiliate.gramedia.com/affiliate-link/generate-link'
        driver.get(product_page_url)

        # Tunggu hingga halaman produk dimuat sepenuhnya
        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="fuse-main"]/div/div/div[3]/div/table/tbody/tr')))

        # Set jumlah baris per halaman menjadi 100
        set_rows_per_page(driver)

        # Tambahkan jeda waktu tambahan untuk memastikan halaman selesai dimuat
        time.sleep(10)

        with open(output_file, 'w', encoding='utf-8') as file:
            while True:
                # Ambil semua baris produk setelah pencarian
                rows = driver.find_elements(By.XPATH, '//*[@id="fuse-main"]/div/div/div[3]/div/table/tbody/tr')

                for row in tqdm(rows, desc="Mengambil data", unit="baris"):
                    try:
                        # Ambil judul produk
                        judul_produk = row.find_element(By.XPATH, './td[1]/div').text.strip()

                        # Ambil link produk
                        link_produk = row.find_element(By.XPATH, './td[3]/div/div').get_attribute('innerHTML').strip()

                        # Tulis ke file dengan format yang diminta
                        file.write(f'{judul_produk}\nGramedia: {link_produk}\n\n')
                    except Exception as e:
                        print(f'Terjadi kesalahan saat memproses baris: {str(e)}')
                        print('HTML baris:', row.get_attribute('innerHTML'))

                # Coba klik tombol 'Next' untuk menelusuri halaman selanjutnya
                try:
                    next_button = driver.find_element(By.XPATH, "//button[@aria-label='Go to next page']")
                    if next_button.is_enabled():
                        next_button.click()
                        # Tunggu beberapa detik untuk halaman berikutnya dimuat
                        time.sleep(10)
                    else:
                        print('Tombol Next dinonaktifkan. Tidak ada halaman lebih lanjut untuk dinavigasi.')
                        break  # Keluar dari loop jika tombol 'Next' dinonaktifkan
                except Exception as e:
                    print(f'Terjadi kesalahan saat mengklik tombol Next: {str(e)}')
                    break  # Keluar dari loop jika tombol 'Next' tidak ditemukan atau tidak bisa diklik

    except Exception as e:
        print('Terjadi kesalahan saat scraping halaman produk:', str(e))

def main():
   
   
    # Path to the chromedriver executable
    chromedriver_path = '/usr/bin/chromedriver'

    # Email dan password diambil dari variabel lingkungan
    email = os.getenv('EMAIL')
    password = os.getenv('PASSWORD')

    # Nama file untuk menyimpan hasil
    output_file = 'hasil_scraping.txt'

    # Set options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")

    # Initialize the WebDriver with options
    service = Service(chromedriver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Perform login
        perform_login(driver, email, password)

        # Scraping product page
        scrape_product_page(driver, output_file)

    finally:
        driver.quit()

if __name__ == "__main__":
    main()
