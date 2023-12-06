# 참고: https://m.blog.naver.com/dsz08082/221868934940


from flask import Flask, render_template, request, send_from_directory
import os


app=Flask(__name__)
UPLOAD_FOLDER = os.getcwd() + '\\uploads'  # 절대 파일 경로


@app.route('/')
def home():    # 메인 경로
    return render_template("home.html")


@app.route("/fileUpload", methods = ['POST']) 
def upload():  # 파일 업로드 처리
    if request.method == "POST":
        f = request.files['file']
        file_name = f.filename
        file_path = os.path.join(UPLOAD_FOLDER, file_name)
        f.save(file_path)
        files = os.listdir("./uploads")
        return render_template("upload_result.html", name=file_name)
    
    return render_template("home.html")


@app.route("/getFile") # 파일목록 나열
def get_files():
	files = os.listdir("./uploads")
	return render_template('get_file.html', files=files)


@app.route('/uploads')
def uploaded_file():
    f = request.args.get('data')
    return render_template('open_file.html', data=f)


# @app.route("/open_file")
# def open_file():
#      f = request.args.get("data")
#      return render_template("open_file.html", data = f)


# 달성 작업: 파일 업로드, 업로드한 파일 목록 나열, 업로드한 파일로 이동할 링크 생성, 링크에서 파일명 출력가능
# 필요 작업: 링크에서 파일 열기, 파일형식 필터링 추가(초기 구현 후 적용)
#


# @app.route("/showFile", methods = ['GET', 'POST'])
# def show_files():
#     if request.method == 'POST':
#         sw = 0
#         files = os.listdir("./uploads")
#         for x in files:
#             if (x == request.form['file']):
#                 sw = 1
#         path = "./uploads/" 
#         return "file shown"



if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)