# EcoTerrace Paper Figures and Charts Guide

## Figure 1: System Architecture Diagram

**Description:** Multi-platform architecture showing web and mobile applications, Flask backend, PostgreSQL database, and external integrations.

**Caption:** Figure 1: EcoTerrace multi-platform architecture illustrating React Native mobile applications, responsive web frontend, Flask RESTful API backend, PostgreSQL database, and external service integrations including weather API, push notifications, and image processing services.

**How to Create:**
- Use PowerPoint/Lucidchart to draw layered architecture
- Top layer: Mobile (iOS/Android) + Web browsers
- Middle layer: Flask API endpoints (25 RESTful APIs)
- Bottom layer: PostgreSQL database
- External connections: OpenWeatherMap, Push notification service, Image processing

---

## Figure 2: Database Schema Diagram

**Description:** Entity relationship diagram showing 13 core entities and their relationships.

**Caption:** Figure 2: EcoTerrace database schema with 13 interconnected entities supporting user management, crop recommendations, community features, garden scheduling, and marketplace functionality.

**Entities to Include:**
- User (central)
- Crop, CropGuide
- ForumPost, Comment, PrivateMessage
- GardenSchedule, CareReminder, GardenJournal
- Product, Order, Cart, Review
- Notification, WeatherAlert, PlantImage

**How to Create:**
- Use draw.io or Lucidchart
- Show primary keys and relationships
- Group related entities (User, Community, Garden, Marketplace)

---

## Figure 3: Crop Success Rate Comparison

**Data:**
- EcoTerrace AI: 95%
- Traditional Methods: 65%
- Other Apps: 75%

**Caption:** Figure 3: Crop success rate comparison showing EcoTerrace AI recommendations (95%) significantly outperforming traditional gardening methods (65%) and existing applications (75%).

**Chart Type:** Bar chart
**Colors:** Green (EcoTerrace), Gray (Traditional), Light Blue (Others)

**Excel Instructions:**
1. Column A: Method (EcoTerrace AI, Traditional, Other Apps)
2. Column B: Success Rate (95, 65, 75)
3. Insert → Chart → Bar Chart
4. Add data labels and axis titles

---

## Figure 4: Yield Improvement by Crop Type

**Data:**
- Tomato: 42% increase
- Leafy Greens: 38% increase
- Herbs: 28% increase
- Overall Average: 35% increase

**Caption:** Figure 4: Yield improvement percentages by crop type using EcoTerrace recommendations compared to traditional methods, with tomatoes showing the highest improvement at 42%.

**Chart Type:** Grouped bar chart
**Colors:** Different shades of green for each crop

**Excel Instructions:**
1. Column A: Crop Type
2. Column B: Yield Improvement (%)
3. Insert → Chart → Bar Chart
4. Sort by improvement percentage

---

## Figure 5: Community Activity Breakdown

**Data:**
- Pest Management: 32% (50 posts)
- Container Gardening: 28% (44 posts)
- Seasonal Planting: 21% (33 posts)
- Soil Preparation: 12% (19 posts)
- Harvesting Tips: 7% (10 posts)

**Caption:** Figure 5: Community forum activity distribution across gardening topics, with pest management (32%) and container gardening (28%) being the most discussed subjects.

**Chart Type:** Pie chart
**Colors:** Different colors for each category

**Excel Instructions:**
1. Column A: Category
2. Column B: Percentage
3. Insert → Chart → Pie Chart
4. Add data labels with percentages

---

## Figure 6: Learning Curve Comparison

**Data:**
- Week 1: Traditional 20%, EcoTerrace 45%
- Week 2: Traditional 35%, EcoTerrace 70%
- Week 3: Traditional 50%, EcoTerrace 85%
- Week 4: Traditional 65%, EcoTerrace 95%

**Caption:** Figure 6: Learning curve comparison showing EcoTerrace users achieve 95% proficiency in 4 weeks compared to 65% for traditional methods, representing a 60% faster learning rate.

**Chart Type:** Line chart with two lines
**Colors:** Blue (EcoTerrace), Orange (Traditional)

**Excel Instructions:**
1. Column A: Week (1,2,3,4)
2. Column B: EcoTerrace % (45,70,85,95)
3. Column C: Traditional % (20,35,50,65)
4. Insert → Chart → Line Chart

---

## Figure 7: Marketplace Transaction Distribution

**Data:**
- Seeds: 45% (40 transactions)
- Organic Fertilizers: 25% (22 transactions)
- Gardening Tools: 20% (18 transactions)
- Plants: 7% (6 transactions)
- Soil: 3% (3 transactions)

