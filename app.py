from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def kripto_fiyat_getir():
    """Popüler madencilik coinlerinin canlı fiyatlarını çeker"""
    ids = "bitcoin,ethereum,ravencoin,dogecoin,solana,flux"
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={ids}&vs_currencies=usd"
    try:
        cevap = requests.get(url, timeout=5).json()
        return {
            'BTC': cevap['bitcoin']['usd'],
            'ETH': cevap['ethereum']['usd'],
            'RVN': cevap['ravencoin']['usd'],
            'DOGE': cevap['dogecoin']['usd'],
            'SOL': cevap['solana']['usd'],
            'FLUX': cevap['flux']['usd']
        }
    except:
        # Hata durumunda varsayılan değerler
        return {'BTC': 0, 'ETH': 0, 'RVN': 0, 'DOGE': 0, 'SOL': 0, 'FLUX': 0}

@app.route('/', methods=['GET', 'POST'])
def index():
    sonuc = None
    fiyatlar = kripto_fiyat_getir()
    
    if request.method == 'POST':
        try:
            # GÜNCELLENMİŞ KISIM BAŞLANGICI
            # get('veri_adi', 0) diyerek, eğer veri gelmezse 0 kabul et diyoruz.
            # Böylece program asla çökmez.
            
            hashrate = float(request.form.get('hashrate', 0))
            guc_tuketimi = float(request.form.get('power', 0))
            elektrik_ucreti = float(request.form.get('cost', 0))
            pool_fee = float(request.form.get('pool_fee', 0)) # Hata veren satır buydu
            tahmini_kazanc = float(request.form.get('daily_reward', 0))
            donanim_maliyeti = float(request.form.get('hardware_cost', 0))
            secilen_coin_fiyati = float(request.form.get('coin_price', 0))
            # GÜNCELLENMİŞ KISIM BİTİŞİ

            # --- HESAPLAMALAR ---
            
            # 1. Gelir & Gider
            gunluk_ciro = tahmini_kazanc * secilen_coin_fiyati
            havuz_kesintisi_tutari = gunluk_ciro * (pool_fee / 100)
            net_gunluk_ciro = gunluk_ciro - havuz_kesintisi_tutari
            
            gunluk_elektrik_maliyeti = (guc_tuketimi / 1000) * 24 * elektrik_ucreti
            
            gunluk_net_kar = net_gunluk_ciro - gunluk_elektrik_maliyeti
            
            # 2. ROI (Amorti Süresi) Hesabı
            amorti_gun = 0
            if gunluk_net_kar > 0:
                amorti_gun = donanim_maliyeti / gunluk_net_kar
            
            # 3. Grafik Verileri İçin Hazırlık (Aylık Projeksiyon)
            aylik_veriler = []
            birikimli_kazanc = 0
            for ay in range(1, 13):
                birikimli_kazanc += gunluk_net_kar * 30
                aylik_veriler.append(round(birikimli_kazanc, 2))

            sonuc = {
                'gunluk_net': round(gunluk_net_kar, 2),
                'aylik_net': round(gunluk_net_kar * 30, 2),
                'yillik_net': round(gunluk_net_kar * 365, 2),
                'elektrik_maliyeti': round(gunluk_elektrik_maliyeti, 2),
                'ciro': round(net_gunluk_ciro, 2),
                'amorti_gun': int(amorti_gun) if amorti_gun > 0 else "Asla",
                'amorti_ay': round(amorti_gun / 30, 1) if amorti_gun > 0 else "∞",
                'grafik_data': aylik_veriler
            }

        except ValueError:
            pass

    return render_template('index.html', fiyatlar=fiyatlar, sonuc=sonuc)
    return render_template('index.html', fiyatlar=fiyatlar, sonuc=sonuc)

if __name__ == '__main__':
    app.run(debug=True)