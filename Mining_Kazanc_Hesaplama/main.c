#include <stdio.h>

void kazancHesapla(float hashOrani, float gucTuketimi, float elektrikMaliyeti, float blokOdulu, float zorlukSeviyesi, float btcUsdFiyati);

int main() {

    float hashOrani, gucTuketimi, elektrikMaliyeti, blokOdulu, zorlukSeviyesi, btcUsdFiyati;

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

    kazancHesapla(hashOrani, gucTuketimi, elektrikMaliyeti, blokOdulu, zorlukSeviyesi, btcUsdFiyati);

    return 0;
}

void kazancHesapla(float hashOrani, float gucTuketimi, float elektrikMaliyeti, float blokOdulu, float zorlukSeviyesi, float btcUsdFiyati) {

    float kazanc, gunlukElektrikMaliyeti;

    // Elektrik maliyetini hesapla (BTC cinsinden)
    gunlukElektrikMaliyeti = ((gucTuketimi / 1000) * 24 * elektrikMaliyeti) / btcUsdFiyati;

    kazanc = (hashOrani * blokOdulu) / zorlukSeviyesi;

    // Günlük net kazanç
    float netKazanc = kazanc - gunlukElektrikMaliyeti;

    printf("Gunluk Kazanc: %.8f BTC\n", kazanc);
    printf("Gunluk Elektrik Maliyeti: %.8f BTC\n", gunlukElektrikMaliyeti);
    printf("Gunluk Net Kazanc: %.8f BTC\n", netKazanc);
}
