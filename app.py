from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    images = [
        'image000000 (2).JPG',
        'image000000 (3).JPG',
        'image000000.JPG',
        'image000001.JPG',
        'image000002.JPG',
        'image000003.JPG',
        'image000004.JPG',
        'image000000 (1).JPG'
    ]
    messages = [
        'Welcome to my website!',
        'Check out these amazing pictures!',
        'Explore the beauty captured in these images!',
        'Feel free to reach out if you have any questions!',
        'Enjoy your stay!',
        'Discover more about us!',
        'Join our community!',
        'Stay updated with our latest news!'
    ]
    return render_template('index.html', images=images, messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
