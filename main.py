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

    # 각 MBTI 유형에 대한 자세한 설명과 영화 추천 데이터를 딕셔너리 형태로 저장합니다.
    mbti_recommendations_full = {
        "ISTJ": {
            "summary": "현실적이고 사실을 중요시하며, 책임감이 강하고 신중한 유형입니다. 논리적이고 체계적인 접근을 선호하며, 약속을 잘 지킵니다. 전통을 존중하고 안정성을 추구하며, 세부사항에 주의를 기울입니다.",
            "movies": [
                {"title": "A Beautiful Mind (2001) 🧠",
                 "description": "천재 수학자 존 내쉬의 삶과 그의 내면의 투쟁을 그린 영화입니다.",
                 "relevance": "ISTJ는 논리적이고 체계적인 사고를 통해 문제를 해결하는 데 능숙합니다. 존 내쉬가 복잡한 수학 문제를 끈기 있게 파고들고, 자신의 내면적 혼란 속에서도 질서를 찾으려는 모습은 ISTJ의 분석적이고 신중한 특성과 잘 부합합니다. 사실에 기반한 접근과 인내심으로 목표를 달성하는 과정이 깊은 공감을 불러일으킬 것입니다."},
                {"title": "Apollo 13 (1995) 🚀",
                 "description": "실제 사건을 바탕으로, 우주에서 발생한 위기를 해결하는 과정을 보여주는 영화입니다.",
                 "relevance": "ISTJ는 위기 상황에서 침착하게 사실을 분석하고, 현실적이고 실용적인 해결책을 찾는 데 탁월합니다. 아폴로 13호 팀이 제한된 자원과 시간 속에서 체계적인 절차와 냉철한 판단으로 위기를 극복하는 과정은 ISTJ의 책임감과 실행 능력을 극대화하여 보여줍니다. 계획을 중시하고 세부사항을 꼼꼼히 살피는 ISTJ에게 특히 인상 깊을 영화입니다."},
                {"title": "The Martian (2015) �",
                 "description": "화성에 홀로 남겨진 우주인이 과학적 지식과 실용적인 기술로 생존하는 이야기입니다.",
                 "relevance": "ISTJ는 실제적인 문제 해결에 탁월하며, 주어진 자원 내에서 효율적인 방안을 모색하는 데 능합니다. 마크 와트니가 제한된 환경 속에서 논리적이고 실용적인 해결책을 찾아 생존하는 과정은 ISTJ의 현실적이고 끈기 있는 특성과 일치하여 큰 공감을 얻을 것입니다."}
            ],
            "good_combinations": [
                {"type": "ENFP", "reason": "ENFP의 통찰력과 상상력이 ISTJ의 현실적인 관점에 새로운 시야를 제공하여, 영화에 대한 깊이 있는 대화를 나눌 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "The Social Dilemma (2020) 📱", "description": "소셜 미디어의 어두운 면과 기술이 사회에 미치는 영향을 다룬 다큐멘터리."},
                     {"title": "Arrival (2016) 👽", "description": "외계 언어를 통해 인류의 운명을 바꾸는 과정을 그린 SF 영화."}
                 ]},
                {"type": "ESTJ", "reason": "비슷하게 현실 지향적이고 체계적인 사고를 가진 유형으로, 효율적이고 빈틈없는 여행 계획을 함께 세우는 데 최적입니다.",
                 "combination_movie_recommendations": [
                     {"title": "Contagion (2011) 🦠", "description": "치명적인 전염병의 확산과 이를 막기 위한 전 세계적인 노력을 그린 영화."},
                     {"title": "Deepwater Horizon (2016) 🛢️", "description": "멕시코만 원유 시추선 폭발 사고를 다룬 영화로, 재난 상황에서의 시스템과 대응을 보여줍니다."}
                 ]}
            ]
        },
        "ISFJ": {
            "summary": "차분하고 성실하며, 타인을 배려하고 헌신적인 유형입니다. 실제적인 도움을 주기를 좋아하며, 안정과 조화를 중요하게 생각합니다. 따뜻하고 배려심이 깊으며, 책임감이 강해 맡은 일을 꼼꼼히 처리합니다.",
            "movies": [
                {"title": "Hidden Figures (2016) 👩‍🔬",
                 "description": "NASA의 숨겨진 영웅들이 인종 차별과 성 차별을 극복하고 우주 경쟁을 승리로 이끈 감동적인 실화입니다.",
                 "relevance": "ISFJ는 타인을 돕고 공동체에 기여하는 것을 중요하게 생각하며, 헌신적인 태도로 자신의 역할을 충실히 수행합니다. 이 영화의 주인공들은 자신의 뛰어난 능력으로 동료와 국가를 돕기 위해 묵묵히 노력하며, ISFJ의 책임감과 희생적인 면모를 아름답게 보여줍니다. 따뜻한 마음으로 주변을 돌보는 ISFJ에게 큰 감동을 선사할 것입니다."},
                {"title": "The Theory of Everything (2014) 💖",
                 "description": "스티븐 호킹 박사의 삶과 사랑, 그리고 물리학에 대한 열정을 그린 영화입니다.",
                 "relevance": "ISFJ는 타인의 필요를 세심하게 살피고 헌신적으로 지원하는 데 강합니다. 영화 속 제인 호킹은 스티븐 호킹의 곁에서 그의 꿈을 지지하고, 어려운 상황 속에서도 꿋꿋하게 가족을 돌봅니다. 이러한 인내심과 따뜻한 배려는 ISFJ의 깊은 이타심과 사랑을 잘 드러내며, 관계의 소중함을 중요하게 생각하는 ISFJ에게 깊은 울림을 줄 것입니다."},
                {"title": "Gifted (2017) 👧",
                 "description": "천재적인 수학 재능을 가진 소녀와 그녀를 지키려는 삼촌의 감동적인 이야기입니다.",
                 "relevance": "ISFJ는 따뜻하고 보호 본능이 강하며, 약자를 돕는 것에 보람을 느낍니다. 이 영화는 어린 천재 소녀를 사랑으로 보살피는 삼촌의 헌신적인 모습을 통해 ISFJ가 추구하는 관계의 소중함과 따뜻한 이타심을 보여줍니다. 감동과 위로를 받을 수 있는 영화입니다."}
            ],
            "good_combinations": [
                {"type": "ESFP", "reason": "ESFP의 밝고 긍정적인 에너지가 ISFJ에게 편안함을 주고, 영화 감상을 더욱 즐겁게 만들어줍니다.",
                 "combination_movie_recommendations": [
                     {"title": "The Blind Side (2009) 🏈", "description": "역경을 딛고 꿈을 이루는 한 소년과 그를 지원하는 가족의 감동 실화."},
                     {"title": "School of Rock (2003) 🎸", "description": "음악을 통해 아이들의 잠재력을 끌어내는 유쾌한 코미디 영화."}
                 ]},
                {"type": "ISTJ", "reason": "비슷한 현실 지향적이고 안정적인 성향으로 영화에 대한 깊은 공감대를 형성할 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Sully (2016) ✈️", "description": "허드슨 강의 기적을 이룬 비행기 기장의 실화."},
                     {"title": "Bridge of Spies (2015) ⚖️", "description": "냉전 시대, 스파이 교환 협상을 다룬 스릴러 영화로, 원칙과 협상을 중시합니다."}
                 ]}
            ]
        },
        "INFJ": {
            "summary": "통찰력이 뛰어나고 이상주의적이며, 의미와 가치를 추구하는 유형입니다. 타인의 성장에 관심을 가지고 깊은 대화를 선호합니다. 직관적이고 창의적이며, 복잡한 문제의 본질을 꿰뚫어 보는 능력이 있습니다.",
            "movies": [
                {"title": "Arrival (2016) 👽",
                 "description": "외계 언어를 통해 인류의 운명을 바꾸는 과정을 그린 SF 영화입니다.",
                 "relevance": "INFJ의 통찰력과 이상주의적인 시각은 이 영화의 복잡한 메시지와 시간의 비선형성을 이해하는 데 큰 도움이 됩니다. 주인공이 외계 언어를 통해 미래를 예지하고 인류의 갈등을 해소하려는 모습은 INFJ가 추구하는 평화와 조화, 그리고 본질적인 의미 탐구와 맞닿아 있습니다. 깊이 있는 상징과 은유를 통해 INFJ의 직관을 자극합니다."},
                {"title": "Contact (1997) 🔭",
                 "description": "외계 문명과의 조우를 통해 과학과 신념의 갈등을 탐구하는 영화입니다.",
                 "relevance": "INFJ는 의미와 가치를 중요하게 생각하며, 깊은 내면의 세계를 탐구합니다. 엘리 애로웨이 박사가 외계 신호를 통해 우주의 진리를 탐구하고, 과학과 영성 사이에서 자신만의 믿음을 찾아가는 과정은 INFJ의 이상주의적이고 사색적인 면모를 만족시킬 것입니다. 인류 전체의 화합과 발전을 꿈꾸는 INFJ에게 깊은 영감을 줍니다."},
                {"title": "Interstellar (2014) 🌌",
                 "description": "우주와 시간의 신비를 탐구하며 인류의 생존을 위한 여정을 그린 SF 대작입니다.",
                 "relevance": "INFJ는 인류의 미래와 우주의 신비에 대한 깊은 관심을 가집니다. 이 영화는 광대한 우주 속에서 인류애와 희생의 가치를 탐구하며, INFJ의 이상주의와 인류 전체에 대한 관심에 깊은 울림을 줄 것입니다. 복잡한 과학적 개념과 철학적 메시지가 INFJ의 통찰력을 자극합니다."}
            ],
            "good_combinations": [
                {"type": "ENFP", "reason": "INFJ와 ENFP는 감성적 유대감을 형성하며 영화의 깊은 의미를 함께 탐구하고 감정을 공유합니다.",
                 "combination_movie_recommendations": [
                     {"title": "Eternal Sunshine of the Spotless Mind (2004) 💔", "description": "기억과 사랑, 관계의 본질을 탐구하는 독특한 SF 로맨스."},
                     {"title": "Into the Wild (2007) 🏕️", "description": "사회 시스템을 거부하고 알래스카 야생으로 떠난 청년의 실화를 그린 영화."}
                 ]},
                {"type": "ENTP", "reason": "ENTP의 논리적인 분석과 INFJ의 통찰력이 만나 영화에 대한 풍부하고 다각적인 대화를 이끌어낼 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Inception (2010) 💭", "description": "꿈속으로 들어가 생각을 훔치거나 심는 복잡한 개념의 SF 스릴러."},
                     {"title": "Mr. Nobody (2009) ❓", "description": "한 남자의 삶이 여러 가지 선택에 따라 어떻게 변하는지 보여주는 철학적인 SF 영화."}
                 ]}
            ]
        },
        "INTJ": {
            "summary": "전략적이고 분석적이며, 독립적이고 비판적인 사고를 가진 유형입니다. 복잡한 문제를 해결하는 데 능숙하며, 미래를 계획하고 비전을 제시하는 것을 좋아합니다. 효율성과 합리성을 중시하며, 지적인 도전을 즐깁니다.",
            "movies": [
                {"title": "The Imitation Game (2014) 💻",
                 "description": "암호 해독가 앨런 튜링의 삶과 그의 천재성을 그린 영화입니다.",
                 "relevance": "INTJ는 복잡한 시스템을 분석하고 효율적인 전략을 세우는 데 뛰어납니다. 앨런 튜링이 남들과 다른 방식으로 문제를 접근하고, 비판적 사고를 통해 난제를 해결하는 모습은 INTJ의 독립적이고 혁신적인 사고방식을 잘 보여줍니다. 지적인 도전과 논리적 추론을 즐기는 INTJ에게 최고의 선택입니다."},
                {"title": "Oppenheimer (2023) 💣",
                 "description": "원자폭탄 개발을 주도한 J. 로버트 오펜하이머의 복잡한 내면과 윤리적 고민을 다룬 영화입니다.",
                 "relevance": "INTJ는 큰 그림을 보고 장기적인 계획을 세우는 데 능하며, 자신의 비전을 실현하기 위해 강력하게 추진합니다. 오펜하이머의 뛰어난 지성과 목표 지향적인 태도는 INTJ의 특성과 일치하며, 과학적 발견이 가져오는 윤리적 딜레마는 INTJ의 비판적 사고와 깊은 성찰을 자극할 것입니다. 통제와 완벽함을 추구하는 INTJ에게 흥미로운 관점을 제공합니다."},
                {"title": "The Social Network (2010) 💻",
                 "description": "페이스북의 탄생과정과 그 이면에 숨겨진 창립자들의 갈등을 다룬 영화입니다.",
                 "relevance": "INTJ는 전략적인 사고와 혁신적인 아이디어를 추구합니다. 마크 주커버그가 새로운 시스템을 구축하고 그 과정에서 겪는 갈등은 INTJ의 비판적 사고와 효율성을 중시하는 면모를 자극합니다. 기술과 사회에 미치는 영향에 대한 깊은 분석을 유도하는 영화입니다."}
            ],
            "good_combinations": [
                {"type": "INTP", "reason": "INTJ와 INTP는 모두 논리적이고 분석적인 사고를 선호하여 영화의 과학적, 철학적 의미에 대해 깊이 있는 토론을 할 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Coherence (2013) 🌌", "description": "혜성이 지구에 접근하면서 벌어지는 기이한 현상과 다중 우주를 다룬 저예산 SF 스릴러."},
                     {"title": "Cube (1997) 🟥", "description": "탈출해야 하는 미로 속에서 수학적 지식으로 문제를 해결하는 SF 스릴러."}
                 ]},
                {"type": "ENFP", "reason": "ENFP의 창의적이고 감성적인 관점이 INTJ의 논리적 사고에 새로운 영감을 주어 영화를 더 다채롭게 이해할 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Gattaca (1997) 🧬", "description": "유전자 조작이 보편화된 미래 사회에서 자연적으로 태어난 한 남자가 우주 비행의 꿈을 이루기 위해 노력하는 이야기."},
                     {"title": "Big Hero 6 (2014) 🤖", "description": "천재 로봇 공학 소년과 로봇 베이맥스의 따뜻한 우정을 그린 애니메이션 영화."}
                 ]}
            ]
        },
        "ISTP": {
            "summary": "논리적이고 실용적이며, 호기심이 많고 문제 해결에 능한 유형입니다. 새로운 경험을 좋아하고, 위기 상황에서 침착하게 대응합니다. 손재주가 뛰어나고 기계나 도구를 다루는 것을 좋아합니다.",
            "movies": [
                {"title": "The Martian (2015) 🥔",
                 "description": "화성에 홀로 남겨진 우주인이 과학적 지식과 실용적인 기술로 생존하는 이야기입니다.",
                 "relevance": "ISTP는 실제적인 문제 해결에 탁월하며, 손재주가 좋고 도구를 다루는 데 능합니다. 마크 와트니가 제한된 자원과 극한의 환경 속에서 자신의 지식과 기술을 활용하여 기발한 생존 방안을 찾아내는 모습은 ISTP의 실용적이고 즉흥적인 문제 해결 능력을 완벽하게 보여줍니다. 직접 몸으로 부딪혀 문제를 해결하는 것을 선호하는 ISTP에게 깊은 만족감을 줄 것입니다."},
                {"title": "Source Code (2011) ⏱️",
                 "description": "반복되는 시간 속에서 테러를 막으려는 주인공의 이야기를 다룬 SF 스릴러입니다.",
                 "relevance": "ISTP는 상황을 빠르게 분석하고 실용적인 해결책을 찾습니다. 주인공이 주어진 정보를 바탕으로 시행착오를 겪으며 미스터리를 풀어가는 과정은 ISTP의 논리적 추론과 위기 상황에서의 침착한 대응 능력을 잘 드러냅니다. 예측 불가능한 상황에서 즉각적으로 행동하는 ISTP에게 긴장감과 재미를 선사할 영화입니다."},
                {"title": "Edge of Tomorrow (2014) 🤖",
                 "description": "외계 종족과의 전투에서 반복되는 시간 루프에 갇힌 주인공의 이야기입니다.",
                 "relevance": "ISTP는 실용적인 문제 해결과 즉각적인 행동을 중요하게 생각합니다. 주인공이 반복되는 상황 속에서 시행착오를 통해 최적의 해결책을 찾아 나가는 과정은 ISTP의 유연한 사고와 뛰어난 적응력, 그리고 직접적인 행동을 선호하는 면모를 잘 보여줍니다. 긴장감 넘치는 액션과 전략적 요소가 ISTP의 흥미를 유발합니다."}
            ],
            "good_combinations": [
                {"type": "ESFP", "reason": "ISTP의 논리적이고 실용적인 면모와 ESFP의 활동적이고 즉흥적인 면모가 결합하여 영화에 대한 흥미로운 관점과 즉각적인 반응을 공유할 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Jumanji: Welcome to the Jungle (2017) 🌴", "description": "비디오 게임 속으로 빨려 들어간 주인공들이 각자의 특수 능력을 활용해 미션을 해결하는 어드벤처 코미디."},
                     {"title": "Baby Driver (2017) 🚗", "description": "음악에 맞춰 짜릿한 드라이빙을 선보이는 천재 운전자의 이야기."}
                 ]},
                {"type": "ENTP", "reason": "ENTP의 창의적인 아이디어와 ISTP의 문제 해결 능력이 시너지를 내어 영화의 복잡한 설정이나 과학적 원리에 대해 깊이 있는 대화를 나눌 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Now You See Me (2013) 🎩", "description": "천재 마술사들이 펼치는 화려한 마술과 그 안에 숨겨진 치밀한 계획을 다룬 범죄 스릴러."},
                     {"title": "Sherlock Holmes (2009) 🕵️‍♂️", "description": "천재 탐정 셜록 홈즈와 왓슨 박사의 활약을 그린 추리 액션 영화."}
                 ]}
            ]
        },
        "ISFP": {
            "summary": "예술적 감각이 뛰어나고, 온화하며, 겸손하고 관대한 유형입니다. 현재를 즐기며, 자신만의 가치와 삶의 방식을 중요하게 생각합니다. 자유롭고 유연하며, 주변 환경에 대한 섬세한 감각을 가지고 있습니다.",
            "movies": [
                {"title": "Good Will Hunting (1997) ✨",
                 "description": "천재적인 재능을 가졌지만 방황하는 청년이 수학과 심리학을 통해 성장하는 영화입니다.",
                 "relevance": "ISFP는 자신의 내면과 감정에 솔직하며, 예술적인 감각으로 세상을 봅니다. 윌 헌팅이 자신의 천재성을 인정하고, 진정한 자아와 삶의 의미를 찾아가는 과정은 ISFP의 개인적인 성장과 가치 탐구에 대한 깊은 공감을 불러일으킵니다. 따뜻한 인간미와 감성적인 메시지가 ISFP의 마음에 와닿을 것입니다."},
                {"title": "Hidden Figures (2016) 👩‍🔬",
                 "description": "NASA의 숨겨진 영웅들이 인종 차별과 성 차별을 극복하고 우주 경쟁을 승리로 이끈 감동적인 실화입니다.",
                 "relevance": "ISFP는 다른 사람의 가치와 개성을 존중하며, 따뜻한 마음으로 주변을 대합니다. 이 영화의 주인공들이 사회적 편견 속에서도 자신의 능력을 증명하고, 개인의 존엄성을 지키려는 모습은 ISFP의 정의감과 진정성을 추구하는 마음과 잘 어울립니다. 조용하지만 강한 영향력을 발휘하는 ISFP의 특성을 느낄 수 있습니다."},
                {"title": "Little Miss Sunshine (2006) 🚌",
                 "description": "이상한 가족이 미인 대회에 참가하기 위해 로드트립을 떠나는 유쾌하고 감동적인 코미디 드라마입니다.",
                 "relevance": "ISFP는 자신만의 가치와 개성을 중요하게 생각하며, 진정성을 추구합니다. 이 영화는 완벽하지 않은 가족 구성원들이 서로의 개성을 존중하고 사랑하며 함께 성장하는 과정을 통해 ISFP의 따뜻한 감수성과 개방적인 태도에 공감을 줍니다. 각자의 삶의 방식을 인정하는 메시지가 인상 깊을 것입니다."}
            ],
            "good_combinations": [
                {"type": "ENFJ", "reason": "ENFJ의 따뜻하고 지지적인 성향이 ISFP의 감수성과 어우러져 영화 속 인물들의 감정을 깊이 있게 공감하며 대화할 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Dead Poets Society (1989) 📚", "description": "전통적인 학교에 부임한 자유로운 영혼의 영문학 선생님이 학생들에게 삶의 새로운 의미를 가르치는 이야기."},
                     {"title": "Patch Adams (1998) 🤡", "description": "환자들에게 웃음을 통해 치유를 선사하는 의사의 감동적인 실화."}
                 ]},
                {"type": "INFP", "reason": "ISFP와 INFP는 비슷한 감성적 깊이를 가지고 있어 영화가 전달하는 메시지나 감동을 함께 느끼고 나눌 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Big Fish (2003) 🐠", "description": "과장된 이야기 속에서 아버지의 진정한 삶의 의미를 찾아가는 아들의 여정을 그린 환상적인 영화."},
                     {"title": "Edward Scissorhands (1990) ✂️", "description": "가위손을 가진 순수한 영혼의 남자가 마을 사람들과 교류하며 겪는 이야기."}
                 ]}
            ]
        },
        "INFP": {
            "summary": "이상주의적이고 창의적이며, 깊은 감수성과 공감 능력을 가진 유형입니다. 의미와 진정성을 중요하게 생각하며, 세상을 더 나은 곳으로 만들고자 합니다. 몽상적이고 영감을 추구하며, 개인의 가치를 소중히 여깁니다.",
            "movies": [
                {"title": "Contact (1997) 🔭",
                 "description": "외계 문명과의 조우를 통해 과학과 신념의 갈등을 탐구하는 영화입니다.",
                 "relevance": "INFP는 깊은 의미와 이상적인 가치를 추구하며, 우주와 인간 존재에 대한 근본적인 질문에 매료됩니다. 엘리 애로웨이 박사가 미지의 신호를 통해 우주의 진리를 탐구하고, 과학적 사실을 넘어선 신념과 직관을 따르는 여정은 INFP의 창의적이고 사색적인 면모를 만족시킬 것입니다. 더 나은 세상을 꿈꾸는 INFP에게 깊은 영감을 줍니다."},
                {"title": "Good Will Hunting (1997) ✨",
                 "description": "천재적인 재능을 가졌지만 방황하는 청년이 수학과 심리학을 통해 성장하는 영화입니다.",
                 "relevance": "INFP는 개인의 성장과 진정성을 중요하게 생각하며, 타인과의 깊은 연결을 갈망합니다. 윌 헌팅의 내면적 갈등과 그를 둘러싼 사람들과의 관계, 특히 션 교수와의 교감을 통해 진정한 자신을 찾아가는 모습은 INFP가 추구하는 깊은 인간적인 연결과 이상적인 가치에 대한 공감을 불러일으킵니다. 따뜻한 위로와 성찰의 기회를 제공합니다."},
                {"title": "Amelie (2001) ❤️",
                 "description": "파리의 몽마르뜨에 사는 아멜리의 따뜻하고 기발한 상상력으로 세상을 행복하게 만드는 이야기입니다.",
                 "relevance": "INFP는 독특한 시각으로 세상을 바라보고, 따뜻한 마음으로 주변에 긍정적인 영향을 주기를 바랍니다. 아멜리의 순수하고 몽상적인 면모, 그리고 주변 사람들에게 몰래 행복을 선사하는 모습은 INFP의 깊은 감수성과 이상주의적인 따뜻함과 잘 어울립니다. 삶의 소소한 아름다움을 발견하고 영감을 얻을 수 있는 영화입니다."}
            ],
            "good_combinations": [
                {"type": "ENFP", "reason": "INFP와 ENFP는 모두 이상주의적이고 감수성이 풍부하여 영화의 숨겨진 의미나 감성적인 부분에 대해 깊이 있는 대화를 나눌 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "About Time (2013) ⏳", "description": "시간 여행 능력을 가진 남자가 사랑과 삶의 의미를 찾아가는 과정을 그린 로맨스 판타지."},
                     {"title": "Sing Street (2016) 🎶", "description": "음악을 통해 꿈을 찾아가는 청년들의 유쾌하고 감동적인 성장 영화."}
                 ]},
                {"type": "INFJ", "reason": "INFJ의 통찰력과 INFP의 이상주의가 만나 영화의 철학적 메시지에 대해 심도 깊은 논의를 할 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Life of Pi (2012) 🐅", "description": "난파선에서 홀로 남은 소년과 호랑이의 생존기를 다룬 철학적인 모험 영화."},
                     {"title": "Blade Runner 2049 (2017) 🌃", "description": "인간의 정체성과 존재 의미를 탐구하는 SF 느와르 영화."}
                 ]}
            ]
        },
        "INTP": {
            "summary": "논리적이고 분석적이며, 호기심이 많고 이론적인 유형입니다. 복잡한 아이디어를 탐구하고, 지적인 자극을 추구하는 것을 좋아합니다. 독창적이고 독립적인 사고를 하며, 문제 해결에 있어 창의적인 방법을 모색합니다.",
            "movies": [
                {"title": "Primer (2004) 🧪",
                 "description": "저예산으로 만들어졌지만 매우 복잡한 시간 여행의 논리를 다룬 SF 영화입니다.",
                 "relevance": "INTP는 복잡한 시스템과 이론에 매력을 느끼며, 추상적인 개념을 분석하고 새로운 가능성을 탐구하는 것을 즐깁니다. 이 영화는 시간 여행의 과학적, 논리적 가능성을 매우 심도 깊게 다루며, 다중 타임라인과 인과 관계의 복잡성은 INTP의 분석적이고 이론적인 사고를 충족시켜 줄 것입니다. 지적인 퍼즐을 맞추는 재미를 선사합니다."},
                {"title": "Interstellar (2014) 🌌",
                 "description": "우주와 시간의 신비를 탐구하는 SF 대작으로, 아인슈타인의 상대성 이론과 웜홀 등 과학적 개념을 시각적으로 구현했습니다.",
                 "relevance": "INTP는 지적인 호기심과 탐구심이 강하며, 우주의 미스터리와 과학적 이론에 대한 깊은 이해를 추구합니다. 이 영화는 단순한 스토리텔링을 넘어 블랙홀, 시간 지연 등 복잡한 과학적 개념을 시각적으로 구현하여 INTP의 지적 욕구를 자극합니다. 인류의 생존과 미래에 대한 근본적인 질문을 던지며 INTP의 사색적인 면모를 만족시킵니다."},
                {"title": "Ex Machina (2014) 🤖",
                 "description": "인공지능 로봇의 의식과 인간 본질을 탐구하는 심리 스릴러입니다.",
                 "relevance": "INTP는 복잡한 시스템과 이론에 깊이 파고들고, 지적인 질문을 던지는 것을 즐깁니다. 이 영화는 인공지능의 윤리적 문제, 인간의 의식과 존재론적 질문을 던지며 INTP의 분석적 사고와 추상적 사고 능력을 자극합니다. 철학적이고 과학적인 논쟁을 유발하는 영화입니다."}
            ],
            "good_combinations": [
                {"type": "INTJ", "reason": "INTP와 INTJ는 모두 논리적이고 분석적인 사고를 선호하여 영화의 과학적, 철학적 의미에 대해 깊이 있는 토론을 할 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Coherence (2013) 🌌", "description": "혜성이 지구에 접근하면서 벌어지는 기이한 현상과 다중 우주를 다룬 저예산 SF 스릴러."},
                     {"title": "Arrival (2016) 👽", "description": "외계 언어를 통해 인류의 운명을 바꾸는 과정을 그린 SF 영화."}
                 ]},
                {"type": "ENTP", "reason": "비슷한 지적 호기심과 논리적 탐구심을 공유하여 영화의 복잡한 주제에 대해 흥미로운 대화를 나눌 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "The Social Network (2010) 💻", "description": "페이스북의 탄생과정과 그 이면에 숨겨진 창립자들의 갈등을 다룬 영화."},
                     {"title": "Mr. Nobody (2009) ❓", "description": "한 남자의 삶이 여러 가지 선택에 따라 어떻게 변하는지 보여주는 철학적인 SF 영화."}
                 ]}
            ]
        },
        "ESTP": {
            "summary": "현실적이고 활동적이며, 개방적이고 적응력이 뛰어난 유형입니다. 새로운 경험을 좋아하고, 문제 해결에 적극적입니다. 에너지가 넘치고 즉흥적이며, 뛰어난 관찰력으로 현실을 파악합니다. 스릴과 재미를 추구하며, 활동적인 여행을 선호합니다.",
            "movies": [
                {"title": "The Martian (2015) 🥔",
                 "description": "화성에 홀로 남겨진 우주인이 과학적 지식과 실용적인 기술로 생존하는 이야기입니다.",
                 "relevance": "ESTP는 행동 지향적이며, 실제적인 문제 해결에 능합니다. 마크 와트니가 제한된 자원과 극한의 환경 속에서 자신의 지식과 기술을 활용하여 기발한 생존 방안을 찾아내는 모습은 ESTP의 실용적이고 즉흥적인 문제 해결 능력을 완벽하게 보여줍니다. 직접 몸으로 부딪혀 문제를 해결하는 것을 선호하는 ESTP에게 깊은 만족감을 줄 것입니다."},
                {"title": "Moneyball (2011) ⚾",
                 "description": "통계를 이용해 야구팀을 혁신하는 실화로, 직관적이고 현실적인 접근이 돋보입니다.",
                 "relevance": "ESTP는 실용적인 사고와 빠른 판단으로 새로운 기회를 포착하는 데 능합니다. 빌리 빈 단장이 전통적인 야구 운영 방식에 얽매이지 않고 데이터를 기반으로 효율적인 전략을 세워 성공을 이끌어내는 과정은 ESTP의 현실적이고 결과 지향적인 면모를 만족시킬 것입니다. 현장에서 직접 부딪히며 문제를 해결하는 ESTP에게 흥미로운 관점을 제공합니다."},
                {"title": "Ford v Ferrari (2019) 🏎️",
                 "description": "1960년대 르망 24시간 레이스에서 포드가 페라리에 맞서기 위해 벌이는 도전을 그린 실화입니다.",
                 "relevance": "ESTP는 스릴과 도전을 즐기며, 실용적인 기술과 경쟁을 통해 성취감을 느낍니다. 이 영화는 빠른 판단력과 행동력, 그리고 기술적인 문제 해결 능력이 중요한 레이싱 세계를 통해 ESTP의 역동적이고 현실적인 면모를 만족시킵니다. 직접 부딪혀 문제를 해결하고 짜릿한 성취감을 맛보는 것을 좋아하는 ESTP에게 최고의 선택이 될 것입니다."}
            ],
            "good_combinations": [
                {"type": "ESFP", "reason": "ESTP의 현실적인 관점과 ESFP의 예술적인 감각이 만나 영화를 다양한 시각에서 즐길 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Jumanji: Welcome to the Jungle (2017) 🌴", "description": "비디오 게임 속으로 빨려 들어간 주인공들이 각자의 특수 능력을 활용해 미션을 해결하는 어드벤처 코미디."},
                     {"title": "The Greatest Showman (2017) 🎩", "description": "환상적인 쇼를 만들어가는 P.T. 바넘의 이야기를 그린 뮤지컬 영화."}
                 ]},
                {"type": "ENTJ", "reason": "ENTJ의 전략적인 사고와 ESTP의 실행력이 결합하여 영화의 주제나 전개에 대해 활발하고 생산적인 대화를 나눌 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "The Big Short (2015) 💰", "description": "2008년 금융 위기를 예측하고 월스트리트에 맞서 성공을 거둔 사람들의 이야기."},
                     {"title": "Margin Call (2011) 📉", "description": "글로벌 금융 위기 직전, 거대 투자은행에서 벌어지는 24시간을 그린 스릴러 영화."}
                 ]}
            ]
        },
        "ESFP": {
            "summary": "사교적이고 낙천적이며, 현재를 즐기고 사람들과의 관계를 중요시하는 유형입니다. 활기차고 긍정적인 에너지를 발산하며, 주변 사람들에게 즐거움을 주는 것을 좋아합니다. 즉흥적이고 개방적입니다. 사람들과의 교류와 즐거운 경험을 최우선으로 생각합니다.",
            "movies": [
                {"title": "Hidden Figures (2016) 👩‍🔬",
                 "description": "NASA의 숨겨진 영웅들이 인종 차별과 성 차별을 극복하고 우주 경쟁을 승리로 이끈 감동적인 실화입니다.",
                 "relevance": "ESFP는 사람들과의 상호작용을 통해 에너지를 얻고, 긍정적인 분위기를 만듭니다. 이 영화의 주인공들이 서로 돕고 소통하며 사회적 편견을 극복하고 거대한 목표를 달성하는 과정은 ESFP의 사교적이고 협력적인 면모와 잘 어울립니다. 함께 목표를 향해 나아가는 공동체의 모습을 통해 ESFP는 큰 감동과 영감을 얻을 것입니다."},
                {"title": "The Theory of Everything (2014) 💖",
                 "description": "스티븐 호킹 박사의 삶과 사랑, 그리고 물리학에 대한 열정을 그린 영화입니다.",
                 "relevance": "ESFP는 감정 표현에 솔직하며, 삶의 즐거움을 추구합니다. 이 영화는 과학적 성취뿐만 아니라 스티븐 호킹과 그의 가족, 친구들 간의 깊은 사랑과 관계의 소중함을 보여주며, ESFP의 따뜻하고 감성적인 면모를 만족시킬 것입니다. 인간적인 면모를 통해 과학의 경이로움을 함께 느끼는 기회를 제공합니다."},
                {"title": "Forrest Gump (1994) 🏃‍♂️",
                 "description": "평범한 한 남자가 미국의 주요 역사적 사건들을 겪으며 살아가는 이야기입니다.",
                 "relevance": "ESFP는 현재를 즐기고 삶의 다양한 경험에 개방적입니다. 포레스트 검프가 우연과 순수함으로 여러 역사적 사건의 중심에 서고, 주변 사람들에게 긍정적인 영향을 주는 모습은 ESFP의 낙천적인 성향과 따뜻한 마음을 보여줍니다. 삶의 즐거움과 인간적인 유대감을 중요하게 생각하는 ESFP에게 감동과 재미를 동시에 선사할 것입니다."}
            ],
            "good_combinations": [
                {"type": "ISFJ", "reason": "ESFP의 밝은 에너지와 ISFJ의 차분하고 배려심 깊은 성향이 어우러져 편안하고 즐거운 영화 감상 분위기를 만듭니다.",
                 "combination_movie_recommendations": [
                     {"title": "The Blind Side (2009) 🏈", "description": "역경을 딛고 꿈을 이루는 한 소년과 그를 지원하는 가족의 감동 실화."},
                     {"title": "School of Rock (2003) 🎸", "description": "음악을 통해 아이들의 잠재력을 끌어내는 유쾌한 코미디 영화."}
                 ]},
                {"type": "ENFP", "reason": "ESFP와 ENFP는 비슷한 낙천적이고 사교적인 성향으로 영화에 대한 활발한 감정 공유와 재미있는 대화를 나눌 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "About Time (2013) ⏳", "description": "시간 여행 능력을 가진 남자가 사랑과 삶의 의미를 찾아가는 과정을 그린 로맨스 판타지."},
                     {"title": "Midnight in Paris (2011) 🎨", "description": "파리의 과거로 시간 여행을 떠나는 작가의 이야기로, 예술과 낭만을 즐길 수 있습니다."}
                 ]}
            ]
        },
        "ENFP": {
            "summary": "열정적이고 창의적이며, 상상력이 풍부하고 새로운 아이디어를 추구하는 유형입니다. 사람들과의 교류를 통해 영감을 얻고 긍정적인 영향을 줍니다. 호기심이 많고 개방적이며, 다양한 가능성을 탐색합니다. 의미 있는 경험과 사람들과의 깊은 연결을 중시합니다.",
            "movies": [
                {"title": "Contact (1997) 🔭",
                 "description": "외계 문명과의 조우를 통해 과학과 신념의 갈등을 탐구하는 영화입니다.",
                 "relevance": "ENFP는 새로운 가능성을 탐색하고 영감을 추구하며, 우주의 미스터리에 대한 깊은 호기심을 가지고 있습니다. 이 영화의 주인공이 미지의 신호를 추적하며 우주와의 소통을 시도하는 과정은 ENFP의 탐구심과 상상력을 자극하며, 열정적으로 목표를 향해 나아가는 모습에 깊이 공감할 것입니다. 이상과 현실 사이에서 균형을 찾아가는 과정이 ENFP에게 깊은 울림을 줍니다."},
                {"title": "Interstellar (2014) 🌌",
                 "description": "우주와 시간의 신비를 탐구하며 인류의 생존을 위한 여정을 그린 SF 대작입니다.",
                 "relevance": "ENFP는 상상력이 풍부하고 새로운 아이디어에 개방적이며, 인류의 미래와 가능성에 대한 긍정적인 비전을 가지고 있습니다. 이 영화는 광대한 우주에서 펼쳐지는 놀라운 과학적 상상력과 인류의 생존을 위한 끊임없는 도전을 보여주며 ENFP의 창의적이고 열정적인 면모를 만족시킬 것입니다. 미지의 세계를 탐험하며 새로운 가능성을 찾아가는 과정에서 ENFP는 큰 영감을 얻을 것입니다."},
                {"title": "The Truman Show (1998) 📺",
                 "description": "자신이 리얼리티 쇼의 주인공이라는 사실을 모른 채 살아가는 한 남자의 이야기입니다.",
                 "relevance": "ENFP는 진정한 의미와 가능성을 탐색하며, 틀에 갇히는 것을 싫어합니다. 트루먼이 자신의 삶의 진실을 찾아 자유를 향해 나아가는 과정은 ENFP의 호기심과 끊임없는 탐구 정신, 그리고 이상을 향한 열정을 자극합니다. 현실의 제약을 넘어 새로운 가능성을 추구하는 ENFP에게 깊은 영감을 줄 것입니다."}
            ],
            "good_combinations": [
                {"type": "INFJ", "reason": "ENFP의 열정적인 아이디어와 INFJ의 통찰력이 만나 영화의 깊은 의미와 숨겨진 메시지에 대해 풍부한 대화를 나눌 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Eternal Sunshine of the Spotless Mind (2004) 💔", "description": "기억과 사랑, 관계의 본질을 탐구하는 독특한 SF 로맨스."},
                     {"title": "Inside Out (2015) 😊", "description": "인간의 감정을 의인화하여 보여주는 애니메이션 영화로, 복잡한 내면 세계를 탐구합니다."}
                 ]},
                {"type": "INTJ", "reason": "INTJ의 논리적이고 분석적인 관점에 ENFP의 창의적인 사고가 더해져 영화를 다각도로 해석하고 새로운 관점을 공유할 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Gattaca (1997) 🧬", "description": "유전자 조작이 보편화된 미래 사회에서 자연적으로 태어난 한 남자가 우주 비행의 꿈을 이루기 위해 노력하는 이야기."},
                     {"title": "Big Hero 6 (2014) 🤖", "description": "천재 로봇 공학 소년과 로봇 베이맥스의 따뜻한 우정을 그린 애니메이션 영화."}
                 ]}
            ]
        },
        "ENTP": {
            "summary": "논리적이고 창의적이며, 새로운 아이디어를 탐구하고 토론을 즐기는 유형입니다. 도전적이고, 틀에 얽매이지 않는 사고방식을 가지고 있습니다. 뛰어난 통찰력과 비판적 사고로 문제를 다각도로 분석합니다. 예상치 못한 상황과 지적인 도전을 즐깁니다.",
            "movies": [
                {"title": "Primer (2004) 🧪",
                 "description": "저예산으로 만들어졌지만 매우 복잡한 시간 여행의 논리를 다룬 SF 영화입니다.",
                 "relevance": "ENTP는 복잡한 아이디어를 분석하고 새로운 가능성을 탐구하는 것을 좋아하며, 지적인 도전을 즐깁니다. 이 영화는 시간 여행이라는 주제를 독특하고 지적으로 접근하여 ENTP의 탐구심과 논리적 추론 능력을 극대화시킬 것입니다. 끊임없이 의문을 제기하고 새로운 해결책을 모색하는 ENTP의 특성과 잘 부합하는 영화입니다."},
                {"title": "Oppenheimer (2023) 💣",
                 "description": "원자폭탄 개발을 주도한 J. 로버트 오펜하이머의 복잡한 내면과 윤리적 고민을 다룬 영화입니다.",
                 "relevance": "ENTP는 지적인 토론과 새로운 아이디어를 탐구하는 것을 즐기며, 기존의 관념에 도전하는 것을 두려워하지 않습니다. 오펜하이머의 도전적인 연구와 그 결과에 대한 광범위한 논의는 ENTP의 분석적 사고와 비판적 관점을 자극하며, 복잡한 문제의 다면적인 측면을 탐구하게 합니다. 과학적 발견의 양면성에 대한 깊은 성찰을 제공합니다."},
                {"title": "Minority Report (2002) 🔮",
                 "description": "미래 범죄를 예측하여 미리 막는 시스템을 다룬 SF 스릴러입니다.",
                 "relevance": "ENTP는 혁신적인 아이디어와 논리적 오류를 찾아내는 데 능합니다. 미래 예측 시스템의 완벽성과 그 속에 숨겨진 윤리적 딜레마를 파헤치는 과정은 ENTP의 비판적 사고와 논쟁적인 기질을 자극합니다. 시스템의 허점을 발견하고 새로운 해결책을 모색하는 것을 즐기는 ENTP에게 흥미로운 영화입니다."}
            ],
            "good_combinations": [
                {"type": "INTP", "reason": "ENTP와 INTP는 모두 지적인 호기심과 논리적 탐구심이 강하여 영화의 복잡한 주제나 과학적 원리에 대해 심도 깊은 대화를 나눌 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "The Social Network (2010) 💻", "description": "페이스북의 탄생과정과 그 이면에 숨겨진 창립자들의 갈등을 다룬 영화."},
                     {"title": "Steve Jobs (2015) 🍎", "description": "스티브 잡스의 세 가지 주요 프레젠테이션 뒤편의 이야기를 다룬 전기 영화."}
                 ]},
                {"type": "INFJ", "reason": "INFJ의 통찰력과 ENTP의 논리적 분석이 만나 영화의 숨겨진 의미와 철학적 메시지에 대해 풍부하고 깊이 있는 논의를 이끌어낼 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Inception (2010) 💭", "description": "꿈속으로 들어가 생각을 훔치거나 심는 복잡한 개념의 SF 스릴러."},
                     {"title": "Her (2013) 💖", "description": "인공지능 운영체제와 사랑에 빠지는 남자의 이야기를 그린 로맨스 드라마."}
                 ]}
            ]
        },
        "ESTJ": {
            "summary": "현실적이고 실용적이며, 체계적이고 리더십이 강한 유형입니다. 조직을 잘 이끌고, 목표 달성을 위해 효율적으로 움직입니다. 책임감이 강하고 결단력이 있으며, 규칙과 질서를 중요하게 생각합니다.",
            "movies": [
                {"title": "Apollo 13 (1995) 🚀",
                 "description": "실제 사건을 바탕으로, 우주 비행 중 발생한 위기를 해결하는 과정을 보여주는 영화입니다.",
                 "relevance": "ESTJ는 조직적이고 효율적인 문제 해결에 능하며, 위기 상황에서도 침착하게 리더십을 발휘합니다. 아폴로 13호 팀이 극한의 상황에서 목표를 달성하기 위해 체계적으로 협력하고 리더의 지휘 아래 움직이는 모습은 ESTJ의 강점을 잘 보여줍니다. 계획을 중시하고 세부사항을 꼼꼼히 살피며, 현실적인 해결책을 찾는 ESTJ에게 깊은 인상을 줄 영화입니다."},
                {"title": "Moneyball (2011) ⚾",
                 "description": "통계를 이용해 야구팀을 혁신하는 실화로, 직관적이고 현실적인 접근이 돋보입니다.",
                 "relevance": "ESTJ는 현실적이고 결과 지향적이며, 효율성을 극대화하는 데 능합니다. 빌리 빈 단장이 비효율적인 관행을 개선하고 데이터를 통해 성공을 이끌어내는 과정은 ESTJ의 실용적이고 논리적인 접근 방식을 만족시킬 것입니다. 명확한 목표를 설정하고, 체계적인 실행을 통해 성과를 창출하는 ESTJ의 특성을 잘 보여주는 영화입니다."},
                {"title": "The Big Short (2015) 💰",
                 "description": "2008년 금융 위기를 예측하고 월스트리트에 맞서 성공을 거둔 사람들의 이야기입니다.",
                 "relevance": "ESTJ는 현실적이고 실용적인 분석을 통해 문제를 파악하고 해결하는 데 능숙합니다. 금융 위기 속에서 비합리적인 시장의 흐름을 분석하고, 명확한 전략으로 위험을 기회로 바꾸는 영화 속 인물들의 모습은 ESTJ의 체계적인 사고와 단호한 결단력에 깊은 공감을 불러일으킬 것입니다. 실질적인 결과와 효율성을 중요하게 생각하는 ESTJ에게 흥미로운 영화입니다."}
            ],
            "good_combinations": [
                {"type": "ISTJ", "reason": "ESTJ와 ISTJ는 모두 현실적이고 체계적인 사고를 선호하여 영화의 사실적 배경이나 논리적 전개에 대해 깊은 공감대를 형성하며 감상할 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Contagion (2011) 🦠", "description": "치명적인 전염병의 확산과 이를 막기 위한 전 세계적인 노력, 그리고 사회 시스템의 반응을 현실적으로 그린 영화."},
                     {"title": "Sully (2016) ✈️", "description": "허드슨 강의 기적을 이룬 비행기 기장의 실화."}
                 ]},
                {"type": "ENTJ", "reason": "ENTJ와 ESTJ는 강력한 리더십과 목표 지향적인 성향을 공유하여 영화 속 전략이나 효율성에 대해 활발한 논의를 할 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "The Big Short (2015) 💰", "description": "2008년 금융 위기를 예측하고 월스트리트에 맞서 성공을 거둔 사람들의 이야기."},
                     {"title": "Margin Call (2011) 📉", "description": "글로벌 금융 위기 직전, 거대 투자은행에서 벌어지는 24시간을 그린 스릴러 영화."}
                 ]}
            ]
        },
        "ESFJ": {
            "summary": "사교적이고 친절하며, 타인을 배려하고 협력적인 유형입니다. 주변 사람들과의 조화를 중요하게 생각하며, 봉사 정신이 강합니다. 따뜻하고 배려심이 깊으며, 다른 사람의 감정에 공감하고 지원하는 것을 좋아합니다. 사람들과 함께하는 편안하고 즐거운 여행을 선호합니다.",
            "movies": [
                {"title": "Hidden Figures (2016) 👩‍🔬",
                 "description": "NASA의 숨겨진 영웅들이 인종 차별과 성 차별을 극복하고 우주 경쟁을 승리로 이끈 감동적인 실화입니다.",
                 "relevance": "ESFJ는 사람들과의 상호작용을 통해 에너지를 얻고, 긍정적인 분위기를 만듭니다. 이 영화의 주인공들이 서로 돕고 소통하며 사회적 편견을 극복하고 거대한 목표를 달성하는 과정은 ESFJ의 사교적이고 협력적인 면모와 잘 어울립니다. 함께 목표를 향해 나아가는 공동체의 모습을 통해 ESFJ는 큰 감동과 영감을 얻을 것입니다."},
                {"title": "The Theory of Everything (2014) 💖",
                 "description": "스티븐 호킹 박사의 삶과 사랑, 그리고 물리학에 대한 열정을 그린 영화입니다.",
                 "relevance": "ESFJ는 감정 표현에 솔직하며, 삶의 즐거움을 추구합니다. 이 영화는 과학적 성취뿐만 아니라 스티븐 호킹과 그의 가족, 친구들 간의 깊은 사랑과 관계의 소중함을 보여주며, ESFJ의 따뜻하고 감성적인 면모를 만족시킬 것입니다. 인간적인 면모를 통해 과학의 경이로움을 함께 느끼는 기회를 제공합니다."},
                {"title": "Green Book (2018) 🚗",
                 "description": "1960년대 미국 남부를 배경으로 한 흑인 피아니스트와 이탈리아계 운전사의 특별한 우정을 그린 영화입니다.",
                 "relevance": "ESFJ는 타인과의 관계를 중요시하고 조화를 추구합니다. 영화 속 두 주인공이 서로의 차이를 이해하고 진정한 우정을 쌓아가는 과정은 ESFJ의 따뜻한 마음과 공감 능력에 큰 울림을 줍니다. 사회적 편견을 넘어 인간적인 연결의 소중함을 보여주는 영화입니다."}
            ],
            "good_combinations": [
                {"type": "ISFJ", "reason": "ESFJ와 ISFJ는 모두 사람들과의 조화를 중요하게 생각하고 따뜻한 마음을 가지고 있어, 영화 속 감동적인 스토리에 깊이 공감하며 함께 즐거운 시간을 보낼 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Green Book (2018) 🚗", "description": "1960년대 미국 남부를 배경으로 한 흑인 피아니스트와 이탈리아계 운전사의 특별한 우정을 그린 영화."},
                     {"title": "The Help (2011) 🏡", "description": "1960년대 미국 남부 흑인 가정부들의 이야기를 다룬 영화로, 사회적 약자의 목소리를 담았습니다."}
                 ]},
                {"type": "ENFJ", "reason": "ENFJ의 리더십과 ESFJ의 협력적인 태도가 만나 영화에 대한 감상평을 활발하게 나누고 서로에게 긍정적인 영향을 줄 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Remember the Titans (2000) 🏈", "description": "인종 차별이 심했던 시기에 통합 미식축구팀을 이끌며 역경을 극복하는 감동 실화."},
                     {"title": "Pay It Forward (2000) ❤️", "description": "도움을 받은 사람이 다른 세 명에게 도움을 베푸는 '세상을 바꾸는 아이디어'를 그린 영화."}
                 ]}
            ]
        },
        "ENFJ": {
            "summary": "사교적이고 설득력 있으며, 타인의 성장에 관심을 가지고 리더십을 발휘하는 유형입니다. 사람들에게 영감을 주고, 긍정적인 변화를 이끌어내는 것을 좋아합니다. 따뜻하고 책임감이 강하며, 비전을 공유하는 데 능숙합니다. 의미 있는 경험과 사회적 교류를 통해 여행의 가치를 찾습니다.",
            "movies": [
                {"title": "Contact (1997) 🔭",
                 "description": "외계 문명과의 조우를 통해 과학과 신념의 갈등을 탐구하는 영화입니다.",
                 "relevance": "ENFJ는 타인에게 영감을 주고 비전을 공유하며, 공동의 목표를 향해 나아가는 데 능합니다. 엘리 애로웨이 박사가 미지의 신호를 통해 인류에게 중요한 메시지를 전달하고, 이를 통해 사람들을 설득하고 하나로 모으려는 모습은 ENFJ의 설득력과 리더십을 잘 보여줍니다. 이상을 향해 나아가는 ENFJ에게 깊은 공감을 불러일으킬 것입니다."},
                {"title": "Hidden Figures (2016) 👩‍🔬",
                 "description": "NASA의 숨겨진 영웅들이 인종 차별과 성 차별을 극복하고 우주 경쟁을 승리로 이끈 감동적인 실화입니다.",
                 "relevance": "ENFJ는 다른 사람의 잠재력을 보고 이들을 이끌어 성장시키는 것을 중요하게 생각합니다. 이 영화의 주인공들이 자신의 역량을 발휘하고, 주변 사람들에게 긍정적인 영향을 주며 함께 목표를 달성하는 모습은 ENFJ의 리더십과 포용력을 잘 드러냅니다. 사회적 변화를 이끌고 타인을 돕는 것에 보람을 느끼는 ENFJ에게 큰 영감을 줄 것입니다."},
                {"title": "Dead Poets Society (1989) 📚",
                 "description": "전통적인 학교에 부임한 자유로운 영혼의 영문학 선생님이 학생들에게 삶의 새로운 의미를 가르치는 이야기입니다.",
                 "relevance": "ENFJ는 타인의 잠재력을 발견하고 그들을 이끌어 성장시키는 것에 큰 보람을 느낍니다. 키팅 선생이 학생들에게 시와 자유로운 사고를 가르치며 긍정적인 변화를 이끌어내는 모습은 ENFJ의 리더십과 따뜻한 영향력을 보여줍니다. 젊은이들에게 영감을 주고 비전을 제시하는 것에 공감을 느낄 것입니다."}
            ],
            "good_combinations": [
                {"type": "INFP", "reason": "ENFJ의 따뜻하고 지지적인 성향과 INFP의 감성적인 깊이가 만나 영화에 대한 감정을 풍부하게 공유하고 서로에게 긍정적인 영향을 줄 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Life of Pi (2012) 🐅", "description": "난파선에서 홀로 남은 소년과 호랑이의 생존기를 다룬 철학적인 모험 영화."},
                     {"title": "Inside Out (2015) 😊", "description": "인간의 감정을 의인화하여 보여주는 애니메이션 영화로, 복잡한 내면 세계를 탐구합니다."}
                 ]},
                {"type": "ESFJ", "reason": "비슷하게 사교적이고 협력적인 성향으로 영화 감상 후 활발한 대화를 나누며 즐거움을 배가시킬 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "Remember the Titans (2000) 🏈", "description": "인종 차별이 심했던 시기에 통합 미식축구팀을 이끌며 역경을 극복하는 감동 실화."},
                     {"title": "The Help (2011) 🏡", "description": "1960년대 미국 남부 흑인 가정부들의 이야기를 다룬 영화로, 사회적 약자의 목소리를 담았습니다."}
                 ]}
            ]
        },
        "ENTJ": {
            "summary": "논리적이고 단호하며, 리더십이 강하고 전략적인 유형입니다. 목표 지향적이고 효율성을 중시하며, 문제를 해결하고 조직을 이끄는 데 능숙합니다. 비전을 제시하고, 이를 현실로 만들기 위해 강력하게 추진합니다. 도전적이고 성취감을 주는 여행을 선호합니다.",
            "movies": [
                {"title": "Oppenheimer (2023) 💣",
                 "description": "원자폭탄 개발을 주도한 과학자의 복잡한 내면과 윤리적 고민을 다룬 영화입니다.",
                 "relevance": "ENTJ는 명확한 목표를 설정하고, 이를 달성하기 위한 효율적인 전략을 수립하는 데 탁월합니다. 오펜하이머가 거대한 프로젝트를 주도하고, 복잡한 과학적 난제를 해결하며 팀을 이끄는 모습은 ENTJ의 강력한 리더십과 추진력을 잘 보여줍니다. 비판적 사고와 결단력을 가진 ENTJ에게 깊은 통찰을 제공할 것입니다."},
                {"title": "The Imitation Game (2014) 💻",
                 "description": "암호 해독가 앨런 튜링의 삶과 그의 천재성을 그린 영화입니다.",
                 "relevance": "ENTJ는 목표 지향적이며, 도전을 두려워하지 않고 문제를 해결하는 데 집중합니다. 앨런 튜링이 암호 해독이라는 거대한 목표를 향해 끊임없이 노력하고, 자신의 비전을 관철시키기 위해 논리적으로 설득하는 모습은 ENTJ의 강력한 추진력과 전략적 사고를 잘 보여줍니다. 효율성을 중시하고 결과를 만들어내는 ENTJ에게 특히 인상 깊은 영화입니다."},
                {"title": "Arrival (2016) 👽",
                 "description": "외계 언어를 통해 인류의 운명을 바꾸는 과정을 그린 SF 영화입니다.",
                 "relevance": "ENTJ는 복잡한 문제를 분석하고 해결책을 제시하는 데 능숙합니다. 외계 언어를 해독하고 인류의 미래를 결정하는 과정은 ENTJ의 전략적 사고와 단호한 결단력을 자극합니다. 미지의 상황에서도 논리적으로 접근하여 목표를 달성하려는 ENTJ에게 깊은 흥미를 줄 것입니다."}
            ],
            "good_combinations": [
                {"type": "INTP", "reason": "ENTJ의 리더십과 INTP의 깊은 분석력이 결합하여 영화의 복잡한 주제나 숨겨진 의미에 대해 심도 있는 토론을 할 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "The Social Network (2010) 💻", "description": "페이스북의 탄생과정과 그 이면에 숨겨진 창립자들의 갈등을 다룬 영화."},
                     {"title": "Steve Jobs (2015) 🍎", "description": "스티브 잡스의 세 가지 주요 프레젠테이션 뒤편의 이야기를 다룬 전기 영화."}
                 ]},
                {"type": "ESTJ", "reason": "비슷하게 목표 지향적이고 효율성을 중시하는 성향으로 영화의 전개나 전략적 요소에 대해 깊이 공감하며 활발한 대화를 나눌 수 있습니다.",
                 "combination_movie_recommendations": [
                     {"title": "The Big Short (2015) 💰", "description": "2008년 금융 위기를 예측하고 월스트리트에 맞서 성공을 거둔 사람들의 이야기."},
                     {"title": "Margin Call (2011) 📉", "description": "글로벌 금융 위기 직전, 거대 투자은행에서 벌어지는 24시간을 그린 스릴러 영화."}
                 ]}
            ]
        }
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
        st.subheader(f"✨ {selected_mbti} 유형을 위한 맞춤 추천 🍿")

        # 선택된 MBTI 유형에 대한 정보 가져오기
        mbti_info = mbti_recommendations_full.get(selected_mbti, {})

        if mbti_info:
            # MBTI 유형 요약 설명
            st.markdown(f"### {selected_mbti} 유형은... 💡")
            st.info(mbti_info["summary"])
            st.markdown("---")

            # 추천 영화 목록 표시 (가로로 나열)
            st.markdown("### 추천 영화와 그 이유 🎬")
            
            # 각 영화를 2개의 컬럼으로 나누어 표시
            num_movies = len(mbti_info["movies"])
            cols = st.columns(2) # 2개의 컬럼 생성

            for i, movie in enumerate(mbti_info["movies"]):
                with cols[i % 2]: # 현재 영화를 해당 컬럼에 배치 (0, 1, 0, 1 순으로 반복)
                    st.write(f"##### {movie['title']}") # 영화 제목
                    # Placehold.co를 사용하여 플레이스홀더 이미지 생성
                    st.image(f"https://placehold.co/300x450/000000/FFFFFF?text={movie['title'].split('(')[0].strip().replace(' ', '+')}%0APoster",
                             caption=f"{movie['title'].split('(')[0].strip()} 영화 포스터", # 포스터 이미지 설명
                             width=150) # 이미지 너비 조정
                    st.markdown(f"**설명:** {movie['description']}") # 영화 설명
                    st.success(f"**이 유형에 추천하는 이유:** {movie['relevance']}") # 영화 관련성
                    
                    # 리뷰 영상 검색 링크 추가
                    movie_search_query = movie['title'].split('(')[0].strip().replace(' ', '+')
                    youtube_link = f"https://www.youtube.com/results?search_query={movie_search_query}+영화리뷰"
                    st.markdown(f"[🎥 **리뷰 영상**]({youtube_link})")
                    st.markdown("<hr style='border:1px solid #f0f2f6'>", unsafe_allow_html=True) # 가벼운 구분선

            # 함께 영화 보기에 좋은 MBTI 조합 추천
            if "good_combinations" in mbti_info and mbti_info["good_combinations"]:
                st.markdown("---")
                st.subheader(f"🤝 {selected_mbti} 유형과 함께 영화 보기에 좋은 MBTI 조합 🍿")
                st.markdown("이 유형들과 함께 영화를 보면 더욱 즐거운 감상 경험을 할 수 있어요!")
                for combo in mbti_info["good_combinations"]:
                    st.write(f"**{combo['type']}**: {combo['reason']}")
                    if "combination_movie_recommendations" in combo and combo["combination_movie_recommendations"]:
                        st.markdown(f"**두 분께 추천하는 영화:**")
                        
                        # 조합 추천 영화도 2개의 컬럼으로 나누어 표시
                        combo_movies = combo["combination_movie_recommendations"]
                        combo_cols = st.columns(2) # 2개의 컬럼 생성
                        for j, combo_movie in enumerate(combo_movies):
                            with combo_cols[j % 2]: # 현재 조합 영화를 해당 컬럼에 배치
                                st.write(f"###### {combo_movie['title']}")
                                # Placehold.co를 사용하여 플레이스홀더 이미지 생성
                                st.image(f"https://placehold.co/300x450/000000/FFFFFF?text={combo_movie['title'].split('(')[0].strip().replace(' ', '+')}%0APoster",
                                         caption=f"{combo_movie['title'].split('(')[0].strip()} 영화 포스터",
                                         width=100) # 이미지 너비 조정
                                st.write(f"{combo_movie['description']}")
                                combo_movie_search_query = combo_movie['title'].split('(')[0].strip().replace(' ', '+')
                                combo_youtube_link = f"https://www.youtube.com/results?search_query={combo_movie_search_query}+영화리뷰"
                                st.markdown(f"[🎥 **리뷰 영상**]({combo_youtube_link})")
                                st.markdown("<hr style='border:0.5px solid #f0f2f6'>", unsafe_allow_html=True) # 더 가벼운 구분선
                    st.markdown("---") # 각 조합 사이에 구분선
            else:
                st.info(f"{selected_mbti} 유형과 함께 영화 보기에 좋은 특정 MBTI 조합 정보가 아직 없습니다. 😅")

        else:
            # 추천 영화가 없을 경우 경고 메시지를 표시합니다.
            st.warning("선택하신 MBTI 유형에 대한 추천 영화가 아직 없습니다. 다른 유형을 선택해주세요! 😅")

    # 앱의 하단에 작은 메시지를 추가합니다.
    st.markdown("Made with ❤️ and Streamlit")

# Streamlit 앱을 실행하는 부분입니다.
if __name__ == "__main__":
    main()
