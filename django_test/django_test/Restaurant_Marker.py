# 소프트웨어학과 2019029029 황근민
# 원하는 식당의 위치, 충북대학교의 위치를 위도, 경도 정보를 이용해 지도에 표시하여 html로 저장
import folium               # folium: 지도를 위한 모듈


class RestaurantMarker:

    def __init__(self):
        self.center = [36.629049, 127.456318]  # 충북대학교 솔못 좌표
        self.map = folium.Map(location=self.center, zoom_start=15)      # 충북대학교를 기준으로 지도데이터 생성

    # 원하는 식당을 지도에 표시
    def restaurant_marker(self, restaurant_name, latitude, longitude):  # 변수설정: 지도(self), 표시할 식당 이름, 위도, 경도
        folium.Marker(
            location=[latitude, longitude],  # 표시할 식당의 위도, 경도
            tooltip=restaurant_name,       # 표시할 식당의 식당 이름
        ).add_to(self.map)

    # 충북대학교의 위치를 지도에 표시
    def center_marker(self):
        folium.Marker(
            location=[36.629049, 127.456318],
            tooltip='충북대학교'
        ).add_to(self.map)

    # 충북대학교와 원하는 식당을 표시한 지도 html로 저장
    def save_html(self):
        self.map.save('./django_test/templates/restaurant_marked_map.html')


# 선언 및 사용 예시
Restaurant = RestaurantMarker()
Restaurant.restaurant_marker("삼미투가리백숙", 36.640393, 127.468736)
Restaurant.center_marker()
Restaurant.save_html()
