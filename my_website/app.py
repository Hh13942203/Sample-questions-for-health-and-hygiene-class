from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/view-pdf')
def view_pdf():
    # مسیر فایل PDF برای نمایش در صفحه
    pdf_url = url_for('static', filename='pdf/my_file.pdf')
    return render_template('view_pdf.html', pdf_url=pdf_url)

if __name__ == '__main__':
    app.run(debug=True)
@app.route('/view_pdf')
def view_pdf():
    return render_template('view_pdf.html', pdf_url=url_for('static', filename='pdf/my_file.pdf'))
