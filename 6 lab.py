import requests
import re

# https://jsonplaceholder.typicode.com/posts

#Задание 1
print('Задание 1')
def get_posts(user_id):
    url = f"https://jsonplaceholder.typicode.com/posts?userId={user_id}"
    response = requests.get(url)
    posts = response.json()
    print("Первые 5 заголовков постов:")
    for post in posts[:5]:
        print(post["title"])

get_posts(1)

#Задание 2
print('Задание 2')
def get_posts_all():
    url = 'https://jsonplaceholder.typicode.com/comments'
    response = requests.get(url)
    if response.status_code == 200:
        comments = response.json()
        for comment in comments:
            print(comment['email'])
    else:
        print('Ошибка при запросе.')

get_posts_all()

#Задание 3
def create_post(title, body, user_id):
    url = 'https://jsonplaceholder.typicode.com/posts'
    new_post = {
        'title': title,
        'body': body,
        'userId': user_id
    }
    response = requests.post(url, json=new_post)
    if response.status_code == 201:
        print(f'Пост создан: {response.json()}')
    else:
        print('Ошибка при создании поста.')

create_post('Новый пост', 'Это содержимое нового поста', 1)

#Задание 4
print('Задание 4')
def update_post_put(post_id, title, body):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    updated_post = {
        'title': title,
        'body': body
    }
    response = requests.put(url, json=updated_post)
    if response.status_code == 200:
        print(f'Пост обновлен (PUT): {response.json()}')
    else:
        print('Ошибка при обновлении поста.')

def update_post_patch(post_id, title):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    updated_post = {'title': title}
    response = requests.patch(url, json=updated_post)
    if response.status_code == 200:
        print(f'Пост обновлен (PATCH): {response.json()}')
    else:
        print('Ошибка при обновлении поста.')

update_post_put(1, 'Обновленный заголовок', 'Новое содержимое поста')
update_post_patch(1, 'Обновленный только заголовок')

#Задание 5
print('Задание 5')
import re

def post_filtered(word):
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        pattern = re.compile(r'\b' + re.escape(word) + r'\b', re.IGNORECASE)
        for post in posts:
            if pattern.search(post['title']) and pattern.search(post['body']):
                print(f'Пост с совпадением: {post["title"]}')
    else:
        print('Ошибка при запросе.')

post_filtered('qui')

#Задание 6
print('Задание 6')
def delete_post(post_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    response = requests.delete(url)
    if response.status_code == 200:
        print(f'Пост с ID {post_id} удален.')
    else:
        print('Ошибка при удалении поста.')

delete_post(1)

