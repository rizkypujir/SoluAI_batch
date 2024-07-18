from web3 import Web3
import time

# Menghubungkan ke node Solu Test Network
solu_rpc_url = 'https://testnet.soluai.net/rpc'
web3 = Web3(Web3.HTTPProvider(solu_rpc_url))

# Periksa koneksi ke node
if not web3.is_connected():
    print("Gagal terhubung ke node Solu Test Network")
else:
    print("Berhasil terhubung ke node Solu Test Network")

# Alamat pengirim dan kunci pribadi
sender_address = ''  # Ganti addressmu yaa
private_key = ''  #  isi private keymu cok

# Alamat penerima dan jumlah yang akan dikirim (dalam Wei)
recipient_address = '0x699a1098477b315e0989c0723814e4Ea98868df2'  # Ganti dengan alamat penerima
amount = web3.to_wei(0.000001, 'ether')  # 0.000001 LUAI, atau sesuai kebutuhan Anda

# Mengambil nonce awal untuk transaksi
nonce = web3.eth.get_transaction_count(sender_address)

# Mengirim 10 transaksi
for i in range(10):
    # Membuat transaksi
    transaction = {
        'to': recipient_address,
        'value': amount,
        'gas': 21000,
        'gasPrice': web3.to_wei('0.1', 'gwei'),  # Ganti dengan gas price yang sesuai
        'nonce': nonce + i,
        'chainId': 101989  # Chain ID Solu Test Network
    }

    # Menandatangani transaksi
    signed_txn = web3.eth.account.sign_transaction(transaction, private_key)

    # Mengirim transaksi
    txn_hash = web3.eth.send_raw_transaction(signed_txn.rawTransaction)

    # Mendapatkan hash transaksi
    print(f"Transaksi {i+1} berhasil dikirim dengan hash: {txn_hash.hex()}")

    # URL untuk melihat transaksi di block explorer
    block_explorer_url = f"https://testnet.soluai.net/tx/{txn_hash.hex()}"
    print(f"Lihat transaksi {i+1} di: {block_explorer_url}")

    # Menunggu sejenak sebelum mengirim transaksi berikutnya (opsional)
    time.sleep(1)  # Sesuaikan waktu tunggu sesuai kebutuhan Anda
