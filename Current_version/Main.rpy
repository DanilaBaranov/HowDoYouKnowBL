init:
    $ mods ["goodname"] = "Как хорошо ты знаешь Бесконечное Лето?"
    $ dissolveVF = Dissolve(0.1)
    $ count = 0
    
label goodname:
    scene bg int_bus
    show unblink
    th "Я проснулся от бившего в глаза солнечного света." 
    show blinking
    play music music_list["raindrops"] fadein 5
    "Проморгался, и начал осматриваться. Кресла, узкий проход…"
    th "Автобус! {w}Неужели получилось!? {w}От радости чуть не заорал, но вовремя одернул себя. Мне все-таки 19 лет, уже взрослый для такого проявления эмоций."
    stop music fadeout 5
    th "И все же это правда, мне обещали день в Совенке, и похоже я его получил. {w}Ну, тогда не будем терять ни минуты!"
    
    play music music_list["forest_maiden"] fadein 5
    scene bg ext_camp_entrance_day with dissolve
    "Пулей вылетел из автобуса и помчался к воротам, и чуть не сбил выходившую оттуда Славю. {w}Ну а кто же еще, все по канону."
    show sl smile pioneer at center with dissolve_fast
    sl "Привет. Ты оттуда, да? На один день?"
    me "Да. Привет,Славя."
    "Она даже не удивилась, что я знаю ее имя. {w}Хотя, я же явно не первый турист, далеко не первый. {w}Сколько ж тут народу уже побывало до меня?"
    "Из раздумий меня вывела Славя"
    sl "Ну так что, пойдем? Остальные девочки уже ждут."
    me "А,да. Пойдем. Замечтался немного."
    "С глупой улыбкой проронил я."
    show sl smile pioneer at center with dspr
    "Славя улыбнулась."
    sl "Понимаю. Многие так стоят в первые минуты. Я уже привыкла."
    
    scene bg ext_clubs_day with dissolve 
    stop music fadeout 5
    "Прошел за Славей в ворота. {w}В далеке начали появляться здания кружков, возле которых стояли две выделяющихся рыжих фигуры."
    play music music_list["so_good_to_be_careless"] fadein 5
    show dv normal pioneer far at fleft with dissolve_fast
    show us grin sport far at fright with dspr
    th "Даа, ну и тандем, их же нельзя вместе ставить." 
    show dv normal pioneer at fleft with dissolve_fast
    show us grin sport at fright with dspr
    th "Если сколлапсируют, Совенок на воздух взлетит. {w}Только обрывки мешков из под сахара будут медленно опускаться вниз."
    show dv grin pioneer close at fleft with dissolve_fast
    show us grin sport at fright with dspr
    "Когда до огненного дуэта оставалось всего пару шагов, я заметил, что Ульянка что-то держит за спиной и хитро улыбается, а Алиса с интересом переводит взгляд с меня на подругу и обратно."
    "Ну, тут не надо быть заядлым игроком, чтобы понять, что она задумала."
    "Я, хитро прищурившись, посмотрел на девочку. {w}В эту игру могут играть двое! {w}Пусть Улька и является моим любимым героем, но так глупо я не собирался поступать."
    me "Ульяна, даже не думай! Меня этим не возьмешь."
    show us sad sport at fright with dissolve_fast
    "Девочка вмиг поникла"
    us "Ну вот. {w}Сколько уже таких как вы тут побывало, а срабатывает лишь на единицах. {w}Мог бы и подыграть девушке!"
    show dv smile pioneer close at fleft with dissolve_fast
    "Алиса прищурившись, как бы оценивая, посмотрела на меня"
    dv "А ты неплох. {w}Не красавец конечно, но и в кусты от тебя прятаться, желания нету."
    me "И тебе привет, Алиса. {w}Ты как всегда в своем репертуаре."
    th "Похоже мой комплимент пришелся ей по вкусу"
    "Может быть мы и дальше продолжили этот словесный бой, но Славя решила пресечь его на стадии зарождения."
    show sl serious pioneer close at center with dissolve_fast
    show us normal sport far at fright with dspr
    show dv normal pioneer far at fleft with dspr
    stop music fadeout 5
    sl "Так, давайте уже начнем, а то и так времени не очень много. Всего день у парня."
    play music music_list["two_glasses_of_melancholy"] fadein 5
    me "А.. Что начнем?"
    show sl smile2 pioneer close at center with dissolve_fast
    sl "Мы с недавнего времени решили организовать для новоприбывших викторину по вселенной Бесконечного Лета. {w}И ты будешь лишь третьим человеком, который попал под новый формат"
    th "Не то чтобы мне не понравилась такая идея, еще и третьим из всех буду, но я хотел просто прогуляться по лагерю, поиграть в футбол с Ульянкой, может выпить с Алисой, зайти в библиотеку позлить Женю. {w}Ну а в принцпипе теперь у меня нет выбора."
    show us grin sport at fright with dissolve_fast
    show sl smile2 pioneer far at center with dspr
    us "Даа. Посмотрим, как ты внимательно читал."
    "Ухмыльнулась Ульянка"
    show sl serious pioneer close at center with dissolve_fast
    "Славя с недовольством посмотрела на вмешавшуюся девочку, но промолчала и продолжила."
    show us normal sport far at fright with dissolve_fast
    sl "Ну вот. У нас есть три станции, три уровня сложности соответственно."
    sl "Первый, самый легкий, здесь, в кружке кибернетиков. {w}Заведуют Алиса с Ульяной. Если повезет, внутри познакомишься и с парнями, но они в последнее время что-то мастерят в старом лагере и редко здесь появляются."
    th "Оно и к лучшему. {w}Я сюда не ради пары безумных кибернетиков старался попасть"
    "Славя продолжила"
    sl "Вторая станция находится в Библиотеке. Там за главных Лена и Женя. {w}Там средний уровень сложности. Только если не уверен, лучше не испытывай судьбу."
    th "Меня подобное заявление заинтриговало"
    me "Это почему? За неправильные ответы дежурить заставят?"
    show us grin sport at fright with dissolve_fast
    show dv grin pioneer at fleft with dspr
    show sl laugh pioneer close at center with dspr
    "Славя засмеялась, а Алиса с Ульяной синхронно ухмыльнулись."
    show dv grin pioneer close at fleft with dissolve_fast
    show sl laugh pioneer at center with dspr
    dv "Нет, просто Женя очень бесится, когда отвечаешь неправильно. {w}Не дай бог у нее еще и настроение плохое. {w}Из лагеря уже не вернешься. {w}По крайней мере целым."
    th "Что ж. Очень на нее похоже. Ладно, буду начеку."
    me "Ладно, спасибо за наводку. {w}А на третьей станции кто?"
    show us normal sport at fright with dissolve_fast
    show dv grin pioneer at fleft with dspr
    show sl normal pioneer close at center with dspr
    sl "На третьей Мику с Юлей. Обитают в музклубе. Там уже серьезные вопросы. {w}Не только по сюжету и деталям, а уже и по околоигровой теме, про разработчиков, игровые файлы и прочее."
    "Славя на пару секунд замолчала, чтобы перевести дух."
    sl "Теперь в общем: на каждой станции по 15 вопросов. {w}Количество попыток неограничено, можешь пытаться снова и снова. {w}В конце девочки будут говорить тебе количество правильных ответов, но не скажут, в каких ошибки, мы посчитали такую меру неинтересной. {w}Все понял?"
    th "Вроде бы ничего сложного, и все равно моему процессору понадобилось пару десятков секунд, чтобы все уяснить до конца."
    "Наконец я сказал:"
    me "Так точно! Разрешите приступить."
    sl "Разрешаю."
    th "Так. С чего бы начать?"
    stop music fadeout 5
    jump map
    
