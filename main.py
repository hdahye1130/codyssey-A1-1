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
categories = [
    "텍스트 생성",
    "이미지 생성",
    "영상 생성",
    "페르소나",
    "자동화",
    "기타"
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

def add_prompt():
    print("=== 프롬프트 추가 ===")

    while True:
        title = input("제목: ").strip()
        if title:
            break
        print("제목은 비워둘 수 없습니다.")

    while True:
        content = input("내용: ").strip()
        if content:
            break
        print("내용은 비워둘 수 없습니다.")

    while True:
        print("\n카테고리 선택:")

        for index, category in enumerate(categories, start=1):
            print(f"{index}) {category}")

        print("7) 직접 입력")

        category_choice = input("선택: ").strip()

        if category_choice in ["1", "2", "3", "4", "5", "6"]:
            category = categories[int(category_choice) - 1]
            break

        elif category_choice == "7":
            category = input("카테고리 직접 입력: ").strip()

            if category:
                break

            print("카테고리는 비워둘 수 없습니다.")

        else:
            print("잘못된 선택입니다. 다시 선택해주세요.")

    new_prompt = {
        "title": title,
        "content": content,
        "category": category,
        "favorite": False
    }

    prompts.append(new_prompt)

    print("프롬프트가 추가되었습니다!")
  
def show_list():
    print("=== 프롬프트 목록 ===")

    if not prompts:
        print("등록된 프롬프트가 없습니다.")
        return

    for index, prompt in enumerate(prompts, start=1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f'{index}. [{prompt["category"]}] {prompt["title"]}{star}')

    print(f"\n총 {len(prompts)}개의 프롬프트")

def show_by_category():
    print("=== 카테고리별 조회 ===")

    for index, category in enumerate(categories, start=1):
        print(f"{index}) {category}")

    category_choice = input("선택: ").strip()

    if category_choice not in ["1", "2", "3", "4", "5", "6"]:
        print("잘못된 선택입니다.")
        return

    selected_category = categories[int(category_choice) - 1]

    filtered_prompts = []

    for prompt in prompts:
        if prompt["category"] == selected_category:
            filtered_prompts.append(prompt)

    if not filtered_prompts:
        print(f"[{selected_category}] 카테고리에 등록된 프롬프트가 없습니다.")
        return

    print(f"\n[{selected_category}] 카테고리 프롬프트:")

    for index, prompt in enumerate(filtered_prompts, start=1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f'{index}. {prompt["title"]}{star}')

    print(f"\n총 {len(filtered_prompts)}개의 프롬프트")

def search_prompt():
    print("=== 프롬프트 검색 ===")

    keyword = input("검색어: ").strip()

    if not keyword:
        print("검색어를 입력해주세요.")
        return

    results = []

    for prompt in prompts:
        if keyword.lower() in prompt["title"].lower() or keyword.lower() in prompt["content"].lower():
            results.append(prompt)

    if not results:
        print("검색 결과가 없습니다.")
        return

    print("\n검색 결과:")

    for index, prompt in enumerate(results, start=1):
        star = " ⭐" if prompt["favorite"] else ""
        print(f'{index}. [{prompt["category"]}] {prompt["title"]}{star}')

    print(f"\n{len(results)}개의 프롬프트를 찾았습니다.")

while True:
    show_menu()
    choice = input("선택: ")

    if choice == "0":
        print("프로그램을 종료합니다.")
        break

    elif choice == "1":
        add_prompt()

    elif choice == "2":
        show_list()

    elif choice == "3":
        show_by_category()

    elif choice == "4":
        search_prompt()

    elif choice in ["5", "6", "7"]:
        print("아직 구현되지 않은 기능입니다.")

    else:
        print("잘못된 번호입니다. 다시 선택해주세요.")

