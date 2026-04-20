from flask import Flask, request, jsonify
from supabase import create_client
from flask import Flask, request, jsonify, render_template # Thêm render_template
import os

app = Flask(__name__)

# Render sẽ cung cấp các biến này qua mục Environment Variables
url = os.environ.get("SUPABASE_URL")
key = os.environ.get("SUPABASE_KEY")
supabase = create_client(url, key)

@app.route('/')
def home():
    # Trả về giao diện web thay vì dòng chữ thông thường
    return render_template('index.html')

@app.route('/day-du-lieu', methods=['POST'])
def post_data():
    data = request.get_json()
    try:
        # 'ket_qua_giai_ngan' là tên bảng bạn tạo trên Supabase
        response = supabase.table('ket_qua_giai_ngan').insert(data).execute()
        return jsonify({"status": "Thành công", "data": data}), 201
    except Exception as e:
        return jsonify({"status": "Lỗi", "message": str(e)}), 400

if __name__ == '__main__':
    app.run()
