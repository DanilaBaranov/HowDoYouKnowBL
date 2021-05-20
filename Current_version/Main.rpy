init:
    $ mods ["goodname"] = "Кто хочет стать Пионером?"
    $ dissolveVF = Dissolve(0.1)
    $ count = 0
    define user = Character("[ggname]", color="ff03f7", what_color="#f1d076")

label goodname:
    scene bg ext_road_day with dissolve2
    $ ggname = renpy.input("Как нам тебя величать:", 
    length=12, default="", 
    allow="абвгдеёжзийклмнопрстуфхцчшщъыьэюя-АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ") .strip()

    play music music_list["raindrops"] fadein 5
    scene bg int_bus
    show unblink
    th "Я проснулся от бившего в глаза солнечного света." 
    show blinking
    "Проморгался, и начал осматриваться. Кресла, узкий проход…"
    th "Автобус! {w}Неужели получилось!? {w}От радости чуть не заорал, но вовремя одернул себя. Мне все-таки 19 лет, уже взрослый для такого проявления эмоций."
    stop music fadeout 5
    th "И все же это правда, мне обещали день в Совенке, и похоже я его получил. {w}Ну, тогда не будем терять ни минуты!"
    
    play music music_list["forest_maiden"] fadein 5
    scene bg ext_camp_entrance_day with dissolve
    "Пулей вылетел из автобуса и помчался к воротам, и чуть не сбил выходившую оттуда Славю. {w}Ну а кто же еще, все по канону."
    show sl smile pioneer at center with dissolve_fast
    sl "Привет. Ты оттуда, да? На один день?"
    user "Да. Привет,Славя."
    "Она даже не удивилась, что я знаю ее имя. {w}Хотя, я же явно не первый турист, далеко не первый. {w}Сколько ж тут народу уже побывало до меня?"
    "Из раздумий меня вывела Славя"
    sl "Ну так что, пойдем? Остальные девочки уже ждут."
    user "А,да. Пойдем. Замечтался немного."
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
    user "Ульяна, даже не думай! Меня этим не возьмешь."
    show us sad sport at fright with dissolve_fast
    "Девочка вмиг поникла"
    us "Ну вот. {w}Сколько уже таких как вы тут побывало, а срабатывает лишь на единицах. {w}Мог бы и подыграть девушке!"
    show dv smile pioneer close at fleft with dissolve_fast
    "Алиса прищурившись, как бы оценивая, посмотрела на меня."
    dv "А ты неплох. {w}Не красавец конечно, но и в кусты от тебя прятаться, желания нету."
    user "И тебе привет, Алиса. {w}Ты как всегда в своем репертуаре."
    th "Похоже мой комплимент пришелся ей по вкусу"
    "Может быть мы и дальше продолжили этот словесный бой, но Славя решила пресечь его на стадии зарождения."
    show sl serious pioneer close at center with dissolve_fast
    show us normal sport far at fright with dspr
    show dv normal pioneer far at fleft with dspr
    stop music fadeout 5
    sl "Так, давайте уже начнем, а то и так времени не очень много. Всего день у парня."
    play music music_list["two_glasses_of_melancholy"] fadein 5
    user "А.. Что начнем?"
    show sl smile2 pioneer close at center with dissolve_fast
    sl "Мы с недавнего времени решили организовать для новоприбывших викторину по вселенной Бесконечного Лета. {w}Ты войдешь в первую тысячу человек, которые попали под новый формат."
    th "Не то чтобы мне не понравилась такая идея, но я хотел просто прогуляться по лагерю, поиграть в футбол с Ульянкой, может выпить с Алисой, зайти в библиотеку позлить Женю. {w}Ну а в принцпипе теперь у меня нет выбора."
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
    user "Это почему? За неправильные ответы дежурить заставят?"
    show us grin sport at fright with dissolve_fast
    show dv grin pioneer at fleft with dspr
    show sl laugh pioneer close at center with dspr
    "Славя засмеялась, а Алиса с Ульяной синхронно ухмыльнулись."
    show dv grin pioneer close at fleft with dissolve_fast
    show sl laugh pioneer at center with dspr
    dv "Нет, просто Женя очень бесится, когда отвечаешь неправильно. {w}Не дай бог у нее еще и настроение плохое. {w}Из лагеря уже не вернешься. {w}По крайней мере целым."
    th "Что ж. Очень на нее похоже. Ладно, буду начеку."
    user "Ладно, спасибо за наводку. {w}А на третьей станции кто?"
    show us normal sport at fright with dissolve_fast
    show dv grin pioneer at fleft with dspr
    show sl normal pioneer close at center with dspr
    sl "На третьей Мику с Юлей. Обитают в музклубе. Там уже серьезные вопросы. {w}Не только по сюжету и деталям, а уже и по околоигровой теме, про разработчиков, игровые файлы и прочее."
    "Славя на пару секунд замолчала, чтобы перевести дух."
    sl "Теперь в общем: на каждой станции по 15 вопросов. {w}Количество попыток неограничено, можешь пытаться снова и снова. {w}В конце девочки будут говорить тебе количество правильных ответов, но не скажут, в каких ошибки, мы посчитали такую меру неинтересной. {w}Все понял?"
    th "Вроде бы ничего сложного, и все равно моему процессору понадобилось пару десятков секунд, чтобы все уяснить до конца."
    "Наконец я сказал:"
    user "Так точно! Разрешите приступить."
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
            pass
        "5":
            pass
        "8":
            pass
        "13":
            $ count += 1
    
    dv "Следующий вопрос: {w} У какого из перечисленных персонажей нет концовки в оригинальной игре?"
    menu:
        "Мику":
            pass
        "Женя":
            $ count += 1
        "Ульяна":
            pass
        "Алиса":
            pass
            
    dv "Следующий: {w} С кем нельзя пойти в старый лагерь, на поиски Шурика?"
    menu:
        "Мику":
            $ count += 1
        "Славя":
            pass
        "Лена":
            pass
        "Алиса":
            pass
            
    us "Еще один вопросик: {w} Что подарила Славя Семёну на острове, во время сбора земляники?"
    menu:
        "Венок":
            pass
        "Поцелуй":
            pass
        "Фотографию":
            pass
        "Платок":
            $ count += 1
            
    dv "Следующий: {w} Как, по его словам, называет Электроника Ульяна?"
    menu:
        "Киборг":
            pass
        "Серёжка":
            pass
        "Сыроежка":
            $ count += 1
        "Винтик":
            pass
            
    dv "Шестой вопрос: {w} Как назвала Ульяна Семёна в первый день?"   
    menu:
        "Скучный дед":
            pass
        "Гроза Педобиров":
            pass
        "Голодающий Поволжья ":
            $ count += 1
        "Гражданин начальник":
            pass
    
    dv "Идём дальше. {w} По какой причине в плохой концовке Ульяны Семён ехал в автобусе один?"
    menu:
        "Она опоздала на автобус":
            pass
        "Она осталась в лагере, в качестве наказания":
            $ count += 1
        "Ее забрали родители":
            pass
        "Ульяна отсела от него":
            pass
    
    us "И еще один: {w}Альтернативное имя Электроника в Мику-Руте."
    menu:
        "Винтик":
            pass
        "Роутер":
            $ count += 1
        "Модем":
            pass
        "Сыроежка":
            pass
    
    us "Девятый уже: {w} Что забрала с собой Юля из лагеря?"
    menu:
        "Мешок с запасами":
            $ count += 1
        "Мешок с сахаром":
            pass
        "Украденные у пионеров вещи":
            pass
        "Ничего":
            pass
    
    dv "Вот еще про Юлю: {w} Зачем она посыпала грибы сахаром?"
    menu:
        "Просто так":
            pass
        "Ей так сказали":
            pass
        "Чтобы лучше росли":
            $ count += 1
        "Чтобы были вкуснее":
            pass
    
    us "А вот про Мику: {w} Чем больше всего выделялась Мику для Семёна?"
    menu:
        "Цветом волос":
            pass
        "Длинными волосами":
            pass
        "Излишней болтливостью ":
            $ count += 1
        "Красотой":
            pass
    
    us "А где у нас в лагере находится мука, знаешь?"
    menu:
        "Столовая":
            pass
        "Клуб Кибернетики":
            pass
        "Склад":
            pass
        "Библиотека":
            $ count += 1
    
    us "А теперь ответь ка мне, зачем кибернетики хранят у себя в клубе водку?"
    menu:
        "Протирать оптику":
            $ count += 1
        "Дезинфицировать раны":
            pass
        "Пить":
            pass
        "Прячут от Алисы":
            pass
    
    dv "«Челюсть с пола подними»-кому принадлежит эта фраза?"
    menu:
        "Алиса":
            $ count += 1
        "Ульяна":
            pass
        "Шурик":
            pass
        "Пионер":
            pass
    
    us "Последний вопрос: {w} Кто такой Пионер?"
    menu:
        "Перевоплощение Юли":
            pass
        "Дух Лагеря":
            pass
        "Обычный пионер":
            pass
        "Сошедшая с ума копия Семёна":
            $ count += 1
            
    if count == 0:
        show dv rage pioneer2 at right with dspr
        dv "Ты не ответил ни на один вопрос верно! {w}Все-таки я ошиблась насчет тебя! {w}Иди перепройди игру пару раз и возвращайся. Стыдно должно быть!"
    
    if count == 1:
        show us dontlike sport at left with dspr
        us "Всего лишь один правильный ответ. {w}Ты почти безнадежен. {w}Попробуй снова, может что-то еще и получится"
    
    if count == 2:
        show dv rage pioneer2 at right with dspr
        dv "Два верных ответа. {w}Ты зачем вообще приехал сюда? Вопросы же легкие. {w}Ну попробуй еще раз конечно, может что-то в голове еще зашевелится."
    
    if count == 3:
        show us dontlike sport at left with dspr
        us "Три попадания. {w}Бог любит троицу, конечно, но результат то детский. {w}Я и то больше бы ответила."
    
    if count == 4:
        show dv angry pioneer2 at right with dspr
        dv "Четыре верных. {w}Ну, {w}такое ощущение, что ты только один рут прошел, и фанатом себя возомнил."
    
    if count == 5:
        show us dontlike sport at left with dspr
        us "Пять из пятнадцати! {w}На треть справился, но все равно отстой."
    
    if count == 6:
        show dv angry pioneer2 at right with dspr
        dv "Шесть попаданий. {w}Плохой из тебя стрелок, однако."
    
    if count == 7:
        us "Семь верных ответов. {w}Почти половину осилил. {w}Ну, неплохо, но фанатом тебя пока назвать трудно."
    
    if count == 8:
        show dv grin pioneer2 at right with dspr
        dv "Восемь из пятнадцати. {w}Еле половину перевалил. Ну что ж, неплохо, ты из себя что-то да представляешь."
    
    if count == 9:
        show us grin sport at left with dspr
        us "Девять! Видимо, ты что-то да знаешь. {w}Может еще разок, глядишь еще пару наугад правильно выберешь?"
    
    if count == 10:
        show dv grin pioneer2 at right with dspr
        dv "Две трети тебе поддались. {w}Скажи честно, наугад же отвечал."
    
    if count == 11:
        show us grin sport at left with dspr
        us "Ты правильно ответил на целых одиннадцать вопросов. {w}Можно сказать, что ты уже не новичок, но и звание знатока тебе пока рано носить."    
    
    if count == 12:
        show dv smile pioneer2 at right with dspr
        dv "Надо же. Всего три промаха. {w}Ты перестаешь меня бесить. Так держать!"
    
    if count == 13:
        show us surp1 sport at left with dspr
        us "Ну ты даешь, всего два неверных ответа. {w}Не думала, что ты такой умный."
    
    if count == 14:
        show dv smile pioneer2 at right with dspr
        dv "Эх, дурень. {w}Всего один неверный. {w}Не мог уже дотянуть что ли? {w}Ладно, не обижайся. Молодец!"
    
    if count == 15:
        show us surp1 sport at left with dspr
        us "Всё верно! Но ты же сжульничал, признавайся!" 
        
    th "Так. Тут закончили. Куда бы податься дальше?"
    stop music fadeout 3
    jump map
    
