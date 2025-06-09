import streamlit as st

def main():
    # 페이지 설정: 제목과 아이콘을 설정합니다.
    st.set_page_config(page_title="MBTI 맞춤 여행지 추천 서비스", page_icon="✈️")

    # 앱의 메인 제목과 설명입니다.
    st.title("💖 MBTI 맞춤 여행지 추천 서비스 🗺️✨")
    st.markdown("당신의 MBTI 유형에 딱 맞는 완벽한 여행지를 찾아보세요! 👇")

    # MBTI 유형 목록을 정의합니다.
    mbti_types = [
        "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
        "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"
    ]

    # 모든 여행지 정보를 한 곳에 모아 정의합니다.
    # 이렇게 하면 각 MBTI 유형별 추천에서 여행지 정보가 중복되지 않아 코드가 효율적입니다.
    all_destinations = {
        "로마": {
            "name": "로마, 이탈리아 🏛️",
            "description": "고대 로마 유적지와 박물관이 풍부하여 역사적 사실과 정보를 체계적으로 탐험하기 좋습니다. 잘 짜여진 가이드 투어와 편리한 대중교통으로 효율적인 여행이 가능합니다.",
            "relevance": "ISTJ는 역사적 의미와 체계적인 지식 습득을 중요시합니다. 로마는 방대한 역사와 건축물을 통해 그들의 지적 호기심을 충족시키고, 효율적인 여행 계획에 따라 움직이는 것을 선호하는 ISTJ에게 만족감을 줄 것입니다.",
            "image_url": "https://images.unsplash.com/photo-1552832230-c0197cebb15b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=s3h0p-F20u4" # 로마 여행 브이로그
        },
        "도쿄": {
            "name": "도쿄, 일본 🇯🇵",
            "description": "정확한 교통 시스템과 깔끔한 도시 환경, 그리고 풍부한 박물관과 전통 문화 시설이 있습니다. 계획대로 움직이기 좋은 도시입니다.",
            "relevance": "ISTJ는 규칙과 질서를 중요하게 생각하며, 잘 정돈된 환경에서 편안함을 느낍니다. 도쿄의 효율적인 시스템과 신뢰할 수 있는 서비스는 ISTJ의 실용적이고 안정적인 여행 선호를 충족시킬 것입니다.",
            "image_url": "https://images.unsplash.com/photo-1540302830-466c429712a2?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=x_u0g5uW2vI" # 도쿄 브이로그
        },
        "바르셀로나": {
            "name": "스페인 바르셀로나 🇪🇸",
            "description": "가우디 건축물과 활기찬 시장, 밤문화가 어우러진 도시.",
            "image_url": "https://images.unsplash.com/photo-1539037116277-fd91d0c92985?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=FjI1K7d61tI" # 바르셀로나 브이로그
        },
        "베를린": {
            "name": "독일 베를린 🇩🇪",
            "description": "풍부한 역사 유적과 현대적인 도시의 조화가 돋보이는 곳.",
            "image_url": "https://images.unsplash.com/photo-1528164344705-477894340d85?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=i9l1t-fN4t8" # 베를린 브이로그
        },
        "하와이": {
            "name": "하와이, 미국 🌺",
            "description": "아름다운 자연 속에서 휴식을 취하고, 가족이나 연인과 편안하게 시간을 보낼 수 있는 리조트 여행에 적합합니다. 안전하고 친근한 분위기를 자랑합니다.",
            "relevance": "ISFJ는 사랑하는 사람들과의 편안하고 조화로운 경험을 중요하게 생각합니다. 하와이의 평화로운 분위기와 잘 갖춰진 숙박 시설은 ISFJ가 심리적으로 안정감을 느끼고, 타인을 돌보며 휴식하는 데 집중할 수 있도록 돕습니다.",
            "image_url": "https://images.unsplash.com/photo-1507525428034-b723cf961321?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=5Vj-y-r4w6w" # 하와이 브이로그
        },
        "할슈타트": {
            "name": "오스트리아 할슈타트 🇦🇹",
            "description": "그림 같은 호수 마을로, 아름다운 풍경과 아기자기한 상점들이 매력적입니다.",
            "image_url": "https://images.unsplash.com/photo-1601053457199-63e5b3c5e8c4?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=zJg5l1y-y6Q" # 할슈타트 브이로그
        },
        "밴쿠버": {
            "name": "캐나다 밴쿠버 🇨🇦",
            "description": "도시와 자연이 조화롭게 어우러진 곳으로, 안정적이고 안전한 환경을 제공합니다.",
            "image_url": "https://images.unsplash.com/photo-1500382017464-9669527f3944?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=vVj4x73K38M" # 밴쿠버 브이로그
        },
        "교토": {
            "name": "교토, 일본 ⛩️",
            "description": "오랜 역사와 전통이 살아 숨 쉬는 곳으로, 사찰과 정원을 통해 내면의 평화와 성찰의 시간을 가질 수 있습니다. 조용한 분위기에서 깊이 있는 문화 체험을 할 수 있습니다.",
            "relevance": "INFJ는 영적인 성장과 깊이 있는 의미를 추구합니다. 교토의 고즈넉한 사찰과 정원은 INFJ에게 명상과 성찰의 기회를 제공하며, 일본의 전통 문화에 깊이 몰입하여 새로운 통찰을 얻을 수 있도록 돕습니다.",
            "image_url": "https://images.unsplash.com/photo-1524386411545-0d0571f30739?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=4CjYp2D0164" # 교토 브이로그
        },
        "피렌체": {
            "name": "이탈리아 피렌체 🇮🇹",
            "description": "르네상스 예술과 문화의 중심지로, 아름다운 건축물과 예술 작품이 가득합니다.",
            "image_url": "https://images.unsplash.com/photo-1558231718-d703e3a4794e?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=hB9i2d0gYgM" # 피렌체 브이로그
        },
        "아테네": {
            "name": "그리스 아테네 🇬🇷",
            "description": "고대 철학과 민주주의의 발상지로, 유적과 박물관이 많습니다.",
            "image_url": "https://images.unsplash.com/photo-1533105079780-fd91d0c92985?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=UqN6yq_mXG8" # 아테네 브이로그
        },
        "아이슬란드": {
            "name": "아이슬란드 🇮🇸",
            "description": "독특하고 신비로운 자연경관과 지질학적 특성을 가진 곳으로, 일반적인 관광지보다는 탐험과 사색에 적합합니다. 효율적인 이동 계획이 중요합니다.",
            "relevance": "INTJ는 미지의 것을 탐구하고 독창적인 경험을 추구합니다. 아이슬란드의 예측 불가능한 자연과 지질학적 경이로움은 INTJ의 지적 호기심을 자극하고, 혼자만의 시간을 가지며 깊이 생각할 수 있는 환경을 제공합니다.",
            "image_url": "https://images.unsplash.com/photo-1549448981-d0b8e7225143?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=D-h5S4B3A8w" # 아이슬란드 브이로그
        },
        "나오시마": {
            "name": "일본 나오시마 🇯🇵",
            "description": "예술과 자연이 조화된 '예술의 섬'으로, 독특한 건축물과 현대 미술 작품이 많습니다.",
            "image_url": "https://images.unsplash.com/photo-1582046522851-f7e912f2c81b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=oE1x5U2z0I0" # 나오시마 브이로그
        },
        "뉴질랜드 남섬": {
            "name": "뉴질랜드 남섬 🏞️",
            "description": "다양한 액티비티(번지점프, 래프팅, 하이킹 등)와 웅장한 자연경관을 즐길 수 있는 곳입니다. 도전적인 경험과 실용적인 문제 해결이 필요한 여행에 적합합니다.",
            "relevance": "ISTP는 직접적인 경험과 즉각적인 문제 해결을 선호합니다. 뉴질랜드 남섬은 그들의 모험심을 자극하고, 다양한 아웃도어 활동을 통해 실제적인 기술을 사용하고 상황에 대처하는 능력을 발휘할 수 있는 기회를 제공합니다.",
            "image_url": "https://images.unsplash.com/photo-1627918519445-6a58334812a6?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=vVj4x73K38M" # 뉴질랜드 남섬 브이로그
        },
        "방콕": {
            "name": "태국 방콕 🇹🇭",
            "description": "활기찬 시장과 독특한 문화, 다양한 길거리 음식이 있는 도시.",
            "image_url": "https://images.unsplash.com/photo-1549448981-d0b8e7225143?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=hB9i2d0gYgM" # 방콕 브이로그
        },
        "이비자": {
            "name": "스페인 이비자 🎶",
            "description": "세계적인 파티 아일랜드로, 활기찬 클럽 문화와 아름다운 해변이 있습니다.",
            "image_url": "https://images.unsplash.com/photo-1506781708899-7f41f0f4e3c3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=P2_XQz12m6M" # 이비자 브이로그
        },
        "파리": {
            "name": "파리, 프랑스 🇫🇷",
            "description": "세계적인 미술관과 아름다운 건축물, 낭만적인 분위기가 가득한 예술의 도시입니다. 자유롭게 거닐며 영감을 얻고, 감각적인 경험을 즐기기에 좋습니다.",
            "relevance": "ISFP는 예술적인 감각이 뛰어나고 아름다움을 추구합니다. 파리의 예술적 분위기와 감각적인 요소들은 ISFP의 미적 감수성을 자극하고, 자유로운 분위기 속에서 자신만의 영감을 찾을 수 있도록 돕습니다.",
            "image_url": "https://images.unsplash.com/photo-1502602898669-ee2877a165b4?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=p2N0wLz0_00" # 파리 브이로그
        },
        "세비야": {
            "name": "스페인 세비야 💃",
            "description": "정열적인 플라멩코와 아름다운 알카사르 궁전이 있는 곳.",
            "image_url": "https://images.unsplash.com/photo-1594950346857-4560d6e6a17b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=wz-E-7k1t0Q" # 세비야 브이로그
        },
        "제주도": {
            "name": "제주도, 대한민국 🍊",
            "description": "아름다운 자연 경관과 독특한 문화가 어우러진 섬.",
            "image_url": "https://images.unsplash.com/photo-1582046522851-f7e912f2c81b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=q6A22M6M21I" # 제주도 브이로그
        },
        "아일랜드": {
            "name": "아일랜드 ☘️",
            "description": "아름다운 자연과 신화적인 이야기가 가득한 곳으로, 영감을 얻고 감성적인 경험을 하기에 좋습니다. 조용한 시골 마을과 따뜻한 펍 문화도 매력적입니다.",
            "relevance": "INFP는 감수성이 풍부하고 영감을 추구합니다. 아일랜드의 신비로운 분위기와 풍부한 문화는 INFP의 상상력을 자극하고, 감성적인 경험을 통해 자신만의 이야기를 만들어갈 수 있도록 돕습니다. 따뜻한 현지인들과의 교류도 INFP에게 소중한 경험이 될 것입니다.",
            "image_url": "https://images.unsplash.com/photo-1548325983-a75d5e5b327b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=Q2_XQz12m6M" # 아일랜드 브이로그
        },
        "리스본": {
            "name": "포르투갈 리스본 🇵🇹",
            "description": "아름다운 풍경과 역사적인 매력, 그리고 따뜻한 사람들이 있는 도시.",
            "image_url": "https://images.unsplash.com/photo-1588667635905-2b09a06f365d?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=hE_Vv-oY8lI" # 리스본 브이로그
        },
        "바라나시": {
            "name": "인도 바라나시 🇮🇳",
            "description": "삶과 죽음이 공존하는 신비로운 도시로, 강가에서 영적인 경험을 할 수 있습니다.",
            "image_url": "https://images.unsplash.com/photo-1601053457199-63e5b3c5e8c4?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=e_x-dJ4vM6A" # 바라나시 브이로그
        },
        "제네바": {
            "name": "스위스 제네바 🇨🇭",
            "description": "CERN(유럽 입자 물리 연구소)과 같은 과학 연구 기관이 있는 도시로, 물리학과 우주의 비밀을 탐구하기 좋습니다. 조용하고 지적인 분위기를 선호합니다.",
            "relevance": "INTP는 지적인 호기심과 이론적인 탐구를 즐깁니다. 제네바는 세계적인 과학 연구의 중심지로, INTP가 복잡한 과학적 개념을 직접 보고 배우며, 그들의 지적 욕구를 충족시킬 수 있는 이상적인 장소입니다.",
            "image_url": "https://images.unsplash.com/photo-1576483584852-c0e4479e0a0a?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=i9a6gT8t81Q" # 제네바 브이로그
        },
        "암스테르담": {
            "name": "네덜란드 암스테르담 🇳🇱",
            "description": "자유롭고 혁신적인 분위기의 도시로, 과학 박물관, 예술 작품, 그리고 독특한 문화가 있습니다.",
            "image_url": "https://images.unsplash.com/photo-1506781708899-7f41f0f4e3c3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=b1X4wzNq8xQ" # 암스테르담 브이로그
        },
        "라스베이거스": {
            "name": "라스베이거스, 미국 🎲",
            "description": "다양한 엔터테인먼트, 화려한 쇼, 카지노 등 즉흥적이고 활동적인 경험을 즐길 수 있는 도시입니다. 역동적인 에너지가 넘칩니다.",
            "relevance": "ESTP는 스릴과 재미를 추구하며, 활동적이고 즉흥적인 경험을 좋아합니다. 라스베이거스는 그들의 에너지를 발산하고, 다양한 유흥과 활동을 통해 즉각적인 만족감을 얻을 수 있는 최적의 장소입니다.",
            "image_url": "https://images.unsplash.com/photo-1555562157-55c3286b2403?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=L2G5Z0Q0000" # 라스베이거스 브이로그
        },
        "두바이": {
            "name": "두바이, UAE 🇦🇪",
            "description": "세계 최고층 빌딩과 인공 섬 등 혁신적이고 웅장한 건축물이 많은 도시.",
            "image_url": "https://images.unsplash.com/photo-1582236173003-8877e6417736?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=m4y2F529L14" # 두바이 브이로그
        },
        "리우데자네이루": {
            "name": "리우데자네이루, 브라질 🇧🇷",
            "description": "활기찬 축제와 아름다운 해변, 그리고 열정적인 문화가 어우러진 도시입니다. 사람들과의 교류와 파티를 즐기기에 최적입니다.",
            "relevance": "ESFP는 사교적이고 낙천적이며, 활기찬 분위기에서 에너지를 얻습니다. 리우의 카니발과 해변 문화는 ESFP의 즐거움을 극대화하고, 사람들과의 자연스러운 교류를 통해 행복을 느낄 수 있도록 돕습니다.",
            "image_url": "https://images.unsplash.com/photo-1622080061985-05d548332152?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=3g8K1T8Y3tA" # 리우데자네이루 브이로그
        },
        "치앙마이": {
            "name": "태국 치앙마이 🇹🇭",
            "description": "자유로운 분위기와 풍부한 문화 체험, 그리고 현지인과의 교류가 용이한 도시입니다. 요가, 명상, 쿠킹 클래스 등 다양한 경험을 할 수 있습니다.",
            "relevance": "ENFP는 새로운 문화와 사람들과의 교류를 통해 영감을 얻습니다. 치앙마이는 그들의 호기심을 자극하고, 다양한 문화 체험과 현지인과의 소통을 통해 깊이 있는 경험을 할 수 있는 기회를 제공합니다.",
            "image_url": "https://images.unsplash.com/photo-1506781708899-7f41f0f4e3c3?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=J8lF7Q9F81s" # 치앙마이 브이로그
        },
        "발리": {
            "name": "인도네시아 발리 🧘‍♀️",
            "description": "아름다운 자연 속에서 요가, 명상, 예술 활동 등을 통해 영적인 성장과 창의적인 영감을 얻을 수 있는 곳입니다. 자유롭고 개방적인 분위기를 자랑합니다.",
            "relevance": "ENFP는 상상력이 풍부하고 새로운 아이디어에 개방적이며, 영적인 성장을 추구합니다. 발리는 그들의 영감을 자극하고, 자연 속에서 자신을 돌아보며, 새로운 사람들과의 교류를 통해 풍부한 경험을 할 수 있도록 돕습니다.",
            "image_url": "https://images.unsplash.com/photo-1582046522851-f7e912f2c81b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=a1_W_z0Q000" # 발리 브이로그
        },
        "앙코르와트": {
            "name": "캄보디아 시엠립 (앙코르와트) 🇰🇭",
            "description": "고대 유적 앙코르와트의 웅장함과 함께 현지 커뮤니티와의 교류를 통해 문화적 이해를 높일 수 있는 곳입니다. 봉사 활동이나 교육 프로그램에 참여할 수도 있습니다.",
            "relevance": "ENFJ는 타인의 성장에 관심을 가지고 긍정적인 영향을 주는 것을 좋아합니다. 앙코르와트의 역사적 의미와 함께 현지 문화를 체험하고, 도움이 필요한 커뮤니티에 기여하며, 자신의 비전을 공유할 수 있는 기회를 통해 깊이 있는 만족감을 얻을 것입니다.",
            "image_url": "https://images.unsplash.com/photo-1510255375000-0e121ac47c34?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=G2G5Z0Q0000" # 앙코르와트 브이로그
        },
        "뉴욕": {
            "name": "뉴욕, 미국 🗽",
            "description": "세계 경제와 문화의 중심지로, 다양한 비즈니스 기회와 문화 체험, 그리고 도전적인 경험을 할 수 있는 도시입니다. 효율적인 계획과 리더십 발휘에 적합합니다.",
            "relevance": "ENTJ는 목표 지향적이고 전략적인 사고를 하며, 도전적인 환경에서 에너지를 얻습니다. 뉴욕은 그들의 야망을 자극하고, 다양한 분야에서 새로운 기회를 탐색하며, 효율적인 계획을 통해 많은 것을 성취할 수 있는 장소입니다.",
            "image_url": "https://images.unsplash.com/photo-1549448981-d0b8e7225143?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=H2G5Z0Q0000" # 뉴욕 브이로그
        },
        "싱가포르": {
            "name": "싱가포르 �🇬",
            "description": "깨끗하고 안전하며, 효율적인 대중교통 시스템과 잘 정돈된 관광 인프라를 자랑하는 도시입니다. 계획대로 움직이기에 최적의 장소입니다.",
            "relevance": "ESTJ는 효율성과 질서를 중요하게 생각하며, 잘 정돈된 환경에서 편안함을 느낍니다. 싱가포르는 그들의 계획적인 여행 스타일을 만족시키고, 안전하고 예측 가능한 환경에서 효율적으로 관광할 수 있도록 돕습니다.",
            "image_url": "https://images.unsplash.com/photo-1582236173003-8877e6417736?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "video_url": "https://www.youtube.com/watch?v=zJg5l1y-y6Q" # 싱가포르 브이로그
        }
    }

    # 각 MBTI 유형에 대한 자세한 설명과 여행지 추천 데이터를 딕셔너리 형태로 저장합니다.
    # 이제 'destinations'와 'good_combinations' 내부에서는 all_destinations의 키(여행지 이름)를 참조합니다.
    mbti_travel_recommendations_full = {
        "ISTJ": {
            "summary": "현실적이고 사실을 중요시하며, 책임감이 강하고 신중한 유형입니다. 잘 계획된 일정과 실용적인 정보를 바탕으로 안정적이고 효율적인 여행을 선호합니다. 역사와 문화, 교육적인 경험에 흥미를 느낍니다.",
            "destinations": ["로마"], # 로마만 추천
            "good_combinations": [
                {"type": "ENFP", "reason": "ENFP의 즉흥적인 매력과 새로운 시도가 ISTJ의 계획적인 여행에 활력을 불어넣어 예측치 못한 즐거움을 발견하게 할 수 있습니다.",
                 "combination_recommendations": ["바르셀로나"]}, # 바르셀로나만 추천
                {"type": "ESTJ", "reason": "비슷하게 현실 지향적이고 체계적인 사고를 가진 유형으로, 효율적이고 빈틈없는 여행 계획을 함께 세우는 데 최적입니다.",
                 "combination_recommendations": ["베를린"]} # 베를린만 추천
            ]
        },
        "ISFJ": {
            "summary": "차분하고 성실하며, 타인을 배려하고 헌신적인 유형입니다. 편안하고 안전한 환경에서 사랑하는 사람들과 함께하는 여행을 선호합니다. 정감 있는 문화나 지역 커뮤니티에 관심을 가집니다.",
            "destinations": ["하와이"],
            "good_combinations": [
                {"type": "ESFP", "reason": "ESFP의 밝고 긍정적인 에너지가 ISFJ에게 편안함을 주고, 여행을 더욱 즐겁게 만들어줍니다.",
                 "combination_recommendations": ["할슈타트"]},
                {"type": "ISTJ", "reason": "비슷한 현실 지향적이고 안정적인 성향으로 여행에 대한 깊은 공감대를 형성할 수 있습니다.",
                 "combination_recommendations": ["밴쿠버"]}
            ]
        },
        "INFJ": {
            "summary": "통찰력이 뛰어나고 이상주의적이며, 의미와 가치를 추구하는 유형입니다. 단순히 관광하는 것을 넘어, 깊은 의미와 영적인 성장을 줄 수 있는 여행을 선호합니다. 문화적 몰입과 성찰의 시간을 중요하게 생각합니다.",
            "destinations": ["교토"],
            "good_combinations": [
                {"type": "ENFP", "reason": "INFJ와 ENFP는 감성적 유대감을 형성하며 여행지의 숨겨진 의미와 아름다움을 함께 탐구하고 감정을 공유합니다.",
                 "combination_recommendations": ["피렌체"]},
                {"type": "ENTP", "reason": "ENTP의 논리적인 분석과 INFJ의 통찰력이 만나 여행지에 대한 풍부하고 다각적인 대화를 이끌어낼 수 있습니다.",
                 "combination_recommendations": ["아테네"]}
            ]
        },
        "INTJ": {
            "summary": "전략적이고 분석적이며, 독립적이고 비판적인 사고를 가진 유형입니다. 효율적이고 계획적인 여행을 선호하며, 지적인 자극과 새로운 지식을 얻을 수 있는 독특한 목적지를 찾습니다. 혼자만의 시간을 가지며 깊이 탐구하는 것을 즐깁니다.",
            "destinations": ["아이슬란드"],
            "good_combinations": [
                {"type": "INTP", "reason": "INTJ와 INTP는 모두 논리적이고 분석적인 사고를 선호하여 여행지의 과학적, 철학적 의미에 대해 깊이 있는 토론을 할 수 있습니다.",
                 "combination_recommendations": ["나오시마"]},
                {"type": "ENFP", "reason": "ENFP의 창의적이고 감성적인 관점이 INTJ의 논리적 사고에 새로운 영감을 주어 여행을 더 다채롭게 이해할 수 있습니다.",
                 "combination_recommendations": ["뉴질랜드 남섬"]}
            ]
        },
        "ISTP": {
            "summary": "논리적이고 실용적이며, 호기심이 많고 문제 해결에 능한 유형입니다. 새로운 경험을 좋아하고, 위기 상황에서 침착하게 대응합니다. 손재주가 뛰어나고 기계나 도구를 다루는 것을 좋아합니다. 즉흥적이고 자유로운 여행을 선호합니다.",
            "destinations": ["뉴질랜드 남섬"],
            "good_combinations": [
                {"type": "ESFP", "reason": "ISTP의 논리적이고 실용적인 면모와 ESFP의 활동적이고 즉흥적인 면모가 결합하여 여행에 대한 흥미로운 관점과 즉각적인 반응을 공유할 수 있습니다.",
                 "combination_recommendations": ["방콕"]},
                {"type": "ENTP", "reason": "ENTP의 창의적인 아이디어와 ISTP의 문제 해결 능력이 시너지를 내어 여행지의 복잡한 설정이나 과학적 원리에 대해 깊이 있는 대화를 나눌 수 있습니다.",
                 "combination_recommendations": ["아이슬란드"]}
            ]
        },
        "ISFP": {
            "summary": "예술적 감각이 뛰어나고, 온화하며, 겸손하고 관대한 유형입니다. 현재를 즐기며, 자신만의 가치와 삶의 방식을 중요하게 생각합니다. 자유롭고 유연하며, 주변 환경에 대한 섬세한 감각을 가지고 있습니다. 아름다운 풍경과 문화 예술에 대한 감각적인 경험을 추구합니다.",
            "destinations": ["파리"],
            "good_combinations": [
                {"type": "ENFJ", "reason": "ENFJ의 따뜻하고 지지적인 성향이 ISFP의 감수성과 어우러져 여행 속에서 깊이 있는 감정을 나누고 서로에게 영감을 줄 수 있습니다.",
                 "combination_recommendations": ["세비야"]},
                {"type": "INFP", "reason": "ISFP와 INFP는 비슷한 감성적 깊이를 가지고 있어 여행이 전달하는 메시지나 감동을 함께 느끼고 나눌 수 있습니다.",
                 "combination_recommendations": ["제주도"]}
            ]
        },
        "INFP": {
            "summary": "이상주의적이고 창의적이며, 깊은 감수성과 공감 능력을 가진 유형입니다. 의미와 진정성을 중요하게 생각하며, 세상을 더 나은 곳으로 만들고자 합니다. 몽상적이고 영감을 추구하며, 개인의 가치를 소중히 여깁니다. 혼자만의 사색과 영감의 시간을 중요하게 생각합니다.",
            "destinations": ["아일랜드"],
            "good_combinations": [
                {"type": "ENFP", "reason": "INFP와 ENFP는 모두 이상주의적이고 감수성이 풍부하여 여행지의 숨겨진 의미나 감성적인 부분에 대해 깊이 있는 대화를 나눌 수 있습니다.",
                 "combination_recommendations": ["리스본"]},
                {"type": "INFJ", "reason": "INFJ의 통찰력과 INFP의 이상주의가 만나 여행지의 철학적 메시지에 대해 심도 깊은 논의를 할 수 있습니다.",
                 "combination_recommendations": ["바라나시"]}
            ]
        },
        "INTP": {
            "summary": "논리적이고 분석적이며, 호기심이 많고 이론적인 유형입니다. 복잡한 아이디어를 탐구하고, 지적인 자극을 추구하는 것을 좋아합니다. 독창적이고 독립적인 사고를 하며, 문제 해결에 있어 창의적인 방법을 모색합니다. 사람이 많지 않은 곳에서 조용히 탐구하는 것을 선호합니다.",
            "destinations": ["제네바"],
            "good_combinations": [
                {"type": "INTJ", "reason": "INTP와 INTJ는 모두 논리적이고 분석적인 사고를 선호하여 여행지의 과학적, 철학적 의미에 대해 깊이 있는 토론을 할 수 있습니다.",
                 "combination_recommendations": ["나오시마"]},
                {"type": "ENTP", "reason": "비슷한 지적 호기심과 논리적 탐구심을 공유하여 여행지의 복잡한 주제에 대해 흥미로운 대화를 나눌 수 있습니다.",
                 "combination_recommendations": ["암스테르담"]}
            ]
        },
        "ESTP": {
            "summary": "현실적이고 활동적이며, 개방적이고 적응력이 뛰어난 유형입니다. 새로운 경험을 좋아하고, 위기 상황에서 침착하게 대응합니다. 에너지가 넘치고 즉흥적이며, 뛰어난 관찰력으로 현실을 파악합니다. 스릴과 재미를 추구하며, 활동적인 여행을 선호합니다.",
            "destinations": ["라스베이거스"],
            "good_combinations": [
                {"type": "ESFP", "reason": "ESTP의 현실적인 관점과 ESFP의 예술적인 감각이 만나 영화를 다양한 시각에서 즐길 수 있습니다.",
                 "combination_recommendations": ["이비자"]},
                {"type": "ENTJ", "reason": "ENTJ의 전략적인 사고와 ESTP의 실행력이 결합하여 여행의 주제나 전개에 대해 활발하고 생산적인 대화를 나눌 수 있습니다.",
                 "combination_recommendations": ["두바이"]}
            ]
        },
        "ESFP": {
            "summary": "사교적이고 낙천적이며, 현재를 즐기고 사람들과의 관계를 중요시하는 유형입니다. 활기차고 긍정적인 에너지를 발산하며, 주변 사람들에게 즐거움을 주는 것을 좋아합니다. 즉흥적이고 개방적입니다. 사람들과의 교류와 즐거운 경험을 최우선으로 생각합니다.",
            "destinations": ["리우데자네이루"],
            "good_combinations": [
                {"type": "ISFJ", "reason": "ESFP의 밝은 에너지와 ISFJ의 차분하고 배려심 깊은 성향이 어우러져 편안하고 즐거운 영화 감상 분위기를 만듭니다.",
                 "combination_recommendations": ["할슈타트"]},
                {"type": "ENFP", "reason": "ESFP와 ENFP는 비슷한 낙천적이고 사교적인 성향으로 영화에 대한 활발한 감정 공유와 재미있는 대화를 나눌 수 있습니다.",
                 "combination_recommendations": ["방콕"]}
            ]
        },
        "ENFP": {
            "summary": "열정적이고 창의적이며, 상상력이 풍부하고 새로운 아이디어를 추구하는 유형입니다. 사람들과의 교류를 통해 영감을 얻고 긍정적인 영향을 줍니다. 호기심이 많고 개방적이며, 다양한 가능성을 탐색합니다. 의미 있는 경험과 사람들과의 깊은 연결을 중시합니다.",
            "destinations": ["치앙마이"],
            "good_combinations": [
                {"type": "INFJ", "reason": "ENFP의 열정적인 아이디어와 INFJ의 통찰력이 만나 여행지의 깊은 의미와 숨겨진 메시지에 대해 풍부한 대화를 나눌 수 있습니다.",
                 "combination_recommendations": ["피렌체"]},
                {"type": "INTJ", "reason": "INTJ의 논리적이고 분석적인 관점에 ENFP의 창의적인 사고가 더해져 여행지를 다각도로 해석하고 새로운 관점을 공유할 수 있습니다.",
                 "combination_recommendations": ["뉴질랜드 남섬"]}
            ]
        },
        "ENTP": {
            "summary": "논리적이고 창의적이며, 새로운 아이디어를 탐구하고 토론을 즐기는 유형입니다. 도전적이고, 틀에 얽매이지 않는 사고방식을 가지고 있습니다. 뛰어난 통찰력과 비판적 사고로 문제를 다각도로 분석합니다. 예상치 못한 상황과 지적인 도전을 즐깁니다.",
            "destinations": ["베를린"],
            "good_combinations": [
                {"type": "INTP", "reason": "ENTP와 INTP는 모두 지적인 호기심과 논리적 탐구심이 강하여 여행지의 복잡한 주제나 과학적 원리에 대해 심도 깊은 대화를 나눌 수 있습니다.",
                 "combination_recommendations": ["암스테르담"]},
                {"type": "INFJ", "reason": "INFJ의 통찰력과 ENTP의 논리적 분석이 만나 여행지의 숨겨진 의미와 철학적 메시지에 대해 풍부하고 깊이 있는 논의를 이끌어낼 수 있습니다.",
                 "combination_recommendations": ["아테네"]}
            ]
        },
        "ESTJ": {
            "summary": "현실적이고 실용적이며, 체계적이고 리더십이 강한 유형입니다. 조직을 잘 이끌고, 목표 달성을 위해 효율적으로 움직입니다. 책임감이 강하고 결단력이 있으며, 규칙과 질서를 중요하게 생각합니다. 잘 계획된 효율적인 여행을 선호합니다.",
            "destinations": ["싱가포르"],
            "good_combinations": [
                {"type": "ISTJ", "reason": "ESTJ와 ISTJ는 모두 현실적이고 체계적인 사고를 선호하여 여행의 사실적 배경이나 논리적 전개에 대해 깊은 공감대를 형성하며 감상할 수 있습니다.",
                 "combination_recommendations": ["베를린"]},
                {"type": "ENTJ", "reason": "ENTJ의 전략적인 사고와 ESTP의 실행력이 결합하여 여행의 주제나 전개에 대해 활발하고 생산적인 대화를 나눌 수 있습니다.",
                 "combination_recommendations": ["두바이"]}
            ]
        },
        "ESFJ": {
            "summary": "사교적이고 친절하며, 타인을 배려하고 협력적인 유형입니다. 주변 사람들과의 조화를 중요하게 생각하며, 봉사 정신이 강합니다. 따뜻하고 배려심이 깊으며, 다른 사람의 감정에 공감하고 지원하는 것을 좋아합니다. 사람들과 함께하는 편안하고 즐거운 여행을 선호합니다.",
            "destinations": ["바르셀로나"],
            "good_combinations": [
                {"type": "ISFJ", "reason": "ESFJ와 ISFJ는 모두 사람들과의 조화를 중요하게 생각하고 따뜻한 마음을 가지고 있어, 여행지에서 감동적인 스토리에 깊이 공감하며 함께 즐거운 시간을 보낼 수 있습니다.",
                 "combination_recommendations": ["피렌체"]},
                {"type": "ENFJ", "reason": "ENFJ의 리더십과 ESFJ의 협력적인 태도가 만나 여행에 대한 감상평을 활발하게 나누고 서로에게 긍정적인 영향을 줄 수 있습니다.",
                 "combination_recommendations": ["하와이"]}
            ]
        },
        "ENFJ": {
            "summary": "사교적이고 설득력 있으며, 타인의 성장에 관심을 가지고 리더십을 발휘하는 유형입니다. 사람들에게 영감을 주고, 긍정적인 변화를 이끌어내는 것을 좋아합니다. 따뜻하고 책임감이 강하며, 비전을 공유하는 데 능숙합니다. 의미 있는 경험과 사회적 교류를 통해 여행의 가치를 찾습니다.",
            "destinations": ["앙코르와트"],
            "good_combinations": [
                {"type": "INFP", "reason": "ENFJ의 따뜻하고 지지적인 성향과 INFP의 감성적인 깊이가 만나 여행지에서 감정을 풍부하게 공유하고 서로에게 긍정적인 영향을 줄 수 있습니다.",
                 "combination_recommendations": ["발리"]},
                {"type": "ESFJ", "reason": "비슷하게 사교적이고 협력적인 성향으로 여행 감상 후 활발한 대화를 나누며 즐거움을 배가시킬 수 있습니다.",
                 "combination_recommendations": ["피렌체"]}
            ]
        },
        "ENTJ": {
            "summary": "논리적이고 단호하며, 리더십이 강하고 전략적인 유형입니다. 목표 지향적이고 효율성을 중시하며, 문제를 해결하고 조직을 이끄는 데 능숙합니다. 비전을 제시하고, 이를 현실로 만들기 위해 강력하게 추진합니다. 도전적이고 성취감을 주는 여행을 선호합니다.",
            "destinations": ["뉴욕"],
            "good_combinations": [
                {"type": "INTP", "reason": "ENTJ의 리더십과 INTP의 깊은 분석력이 결합하여 여행지의 복잡한 주제나 숨겨진 의미에 대해 심도 있는 토론을 할 수 있습니다.",
                 "combination_recommendations": ["제네바"]},
                {"type": "ESTJ", "reason": "비슷하게 목표 지향적이고 효율성을 중시하는 성향으로 여행의 전개나 전략적 요소에 대해 깊이 공감하며 활발한 대화를 나눌 수 있습니다.",
                 "combination_recommendations": ["싱가포르"]}
            ]
        }
    }

    # 사용자로부터 MBTI 유형을 입력받는 드롭다운 메뉴를 생성합니다.
    selected_mbti = st.selectbox(
        "당신의 MBTI 유형을 선택해주세요! 🎈", # 드롭다운 메뉴의 레이블
        [""] + mbti_types, # 빈 문자열을 추가하여 초기 선택 없음을 나타냅니다.
        index=0, # 초기 선택 인덱스
        help="나에게 딱 맞는 여행지를 추천해 드릴게요! ✨" # 사용자에게 도움말을 제공합니다.
    )

    # MBTI 유형이 선택되었을 때만 추천을 표시합니다.
    if selected_mbti:
        st.write(f"---") # 구분선
        st.subheader(f"✨ {selected_mbti} 유형을 위한 맞춤 추천 🗺️")

        # 선택된 MBTI 유형에 대한 정보 가져오기
        mbti_info = mbti_travel_recommendations_full.get(selected_mbti, {})

        if mbti_info:
            # MBTI 유형 요약 설명
            st.markdown(f"### {selected_mbti} 유형은... 💡")
            st.info(mbti_info["summary"])
            st.markdown("---")

            # 추천 여행지 목록 표시
            st.markdown("### 추천 여행지와 그 이유 🌍")
            
            # 각 여행지를 표시 (하나만 추천하므로 컬럼 나눌 필요 없음)
            for dest_key in mbti_info["destinations"]:
                dest = all_destinations[dest_key] # all_destinations에서 실제 여행지 정보 가져오기
                st.write(f"##### {dest['name']}") # 여행지 이름
                
                # 이미지 표시 (링크 없이, use_container_width 사용)
                st.image(dest['image_url'], 
                         caption=f"{dest['name']} 여행 사진", 
                         use_container_width=True) # use_column_width 대신 use_container_width 사용
                
                st.markdown(f"**설명:** {dest['description']}") # 여행지 설명
                st.success(f"**이 유형에 추천하는 이유:** {dest['relevance']}") # 여행지 관련성
                
                # 리뷰 영상 링크만 표시
                st.markdown(f"[🎥 **'{dest['name']}' 브이로그/리뷰 영상 보기**]({dest['video_url']})")
                st.markdown("<hr style='border:1px solid #f0f2f6'>", unsafe_allow_html=True) # 가벼운 구분선

            # 함께 여행 보기에 좋은 MBTI 조합 추천
            if "good_combinations" in mbti_info and mbti_info["good_combinations"]:
                st.markdown("---")
                st.subheader(f"🤝 {selected_mbti} 유형과 함께 여행하기 좋은 MBTI 조합 🎒")
                st.markdown("이 유형들과 함께 여행하면 더욱 즐거운 경험을 할 수 있어요!")
                for combo in mbti_info["good_combinations"]:
                    st.write(f"**{combo['type']}**: {combo['reason']}")
                    if "combination_recommendations" in combo and combo["combination_recommendations"]:
                        st.markdown(f"**두 분께 추천하는 여행지:**")
                        
                        # 조합 추천 여행지도 하나씩만 표시
                        for combo_dest_key in combo["combination_recommendations"]:
                            combo_dest = all_destinations[combo_dest_key] # all_destinations에서 실제 여행지 정보 가져오기
                            st.write(f"###### {combo_dest['name']}")
                            
                            # 이미지 표시 (링크 없이, use_container_width 사용)
                            st.image(combo_dest['image_url'], 
                                     caption=f"{combo_dest['name']} 여행 사진", 
                                     width=200, # 여기는 작은 사이즈 유지를 위해 width 유지
                                     use_container_width=False) # 여기는 width 고정을 위해 False 유지
                            
                            st.write(f"{combo_dest['description']}")
                            st.markdown(f"[🎥 **'{combo_dest['name']}' 브이로그/리뷰 영상 보기**]({combo_dest['video_url']})")
                            st.markdown("<hr style='border:0.5px solid #f0f2f6'>", unsafe_allow_html=True) # 더 가벼운 구분선
                    st.markdown("---") # 각 조합 사이에 구분선
            else:
                st.info(f"{selected_mbti} 유형과 함께 여행하기 좋은 특정 MBTI 조합 정보가 아직 없습니다. 😅")

        else:
            # 추천 여행지가 없을 경우 경고 메시지를 표시합니다.
            st.warning("선택하신 MBTI 유형에 대한 추천 여행지가 아직 없습니다. 다른 유형을 선택해주세요! 😅")

    # 앱의 하단에 작은 메시지를 추가합니다.
    st.markdown("Made with ❤️ and Streamlit")

# Streamlit 앱을 실행하는 부분입니다.
if __name__ == "__main__":
    main()
