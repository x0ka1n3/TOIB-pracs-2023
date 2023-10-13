## Практическая работа №2
# Идентификация и аутентификация

# Создание пользователя super-{ФИО} с наделением правами суперпользователя

![Создание юзера с помощью useradd](https://github.com/x0ka1n3/TOIB-pracs-2023/blob/main/Prac2/assets/1.png)

# Вход под именем созданного юзера; создание группы group-{группа}

![su username; groupadd group-{группа}](https://github.com/x0ka1n3/TOIB-pracs-2023/blob/main/Prac2/assets/2.png)

# Добавление юзера super-{ФИО} в группу group-{группа}; проверка добавления юзера в группу

![usermod -G group-{группа} super-{ФИО}; sudo -u super-{ФИО} groups](https://github.com/x0ka1n3/TOIB-pracs-2023/blob/main/Prac2/assets/3.png)

# Создание юзера user-{ФИО}

![useradd -m -s /bin/bash user-{ФИО}](https://github.com/x0ka1n3/TOIB-pracs-2023/blob/main/Prac2/assets/4.png)

# Добавление юзера user-{ФИО} в группу group-{группа}

![usermod -G group-{группа} user-{ФИО}](https://github.com/x0ka1n3/TOIB-pracs-2023/blob/main/Prac2/assets/5.png)

# Наделение пользователя user-{ФИО} доступом на RW в директории super-{ФИО}

![setfacl -m u:user-{ФИО}:rwx /home/super-{ФИО}](https://github.com/x0ka1n3/TOIB-pracs-2023/blob/main/Prac2/assets/6.png)

# Проверка доступа

![su user-{ФИО}; ls /home/super-{ФИО}](https://github.com/x0ka1n3/TOIB-pracs-2023/blob/main/Prac2/assets/7.png)