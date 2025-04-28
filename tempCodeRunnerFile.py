

@app.route('/download-cv')
def download_cv():
    return send_from_directory('static/cv', 'mycv.pdf', as_attachment=False)

@app.route('/Education')
def Education():
    return render_template('sekolah.html')

@app.route('/AboutMe')
def utama():