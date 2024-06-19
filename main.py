import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login  # Import the login function from login.py

# Path to the chromedriver executable
chromedriver_path = '/usr/bin/chromedriver'

# Email dan password diambil dari variabel lingkungan
email = os.getenv('EMAIL')
password = os.getenv('PASSWORD')

# URL langsung ke halaman produk yang ingin Anda ambil informasinya
product_page_url = 'https://affiliate.gramedia.com/affiliate-link/generate-link'

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

def perform_login():
    try:
        # Login
        login(driver, email, password)
    except Exception as e:
        print('An error occurred during login:', str(e))
        raise  # Propagate the exception

def scrape_product_page():
    try:
        # Perform login
        perform_login()

        # Akses halaman produk langsung
        driver.get(product_page_url)

        # Tunggu hingga halaman produk dimuat sepenuhnya
        wait = WebDriverWait(driver, 20)  # Increased timeout for potentially slow loading pages
        wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="input-search"]')))

        with open(output_file, 'w', encoding='utf-8') as file:
            while True:
                # Ambil semua baris produk setelah pencarian
                rows = driver.find_elements(By.XPATH, '//*[@id="fuse-main"]/div/div/div[3]/div/table/tbody/tr')

                for row in rows:
                    try:
                        # Ambil judul produk
                        judul_produk = row.find_element(By.XPATH, './td[1]/div').text.strip()

                        # Ambil link produk
                        link_produk = row.find_element(By.XPATH, './td[3]/div/div').get_attribute('innerHTML').strip()

                        # Tulis ke file dengan format yang diminta
                        file.write(f'{judul_produk}\nGramedia: {link_produk}\n\n')

                        # Cetak hasil untuk feedback di console
                        print(f'Judul Produk: {judul_produk}')
                        print(f'Link Produk: {link_produk}')
                        print('---')
                    except Exception as e:
                        print(f'An error occurred while processing a row: {str(e)}')

                # Coba klik tombol 'Next' untuk menelusuri halaman selanjutnya
                try:
                    next_button = driver.find_element(By.XPATH, '//*[@id="fuse-main"]/div/div/div[4]/div[2]/nav/ul/li[9]/button')
                    next_button.click()
                    time.sleep(5)  # Tunggu beberapa detik untuk halaman berikutnya dimuat
                except Exception as e:
                    print(f'Could not find or click on next button: {str(e)}')
                    break  # Keluar dari loop jika tombol 'Next' tidak ditemukan atau tidak bisa diklik

    except Exception as e:
        print('An error occurred during scraping the product page:', str(e))
    finally:
        driver.quit()

# Panggil fungsi untuk melakukan scraping langsung dari halaman produk
scrape_product_page()

