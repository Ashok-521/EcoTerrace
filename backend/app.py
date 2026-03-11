from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import db, Crop, User, ForumPost, Comment, PrivateMessage, GardenSchedule, CareReminder, WeatherAlert, CropGuide, GardenJournal, Notification, Product, Order, Cart, Review
from schemas import CropSchema, UserSchema, ForumPostSchema, CommentSchema, PrivateMessageSchema, GardenScheduleSchema, CareReminderSchema, WeatherAlertSchema, CropGuideSchema, GardenJournalSchema, NotificationSchema, ProductSchema, OrderSchema, CartSchema, ReviewSchema
import requests
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecoterrace.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
CORS(app)

CROP_SCHEMA = CropSchema()
CROPS_SCHEMA = CropSchema(many=True)
FORUM_POST_SCHEMA = ForumPostSchema()
FORUM_POSTS_SCHEMA = ForumPostSchema(many=True)
COMMENT_SCHEMA = CommentSchema()
COMMENTS_SCHEMA = CommentSchema(many=True)
MESSAGE_SCHEMA = PrivateMessageSchema()
MESSAGES_SCHEMA = PrivateMessageSchema(many=True)
SCHEDULE_SCHEMA = GardenScheduleSchema()
SCHEDULES_SCHEMA = GardenScheduleSchema(many=True)
REMINDER_SCHEMA = CareReminderSchema()
REMINDERS_SCHEMA = CareReminderSchema(many=True)
WEATHER_ALERT_SCHEMA = WeatherAlertSchema()
WEATHER_ALERTS_SCHEMA = WeatherAlertSchema(many=True)
CROP_GUIDE_SCHEMA = CropGuideSchema()
CROP_GUIDES_SCHEMA = CropGuideSchema(many=True)
JOURNAL_SCHEMA = GardenJournalSchema()
JOURNALS_SCHEMA = GardenJournalSchema(many=True)
NOTIFICATION_SCHEMA = NotificationSchema()
NOTIFICATIONS_SCHEMA = NotificationSchema(many=True)
PRODUCT_SCHEMA = ProductSchema()
PRODUCTS_SCHEMA = ProductSchema(many=True)
ORDER_SCHEMA = OrderSchema()
ORDERS_SCHEMA = OrderSchema(many=True)
CART_SCHEMA = CartSchema()
CARTS_SCHEMA = CartSchema(many=True)
REVIEW_SCHEMA = ReviewSchema()
REVIEWS_SCHEMA = ReviewSchema(many=True)

# Your OpenWeatherMap API key
API_KEY = "a2fd88ad38939cb61fa26d46dac19b10"

# Initialize DB
with app.app_context():
    db.create_all()

# Add default crops if DB empty
with app.app_context():
    if Crop.query.count() == 0:
        default_crops = [
            Crop(name="Tomato", soil="loamy", sunlight="full", type="vegetables", season="summer"),
            Crop(name="Spinach", soil="sandy", sunlight="partial", type="vegetables", season="winter"),
            Crop(name="Basil", soil="loamy", sunlight="full", type="herbs", season="summer"),
            Crop(name="Mint", soil="sandy", sunlight="partial", type="herbs", season="monsoon"),
            Crop(name="Coriander", soil="loamy", sunlight="full", type="herbs", season="winter"),
            Crop(name="Lettuce", soil="sandy", sunlight="partial", type="vegetables", season="winter"),
            Crop(name="Chili", soil="loamy", sunlight="full", type="vegetables", season="summer"),
            Crop(name="Fenugreek", soil="sandy", sunlight="full", type="herbs", season="monsoon")
        ]
        for crop in default_crops:
            db.session.add(crop)
        db.session.commit()

# Weather API
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        data = response.json()
        temp = data["main"]["temp"]
        weather = data["weather"][0]["main"]
        return temp, weather
    except:
        return None, None

# Recommend crops
@app.route('/get_recommendation', methods=['POST'])
def get_recommendation():
    data = request.json
    soil = data["soil"]
    sunlight = data["sunlight"]
    crop_type = data["crop"]
    size = float(data["size"])
    location = data["location"]

    temp, weather = get_weather(location)
    recommended = []

    crops = Crop.query.filter_by(soil=soil, sunlight=sunlight, type=crop_type).all()

    for crop in crops:
        if temp:
            if crop.name == "Spinach" and temp > 30:
                continue
            if crop.name == "Tomato" and temp < 18:
                continue
        if size < 100 and crop.name in ["Basil", "Mint", "Coriander"]:
            recommended.append(crop.name)
        elif size >= 100:
            recommended.append(crop.name)

    if not recommended:
        recommended.append("No matching crop found. Try different options.")

    return jsonify({"recommended_crops": recommended})

