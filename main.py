prompts = [
    {
        "title": "노코드 자동화 워크플로우 설계",
        "content": "업무 목표와 입력 및 출력 데이터를 분석하여 Make 또는 Activepieces를 활용한 효율적인 자동화 워크플로우를 설계해줘.",
        "category": "자동화",
        "favorite": False
    },
    {
        "title": "영어 문장 첨삭 및 문법 설명",
        "content": "입력한 영어 문장을 자연스럽고 정확하게 교정하고, 수정한 이유를 문법과 표현 측면에서 이해하기 쉽게 설명해줘.",
        "category": "텍스트 생성",
        "favorite": False
    },
    {
        "title": "프레젠테이션 제작",
        "content": "주어진 자료를 발표 흐름에 맞게 구조화하고, 슬라이드별 제목과 핵심 내용 및 적절한 시각자료를 제안해줘.",
        "category": "텍스트 생성",
        "favorite": False
    }
]
def show_menu():
    print("=== 나만의 프롬프트 관리 ===")
    print("1. 프롬프트 추가")
    print("2. 프롬프트 목록")
    print("3. 카테고리별 조회")
    print("4. 프롬프트 검색")
    print("5. 프롬프트 상세 보기")
    print("6. 즐겨찾기 관리")
    print("7. 즐겨찾기 목록")
    print("0. 종료")


while True:
    show_menu()
    choice = input("선택: ")

    if choice == "0":
        print("프로그램을 종료합니다.")
        break

    elif choice in ["1", "2", "3", "4", "5", "6", "7"]:
        print("선택한 번호:", choice)

    else:
        print("잘못된 번호입니다. 다시 선택해주세요.")