from flask import Flask, render_template, request
import requests

app = Flask(__name__)

def kripto_fiyat_getir():
    try:
        url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
        cevap = requests.get(url, timeout=5).json()
        return {
            'btc': cevap['bitcoin']['usd'],
            'eth': cevap['ethereum']['usd']
        }
    except:
        return {'btc': 0, 'eth': 0} 

@app.route('/', methods=['GET', 'POST'])
def index():
    sonuc = None
    fiyatlar = kripto_fiyat_getir() 
    
    if request.method == 'POST':
        try:
            hashrate = float(request.form.get('hashrate')) 
            guc_tuketimi = float(request.form.get('power')) 
            elektrik_ucreti = float(request.form.get('cost'))
            pool_fee = float(request.form.get('pool_fee'))
            tahmini_kazanc = float(request.form.get('daily_reward')) 
            secilen_coin_fiyati = float(request.form.get('coin_price')) 

            gunluk_ciro = tahmini_kazanc * secilen_coin_fiyati
            havuz_kesintisi_tutari = gunluk_ciro * (pool_fee / 100)
            net_gunluk_ciro = gunluk_ciro - havuz_kesintisi_tutari

            gunluk_elektrik_maliyeti = (guc_tuketimi / 1000) * 24 * elektrik_ucreti

            gunluk_net_kar = net_gunluk_ciro - gunluk_elektrik_maliyeti
            aylik_net_kar = gunluk_net_kar * 30
            yillik_net_kar = gunluk_net_kar * 365

            sonuc = {
                'gunluk_net': round(gunluk_net_kar, 2),
                'aylik_net': round(aylik_net_kar, 2),
                'yillik_net': round(yillik_net_kar, 2),
                'elektrik_maliyeti': round(gunluk_elektrik_maliyeti, 2),
                'durum': 'Kârlı' if gunluk_net_kar > 0 else 'Zarar'
            }

        except ValueError:
            pass
    return render_template('index.html', fiyatlar=fiyatlar, sonuc=sonuc)

if __name__ == '__main__':
    app.run(debug=True)