# Communication Hub API Endpoints

# User Management
@app.route('/api/users', methods=['POST'])
def create_user():
    data = request.json
    user = User(
        name=data['name'],
        email=data['email'],
        terrace_size=data.get('terrace_size'),
        soil=data.get('soil'),
        sunlight=data.get('sunlight'),
        preferred_crop=data.get('preferred_crop'),
        location=data.get('location')
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(USER_SCHEMA.dump(user)), 201

@app.route('/api/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(user_id)
    return jsonify(USER_SCHEMA.dump(user))

# Forum Posts
@app.route('/api/forum/posts', methods=['GET'])
def get_forum_posts():
    category = request.args.get('category')
    query = ForumPost.query
    if category:
        query = query.filter_by(category=category)
    posts = query.order_by(ForumPost.created_at.desc()).all()
    return jsonify(FORUM_POSTS_SCHEMA.dump(posts))

@app.route('/api/forum/posts', methods=['POST'])
def create_forum_post():
    data = request.json
    post = ForumPost(
        title=data['title'],
        content=data['content'],
        author_id=data['author_id'],
        category=data['category']
    )
    db.session.add(post)
    db.session.commit()
    return jsonify(FORUM_POST_SCHEMA.dump(post)), 201

@app.route('/api/forum/posts/<int:post_id>', methods=['GET'])
def get_forum_post(post_id):
    post = ForumPost.query.get_or_404(post_id)
    return jsonify(FORUM_POST_SCHEMA.dump(post))

# Comments
@app.route('/api/forum/posts/<int:post_id>/comments', methods=['GET'])
def get_comments(post_id):
    comments = Comment.query.filter_by(post_id=post_id).order_by(Comment.created_at.asc()).all()
    return jsonify(COMMENTS_SCHEMA.dump(comments))

@app.route('/api/forum/posts/<int:post_id>/comments', methods=['POST'])
def create_comment(post_id):
    data = request.json
    comment = Comment(
        content=data['content'],
        author_id=data['author_id'],
        post_id=post_id
    )
    db.session.add(comment)
    db.session.commit()
    return jsonify(COMMENT_SCHEMA.dump(comment)), 201

# Private Messages
@app.route('/api/messages/<int:user_id>', methods=['GET'])
def get_messages(user_id):
    messages = PrivateMessage.query.filter_by(receiver_id=user_id).order_by(PrivateMessage.created_at.desc()).all()
    return jsonify(MESSAGES_SCHEMA.dump(messages))

@app.route('/api/messages', methods=['POST'])
def send_message():
    data = request.json
    message = PrivateMessage(
        content=data['content'],
        sender_id=data['sender_id'],
        receiver_id=data['receiver_id']
    )
    db.session.add(message)
    db.session.commit()
    return jsonify(MESSAGE_SCHEMA.dump(message)), 201

@app.route('/api/messages/<int:message_id>/read', methods=['PUT'])
def mark_message_read(message_id):
    message = PrivateMessage.query.get_or_404(message_id)
    message.is_read = True
    db.session.commit()
    return jsonify({"status": "marked as read"})

# Garden Calendar API
@app.route('/api/garden/schedules', methods=['GET'])
def get_garden_schedules():
    user_id = request.args.get('user_id', 1)
    schedules = GardenSchedule.query.filter_by(user_id=user_id).order_by(GardenSchedule.planting_date.desc()).all()
    return jsonify(SCHEDULES_SCHEMA.dump(schedules))

@app.route('/api/garden/schedules', methods=['POST'])
def create_garden_schedule():
    data = request.json
    schedule = GardenSchedule(
        user_id=data['user_id'],
        crop_name=data['crop_name'],
        planting_date=datetime.strptime(data['planting_date'], '%Y-%m-%d').date(),
        expected_harvest=datetime.strptime(data['expected_harvest'], '%Y-%m-%d').date() if data.get('expected_harvest') else None,
        notes=data.get('notes'),
        status=data.get('status', 'planned')
    )
    db.session.add(schedule)
    db.session.commit()
    return jsonify(SCHEDULE_SCHEMA.dump(schedule)), 201

# Care Reminders API
@app.route('/api/reminders', methods=['GET'])
def get_reminders():
    user_id = request.args.get('user_id', 1)
    reminders = CareReminder.query.filter_by(user_id=user_id, is_completed=False).order_by(CareReminder.reminder_date.asc()).all()
    return jsonify(REMINDERS_SCHEMA.dump(reminders))

@app.route('/api/reminders', methods=['POST'])
def create_reminder():
    data = request.json
    reminder = CareReminder(
        user_id=data['user_id'],
        schedule_id=data['schedule_id'],
        reminder_type=data['reminder_type'],
        reminder_date=datetime.strptime(data['reminder_date'], '%Y-%m-%d').date(),
        notes=data.get('notes')
    )
    db.session.add(reminder)
    db.session.commit()
    return jsonify(REMINDER_SCHEMA.dump(reminder)), 201

@app.route('/api/reminders/<int:reminder_id>/complete', methods=['PUT'])
def complete_reminder(reminder_id):
    reminder = CareReminder.query.get_or_404(reminder_id)
    reminder.is_completed = True
    db.session.commit()
    return jsonify({"status": "completed"})

# Weather Alerts API
@app.route('/api/weather/alerts', methods=['GET'])
def get_weather_alerts():
    location = request.args.get('location', 'Mumbai')
    alerts = WeatherAlert.query.filter_by(location=location, is_active=True).order_by(WeatherAlert.created_at.desc()).all()
    return jsonify(WEATHER_ALERTS_SCHEMA.dump(alerts))

# Crop Guides API
@app.route('/api/crops/guides', methods=['GET'])
def get_crop_guides():
    crop_name = request.args.get('crop_name')
    if crop_name:
        guide = CropGuide.query.filter_by(crop_name=crop_name).first()
        return jsonify(CROP_GUIDE_SCHEMA.dump(guide)) if guide else jsonify({"error": "Guide not found"}), 404
    
    guides = CropGuide.query.all()
    return jsonify(CROP_GUIDES_SCHEMA.dump(guides))

# Garden Journal API
@app.route('/api/garden/journal', methods=['GET'])
def get_garden_journal():
    user_id = request.args.get('user_id', 1)
    entries = GardenJournal.query.filter_by(user_id=user_id).order_by(GardenJournal.entry_date.desc()).all()
    return jsonify(JOURNALS_SCHEMA.dump(entries))

@app.route('/api/garden/journal', methods=['POST'])
def create_journal_entry():
    data = request.json
    entry = GardenJournal(
        user_id=data['user_id'],
        schedule_id=data.get('schedule_id'),
        entry_date=datetime.strptime(data['entry_date'], '%Y-%m-%d').date(),
        title=data['title'],
        content=data['content'],
        mood=data.get('mood'),
        photos=data.get('photos')
    )
    db.session.add(entry)
    db.session.commit()
    return jsonify(JOURNAL_SCHEMA.dump(entry)), 201

# Notifications API
@app.route('/api/notifications', methods=['GET'])
def get_notifications():
    user_id = request.args.get('user_id', 1)
    notifications = Notification.query.filter_by(user_id=user_id).order_by(Notification.created_at.desc()).limit(50).all()
    return jsonify(NOTIFICATIONS_SCHEMA.dump(notifications))

@app.route('/api/notifications', methods=['POST'])
def create_notification():
    data = request.json
    notification = Notification(
        user_id=data['user_id'],
        message=data['message'],
        notification_type=data['notification_type']
    )
    db.session.add(notification)
    db.session.commit()
    return jsonify(NOTIFICATION_SCHEMA.dump(notification)), 201

@app.route('/api/notifications/<int:notification_id>/read', methods=['PUT'])
def mark_notification_read(notification_id):
    notification = Notification.query.get_or_404(notification_id)
    notification.is_read = True
    db.session.commit()
    return jsonify({"status": "marked as read"})

@app.route('/api/notifications/unread/count', methods=['GET'])
def get_unread_count():
    user_id = request.args.get('user_id', 1)
    count = Notification.query.filter_by(user_id=user_id, is_read=False).count()
    return jsonify({"unread_count": count})

@app.route('/api/notifications/mark-all-read', methods=['PUT'])
def mark_all_notifications_read():
    user_id = request.args.get('user_id', 1)
    Notification.query.filter_by(user_id=user_id, is_read=False).update({'is_read': True})
    db.session.commit()
    return jsonify({"status": "all notifications marked as read"})

# Marketplace API Endpoints

# Products
@app.route('/api/products', methods=['GET'])
def get_products():
    category = request.args.get('category')
    search = request.args.get('search')
    location = request.args.get('location')
    min_price = request.args.get('min_price', type=float)
    max_price = request.args.get('max_price', type=float)
    
    query = Product.query.filter_by(is_available=True)
    
    if category:
        query = query.filter_by(category=category)
    if search:
        query = query.filter(Product.name.contains(search) | Product.description.contains(search))
    if location:
        query = query.filter(Product.location.contains(location))
    if min_price:
        query = query.filter(Product.price >= min_price)
    if max_price:
        query = query.filter(Product.price <= max_price)
    
    products = query.order_by(Product.created_at.desc()).all()
    return jsonify(PRODUCTS_SCHEMA.dump(products))

@app.route('/api/products', methods=['POST'])
def create_product():
    data = request.json
    product = Product(
        seller_id=data['seller_id'],
        name=data['name'],
        description=data['description'],
        price=data['price'],
        category=data['category'],
        condition=data['condition'],
        quantity=data['quantity'],
        location=data['location'],
        images=data.get('images')
    )
    db.session.add(product)
    db.session.commit()
    return jsonify(PRODUCT_SCHEMA.dump(product)), 201

@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = Product.query.get_or_404(product_id)
    return jsonify(PRODUCT_SCHEMA.dump(product))

# Shopping Cart
@app.route('/api/cart', methods=['GET'])
def get_cart():
    user_id = request.args.get('user_id', 1)
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    return jsonify(CARTS_SCHEMA.dump(cart_items))

@app.route('/api/cart', methods=['POST'])
def add_to_cart():
    data = request.json
    existing_item = Cart.query.filter_by(
        user_id=data['user_id'], 
        product_id=data['product_id']
    ).first()
    
    if existing_item:
        existing_item.quantity += data['quantity']
    else:
        cart_item = Cart(
            user_id=data['user_id'],
            product_id=data['product_id'],
            quantity=data['quantity']
        )
        db.session.add(cart_item)
    
    db.session.commit()
    return jsonify({"status": "added to cart"})

@app.route('/api/cart/<int:cart_id>', methods=['DELETE'])
def remove_from_cart(cart_id):
    cart_item = Cart.query.get_or_404(cart_id)
    db.session.delete(cart_item)
    db.session.commit()
    return jsonify({"status": "removed from cart"})

# Orders
@app.route('/api/orders', methods=['GET'])
def get_orders():
    user_id = request.args.get('user_id', 1)
    orders = Order.query.filter(
        (Order.buyer_id == user_id) | (Order.seller_id == user_id)
    ).order_by(Order.created_at.desc()).all()
    return jsonify(ORDERS_SCHEMA.dump(orders))

@app.route('/api/orders', methods=['POST'])
def create_order():
    data = request.json
    
    # Get product to calculate total price
    product = Product.query.get(data['product_id'])
    if not product or product.quantity < data['quantity']:
        return jsonify({"error": "Product not available"}), 400
    
    # Create order
    order = Order(
        buyer_id=data['buyer_id'],
        seller_id=product.seller_id,
        product_id=data['product_id'],
        quantity=data['quantity'],
        total_price=product.price * data['quantity'],
        delivery_address=data['delivery_address'],
        contact_phone=data['contact_phone'],
        order_notes=data.get('order_notes')
    )
    
    # Update product quantity
    product.quantity -= data['quantity']
    
    # Clear from cart
    Cart.query.filter_by(
        user_id=data['buyer_id'], 
        product_id=data['product_id']
    ).delete()
    
    db.session.add(order)
    db.session.commit()
    
    return jsonify(ORDER_SCHEMA.dump(order)), 201

@app.route('/api/orders/<int:order_id>/status', methods=['PUT'])
def update_order_status(order_id):
    data = request.json
    order = Order.query.get_or_404(order_id)
    order.status = data['status']
    db.session.commit()
    return jsonify({"status": "order status updated"})

# Reviews
@app.route('/api/products/<int:product_id>/reviews', methods=['GET'])
def get_product_reviews(product_id):
    reviews = Review.query.filter_by(product_id=product_id).order_by(Review.created_at.desc()).all()
    return jsonify(REVIEWS_SCHEMA.dump(reviews))

@app.route('/api/products/<int:product_id>/reviews', methods=['POST'])
def create_review():
    data = request.json
    review = Review(
        product_id=data['product_id'],
        reviewer_id=data['reviewer_id'],
        rating=data['rating'],
        comment=data.get('comment')
    )
    db.session.add(review)
    db.session.commit()
    return jsonify(REVIEW_SCHEMA.dump(review)), 201

@app.route('/')
def home():
    return "Backend Running with DB and Weather API!"

if __name__ == '__main__':
    app.run(debug=True)
