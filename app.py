from flask import Flask, render_template
import folium

app = Flask(__name__)

# ข้อมูลสถานที่ ทริป 1 วัน ในกรุงเทพฯ
LOCATIONS = [
    {
        "id": 1,
        "name": "Chulalongkorn University Centenary Park",
        "category": "Urban Nature & Architecture",
        "lat": 13.739525636693298,
        "lng": 100.52362220484453,
        "desc": "อุทยาน 100 ปี จุฬาฯ พื้นที่สีเขียวขนาดใหญ่ใจกลางเมือง ออกแบบเพื่อซึมซับน้ำและลดปัญหาน้ำท่วม เหมาะกับการเดินเล่นช่วงเช้าสัมผัสบรรยากาศความเรียบง่ายและยั่งยืน",
        "image": "https://images.unsplash.com/photo-1588668214407-6ea9a6d8c272?auto=format&fit=crop&w=800&q=80"
    },  # <-- แก้ไขเพิ่มปีกกาปิด } และเครื่องหมาย , ตรงนี้
    {
        "id": 2,
        "name": "Victory Monument Area",
        "category": "City Landmark & Hub",
        "lat": 13.765309859250024,
        "lng": 100.53595673991005,
        "desc": "ศูนย์กลางการเดินทางและสัญลักษณ์สำคัญของกรุงเทพฯ สัมผัสความคล่องตัวของเมืองและความเป็นสถาปัตยกรรมสไตล์โมเดิร์นคลาสสิก",
        "image": "https://images.unsplash.com/photo-1508009603885-50cf7c579365?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 3,
        "name": "Rattanakosin Historic District",
        "category": "Heritage & Culture",
        "lat": 13.750202443613839,
        "lng": 100.49276017120366,
        "desc": "ย่านพระนครและเกาะรัตนโกสินทร์ โอบล้อมด้วยวัดวาอารามและถนนประวัติศาสตร์ เสน่ห์ของสถาปัตยกรรมไทยคลาสสิกผสานกลิ่นอายอดีต",
        "image": "https://images.unsplash.com/photo-1563492065599-3520f775eeed?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 4,
        "name": "Lumphini Park Boundary",
        "category": "Green Oasis & Skyline",
        "lat": 13.73137815125521,
        "lng": 100.54118940701468,
        "desc": "ปอดของกรุงเทพฯ จุดเชื่อมต่อระหว่างธรรมชาติและเส้นเงาตึกสูง Silhouette สไตล์ Cinematic ยามเย็น",
        "image": "https://images.unsplash.com/photo-1596422846543-75c6fc197f07?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 5,
        "name": "Chao Phraya Riverside (Charoen Nakhon)",
        "category": "Riverfront Experience",
        "lat": 13.725947992586361,
        "lng": 100.50994068677123,
        "desc": "ฝั่งธนบุรีริมแม่น้ำเจ้าพระยา สัมผัสวิถีชีวิตริมน้ำ สายลม และมุมมองทัศนียภาพฝั่งพระนครที่งดงาม",
        "image": "https://images.unsplash.com/photo-1543083477-4f785aeafaa9?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 6,
        "name": "Bang Rak & Charoen Krung Art District",
        "category": "Creative & Heritage Design",
        "lat": 13.726535192705953,
        "lng": 100.51105488397464,
        "desc": "ถนนเจริญกรุง ย่านสร้างสรรค์แห่งแรกของไทย เต็มไปด้วยร้านกาแฟสุดเก๋ คาเฟ่ มิวเซียม และ street art ระดับโลก",
        "image": "https://images.unsplash.com/photo-1513415564515-763d91423bdd?auto=format&fit=crop&w=800&q=80"
    }
]

@app.route('/')
def index():
    avg_lat = sum(loc['lat'] for loc in LOCATIONS) / len(LOCATIONS)
    avg_lng = sum(loc['lng'] for loc in LOCATIONS) / len(LOCATIONS)
    
    m = folium.Map(
        location=[avg_lat, avg_lng],
        zoom_start=13,
        tiles='https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png',
        attr='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors &copy; <a href="https://carto.com/attributions">CARTO</a>',
        control_scale=True
    )

    route_coords = []

    for loc in LOCATIONS:
        coords = [loc['lat'], loc['lng']]
        route_coords.append(coords)
        
        popup_html = (
            f"<div style=\"font-family: sans-serif; color: #111; padding: 4px;\">"
            f"<p style=\"font-size: 11px; text-transform: uppercase; color: #666; margin: 0 0 2px 0;\">STOP {loc['id']}</p>"
            f"<h4 style=\"margin: 0 0 6px 0; font-size: 14px; font-weight: 600;\">{loc['name']}</h4>"
            f"<a href=\"https://www.google.com/maps/dir/?api=1&destination={loc['lat']},{loc['lng']}\" "
            f"target=\"_blank\" style=\"display: inline-block; background: #000; color: #fff; padding: 4px 8px; text-decoration: none; font-size: 11px; border-radius: 4px;\">"
            f"Google Maps ➔</a></div>"
        )
        
        folium.CircleMarker(
            location=coords,
            radius=7,
            color="#E5E7EB",
            fill=True,
            fill_color="#111827",
            fill_opacity=1,
            popup=folium.Popup(popup_html, max_width=220)
        ).add_to(m)

    folium.PolyLine(
        route_coords,
        color="#9CA3AF",
        weight=2,
        opacity=0.6,
        dash_array='5, 10'
    ).add_to(m)

    origin = f"{LOCATIONS[0]['lat']},{LOCATIONS[0]['lng']}"
    destination = f"{LOCATIONS[-1]['lat']},{LOCATIONS[-1]['lng']}"
    waypoints = "|".join([f"{loc['lat']},{loc['lng']}" for loc in LOCATIONS[1:-1]])
    full_route_url = f"https://www.google.com/maps/dir/?api=1&origin={origin}&destination={destination}&waypoints={waypoints}&travelmode=driving"

    map_html = m._repr_html_()

    return render_template('index.html', locations=LOCATIONS, map_html=map_html, full_route_url=full_route_url)

if __name__ == '__main__':
    app.run(debug=True)