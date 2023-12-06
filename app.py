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
        return render_template("upload_result.html", name=file_name)   # 업로드 완료 시, "upload_result.html" 렌더링
    
    return render_template("home.html")


@app.route("/getFile") # 파일목록 나열
def get_files():
	files = os.listdir("./uploads")
	return render_template('get_file.html', files=files)


@app.route('/uploads')
def uploaded_file():
    f = request.args.get('data')
    return render_template('open_file.html', data=f)



# "home.html": 홈페이지, 파일 업로드 가능
# "upload_result.html": 파일 업로드 결과 표시
# "get_file.html": 업로드한 파일 목록 표시, 파일명 클릭 가능
# "open_file.html": 파일 이름이 {{data}}인 파일을 브라우저에 렌더링하는 것이 목적, 현재 파일의 이름만 표시 가능한 상태


if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
