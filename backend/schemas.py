from marshmallow import Schema, fields
from datetime import datetime

class CropSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    soil = fields.Str(required=True)
    sunlight = fields.Str(required=True)
    type = fields.Str(required=True)
    season = fields.Str(required=True)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    email = fields.Email(required=True)
    terrace_size = fields.Float(required=True)
    soil = fields.Str(required=True)
    sunlight = fields.Str(required=True)
    preferred_crop = fields.Str(required=True)
    location = fields.Str(required=True)

class ForumPostSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    author_id = fields.Int(required=True)
    category = fields.Str(required=True)
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    author = fields.Nested(UserSchema, only=['id', 'name'], dump_only=True)
    comments = fields.List(fields.Nested(lambda: CommentSchema(exclude=('post',))), dump_only=True)

class CommentSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    author_id = fields.Int(required=True)
    post_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    author = fields.Nested(UserSchema, only=['id', 'name'], dump_only=True)

class PrivateMessageSchema(Schema):
    id = fields.Int(dump_only=True)
    content = fields.Str(required=True)
    sender_id = fields.Int(required=True)
    receiver_id = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    is_read = fields.Boolean(dump_only=True)
    sender = fields.Nested(UserSchema, only=['id', 'name'], dump_only=True)
    receiver = fields.Nested(UserSchema, only=['id', 'name'], dump_only=True)

class GardenScheduleSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    crop_name = fields.Str(required=True)
    planting_date = fields.Date(required=True)
    expected_harvest = fields.Date()
    notes = fields.Str()
    status = fields.Str()
    created_at = fields.DateTime(dump_only=True)

class CareReminderSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    schedule_id = fields.Int(required=True)
    reminder_type = fields.Str(required=True)
    reminder_date = fields.Date(required=True)
    is_completed = fields.Boolean()
    notes = fields.Str()
    created_at = fields.DateTime(dump_only=True)

class WeatherAlertSchema(Schema):
    id = fields.Int(dump_only=True)
    location = fields.Str(required=True)
    alert_type = fields.Str(required=True)
    message = fields.Str(required=True)
    severity = fields.Str(required=True)
    start_date = fields.DateTime(required=True)
    end_date = fields.DateTime()
    is_active = fields.Boolean()
    created_at = fields.DateTime(dump_only=True)

class CropGuideSchema(Schema):
    id = fields.Int(dump_only=True)
    crop_name = fields.Str(required=True)
    planting_season = fields.Str(required=True)
    growing_time_days = fields.Int(required=True)
    water_frequency = fields.Str(required=True)
    sunlight_needs = fields.Str(required=True)
    soil_type = fields.Str(required=True)
    fertilizer_needs = fields.Str()
    common_pests = fields.Str()
    harvesting_tips = fields.Str()
    difficulty_level = fields.Str(required=True)

class GardenJournalSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    schedule_id = fields.Int()
    entry_date = fields.Date(required=True)
    title = fields.Str(required=True)
    content = fields.Str(required=True)
    mood = fields.Str()
    photos = fields.Str()
    created_at = fields.DateTime(dump_only=True)

class NotificationSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    message = fields.Str(required=True)
    notification_type = fields.Str(required=True)
    is_read = fields.Boolean()
    created_at = fields.DateTime(dump_only=True)

class ProductSchema(Schema):
    id = fields.Int(dump_only=True)
    seller_id = fields.Int(required=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)
    price = fields.Float(required=True)
    category = fields.Str(required=True)
    condition = fields.Str(required=True)
    quantity = fields.Int(required=True)
    images = fields.Str()
    location = fields.Str(required=True)
    is_available = fields.Boolean()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    seller = fields.Nested(UserSchema, only=['id', 'name'], dump_only=True)

class OrderSchema(Schema):
    id = fields.Int(dump_only=True)
    buyer_id = fields.Int(required=True)
    seller_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    total_price = fields.Float(required=True)
    status = fields.Str()
    delivery_address = fields.Str(required=True)
    contact_phone = fields.Str(required=True)
    order_notes = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    buyer = fields.Nested(UserSchema, only=['id', 'name'], dump_only=True)
    seller = fields.Nested(UserSchema, only=['id', 'name'], dump_only=True)
    product = fields.Nested(ProductSchema, only=['id', 'name', 'price'], dump_only=True)

class CartSchema(Schema):
    id = fields.Int(dump_only=True)
    user_id = fields.Int(required=True)
    product_id = fields.Int(required=True)
    quantity = fields.Int(required=True)
    created_at = fields.DateTime(dump_only=True)
    product = fields.Nested(ProductSchema, only=['id', 'name', 'price', 'images'], dump_only=True)

class ReviewSchema(Schema):
    id = fields.Int(dump_only=True)
    product_id = fields.Int(required=True)
    reviewer_id = fields.Int(required=True)
    rating = fields.Int(required=True)
    comment = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    reviewer = fields.Nested(UserSchema, only=['id', 'name'], dump_only=True)