label map:
    $ disable_all_zones() 
    $ set_zone ("clubs", "clubs")
    $ set_zone ("library", "library")
    $ set_zone ("music_club", "music_club")
    $ set_zone ("camp_entrance", "label_end")
    $ show_map()

label map:
    $ disable_all_zones() 
    $ set_zone ("clubs", "clubs")
    $ set_zone ("library", "library")
    $ set_zone ("music_club", "music_club")
    $ set_zone ("camp_entrance", "label_end")
    $ show_map()
    
label clubs:
    if count > 0:
        $ count = 0
    play music music_list["memories"] fadein 3
    scene bg ext_clubs_day with dissolve 
    th "Пожалуй простые вопросы-самое то для меня сейчас.{w} Ну что, огненная команда, я иду!"
    scene bg int_clubs_male_day with dissolve
    "Зашел в клуб кибернетиков."
    show dv grin pioneer2 at right with dspr
    show us smile sport at left with dspr
    th "Хаос, беспорядок. Все как всегда."
    us "Ну что, готов? {w} Поехали!"
    us "Первый вопрос:{w} Назови количество концовок в игре."
    menu:
        "10":
            $ count += 0
        "5":
            $ count += 0
        "8":
            $ count += 0
        "13":
            $ count += 1
    
    dv "Следующий вопрос: {w} У какого из перечисленных персонажей нет концовки в оригинальной игре?"
    menu:
        "Мику":
            $ count += 0
        "Женя":
            $ count += 1
        "Ульяна":
            $ count += 0
        "Алиса":
            $ count += 0
            
    dv "Следующий: {w} С кем нельзя пойти в старый лагерь, на поиски Шурика?"
    menu:
        "Мику":
            $ count += 1
        "Славя":
            $ count += 0
        "Лена":
            $ count += 0
        "Алиса":
            $ count += 0
            
    us "Еще один вопросик: {w} Что подарила Славя Семену на острове, во время сбора земляники?"
    menu:
        "Венок":
            $ count += 0
        "Поцелуй":
            $ count += 0
        "Фотографию":
            $ count += 0
        "Платок":
            $ count += 1
            
    dv "Следующий: {w} Как, по его словам, называет Электроника Ульяна?"
    menu:
        "Киборг":
            $ count += 0
        "Серёжка":
            $ count += 0
        "Сыроежка":
            $ count += 1
        "Винтик":
            $ count += 0
            
    dv "Шестой вопрос: {w} Как назвала Ульяна Семена в первый день?"   
    menu:
        "Скучный дед":
            $ count += 0
        "Гроза Педобиров":
            $ count += 0
        "Голодающий Поволжья ":
            $ count += 1
        "Гражданин начальник":
            $ count += 0
    
    dv "Идём дальше. {w} По какой причине в плохой концовке Ульяны Семен ехал в автобусе один?"
    menu:
        "Она опоздала на автобус":
            $ count += 0
        "Она осталась в лагере, в качестве наказания":
            $ count += 1
        "Ее забрали родители":
            $ count += 0
        "Ульяна отсела от него":
            $ count += 0

    us "И еще один: {w}Альтернативное имя Электроника в Мику-Руте."
    menu:
        "Винтик":
            $ count += 0
        "Роутер":
            $ count += 1
        "Модем":
            $ count += 0
        "Сыроежка":
            $ count += 0

    us "Девятый уже: {w} Что забрала с собой Юля из лагеря?"
    menu:
        "Мешок с запасами":
            $ count += 1
        "Мешок с сахаром":
            $ count += 0
        "Украденные у пионеров вещи":
            $ count += 0
        "Ничего":
            $ count += 0

    dv "Вот еще про Юлю: {w} Зачем она посыпала грибы сахаром?"
    menu:
        "Просто так":
            $ count += 0
        "Ей так сказали":
            $ count += 0
        "Чтобы лучше росли":
            $ count += 1
        "Чтобы были вкуснее":
            $ count += 0
    
    us "А вот про Мику: {w} Чем больше всего выделялась Мику для Семена?"
    menu:
        "Цветом волос":
            $ count += 0
        "Длинными волосами":
            $ count += 0
        "Излишней болтливостью ":
            $ count += 1
        "Красотой":
            $ count += 0
    
    us "А где у нас в лагере находится мука, знаешь?"
    menu:
        "Столовая":
            $ count += 0
        "Клуб Кибернетики":
            $ count += 0
        "Склад":
            $ count += 0
        "Библиотека":
            $ count += 1
    
    us "А теперь ответь ка мне, зачем кибернетики хранят у себя в клубе водку?"
    menu:
        "Протирать оптику":
            $ count += 1
        "Дезинфицировать раны":
            $ count += 0
        "Пить":
            $ count += 0
        "Прячут от Алисы":
            $ count += 0
    
    dv "«Челюсть с пола подними»-кому принадлежит эта фраза?"
    menu:
        "Алиса":
            $ count += 1
        "Ульяна":
            $ count += 0
        "Шурик":
            $ count += 0
        "Пионер":
            $ count += 0
    
    us "Последний вопрос: {w} Кто такой Пионер?"
    menu:
        "Перевоплощение Юли":
            $ count += 0
        "Дух Лагеря":
            $ count += 0
        "Обычный пионер":
            $ count += 0
        "Сошедшая с ума копия Семена":
            $ count += 1
            
    if count == 0:
        dv "Ты не ответил ни на один вопрос верно. {w}Все-таки я ошиблась насчет тебя! {w}Иди перепройди игру пару раз и возвращайся. Стыдно должно быть!"
    
    if count == 1:
        us "Всего лишь один правильный ответ. {w}Ты почти безнадежен. {w}Попробуй снова, может что-то еще и получится"
    
    if count == 2:
        dv "Два верных ответа. {w}Ты зачем вообще приехал сюда? Вопросы же легкие. {w}Ну попробуй еще раз конечно, может что-то в голове еще зашевелится."
    
    if count == 3:
        us "Три попадания. {w}Бог любит троицу, конечно, но результат то детский. {w}Я и то больше бы ответила."
    
    if count == 4:
        dv "Четыре верных. {w}Ну, {w}такое ощущение, что ты только один рут прошел, и фанатом себя возомнил."
    
    if count == 5:
        us "Пять из пятнадцати! {w}На треть справился, но все равно отстой."
    
    if count == 6:
        dv "Шесть попаданий. {w}Плохой из тебя стрелок, однако."
    
    if count == 7:
        us "Семь верных ответов. {w}Почти половину осилил. {w}Ну, неплохо, но фанатом тебя пока назвать трудно."
    
    if count == 8:
        dv "Восемь из пятнадцати. {w}Еле половину перевалил. Ну что ж, неплохо, ты из себя что-то да представляешь."
    
    if count == 9:
        us "Девять! Видимо, ты что-то да знаешь. {w}Может еще разок, глядишь еще пару наугад правильно выберешь?"
    
    if count == 10:
        dv "Две трети тебе поддались. {w}Скажи честно, наугад же отвечал."
    
    if count == 11:
        us "Ты правильно ответил на целых одиннадцать вопросов. {w}Можно сказать, что ты уже не новичок, но и звание знатока тебе пока рано носить."    
    
    if count == 12:
        dv "Надо же. Всего три промаха. {w}Ты перестаешь меня бесить. Так держать!"
    
    if count == 13:
        us "Ну ты даешь, всего два неверных ответа. {w}Не думала, что ты такой умный."
    
    if count == 14:
        dv "Эх, дурень. {w}Всего один неверный. {w}Не мог уже дотянуть что ли? {w}Ладно, не обижайся. Молодец!"
    
    if count == 15:
        us "Всё верно! Но ты же сжульничал, признавайся!" 
        
    th "Так. Тут закончили. Куда бы податься дальше?"
    stop music fadeout 3
    jump map
    
