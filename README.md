# booking_rooms
# django приложение для бронирования аудиторий(любых других помещений)

Модели:
1) Аудитория (её название; вместительность)
2) Запись в расписании (аудитория,которую бронируют;время, на которе бронируют(начало и конец периода))
3) Пользовател

План работы:
1) Админ создаёт аудитории, которые записываются в базу данных.
2) Хорошо было бы написать процесс регистрации пользователей, но пока можно создавать их через админку.
3) Пользователь заходит в систему под своим логином.
4) Пользователь может по параметрам аудитории и времени, на которое он хочет её забронировать, посмотреть рекомендации по выбору аудитории.
5) Пользователь может создать запись в расписание, если выбранная аудитория не занята в этот период времени.


P.S.В процессе создания столкнулся с проблемой создания(входа в систему) пользователей.Из-за этого в проекте пока реализованы только модели аудиторий и расписания и функции с ними. В дальнешем планируется создать форнтенд для проекта и реализовать модель пользователя и все её методы.
