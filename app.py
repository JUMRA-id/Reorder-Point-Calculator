from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/hitung", methods=["POST"])
def hitung():
    data = request.get_json()

    penjualan_per_hari  = float(data.get("penjualan_per_hari", 0))
    waktu_tunggu        = float(data.get("waktu_tunggu", 0))
    stok_cadangan       = float(data.get("stok_cadangan", 0))
    stok_sekarang       = float(data.get("stok_sekarang", 0))

    # Validasi
    if penjualan_per_hari <= 0:
        return jsonify({"error": "Penjualan per hari harus lebih dari 0"}), 400
    if waktu_tunggu <= 0:
        return jsonify({"error": "Waktu tunggu supplier harus lebih dari 0"}), 400

    # ── RUMUS UTAMA ──────────────────────────────────────────────────────────
    # Reorder Point = (penjualan per hari × waktu tunggu) + stok cadangan
    # Artinya: titik stok di mana kamu HARUS order sekarang
    # supaya barang tidak habis sebelum kiriman datang
    reorder_point   = (penjualan_per_hari * waktu_tunggu) + stok_cadangan

    # Stok habis dalam berapa hari dari sekarang
    hari_habis      = stok_sekarang / penjualan_per_hari if stok_sekarang > 0 else 0

    # Kapan harus order (berapa hari lagi dari sekarang)
    hari_order      = (stok_sekarang - reorder_point) / penjualan_per_hari
    hari_order      = max(0, hari_order)  # tidak boleh negatif

    # Status stok sekarang
    if stok_sekarang <= reorder_point:
        status = "bahaya"
        pesan  = "Stok kritis! Kamu harus order sekarang!"
    elif stok_sekarang <= reorder_point * 1.5:
        status = "waspada"
        pesan  = f"Segera order dalam {hari_order:.0f} hari lagi."
    else:
        status = "aman"
        pesan  = f"Stok aman. Order lagi dalam {hari_order:.0f} hari."

    def unit(angka):
        return f"{angka:,.0f} pcs".replace(",", ".")

    return jsonify({
        "reorder_point":    unit(reorder_point),
        "hari_habis":       f"{hari_habis:.0f} hari",
        "hari_order":       f"{hari_order:.0f} hari lagi" if hari_order > 0 else "Sekarang!",
        "stok_cadangan":    unit(stok_cadangan),
        "status":           status,
        "pesan":            pesan,
    })

if __name__ == "__main__":
    app.run(debug=True)