label library:
    if count > 0:
        $ count = 0
    play music music_list["your_bright_side"] fadein 5
    scene bg ext_library_day with dissolve    
    th "Среднячок-это мое. {w}Думаю справлюсь."
    "Немного постояв на пороге..."
    scene bg int_library_day with dissolve
    "Зашел в обитель Жени"
    show mz normal glasses pioneer at right with dspr
    show un smile pioneer at left with dspr
    sl "Привет ещё раз. {w}Готов?"
    me "Всегда готов!"
    show mz angry glasses pioneer with dissolveVF
    "Чуть ли не выкрикнул я, заработав очень неодобрительный взгляд от Жени."
    show mz normal glasses pioneer at right with dspr
    un "Итак. {w}Первый вопрос: {w}Назови композитора Тёмной стороны игрового саундтрека."
    menu:
        "Between August and December":
            $ count += 1
        "From Ashes to New":
            pass
        "Sergey Eybog":
            pass
        "Sati Akura":
            pass
          
    mz "Второй: {w}Скажи название трека-темы Мику."
    menu:
        "Miku’s Song":
            pass
        "Memories":
            pass
        "So good to be careless":
            $ count += 1
        "I want to play":
            pass
    mz "Следующий вопрос таков: {w}Как называется достижение за хорошую концовку Алисы?"
    menu:
            "Эпик Фейл":
                pass
            "Мое рыжее счастье":
                pass
            "Гуру Пикапа":
                $ count += 1
            "Лидер Митол-группы":
                pass
    
    un "Четвертый вопрос: {w}Вспомни год выпуска игры."
    menu:
            "2010":
                pass
            "2012":
                pass
            "2011":
                pass
            "2013":
                $ count += 1
        
    un "Вопрос номер следующий: {w}В мастерской Steam присутствует модификация, которая вышла еще до релиза оригинала. {w}Как называется эта модификация?" 
    menu:
            "Возвращение в Совенок":
                pass
            "7 дней лета":
                pass
            "Чистовик":
                pass
            "Wintertale":
                $ count += 1
        
    mz "На кого учится реальная Славя из мира Семёна в хорошей концовке?"
    menu:
            "Краевед":
                pass
            "Эколог":
                $ count += 1
            "Ветеринар":
                pass
            "Учитель":
                pass
    
    un "Уже седьмой: {w} Единственная концовка, в которой можно увидеть глаза Семёна." 
    menu:
            "Лена хорошая":
                $ count += 1
            "Лена плохая":
                pass
            "Славя хорошая":
                pass
            "Славя плохая":
                pass
        
    mz "Половина позади. {w} Куда, по словам Лены, она хотела попасть?"
    menu:
            "В кружок танцев":
                pass
            "В актерский кружок":
                pass
            "В клуб карточных игр":
                pass
            "В сборную по бадминтону":
                $ count += 1
                
    un "Вопрос про Ульянку: {w} Какую она искала аудиторию с хорошей концовке?"
    menu:
            "34":
                $ count += 1
            "865":
                pass
            "57":
                pass
            "410":
                pass
        
    mz "Десятый. {w}Сколько человек осталось в лагере после массового исчезновения происшествия в Мику-руте?"
    menu:
            "3":
                pass
            "4":
                pass
            "5":
                $ count += 1
            "6":
                pass
        
    un "Ещё вопрос: {w}Кто живет в одном домике с Мику?"
    menu:
            "Лена":
                $ count += 1
            "Женя":
                pass
            "Славя":
                pass
            "Ульяна":
                pass
        
    mz "Вопрос на знание технической стороны игры. {w}Какого из этих фильтров нет в оригинальной игре?"
    menu:
            "Черно-белое лето":
                pass
            "27-цветное лето":
                pass
            "Яркое лето":
                $ count += 1
            "Ностальгическое лето":
                pass
        
    mz "Держи ещё один: {w}Какой фильм смотрели Семён с Ульяной в каморке клуба кибернетиков?" 
    menu:
            "Назад в будущее":
                pass
            "Матрица":
                pass
            "Ирония судьбы":
                pass
            "Терминатор":
                $ count += 1
                
    un "Вот вопрос посложнее: {w}Какого цвета глаза у Виолы?"
    menu:
            "Карий и голубой":
                $ count += 1
            "Карий и зеленый":
                pass
            "Зеленый и желтый":
                pass
            "Карий и желтый":
                pass
        
    mz "И последний: {w}Кем работает папа Мику?"
    menu:
            "Русский инженер":
                $ count += 1
            "Японский инженер":
                pass
            "Русский композитор":
                pass
            "Японский композитор":
                pass
        
    if count == 0:
        show un sad pioneer at left with dspr
        un "Ой. Ты везде ошибся. {w}Не расстраивайся, все хорошо… "
    
    if count == 1:
        show mz rage pioneer at right with dspr
        mz "Всего один верный ответ! {w}И стоило ради этого тратить наше время?!"
    
    if count == 2:
        show un sad pioneer at left with dspr
        un "Два верных ответа..."
    
    if count == 3:
        show mz angry glasses pioneer at right with dspr
        mz "Три ответа верных. {w}Ты уверен, что стоило идти на эту станцию с таким «багажом» знаний?"
    
    if count == 4:
        show un shy pioneer at left with dspr
        un "Четыре ответа. {w}Уже хорошо."
    
    if count == 5:
        show mz normal glasses pioneer at right with dspr
        mz "Треть верно, на троечку, больше и не рассчитывай."
    
    if count == 6:
        show un shy pioneer at left with dspr
        un "Ты дал шесть верных ответов, молодец, ты неплохо разбираешься в игре."
    
    if count == 7:
        show mz normal glasses pioneer at right with dspr
        mz "Семь из пятнадцати. {w}Читал бы внимательнее, больше бы ответил."
    
    if count == 8:
        show un shy pioneer at left with dspr
        un "Восемь, это больше половины! {w}Молодец!"
    
    if count == 9:
        show mz normal glasses pioneer at right with dspr
        mz "Девять из пятнадцати. {w}Может та не такой уж и тупой. {w}И не считай это комплиментом, просто факт!"
    
    if count == 10:
        show un smile2 pioneer at left with dspr
        un "Десять из пятнадцати! {w}Ты хорошо знаешь наш мир."
    
    if count == 11:
        show mz normal glasses pioneer at right with dspr
        mz "Одиннадцать верных. {w}Ну, уже что-то..."    
    
    if count == 12:
        show un smile2 pioneer at left with dspr
        un "Всего лишь три неверных! {w}Какой ты умный!"
    
    if count == 13:
        show mz smile glasses pioneer at right with dspr
        mz " Два промаха. {w}Неплохо, {w}может, я даже позволю тебе взять какую-нибудь книжку."
    
    if count == 14:
        show un smile2 pioneer at left with dspr
        un "Всего один неверный! {w}Наверное, ты просто случайно ошибся. {w}Какой ты молодец!"
    
    if count == 15:
        show mz laugh glasses pioneer at right with dspr
        mz "Все верно, надо же! {w}А ты не такой тюфяк, каким показался сначала." 
        
    th "Так. Тут закончили. Куда бы податься дальше?"
    stop music fadeout 3
    jump map
    