label label_end:
    scene bg ext_bus with dissolve
    play music music_list["dance_of_fireflies"] fadein 5
    th "Наверное, с меня хватит."
    "Вышел за ворота, где меня уже ожидал автобус."
    sl "Уже уезжаешь?"
    "Послышался за спиной грустный голос Слави."
    stop music fadeout 3
    "Развернулся, ожидая увидеть лишь её, но..."
    play music music_list["goodbye_home_shores"] fadein 5
    scene bg ext_camp_entrance_day with dissolve
    show dv sad pioneer far at fleft with dissolveVF
    show un cry pioneer far at fright with dissolveVF
    show us sad sport at left with dissolveVF
    show mi sad pioneer at right with dissolveVF
    show sl sad pioneer at center with dissolveVF
    "Увидел всех девочек. {w}Они все выглядели расстроенными. {w}Даже Алиса не улыбалась, как обычно."
    "Причем что-то мне подсказывало, что это не заученный сценарий. {w}Видимо я им действительно понравился за этот день, и они действительно расстроены моим уходом."
    "Я переводил взгляд с одного кислого лица на другое. {w} Я четко видел, что каждая из них хотела что-то сказать, но слова не шли."
    me "Я понимаю вас. Мне тоже не хочется уезжать, но что поделать.{w} Мне было приятно встретиться о всеми вами вживую, я никогда не забуду нашу встречу, и думаю, что вы тоже. {w}Если повезет, я выбью еще одну поездку. {w}Будете ждать?"
    dreamgirl "Конечно!" 
    stop music fadeout 5
    "Разом воскликнули все. Я даже опешил."
    me "Ну тогда договорились."
    show dv smile pioneer far at fleft with dissolveVF
    show un smile pioneer far at fright with dissolveVF
    show us smile sport at left with dissolveVF
    show mi smile pioneer at right with dissolveVF
    show sl smile pioneer at center with dissolveVF
    "Я улыбнулся и подмигнул девчёнкам. Они сразу приободрились."
    dreamgirl "Пока, Семен."
    play music music_list["reflection_on_water"]
    me "Не прощаюсь. Увидимся ещё!"
    "Я заставил себя отвернуться и зайти в автобус, не оборачиваясь."
    scene bg int_bus with dissolve2
    "Сел на то же место, на котором сидел, когда приехал. {w}В окно смотреть не стал. {w}Еще сложнее уезжать будет. {w}Надеюсь они поймут и не обидятся."
    th "Хороший был день. Один из лучших в жизни. Обязательно вернусь сюда. {w}{w}И возможно уже не на один день."
    stop music fadeout 5
    
    return