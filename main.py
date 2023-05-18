class Magaza:
    def __init__(self, magaza_adi, satici_adi, satici_cinsi, satis_tutari):
        # private özellikleri atıyoruz:
        self.__magaza_adi = magaza_adi
        self.__satici_adi = satici_adi
        self.__satici_cinsi = satici_cinsi
        self.__satis_tutari = satis_tutari

    # accessor metodu
    def get_magaza_adi(self):
        return self.__magaza_adi
    # mutator metodu
    def set_magaza_adi(self, magaza_adi):
        self.__magaza_adi = magaza_adi

    def get_satici_adi(self):
        return self.__satici_adi

    def set_satici_adi(self, satici_adi):
        self.__satici_adi = satici_adi

    def get_satici_cinsi(self):
        return self.__satici_cinsi

    def set_satici_cinsi(self, satici_cinsi):
        self.__satici_cinsi = satici_cinsi

    def get_satis_tutari(self):
        return self.__satis_tutari

    def set_satis_tutari(self, satis_tutari):
        self.__satis_tutari = satis_tutari

    def __str__(self):
        return f"Mağaza adı: {self.__magaza_adi}, Satıcı adı: {self.__satici_adi}, " \
               f"Satıcı cinsi: {self.__satici_cinsi}, Satış tutarı: {self.__satis_tutari}"

# toplam satış tutar değerini hesaplamak için fonks:
def magaza_satis_tutari_hesapla(magaza_listesi, satici_adi):
    saticinin_satislari = [magaza for magaza in magaza_listesi if magaza.get_satici_adi() == satici_adi]
    toplam_satis_tutari = sum([magaza.get_satis_tutari() for magaza in saticinin_satislari]) # sum metodu ile toplama
    return toplam_satis_tutari

def main():
    # mağaza ve satıcı adı listeleri oluştur:
    magaza_listesi = []
    satici_adlari = []
    satis_tutarlari = {}

    while True:
        # kullanıcıdan bilgileri alıyoruz:
        magaza_adi = input("Mağazanın adını giriniz: ")
        satici_adi = input("Satıcının adını giriniz: ")
        satici_cinsi = input("Satıcının cinsini giriniz (tv, bilgisayar, beyaz eşya, diğer): ")
        satis_tutari = float(input("Satış tutarını giriniz: "))

        # girilen satıcı adının daha önce girilip girilmediğini kontrol edip listeye ekliyoruz:
        if satici_adi in satici_adlari:
            satis_tutarlari[satici_adi] += satis_tutari
        else:
            satici_adlari.append(satici_adi)
            satis_tutarlari[satici_adi] = satis_tutari

        magaza_listesi.append(Magaza(magaza_adi, satici_adi, satici_cinsi, satis_tutari))

        # kullanıcıya devam etmesi için seçim sunuyoruz:
        devam_et = input("Devam etmek ister misiniz? (Evet ise 'E' Hayır ise 'H'): ")
        if devam_et.lower() != 'e':
            break

    print("\nMağaza satış bilgileri: ")
    # satıcıların toplam tutar değerlerini yazdırıyoruz:
    for satici_adi in satici_adlari:
        saticinin_toplam_satis_tutari = satis_tutarlari[satici_adi]
        print(f"{satici_adi} satıcısının toplam satış tutarı: {saticinin_toplam_satis_tutari}")

        # birden fazla satış yapan satıcılar listesi
        if saticinin_toplam_satis_tutari > 0:
            satis_sayisi = len([magaza for magaza in magaza_listesi if magaza.get_satici_adi() == satici_adi])
            if satis_sayisi > 1:
                print(f"{satici_adi} satıcısı {satis_sayisi} satış yaptı.\n")

        # birden çok satış yapan satıcıların listesi
    birden_cok_satis_yapanlar = [satici_adi for satici_adi in satici_adlari
                                 if len([magaza for magaza in magaza_listesi if
                                         magaza.get_satici_adi() == satici_adi]) > 1]
  # birden çok satış yapan satıcıları yazdırma:
    if len(birden_cok_satis_yapanlar) > 0:
        print("Birden çok satış yapan satıcıların adları:")
        for satici_adi in birden_cok_satis_yapanlar:
            print(satici_adi)
if __name__ == "__main__":
    main()
    