label music_club:
    if count > 0:
        $ count = 0
    play music music_list["reflection_on_water"] fadein 5
    scene bg ext_musclub_day with dissolve
    "Неспешно пошел по дорожке по направлению к музыкальному клубу. {w}Не стоит торопиться. Все-таки вопросы тут будут далеко не детские."
    "Ну ничего, попытка не пытка!"
    scene bg int_musclub_day with dissolve
    show mi normal pioneer at left with dissolve
    show uv smile at right with dissolve
    "Сколько ж тут инструментов! {w}На полноценный оркестр хватило бы."
    uv "О, а ты у нас смельчак! {w}На сложную станцию пришел! {w}Ну что ж, проверим насколько ты профи."
    uv "Начинаем: {w}Назови общее количество фонов в игре."
    menu:
        "107":
            pass
        "85":
            pass
        "115":
            $ count += 1
        "93":
            pass
    
    mi "Следующий вопросик: {w}В каком порядке появляются девушки во вступительном ролике?"
    menu:
        "Лена-Алиса-Ульяна-Мику-Юля-Славя":
            pass
        "Славя-Лена-Ульяна-Алиса-Мику-Юля":
            $ count += 1
        "Славя-Лена-Алиса-Ульяна-Мику-Юля":
            pass
        "Юля-Лена-Славя-Мику-Алиса-Ульяна":
            pass
    
    mi "Ты уже видел Женю? {w}Знаешь прототипом какого маскота она является?"
    menu:
        "Коллайдер-тян":
            pass
        "Митцгёрл":
            $ count += 1
        "Уныл-тян":
            pass
        "Славя-тян":
            pass
    
    uv "А вот вопрос для истинных фанатов: {w}У какого персонажа больше всего спрайтов в пионерской форме?"
    menu:
        "Ульяна":
            $ count += 1
        "Лена":
            pass
        "Славя":
            pass
        "Мику":
            pass
    
    mi "Замечал ли ты, есть ли в игре выборы которые ни на что не влияют?"
    menu:
        "Есть,один":
            $ count += 1
        "Есть,два":
            pass
        "Есть,три":
            pass
        "Нет ни одного":
            pass
       
    uv "Не расслабляться! Следующий: {w}Какая из девушек является не прототипом, а  самостоятельным маскотом ?"
    menu:
        "Славя":
            $ count += 1
        "Ульяна":
            pass
        "Ольга Дмитриевна":
            pass
        "Виола":
            pass
    
    mi "В … квартире один на один с имиджбордами пустые вечера проводил."
    menu:
        "Грязной":
            pass
        "Пустой":
            pass
        "Опустевшей":
            pass
        "Захламлённой":
            $ count += 1
    
    uv "Помнится Семён впервые услышал Рена, а не Лена. {w}А ведь это отсылка, только вот к какому произведению?"
    menu:
        "Евангелион":
            pass
        "Атака Титанов":
            pass
        "Когда плачут цикады":
            $ count += 1
        "Токийский Гуль":
            pass
    
    mi "Много ли ты раз бывал у домика Алисы с Ульяной? {w}Что там можно увидеть помимо флага?"
    menu:
        "Кота":
            pass
        "Куст":
            pass
        "Сову":
            $ count += 1
        "Записку \"Не входить\" ":
            pass
    
    uv "Десятый уже, кстати: {w}Что было в руках у Лены, когда она шла по лесу в направлении Семёна и Слави?"
    menu:
        "Нож":
            $ count += 1
        "Фонарь":
            pass
        "Ничего":
            pass
        "Книга":
            pass
    
    mi "Скажи, как зовут шуточного персонажа, который всегда сидит в дальнем конце столовой."
    menu:
        "Антон":
            pass
        "Женя":
            pass
        "Вася":
            pass
        "Толик":
            $ count += 1
    
    uv "А знаешь ли ты, сколько флагов висит на площади?"
    menu:
        "1":
            pass
        "2":
            pass
        "3":
            $ count += 1
        "4":
            pass
    
    mi "Ты наверное заметил, что домики в лагере разной формы. {w}А помнишь ли ты форму домика Слави и Жени?"
    menu:
        "Треугольный":
            pass
        "Полукруглый":
            $ count += 1
        "Квадратный":
            pass
        "Призматический":
            pass
    
    uv "Ладно форма, а знаешь ли ты сколько вообще домиков для пионеров находится на территории лагеря?"
    menu:
        "25":
            pass
        "10":
            pass
        "35":
            pass
        "30":
            $ count += 1
    
    uv "И последний, на мой взгляд самый интересный: {w}В какой период времен происходят события в игре?"
    menu:
        "7-13 июня 1987":
            $ count += 1
        "8-14 августа 1988":
            pass
        "7-13 июня 1986":
            pass
        "15-21 июля 1987":
            pass
    
    if count == 0:
        show uv dontlike at right with dspr
        uv "Ни одного верного ответа. {w}Не готов ты еще к сложным вопросам. {w}Не расстраивайся, мало кто справляется."
    
    if count == 1:
        show mi upset pioneer at left with dspr
        mi "Всего один верный, {w}ну тоже неплохо, значит что-то знаешь, может еще раз пройдешь?"
    
    if count == 2:
        show uv normal at right with dspr
        uv "Два верных. {w}Хмм, да у меня лапок больше."
    
    if count == 3:
        show mi surprise pioneer at left with dspr
        mi "Три правильных. {w}Молодец! {w}Я бы и на один не ответила, а ты целых три!"
    
    if count == 4:
        show uv grin at right with dspr
        uv "Четырррре! {w}Прям как количество моих лапок."
    
    if count == 5:
        show mi surprise pioneer at left with dspr
        mi "Ух ты! Пять верных! {w}Ты такой молодец, вопросы такие сложные, я когда читала, сама ответила лишь на парочку."
    
    if count == 6:
        show uv smile at right with dspr
        uv "Шесть верных. {w}Я бы тебе на первом неправильном подсказала, но... {w}у меня лапки."
    
    if count == 7:
        show mi smile pioneer at left with dspr
        mi "Семь правильных. {w}Ух ты, почти половина, вопросы такие сложные, я бы лучше какую-нибудь новую песню выучила."
    
    if count == 8:
        show uv surprise at right with dspr
        uv "Восемь правильных ответов. {w}Клянусь хвостом, мало таких я на своем веку видела."
    
    if count == 9:
        show mi happy pioneer at left with dspr
        mi "Девять правильных! {w}Давно такого умненького не было!"
    
    if count == 10:
        show uv smile at right with dspr
        uv "Две трети правильно. {w}Уже достойно для того, чтобы показать тебе свои запасы."
    
    if count == 11:
        show mi smile pioneer at left with dspr
        mi "Целых одиннадцать попаданий! クール!"    
    
    if count == 12:
        show uv laugh at right with dspr
        uv "Двенадцать замуррчательных ответов. {w}А ты не так прост, как кажешься."
    
    if count == 13:
        show mi dontlike pioneer at left with dspr
        mi "Тринадцать правильных ответов. {w}Не нравится мне это число. {w}Несчастливое, как мне папа говорил."
    
    if count == 14:
        show uv surprise2 at right with dspr
        uv "Всего лишь один неверный! {w}Таких как ты у нас было от силы десять человек! {w}Впечатляет."
    
    if count == 15:
        show mi smile pioneer at left with dspr
        mi "Все правильно! {w}Ну ты даешь!"  
        show mi laugh pioneer at left with dspr
        "Похоже у тебя совсем нет личной жизни!"
        "..."
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
    user "Я понимаю вас. Мне тоже не хочется уезжать, но что поделать.{w} Мне было приятно встретиться о всеми вами вживую, я никогда не забуду нашу встречу, и думаю, что вы тоже. {w}Если повезет, я выбью еще одну поездку. {w}Будете ждать?"
    dreamgirl "Конечно!" 
    stop music fadeout 5
    "Разом воскликнули все. Я даже опешил."
    user "Ну тогда договорились."
    show dv smile pioneer far at fleft with dissolveVF
    show un smile pioneer far at fright with dissolveVF
    show us smile sport at left with dissolveVF
    show mi smile pioneer at right with dissolveVF
    show sl smile pioneer at center with dissolveVF
    "Я улыбнулся и подмигнул девчёнкам. Они сразу приободрились."
    dreamgirl "Пока, [ggname]."
    play music music_list["reflection_on_water"]
    user "Не прощаюсь. Увидимся ещё!"
    "Я заставил себя отвернуться и зайти в автобус, не оборачиваясь."
    scene bg int_bus with dissolve2
    "Сел на то же место, на котором сидел, когда приехал. {w}В окно смотреть не стал. {w}Еще сложнее уезжать будет. {w}Надеюсь они поймут и не обидятся."
    th "Хороший был день. Один из лучших в жизни. Обязательно вернусь сюда. {w}{w}И возможно уже не на один день."
    stop music fadeout 5
    
    return