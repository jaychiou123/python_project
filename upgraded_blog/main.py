from flask import Flask, render_template, request
import requests
import smtplib

my_mail = "jay912145@gmail.com"
password = "prniebnwidnvddeu"
receive = "jay912145@gmail.com"

app = Flask(__name__)
@app.route('/')
def home():
    response = requests.get("https://api.npoint.io/65226b7cb69086515408")
    content = response.json()
    return render_template('index.html', post=content)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        data = request.form
        with smtplib.SMTP("smtp.gmail.com") as connect:
            connect.starttls()  # to secure the content
            connect.login(user=my_mail, password=password)
            connect.sendmail(
                from_addr=my_mail,
                to_addrs=receive,
                msg=f'Subject:New message\n\nName: {data["name"]}\nEmail: {data["email"]}\nPhone number: {data["phone"]}\nMessage: {data["message"]}'
            )
        return render_template('contact.html', msg_sent=True)
    return render_template('contact.html', msg_sent=False)

@app.route('/post/<num>')
def get_blog(num):
    response = requests.get("https://api.npoint.io/65226b7cb69086515408")
    content = response.json()[int(num)-1]
    return render_template('post.html', post=content)

if __name__ == "__main__":
    app.run(debug=True)