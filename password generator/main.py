import random
import string

def sifre_olustur(uzunluk, buyuk_harf=True, kucuk_harf=True, rakamlar=True, semboller=True):
    """
    Belirtilen uzunlukta ve karakter türlerinde rastgele şifre oluşturur.
    
    Parametreler:
        uzunluk (int): Şifrenin istenen uzunluğu.
        buyuk_harf (bool): Şifrede büyük harf kullanılsın mı?
        kucuk_harf (bool): Şifrede küçük harf kullanılsın mı?
        rakamlar (bool): Şifrede rakam kullanılsın mı?
        semboller (bool): Şifrede sembol kullanılsın mı?

    Dönüş:
        str: Oluşturulan şifre veya hata mesajı.
    """
    karakterler = ""
    
    if buyuk_harf:
        karakterler += string.ascii_uppercase
    if kucuk_harf:
        karakterler += string.ascii_lowercase
    if rakamlar:
        karakterler += string.digits
    if semboller:
        karakterler += string.punctuation
    
    # Karakter havuzu boşsa, şifre oluşturulamaz.
    if not karakterler:
        return "Hata: Şifre oluşturmak için en az bir karakter türü (harf, rakam, sembol) seçmelisiniz."
    
    # Şifre uzunluğu geçerli mi kontrolü
    if uzunluk <= 0:
        return "Hata: Şifre uzunluğu pozitif bir sayı olmalıdır."

    # Şifreyi oluştur
    sifre = ''.join(random.choice(karakterler) for _ in range(uzunluk))
    return sifre

def kullanici_etkilesimi():
    """
    Kullanıcıdan şifre oluşturma tercihlerini alır ve sonucu yazdırır.
    """
    print("--- Güvenli Şifre Oluşturucu ---")
    
    try:
        uzunluk = int(input("Şifrenin uzunluğu kaç karakter olsun? (Örn: 12): "))
    except ValueError:
        print("Hata: Geçerli bir sayı girmelisiniz.")
        return

    # Karakter türleri için kullanıcıdan tercih alımı
    def evet_hayir_sor(soru):
        yanit = input(f"{soru} (e/h): ").lower().strip()
        return yanit == 'e'

    kucuk = evet_hayir_sor("Küçük harf (a-z) kullanılsın mı?")
    buyuk = evet_hayir_sor("Büyük harf (A-Z) kullanılsın mı?")
    rakam = evet_hayir_sor("Rakam (0-9) kullanılsın mı?")
    sembol = evet_hayir_sor("Semboller (!@#$ vb.) kullanılsın mı?")

    # Şifreyi oluştur ve sonucu yazdır
    yeni_sifre = sifre_olustur(uzunluk, buyuk, kucuk, rakam, sembol)
    
    print("\n--- Sonuç ---")
    print(f"Oluşturulan Şifre: {yeni_sifre}")
    print("-------------\n")

if __name__ == "__main__":
    kullanici_etkilesimi()