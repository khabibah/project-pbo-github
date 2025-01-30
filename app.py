# app.py
from flask import Flask, render_template, redirect, url_for
import webbrowser

app = Flask(__name__)

# Product data
products = [
    {
        "name": "Professional poster design",
        "description": "for your small business",
        "price": "Rp 15,000",
        "image": "product1.png"
    },
    {
        "name": "Gaming Tournament",
        "description": "Eye-catching posters for your gaming events",
        "price": "Rp 35,000",
        "image": "product2.png"
    },
    {
        "name": "Jersey Desain",
        "description": "Custom jersey designs for your team",
        "price": "Rp 150,000",
        "image": "product3.png"
    }
]

# Team data
team = [
    {
        "name": "Arasha",
        "role": "Owner",
        "image": "team1.png"
    },
    {
        "name": "Thia Shopy",
        "role": "Editor",
        "image": "team2.png"
    },
    {
        "name": "Khabibah",
        "role": "Pemasaran",
        "image": "team3.png"
    }
]

# Testimonial data
testimonials = [
    {"name": "Taufik", "text": "Hasilnya kerennnn.. mana murahh lagi ga nyesel whehe"},
    {"name": "Iman", "text": "mantap dahh cepetttttt sehari dah kelarr"},
    {"name": "Aulia", "text": "Hasilnya bagus, beda dari yang lain, mantapp"},
    {"name": "Andri", "text": "Termurah yang pernah gw temuin, di yang lain 1 poster doang ampe 50k njirr, disini kagak, kerennnn"},
    {"name": "werkloze", "text": "Gua dah langganan lama disini, gapernah ngecewain mantap."},
    {"name": "Taufik", "text": "ganyesell dahh lu order disini, murah tapi ga murahan"}
]

@app.route('/')
def home():
    return render_template('index.html', products=products, team=team, testimonials=testimonials)

@app.route('/order/<int:product_id>')
def order(product_id):
    product = products[product_id]
    # Format WhatsApp message
    message = f"Halo, saya ingin memesan {product['name']} - {product['price']}"
    # WhatsApp number from the UI
    whatsapp_number = "6285182205970"
    # Create WhatsApp URL
    whatsapp_url = f"https://wa.me/{whatsapp_number}?text={message}"
    return redirect(whatsapp_url)

if __name__ == '__main__':
    app.run()