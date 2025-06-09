import streamlit as st

def main():
    # 페이지 설정: 제목과 아이콘을 설정합니다.
    st.set_page_config(page_title="MBTI 맞춤 영화 추천 서비스", page_icon="🎬")

    # 앱의 메인 제목과 설명입니다.
    st.title("💖 MBTI 맞춤 수학 & 과학 명작 영화 추천 서비스 🎥✨")
    st.markdown("당신의 MBTI 유형에 딱 맞는 인생 영화를 찾아보세요! 👇")

    # MBTI 유형 목록을 정의합니다.
    mbti_types = [
        "ISTJ", "ISFJ", "INFJ", "INTJ", "ISTP", "ISFP", "INFP", "INTP",
        "ESTP", "ESFP", "ENFP", "ENTP", "ESTJ", "ESFJ", "ENFJ", "ENTJ"
    ]

    # 각 MBTI 유형에 따른 영화 추천 데이터를 딕셔너리 형태로 저장합니다.
    # 각 영화는 제목과 설명을 포함합니다.
    movie_recommendations = {
        "ISTJ": [
            {"title": "A Beautiful Mind (2001) 🧠", "description": "천재 수학자의 삶과 그의 내면의 투쟁을 그린 영화. 논리적 사고와 문제 해결에 대한 흥미를 자극합니다."},
            {"title": "Apollo 13 (1995) 🚀", "description": "실제 사건을 바탕으로, 우주에서 발생한 위기를 해결하는 과정을 보여주는 영화. 현실적이고 체계적인 접근이 돋보입니다."}
        ],
        "ISFJ": [
            {"title": "Hidden Figures (2016) 👩‍🔬", "description": "NASA의 숨겨진 영웅들이 우주 경쟁을 승리로 이끈 감동적인 실화. 헌신과 성실함이 빛나는 이야기입니다."},
            {"title": "The Theory of Everything (2014) 💖", "description": "스티븐 호킹 박사의 삶과 사랑, 그리고 물리학에 대한 열정을 그린 영화. 따뜻한 감동과 깊은 통찰을 선사합니다."}
        ],
        "INFJ": [
            {"title": "Arrival (2016) 👽", "description": "외계 언어를 통해 인류의 운명을 바꾸는 과정을 그린 SF 영화. 통찰력과 이상주의적인 시각을 자극합니다."},
            {"title": "Contact (1997) 🔭", "description": "외계 문명과의 조우를 통해 과학과 신념의 갈등을 탐구하는 영화. 깊은 철학적 메시지를 담고 있습니다."}
        ],
        "INTJ": [
            {"title": "The Imitation Game (2014) 💻", "description": "암호 해독가 앨런 튜링의 삶과 그의 천재성을 그린 영화. 전략적이고 분석적인 사고를 요하는 명작입니다."},
            {"title": "Oppenheimer (2023) 💣", "description": "원자폭탄 개발을 주도한 과학자의 복잡한 내면과 윤리적 고민을 다룬 영화. 독립적이고 비판적인 시각을 가진 INTJ에게 추천합니다."}
        ],
        "ISTP": [
            {"title": "The Martian (2015) 🥔", "description": "화성에 홀로 남겨진 우주인이 과학적 지식으로 생존하는 이야기. 문제 해결 능력과 실용적인 접근이 돋보입니다."},
            {"title": "Source Code (2011) ⏱️", "description": "반복되는 시간 속에서 테러를 막으려는 주인공의 이야기를 다룬 SF 스릴러. 유연한 사고와 논리적인 추론이 필요합니다."}
        ],
        "ISFP": [
            {"title": "Good Will Hunting (1997) ✨", "description": "천재적인 재능을 가졌지만 방황하는 청년이 수학과 심리학을 통해 성장하는 영화. 예술적인 감각과 감수성을 자극합니다."},
            {"title": "Hidden Figures (2016) 👩‍🔬", "description": "NASA의 숨겨진 영웅들이 우주 경쟁을 승리로 이끈 감동적인 실화. 따뜻한 마음과 개방적인 사고를 가진 ISFP에게도 좋은 선택입니다."}
        ],
        "INFP": [
            {"title": "Contact (1997) 🔭", "description": "외계 문명과의 조우를 통해 과학과 신념의 갈등을 탐구하는 영화. 창의적이고 감수성 풍부한 INFP에게 깊은 영감을 줍니다."},
            {"title": "Good Will Hunting (1997) ✨", "description": "천재적인 재능을 가졌지만 방황하는 청년이 수학과 심리학을 통해 성장하는 영화. 이상주의적인 INFP에게 공감과 위로를 줄 수 있습니다."}
        ],
        "INTP": [
            {"title": "Primer (2004) 🧪", "description": "저예산으로 만든 복잡한 시간 여행 영화. 분석적이고 논리적인 사고를 가진 INTP의 탐구심을 자극합니다."},
            {"title": "Interstellar (2014) 🌌", "description": "우주와 시간의 신비를 탐구하는 SF 대작. 이론적이고 탐구적인 INTP에게 끝없는 질문을 던집니다."}
        ],
        "ESTP": [
            {"title": "The Martian (2015) 🥔", "description": "화성에 홀로 남겨진 우주인이 과학적 지식으로 생존하는 이야기. 현실적이고 활동적인 ESTP의 문제 해결 능력을 보여줍니다."},
            {"title": "Moneyball (2011) ⚾", "description": "통계를 이용해 야구팀을 혁신하는 실화. 실용적이고 논리적인 ESTP에게 흥미로운 관점을 제공합니다."}
        ],
        "ESFP": [
            {"title": "Hidden Figures (2016) 👩‍🔬", "description": "NASA의 숨겨진 영웅들이 우주 경쟁을 승리로 이끈 감동적인 실화. 사교적이고 낙천적인 ESFP에게 영감을 주는 이야기입니다."},
            {"title": "The Theory of Everything (2014) 💖", "description": "스티븐 호킹 박사의 삶과 사랑, 그리고 물리학에 대한 열정을 그린 영화. 인간적인 면모를 좋아하는 ESFP에게도 매력적입니다."}
        ],
        "ENFP": [
            {"title": "Contact (1997) 🔭", "description": "외계 문명과의 조우를 통해 과학과 신념의 갈등을 탐구하는 영화. 열정적이고 창의적인 ENFP에게 새로운 영감을 줍니다."},
            {"title": "Interstellar (2014) 🌌", "description": "우주와 시간의 신비를 탐구하는 SF 대작. 상상력이 풍부하고 영감을 추구하는 ENFP에게 깊은 울림을 선사합니다."}
        ],
        "ENTP": [
            {"title": "Primer (2004) 🧪", "description": "저예산으로 만든 복잡한 시간 여행 영화. 논리적이고 창의적인 ENTP의 도전을 자극합니다."},
            {"title": "Oppenheimer (2023) 💣", "description": "원자폭탄 개발을 주도한 과학자의 복잡한 내면과 윤리적 고민을 다룬 영화. 지적인 토론과 새로운 아이디어를 좋아하는 ENTP에게 흥미로운 주제입니다."}
        ],
        "ESTJ": [
            {"title": "Apollo 13 (1995) 🚀", "description": "실제 사건을 바탕으로, 우주에서 발생한 위기를 해결하는 과정을 보여주는 영화. 체계적이고 추진력 있는 ESTJ의 강점을 보여줍니다."},
            {"title": "Moneyball (2011) ⚾", "description": "통계를 이용해 야구팀을 혁신하는 실화. 현실적이고 효율적인 ESTJ에게 깊은 인상을 줄 수 있습니다."}
        ],
        "ESFJ": [
            {"title": "Hidden Figures (2016) 👩‍🔬", "description": "NASA의 숨겨진 영웅들이 우주 경쟁을 승리로 이끈 감동적인 실화. 협력적이고 헌신적인 ESFJ에게 큰 울림을 줍니다."},
            {"title": "The Theory of Everything (2014) 💖", "description": "스티븐 호킹 박사의 삶과 사랑, 그리고 물리학에 대한 열정을 그린 영화. 타인과의 관계를 중요시하는 ESFJ에게 감동적인 스토리입니다."}
        ],
        "ENFJ": [
            {"title": "Contact (1997) 🔭", "description": "외계 문명과의 조우를 통해 과학과 신념의 갈등을 탐구하는 영화. 사교적이고 설득력 있는 ENFJ에게 영감을 주고 리더십을 발휘하는 장면에서 공감할 수 있습니다."},
            {"title": "Hidden Figures (2016) 👩‍🔬", "description": "NASA의 숨겨진 영웅들이 우주 경쟁을 승리로 이끈 감동적인 실화. 타인을 이끌고 긍정적인 영향을 주는 ENFJ의 모습을 찾아볼 수 있습니다."}
        ],
        "ENTJ": [
            {"title": "Oppenheimer (2023) 💣", "description": "원자폭탄 개발을 주도한 과학자의 복잡한 내면과 윤리적 고민을 다룬 영화. 논리적이고 단호한 ENTJ의 리더십과 전략적 사고를 보여줍니다."},
            {"title": "The Imitation Game (2014) 💻", "description": "암호 해독가 앨런 튜링의 삶과 그의 천재성을 그린 영화. 목표 지향적이고 도전적인 ENTJ에게 흥미로운 이야기입니다."}
        ]
    }

    # 사용자로부터 MBTI 유형을 입력받는 드롭다운 메뉴를 생성합니다.
    selected_mbti = st.selectbox(
        "당신의 MBTI 유형을 선택해주세요! 🎈", # 드롭다운 메뉴의 레이블
        [""] + mbti_types, # 빈 문자열을 추가하여 초기 선택 없음을 나타냅니다.
        index=0, # 초기 선택 인덱스
        help="나에게 딱 맞는 영화를 추천해 드릴게요! ✨" # 사용자에게 도움말을 제공합니다.
    )

    # MBTI 유형이 선택되었을 때만 추천을 표시합니다.
    if selected_mbti:
        st.write(f"---") # 구분선
        st.subheader(f"✨ {selected_mbti} 유형을 위한 추천 영화 🍿")
        st.balloons() # 사용자가 선택하면 풍선 효과를 띄웁니다! 🥳

        # 선택된 MBTI 유형에 해당하는 영화 목록을 가져옵니다.
        recommendations = movie_recommendations.get(selected_mbti, [])

        # 추천 영화가 있을 경우 각 영화의 제목과 설명을 표시합니다.
        if recommendations:
            for movie in recommendations:
                st.write(f"### {movie['title']}") # 영화 제목
                st.info(movie['description']) # 영화 설명 (정보 박스로 표시)
                st.markdown("---") # 각 영화 사이에 구분선
        else:
            # 추천 영화가 없을 경우 경고 메시지를 표시합니다.
            st.warning("선택하신 MBTI 유형에 대한 추천 영화가 아직 없습니다. 다른 유형을 선택해주세요! 😅")

    # 앱의 하단에 작은 메시지를 추가합니다.
    st.markdown("Made with ❤️ and Streamlit")

# Streamlit 앱을 실행하는 부분입니다.
if __name__ == "__main__":
    main()
