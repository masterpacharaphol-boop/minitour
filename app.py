from flask import Flask, render_template
import folium

app = Flask(__name__)

locations = [
    {
        "id": 1,
        "name": "อุทยาน 100 ปี จุฬาลงกรณ์มหาวิทยาลัย",
        "lat": 13.739625848977973, 
        "lng": 100.5229228838029,
        "desc": "พื้นที่สีเขียวใจกลางเมืองหลวง สถาปัตยกรรมที่ผสานธรรมชาติและการออกแบบเพื่อความยั่งยืน เหมาะสำหรับการเดินเล่นรับแรงบันดาลใจ",
        "img": "https://images.unsplash.com/photo-1588651944883-7cb7217dbbf3?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 2,
        "name": "อนุสาวรีย์ชัยสมรภูมิ",
        "lat": 13.765309859250024, 
        "lng": 100.53595673991005,
        "desc": "ศูนย์กลางการคมนาคมและแลนด์มาร์คประวัติศาสตร์ที่คึกคักตลอด 24 ชั่วโมง จุดเชื่อมโยงวิถีชีวิตคนกรุงเทพฯ อย่างแท้จริง",
        "img": "https://images.unsplash.com/photo-1563492065599-3520f775eeed?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 3,
        "name": "หอพระสุราลัยพิมาน",
        "lat": 13.750202443613839, 
        "lng": 100.49276017120366,
        "desc": "สถาปัตยกรรมไทยอันวิจิตรตระการตา ซ่อนตัวอยู่ในความเงียบสงบ แหล่งเรียนรู้ศิลปะและวัฒนธรรมชั้นครู",
        "img": "https://images.unsplash.com/photo-1582468546235-9bf31e5bc4cb?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 4,
        "name": "สวนลุมพินี",
        "lat": 13.73137815125521, 
        "lng": 100.54118940701468,
        "desc": "ปอดขนาดใหญ่แห่งแรกของกรุงเทพฯ ดื่มด่ำกับแสงตะวันยามเย็นที่สะท้อนผิวน้ำ ท่ามกลางป่าคอนกรีตที่ล้อมรอบ",
        "img": "https://images.unsplash.com/photo-1508006728353-0c4c4786807e?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 5,
        "name": "ไอคอนสยาม",
        "lat": 13.725947992586361, 
        "lng": 100.50994068677123,
        "desc": "อภิมหาโครงการริมแม่น้ำเจ้าพระยา แหล่งรวมไลฟ์สไตล์ระดับโลกที่สะท้อนเอกลักษณ์ความงามของไทยสู้สายตาสากล",
        "img": "https://images.unsplash.com/photo-1627042571343-494d455476d0?auto=format&fit=crop&w=800&q=80"
    },
    {
        "id": 6,
        "name": "ไอคอนสยามพาร์ค",
        "lat": 13.726535192705953, 
        "lng": 100.51105488397464,
        "desc": "จุดชมทัศนียภาพริมแม่น้ำที่สวยที่สุด พร้อมชมแสงสีตระการตาในยามค่ำคืน เป็นจุดจบของวันทริปที่สมบูรณ์แบบ",
        "img": "https://images.unsplash.com/photo-1598501258169-25ea7a4c4b69?auto=format&fit=crop&w=800&q=80"
    }
]

@app.route('/')
def index():
    return render_template('index.html', locations=locations)

# Route สำหรับเรนเดอร์แผนที่ Folium โดยเฉพาะ
@app.route('/map')
def map_view():
    start_coords = [13.742, 100.52]
    tour_map = folium.Map(location=start_coords, zoom_start=13, tiles='OpenStreetMap')

    for loc in locations:
        folium.Marker(
            [loc['lat'], loc['lng']],
            popup=f"<b>{loc['name']}</b>",
            tooltip=loc['name'],
            icon=folium.Icon(color='red', icon='info-sign')
        ).add_to(tour_map)

    return tour_map._repr_html_()

if __name__ == '__main__':
    app.run(debug=True)
