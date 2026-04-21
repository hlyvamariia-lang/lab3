# Списки для збереження всіх хештегів
all_hashtags = []

# Отримання текстів від користувача
num_posts = int(input("Введіть кількість постів: "))

for i in range(num_posts):
    post = input(f"Введіть пост {i + 1}: ")

    # Знаходимо всі слова що починаються з #
    words = post.split()
    for word in words:
        if word.startswith('#'):
            # Очищаємо від розділових знаків і переводимо в нижній регістр
            hashtag = word.lower().rstrip('.,!?')
            all_hashtags.append(hashtag)

# Аналіз хештегів
print("\nРезультати аналізу:")

if not all_hashtags:
    print("Хештегів не знайдено!")
else:
    # Підраховуємо кількість кожного хештегу
    hashtag_count = {}
    for tag in all_hashtags:
        hashtag_count[tag] = hashtag_count.get(tag, 0) + 1

    # Сортуємо за популярністю
    sorted_hashtags = sorted(hashtag_count.items(), key=lambda x: x[1], reverse=True)

    print(f"Всього хештегів знайдено: {len(all_hashtags)}")
    print(f"Унікальних хештегів: {len(hashtag_count)}")
    print(f"\nНайпопулярніший хештег: {sorted_hashtags[0][0]} ({sorted_hashtags[0][1]} раз)")

    print("\nТоп хештегів:")
    for i, (tag, count) in enumerate(sorted_hashtags[:3], 1):
        print(f"  {i}. {tag} — {count} раз")