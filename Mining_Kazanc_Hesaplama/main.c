#include <stdio.h>

void kazancHesapla(float hashOrani, float gucTuketimi, float elektrikMaliyeti, float blokOdulu, float zorlukSeviyesi, float btcUsdFiyati,int madencilikSuresi);

int main() {

    float hashOrani, gucTuketimi, elektrikMaliyeti, blokOdulu, zorlukSeviyesi, btcUsdFiyati;
    int madencilikSuresi;

    printf("Hash oranini (TH/s) girin: ");
    scanf("%f", &hashOrani);

    printf("Guc tuketimini (Watt) girin: ");
    scanf("%f", &gucTuketimi);

    printf("Elektrik maliyetini ($/kWh) girin: ");
    scanf("%f", &elektrikMaliyeti);

    printf("Blok odulunu (BTC) girin: ");
    scanf("%f", &blokOdulu);

    printf("Zorluk seviyesini girin: ");
    scanf("%f", &zorlukSeviyesi);

    printf("BTC'nin USD karsiligini girin: ");
    scanf("%f", &btcUsdFiyati);

    printf("Madencilik yapilacak sureyi (gun olarak) giriniz: \n");
    scanf("%d", &madencilikSuresi);

kazancHesapla(hashOrani, gucTuketimi, elektrikMaliyeti, blokOdulu, zorlukSeviyesi, btcUsdFiyati, madencilikSuresi);
    return 0;
}

void kazancHesapla(float hashOrani, float gucTuketimi, float elektrikMaliyeti, float blokOdulu, float zorlukSeviyesi, float btcUsdFiyati,int madencilikSuresi) {

    float kazanc, gunlukElektrikMaliyeti;

    // Elektrik maliyetini hesapla (BTC cinsinden)
    gunlukElektrikMaliyeti = ((gucTuketimi / 1000) * 24 * elektrikMaliyeti) / btcUsdFiyati;

    kazanc = (hashOrani * blokOdulu) / zorlukSeviyesi;


    // G�nl�k net kazan�
    float netKazanc = kazanc - gunlukElektrikMaliyeti;

    //Aylık olarak kazancı (30 gün)
    float aylikKazanc = netKazanc * 30;

    // Aylık elektrik maliyetini hesaplama
    float aylikElektrikMaliyeti = gunlukElektrikMaliyeti * 30;

     // Aylık net kazanç
    float aylikNetKazanc = aylikKazanc - aylikElektrikMaliyeti;

    printf("Gunluk Kazanc: %.8f BTC\n", kazanc);
    printf("Gunluk Elektrik Maliyeti: %.8f BTC\n", gunlukElektrikMaliyeti);
    printf("Gunluk Net Kazanc: %.8f BTC\n", netKazanc);
    printf("\n");
    printf("Madencilik Yapilacak Sure: %d gun\n", madencilikSuresi);
    printf("Madencilik Sureli Aylik Kazanc: %.8f BTC\n", aylikKazanc);
    printf("Madencilik Sureli Aylik Elektrik Maliyeti: %.8f BTC\n", aylikElektrikMaliyeti);
    printf("Madencilik Sureli Aylik Net Kazanc: %.8f BTC\n", aylikNetKazanc);

}