**Caption:** Figure 7: Marketplace transaction distribution showing seeds as the dominant category (45%) followed by organic fertilizers (25%) and gardening tools (20%).

**Chart Type:** Pie chart
**Colors:** Green shades for organic items, brown for soil, gray for tools

---

## Figure 8: Cost Savings Analysis

**Data:**
- Traditional Garden Center: $100 (baseline)
- EcoTerrace Marketplace: $78 (22% savings)
- Local Sourcing: $65 (35% savings)

**Caption:** Figure 8: Cost comparison showing EcoTerrace marketplace users achieve 22% average savings, with local sourcing providing up to 35% savings compared to traditional garden centers.

**Chart Type:** Bar chart
**Colors:** Red (Traditional), Green (EcoTerrace), Dark Green (Local)

---

## Figure 9: Mobile App Usage Metrics

**Data:**
- Daily Active Users: 85%
- Camera Usage: 3.2 photos/week/user
- Push Notification Open Rate: 94%
- Disease Detection Accuracy: 92%
- Offline Usage: 34%

**Caption:** Figure 9: Mobile application key performance indicators showing high user engagement with 85% daily active users, 94% push notification open rate, and 92% disease detection accuracy.

**Chart Type:** Dashboard-style combination chart
**Elements:** Use gauges, bars, and indicators

---

## Figure 10: System Performance Metrics

**Data:**
- API Response Time: 245ms average
- Database Query Time: 45ms average
- Page Load Time: 1.8s desktop, 2.3s mobile
- Uptime: 99.2%
- Weather API Success: 98.7%

**Caption:** Figure 10: Technical performance metrics demonstrating sub-250ms API response times, sub-2s page loads, and 99.2% system uptime during testing period.

**Chart Type:** Combination chart with bars and indicators

---

## Mobile App Screenshots (Figures 11-14)

### Figure 11: Mobile App Home Screen
**Caption:** Figure 11: EcoTerrace mobile application home screen showing personalized crop recommendations, weather integration, and quick access to community features.

### Figure 12: Camera Disease Detection
**Caption:** Figure 12: Mobile camera interface for plant disease detection with real-time AI analysis showing 92% accuracy in identifying common plant pathogens.

### Figure 13: Push Notifications
**Caption:** Figure 13: Care reminder push notifications demonstrating 94% open rate with personalized watering, fertilizing, and harvesting alerts.

### Figure 14: Community Forum Mobile View
**Caption:** Figure 14: Mobile-optimized community forum interface enabling knowledge sharing with 156 posts and 423 comments during testing period.

---

## How to Create These Charts

### Using Excel:
1. Input data as specified
2. Select data range
3. Insert → Chart → Choose type
4. Customize colors and labels
5. Export as PNG/PDF

### Using PowerPoint:
1. Insert → Chart
2. Enter data directly
3. Design with conference colors (green theme)
4. Add captions and labels

### Using Python (if you prefer):
```python
import matplotlib.pyplot as plt
import seaborn as sns

# Example for Figure 3
methods = ['EcoTerrace AI', 'Traditional', 'Other Apps']
success_rates = [95, 65, 75]

plt.figure(figsize=(8, 6))
bars = plt.bar(methods, success_rates, color=['#2E7D32', '#757575', '#64B5F6'])
plt.title('Crop Success Rate Comparison')
plt.ylabel('Success Rate (%)')
plt.ylim(0, 100)

# Add data labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 1,
             f'{height}%', ha='center', va='bottom')
plt.savefig('figure3_success_rates.png', dpi=300, bbox_inches='tight')
```

## Conference Guidelines
- **Figure Quality:** Minimum 300 DPI
- **File Format:** PNG or PDF
- **Size:** Fit within column width (3.5 inches) or full width (7 inches)
- **Font Size:** Minimum 8pt for labels, 10pt for captions
- **Colors:** Use colorblind-friendly palette

## Placement in Paper
- **Section 3:** Figures 1, 2 (Architecture, Database)
- **Section 4:** Figures 3-10 (Results, Performance)
- **Section 5:** Figures 11-14 (Mobile App Screenshots)

## File Naming Convention
- figure1_architecture.png
- figure2_database.png
- figure3_success_rates.png
- figure4_yield_improvement.png
- figure5_community_activity.png
- figure6_learning_curve.png
- figure7_marketplace_distribution.png
- figure8_cost_savings.png
- figure9_mobile_metrics.png
- figure10_system_performance.png
- figure11_mobile_home.png
- figure12_camera_detection.png
- figure13_push_notifications.png
- figure14_mobile_forum.png
