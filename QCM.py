questions = [
    {
        "question": "Quel est le capital de France?",
        "choices": ["Paris", "Londres", "Berlin", "Rome"],
        "correct": "Paris"
    },
    {
        "question": "Quel est le plus grand pays du monde?",
        "choices": ["Etats-Unis", "Chine", "Russie", "Canadà"],
        "correct": "Russie"
    },
    {
        "question": "Quel est le plus petit pays du monde?",
        "choices": ["Vatican", "Monaco", "Nauru", "Tuvalu"],
        "correct": "Vatican"
    },
    {
        "question": "Comment je m'appelle ?",
        "choices": ["Tacos", "Elon Musk", "Jean", "Macron"],
        "correct": "Elon Musk"
    },
    {
        "question": "Qui a écrit Les Miserables?",
        "choices": ["Victor Hugo", "Alexandre Dumas", "Emile Zola", "Gustave Flaubert"],
        "correct": "Victor Hugo"
    },
    {
        "question": "Quel est le plus grand océan du monde?",
        "choices": ["Atlantique", "Pacifique", "Indien", "Arctique"],
        "correct": "Pacifique"
    }
]
while True:
    score = 0
    for question in questions:
        print(question["question"])
        for i, choice in enumerate(question["choices"]):
            print(f"{i + 1}. {choice}")
        answer = input("Entrez le numéro de votre réponse : ")
        if question["choices"][int(answer) - 1] == question["correct"]:
            print("\033[32mBonne réponse!\033[0m")
            score += 1
        else:
            print("\033[91mMauvaise réponse.\033[0m")

    print(f"Votre score est de {score} sur {len(questions)}.")
    if input("Voulez-vous rejouer? (oui/non)").lower() == "non":
        break

