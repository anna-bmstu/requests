# requests
Requests library, API VK

Клиент к API VK, который считает распределение возрастов друзей для указанного пользователя. 
В функцию calc_age передается username или user_id пользователя, она возвращает список пар (возраст, количество друзей с таким возрастом).
Список отсортирован по убыванию по второму ключу (количество друзей) и по возрастанию по первому ключу (возраст).