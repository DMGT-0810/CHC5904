import streamlit as st
import pathlib
import base64


# Set the page configuration
st.set_page_config(page_title='My Website', layout='wide')

# Sidebar navigation with emojis
page = st.sidebar.radio('Navigation',
                        ['🏠 Introduction', '🌱 Plants', '😊 Interaction', '💖 About Us'])

if page == '🏠 Introduction':
    cover_photo_path = "https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/15.PNG?raw=true"
    st.image(cover_photo_path, use_column_width=True)

    st.title("🌺Exploring Plant Imagery and Symbolism in the Book of Poetry")

    # First submodule: Introduction to the Book of Songs
    st.header('🏠 Introduction')
    st.write('''
    Let's Embark on a Journey Through Poetry, Plants, and Time!

    The Book of Songs (《诗经》) is a foundational collection of poems intricately tied to social and historical development, serving as a prelude to Chinese national history. Created during the agricultural era, these poems capture:

    - Social Landscapes: Depictions of rural villages, marketplaces, and royal courts.
    - Historical Snapshots: Insights into ancestral lifestyles and living scenes.

    Through the Book of Songs, later generations can learn about the natural landscapes, flora and fauna, climate changes, land structures, production systems, ethnic distributions, transportation systems, and cultural customs from the early Western Zhou to mid-Spring and Autumn periods. The poems, carefully compiled, serve as vital historical documents for in-depth research into this era.

    In the Book of Songs, plants take center stage, weaving through nearly half of its 305 poems. With 386 plant-related references and 130 unique species, these verses reveal how deeply nature shaped ancient Chinese culture.
    ''')

    # Second submodule: Plants in the Spotlight
    st.header('✨ Plants in the Spotlight')
    st.subheader('🏆 The Plant Leaderboard')
    st.write('''
    🌿 桑 (Mulberry) – 40 mentions

    🌾 黍 (Millet) – 26 mentions

    🍂 葛 (Kudzu) – 21 mentions

    🍃 草 (Grass) – 19 mentions

    🫘 豆 (Bean) – 11 mentions

    🌲 松 (Pine) – 11 mentions

    🍁 柏 (Cypress) – 10 mentions

    🎋 竹 (Bamboo) – 7 mentions
    ''')

    # Image placeholders with local paths
    st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/1.PNG')
    st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/2.PNG')

    # Third submodule: Plants, Emotions, Seasons & Locations
    st.header('🌍 Plants, Emotions, Seasons & Locations')

    # 3-1
    st.subheader('Why should we care about the connection between plants and emotions?')
    st.write('''
    Most plants don’t express a single emotion—they are rich tapestries of overlapping feelings.

    In the Classic of Poetry, emotions are categorized into seven distinct types: 

    🌟 Joy

    🔥 Anger

    💭 Worry

    🤔 Contemplation

    😢 Sadness

    😨 Fear

    😲 Surprise

    By visualizing plants through this emotional lens, we can unlock a deeper understanding of their emotional significance, allowing us to connect with the poems written by our ancestors on a more personal level.
    ''')

    # Additional image placeholders for the third submodule
    st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/3.PNG')
    st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/4.PNG')

    # 3-2
    st.subheader('Seasonal Distribution of Selected Plants')
    st.write('''
        The Book of Songs beautifully ties plants to the rhythm of the seasons, revealing our ancestors' close relationship with nature. Our selected plants are predominantly associated with spring and autumn, reflecting the importance of these seasons in ancient agricultural life, however, 42% are not specified, which shows that the symbolic use of plants beyond seasonal constraints.
        ''')

    # Additional image placeholders for the third submodule
    st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/5.PNG')
    st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/6.PNG')

    # 3-3
    st.subheader('Tracing the Ancient Roots')
    st.write('''
        The Book of Songs also reveals the natural and cultural landscapes of early China, showing how the people in the past interacted with their environment. This geographical map invites you to connect with the landscapes that shaped our ancestors’ lives, offering a unique link to the past. As you explore these places, you’ll be reminded of how nature was deeply woven into daily life, agriculture, and culture.
        ''')

    # Load and display the HTML file
    file_path = pathlib.Path(__file__).parent / 'plants_in_poetry.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        html_content = f.read()
    st.components.v1.html(html_content, height=600, scrolling=True)

    # Additional image placeholders for the third submodule
    # st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/5.PNG', caption='Third Plant Image')
    # st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/6.PNG', caption='Fourth Plant Image')

    categories_content = {
        "Mulberry(桑)": "期我乎桑中，要我乎上宫[《鄘风·桑中》]\n  - In Ancient Times: widespread in the Yellow River region, especially in Wei State (modern-day northern Henan and southern Hebei).\n  - Today: Mulberry trees are still common in northern China, particularly in areas like the ancient mulberry tree cluster in Xiajin, Shandong.",
        "Kudzu(葛)": "“葛生蒙楚，蔹蔓于野”[《周南·樛木》]\n  - In Ancient Times: Widespread in ancient China, especially in Chu (modern-day Hubei and Hunan).\n  - Today: Kudzu still grows in southern China, primarily used for traditional medicinal purposes and food processing.",
        "Panicum miliaceum(黍)": "“彼黍离离，彼稷之苗”[《王风·黍离》]\n  - In Ancient Times: Widely cultivated in the Yellow River region.\n  - Today: Still grown in northern China, especially in the Yellow River region, known as yellow millet, used in food processing.",
        "Various grasses(草)": "“蒹葭苍苍，白露为霜”[《秦风·蒹葭》]\n  - In Ancient Times: Various grasses, such as reeds, were common in ancient China’s wetland environments.\n  - Today: Grasses are found all over China, especially in the north, used in livestock farming, weaving, and other purposes.",
        "Beans and peas(豆)": "“菽（大豆）”[《豳风·七月》]\n  - In Ancient Times: Beans played an important role in ancient China’s agricultural society.\n  - Today: Beans are grown across China, being an important source of food and vegetables.",
        "Pine(松)": "“松柏丸丸，其下侯旬”[《小雅·斯干》]\n  - In Ancient Times: Pines were widespread in ancient China, especially in mountainous and hilly areas.\n  - Today: Pine trees are very common throughout China, particularly in the north and southwest, used for construction, furniture, and other purposes.",
        "Cypress(柏)": "“桧楫松舟”[《鄘风·柏舟》]\n  - In Ancient Times: Cypress trees were common in areas near water bodies in ancient China.\n  - Today: Cypress trees are primarily found in southern China, especially in Sichuan, Hubei, and Guizhou provinces.",
        "Bamboo(竹)": "“籊籊竹竿，以钓于淇”[《卫风·竹竿》]\n  - In Ancient Times: Bamboo was found along rivers in ancient China.\n  - Today: Bamboo grows widely in China, especially in the southern regions, used for construction, furniture, weaving, and various other purposes."
    }

    # 创建展开框显示各类别内容
    for category, content in categories_content.items():
        with st.expander(f"{category}"):
            st.write(content)

elif page == '🌱 Plants':

    cover_photo_path = "https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/16.PNG"
    st.image(cover_photo_path, use_column_width=True)

    st.title('🌱 Deep Dives into Plant Symbolism')

    # Sub-navigation for the "Plants" page
    plant_page = st.sidebar.radio('Plant Sections',
                                  ['🌿 Mulberry', '🍂 Kudzu', '🌾 Millet', '🍃 Grass', '🫘 Beans', '🌲 Pine and Cypress',
                                   '🎋 Bamboo'])

    if plant_page == '🌿 Mulberry':
        st.header('Mulberry 桑')
        st.write(
            '''Mulberry is one of the earliest cultivated tree species in China, and it is also the most common plant near private houses in ancient times. The word "桑梓" has become a substitute for hometown. Mulberry trees have a wide range of uses: the leaves can be used to feed silkworms, while the fruit is sweet and edible, which can satisfy hunger and make into wine; The bark has been a famous medicine since ancient times, it can even be used to make bow, gricultural tools, utensils, chariots, etc. The line “十亩之间兮，桑者闲闲兮” shows the scene of a peasant woman happily picking mulberries, reflecting the praise of hardworking life.''')

        st.subheader('Symbolic Poems Associated with the Plant')
        poems = [
            ("《豳风·七月》",
             '''- “女执懿筐，遵彼微行，爰求柔桑。”\n- “七月流火，九月授衣。春日载阳，有鸣仓庚。女执懿筐，遵彼微行，爰求柔桑。'''),
            ("《氓》",
             '''- “氓之蚩蚩，抱布贸丝。匪来贸丝，来即我谋。”\n- “桑之未落，其叶沃若。于嗟鸠兮！无食桑葚。于嗟女兮！无与士耽。'''),
            ("《小雅·隰桑》",
             '''- “隰桑有阿，其叶有难。既见君子，其乐如何！”\n- “隰桑有阿，其叶有沃。既见君子，云何不乐！”\n- “隰桑有阿，其叶有幽。既见君子，德音孔胶。'''),
            ("《魏风·十亩之间》", '''- “十亩之间兮，桑者闲闲兮。行与子还兮。”\n- “十亩之外兮，桑者泄泄兮。行与子逝兮。'''),
            ("《鄘风·桑中》", "爰采唐矣？沬之乡矣。云谁之思？美孟姜矣。期我乎桑中，要我乎上宫，送我乎淇之上矣。"),
        ]

        # 创建多列
        cols = st.columns(5)  # 根据需要调整列数

        for col, (title, content) in zip(cols, poems):
            with col:
                # 使用更小号的标题字体
                st.markdown(f"<h4 style='text-align: center; font-size:18px;'>{title}</h4>", unsafe_allow_html=True)
                st.write(content)

        st.subheader('1. Seasonal connections ')
        tabs = st.tabs(["Statistical Results", "Agriculture", "Love"])
        contents = [
            "By screening the poems related to ‘桑 (mulberry)’ in the Book of Songs and the time elements contained in them, the results show that among the 36 occurrences of ‘桑’, 18 are in ‘spring’, 3 in ‘autumn’, and 2 include the flow of the three seasons ‘spring, summer, and autumn’, while the remaining 13 do not clearly reflect the seasonal characteristics. The results show that of the 36 occurrences of ‘桑’, 18 are in ‘spring’, 3 are in ‘autumn’, and 2 include the flow of the three seasons of ‘spring, summer, and autumn’, while the remaining 13 do not clearly reflect seasonal characteristics. From this we can see that in terms of seasons, ‘mulberry’ is more often associated with spring, followed by autumn, which may be related to the themes expressed in these verses, the two most prominent of which are agriculture and love, which are also two important themes of the Book of Songs.<br>In addition to this, related to time are the date and hour. Among these 36 occurrences, only one poem, ‘國風·豳風·七月’, mentions a specific month, from July to September, reflecting a detailed record of the months of agricultural activities in ancient societies. As for the hour, none of the verses explicitly mentions the hour, probably because these verses focus more on describing agricultural activities or emotional expressions than on specific points in time. It can be seen that compared to the relationship between ‘mulberry’ and the season, other time factors can hardly be taken into consideration.",
            "As far as farming is concerned, the two seasons of spring and autumn are crucial, one for sowing and the other for harvesting. Most of the poems related to ‘桑’ focus on spring, which is consistent with the fact that spring was the beginning of agricultural activities in ancient agricultural societies. Mulberry trees, as an important cash crop, and their young leaves were food for silkworms, so there were frequent activities of mulberry harvesting in spring. In addition, agricultural activities would also reflect seasonal changes. For example, the poem ‘國風·豳風·七月’ covers agricultural activities in all seasons of the year, from sowing in the spring to growing in the summer to harvesting in the autumn and preparing for the winter, which reflects the ancient agricultural society's reliance on and adaptation to seasonal changes. In the spring, the poem mentions ‘春日載陽’, indicating the arrival of spring, when agricultural activities, such as mulberry picking, begin. In the summer, the poem ‘七月流火’ implies the heat of summer, and ‘八月萑葦’ indicates the summer reeds. In autumn, the poem ‘八月其獲’ suggests that autumn is the season of harvesting. In winter, the poem ‘二之日鑿冰衝衝’ indicates that ice is chiselled in winter and used for preserving food.",
            "In the case of love, it is also tied to the seasons. In spring, there is an activity closely related to ‘桑’, namely ‘采桑 (picking mulberry)’. In the time of the Book of Songs, ‘采桑’ did not only represent agricultural activities, but was also a place for the expression of emotions and love between a man and a woman, as the activity of picking mulberry created an opportunity for young men and women to meet and get to know each other. The fact that most of these poems focus on spring reflects the importance of the mulberry tree in the economy and culture of ancient societies. The mulberry tree was not only a cash crop, but also a carrier of emotional and political allegories, such as a place for love between men and women and a praise for hard work."
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content, unsafe_allow_html=True)

        st.subheader('2. Emotional associations')
        tabs = st.tabs(["Love and Marriage", "Diligent Living", "Homesick and Longing", "Politics"])
        contents = [
            '''《鄘风·桑中》, “期我乎桑中，要我乎上宫，送我乎淇之上矣”<br>Mulberry is often associated with love between men and women. In this poem, it depicts the meeting of young men and women in the Mulberry Forest, where mulberry has become a place for men and women to meet, and the tenderness and luxuriantness of the “桑树” shows the happiness and joy of the Mulberry picker and the gentleman. The tenderness and luxuriantness of the mulberry trees show the happiness and joy of the woman picking the mulberry tree when she meets with the gentleman, and expresses her joy and yearning for love.''',
            '''《卫风·氓》:“桑之未落，其叶沃若。于嗟鸠兮，无食桑葚！于嗟女兮，无与士耽！士之耽兮，犹可说也。女之耽兮，不可说也。桑之落矣，其黄而陨。自我徂尔，三岁食贫。”<br>Here, the growing state of the mulberry tree is both a metaphor for the changes in sweet love, showing the woman's desire for love and her grief over the misfortune of marriage, and also a symbol of liveliness. In the first section:"The mulberry has not fallen, and its leaves are fertile", Mulberry is a metaphor for the harmony of the newlyweds with the growth and prosperity of the mulberry leaves; while the scene of the mulberry leaves withering and turning yellow to the ground is a metaphor for the misery of time and the change of lover's heart.<br>Here, the growing state of the mulberry tree is both a metaphor for the changes in sweet love, showing the woman's desire for love and her grief over the misfortune of marriage, and also a symbol of liveliness. In the first section:"The mulberry has not fallen, and its leaves are fertile", Mulberry is a metaphor for the harmony of the newlyweds with the growth and prosperity of the mulberry leaves; while the scene of the mulberry leaves withering and turning yellow to the ground is a metaphor for the misery of time and the change of lover's heart.''',
            '''In some poems, mulberry is also associated with homesickness and nostalgia. For example, the verse “蜎蜎者蠋，烝在桑野” expresses the sadness of soldiers who do not return from an expedition and who miss their homes.''',
            '''“迨天之未阴雨，彻彼桑土，绸缪牖户”<br>The verse conveys, through the image of the mulberry, a political message of diligence and self-reliance, of saving for a rainy day, and of preventive preparations to protect one's homeland.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content, unsafe_allow_html=True)

        st.subheader('3. Human qualities')
        st.write('''
            《小雅·隰桑》

            隰桑有阿，其叶有难。既见君子，其乐如何！

            隰桑有阿，其叶有沃。既见君子，云何不乐！

            隰桑有阿，其叶有幽。既见君子，德音孔胶。
            ''')

        st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/8.PNG', width=300)

        tabs = st.tabs(["The purity and boldness of emotions", "Admiration and pursuit of morality for gentlemen"])
        contents = [
            "The emotional expression in the poem is pure and bold, direct and passionate, reflecting the poet's frank attitude and brave pursuit of love. In personal qualities, this frankness and courage are commendable, as they reflect one's sincerity and steadfastness",
            '''The term '君子' in the poem is not only a title for the beloved, but also implies an appreciation for their character. In ancient times, the term '君子' was often used to refer to a person of moral character. Therefore, the admiration for a "gentleman" is not only an admiration for oneself, but also a pursuit and longing for noble character'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)


    elif plant_page == '🍂 Kudzu':
        st.header('Kudzu 葛')
        st.write('''
                Before cotton was imported to China, Gebu was the fabric to make summer clothing. Here, the poem describes the size and strength of the kudzu vine and what it could be used for: kudzu grows long and strong, spreading all over the hills and valleys, with dense and lush leaves. Harvested and boiled, the fibers are stripped into fine threads to weave into kudzu cloth, wearing kudzu garments is truly comfortable!

                《周南·葛覃》:“葛之覃兮，施于中谷，维叶莫莫。是刈是濩，为絺为綌，服之无斁。”
                ''')

        st.subheader('Symbolic Poems Associated with the Plant')
        poems = [
            ("《王风·采葛》",
             '''- “彼采葛兮，一日不见，如三月兮。”\n- “彼采萧兮，一日不见，如三秋兮。”\n- “彼采艾兮，一日不见，如三岁兮。'''),
            ("《周南·葛覃》",
             '''- “葛之覃兮，施于中谷，维叶萋萋。”\n- “葛之覃兮，施于中谷，维叶莫莫。”\n- “是刈是濩，为絺为綌，服之无斁。'''),
            ("《唐风·葛生》",
             '''- “葛生蒙楚，蔹蔓于野。”\n- “葛生蒙棘，蔹蔓于域。”\n- “角枕粲兮，锦衾烂兮。'''),
            ("《邶风·旄丘》",
             '''  - “旄丘之葛兮，何诞之节兮。”\n  - “叔兮伯兮，何多日也？何其处也？必有与也！”\n  - “何其久也？必有以也！”'''),
            ("《王风·葛藟》", '''  - “绵绵葛藟，在河之浒。”\n  - “终远兄弟，谓他人父。”\n  - “谓他人父，亦莫我顾。”'''),
        ]

        # 创建多列
        cols = st.columns(5)  # 根据需要调整列数

        for col, (title, content) in zip(cols, poems):
            with col:
                # 使用更小号的标题字体
                st.markdown(f"<h4 style='text-align: center; font-size:18px;'>{title}</h4>", unsafe_allow_html=True)
                st.write(content)

        st.subheader('1. Seasonal connections ')
        tabs = st.tabs(["Statistical Results", "Symbolism"])
        contents = [
            '''By screening the poems related to ‘葛 (Kudze)’ in The Book of Songs and the time elements contained in them, the results show that among the 16 occurrences of ‘葛’, 5 are in ‘spring’, 4 in ‘autumn’, 3 in ‘winter’, 1 in ‘summer’, and the remaining 3 do not clearly reflect the seasonal characteristics. The results show that of the 16 occurrences of ‘葛’, 5 are in ‘spring’, 4 in ‘autumn’, 3 in ‘winter’, 1 in ‘summer’, and the remaining 3 do not clearly reflect the seasonal characteristics. Thus, in terms of seasons, ‘葛’ is more often associated with spring, followed by autumn and winter, and also with summer. This has something to do with the characteristics of ‘葛’ itself. In Shuowen Jiezi (說文解字), ‘葛’ means ‘grass’, which can grow all year round as long as the environment allows. At the same time, the fibres of ‘葛’ can be woven into cloth, which is closely related to clothes. Therefore, words related to wearing clothes appear several times in the poem, such as ‘葛屢 (grass shoes)’ three times, i.e., ‘葛屨五兩，冠緌雙止’ (國風·齊風·南山) , ‘糾糾葛屨，可以履霜’ (小雅·小旻之什·大東).<br>Specifically, spring is the most frequently mentioned season in these poems, with a total of five poems related to spring. Most of these poems depict the growth and gathering of kudzu, such as the description of the luxuriant growth of kudzu in the valley in ‘國風·周南·葛覃’ and the expression of longing for the kudzu gatherers in ‘國風·鄭風·采葛’. There are three poems related to autumn, such as ‘國風·邶風·旄丘’ and ‘國風·王風·葛藟’, in which most of the verses express thoughts of distant relatives and feelings about fate. Three poems are related to winter, such as ‘國風·齊風·南山’ and ‘小雅·小旻之什·大東’. The image of kudzu in these verses is mostly associated with cold frosts, symbolising resilience and vitality. One poem is associated with summer, namely ‘國風·魏風·葛屨’, which describes the use of kudzu shoes to tread on frost, reflecting the use of kudzu products in summer.\nApart from this, there is no explicit reference to a specific month in the verses, so the distribution of months cannot be analysed in detail. The verses also do not mention the specific hour, so the distribution of the hour cannot be analysed. However, from the content of the verses, most of them are related to daily work and life, which may coincide with the farming life of working at sunrise and resting at sunset.''',
            '''‘葛’ is not only a plant in nature in these verses, but also carries a rich symbolic meaning. It is not only a symbol of life force, but also a carrier of thoughts and emotions. The growth, collection and use of kudzu in the verses are closely related to people's daily life, reflecting the ancient people's lifestyle of living in harmony with nature. Whether it is the longing for loved ones, the feeling of fate or the desire for a better life, kudzu grass has become an important medium for the poet to express his emotions. To sum up, these verses not only depict the growth of kudzu grass in different seasons, but also reflect the ancient people's delicate observation and deep perception of natural landscape, as well as the important position of kudzu grass in ancient social life.''',
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content, unsafe_allow_html=True)

        st.subheader('2. Emotional associations')
        tabs = st.tabs(["Diligent Living", "Thoughts of Longing", "Filial piety (归宁孝道)", "Mourning",
                        "Estrangement of Relatives"])
        contents = [
            '''《周南·葛覃》:“葛之覃兮，施于中谷，维叶萋萋。是刈是濩，为絺为。”<br>Kudzu is often associated with women's hard work and family life. This poem describes the growth of Kudzu and the labor of women, showing women harvesting kudzu vines, cooking the fibers, and weaving them into cloth, reflecting praise for hard work and women's contribution to the family.''',
            '''《王风·采葛》,:“彼采葛兮，一日不见，如三月兮！”<br>This poem expresses the deep longing for the woman who picks kudzu, and the fact that one day's absence is like three autumns, showing the intensity of the emotion and the longing for the beloved through the exaggerated sense of time. Here the word “kudzu” is used as a starting point, which actually comes from the daily life of production and is used as a starting point.''',
            '''《周南·葛覃》, “言告师氏，言告言归。薄污我私，薄澣我衣。害澣害否？归宁父母。”<br>Here, a woman is preparing to go home to visit her parents after laboring, reflecting filial piety and the importance of family.''',
            '''《唐风·葛生》, “葛生蒙楚，蔹蔓于野。予美亡此，谁与独处？”<br>Through the scene that the kudzu vine is left untended and wild to express the pain of mourning for the female lover, the worst result of planting kudzu is used as a metaphor for the sadness and misfortune of losing a lover.''',
            '''《王风·葛藟》中，“绵绵葛藟，在河之浒。终远兄弟，谓他人父。”<br>Here, the poem describes a scene where the growth pattern of the kudzu vine branches out without being able to support each other. It is a metaphor for the estrangement and strangeness between members of the kinship.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content, unsafe_allow_html=True)

        st.subheader('3. Human qualities')
        st.write('''
                    《周南·葛覃》

                    葛之覃兮，施于中谷，维叶萋萋。黄鸟于飞，集于灌木，其鸣喈喈。

                    葛之覃兮，施于中谷，维叶莫莫。是刈是濩，为絺为綌，服之无斁。

                    言告师氏，言告言归。薄污我私，薄澣我衣。害澣害否？归宁父母。
                    ''')

        st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/9.PNG', width=300)

        tabs = st.tabs(["Diligence", "Filial Piety", "Sense of Responsibility"])
        contents = [
            "The woman in the poem not only collects kudzu vines, but also personally weaves and makes clothes, which reflects the diligent qualities of ancient women. They not only had to participate in field work, but also be responsible for the textile work at home. This diligent spirit was an expectation and requirement of society for women at that time.",
            "The poem mentions a woman preparing to wash her clothes in order to visit her parents at home, which demonstrates her filial piety towards her parents. In the social context of that time, women still had to visit their parents' homes regularly after getting married to show respect and care for their parents.",
            "While preparing to return to her mother's home, the woman did not forget to seek advice from Shi, which shows her emphasis on family responsibilities. She not only has to take care of her own family, but also cares about the health of her parents, and this sense of responsibility is an important component of her personal qualities."
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)


    elif plant_page == '🌾 Millet':
        st.header('🌾 Millet 黍')
        st.write('''
                        While millet is no longer the staple food of modern people, in the northern regions of China, glutinous millet, especially the sticky variety, is a high-quality glutinous food that can be used to make a variety of pastries and festive foods. When Qu Yuan died of drowning in the river, the people of Chu used millet to make zongzi as an offering in his honor. 

                        This section describes the season of harvest, where the grains and millets pile high in heaps, which is the greatest reward for a year's worth of hard work. This further highlights millet being very popular in accient china especially during The Spring and Autumn Period.

                        《周颂·丰年》: "丰年多黍多稌, 亦有高廪,万亿及秭。"

                        ''')

        st.subheader('Symbolic Poems Associated with the Plant')
        poems = [
            ("《王风·黍离》",
             '''- 彼黍离离，彼稷之苗。行迈靡靡，中心摇摇。\n- 彼黍离离，彼稷之穗。行迈靡靡，中心如醉。\n- 彼黍离离，彼稷之实。行迈靡靡，中心如噎。'''),
            ("《硕鼠》",
             '''- 硕鼠硕鼠，无食我黍！三岁贯女，莫我肯顾。逝将去女，适彼乐土。乐土乐土，爰得我所。\n- 硕鼠硕鼠，无食我麦！三岁贯女，莫我肯德。逝将去女，适彼乐国。乐国乐国，爰得我直。\n- 硕鼠硕鼠，无食我苗！三岁贯女，莫我肯劳。逝将去女，适彼乐郊。乐郊乐郊，谁之永号？'''),
            ("《黍苗》",
             '''- 芃芃黍苗，阴雨膏之。\n- 悠悠南行，召伯劳之。\n- 我任我辇，我车我牛。\n- 我行既集，盖云归哉。'''),
            ("《七月》",
             '''- 六月食郁及薁，七月亨葵及菽，八月剥枣，十月获稻，为此春酒，以介眉寿。七月食瓜，八月断壶，九月叔苴，采荼薪樗，食我农夫。\n- 九月筑场圃，十月纳禾稼。黍稷重穋，禾麻菽麦。嗟我农夫，我稼既同，上入执宫功。昼尔于茅，宵尔索綯。亟其乘屋，其始播百谷。'''),
            ("《小雅·甫田》",
             '''- 倬彼甫田，岁取十千。我取其陈，食我农人。自古有年。今适南亩，或耘或耔。黍稷薿薿，攸介攸止，烝我髦士。\n- 以我齐明，与我牺羊，以社以方。我田既臧，农夫之庆。琴瑟击鼓，以御田祖。以祈甘雨，以介我稷黍，以穀我士女。'''),
        ]

        # 创建多列
        cols = st.columns(5)  # 根据需要调整列数

        for col, (title, content) in zip(cols, poems):
            with col:
                # 使用更小号的标题字体
                st.markdown(f"<h4 style='text-align: center; font-size:18px;'>{title}</h4>", unsafe_allow_html=True)
                st.write(content)

        st.subheader('1. Seasonal connections ')
        tabs = st.tabs(["Statistical Results", "Nature and Human Activities"])
        contents = [
            '''By screening the poems related to ‘黍 (Millet)’ in The Book of Songs and the time elements contained in them, the results show that among the 23 occurrences of ‘黍’, 6 are in ‘autumn’, 5 are in ‘spring’, 4 are in ‘spring and autumn’ together, and 1 is in ‘spring, autumn and winter’ together, while the remaining 7 do not clearly reflect the seasonal characteristics. The results show that of the 16 occurrences of ‘Ge’, 6 are in ‘autumn’, 5 in ‘spring’, 4 in ‘spring and autumn’, 1 in ‘spring, autumn and winter’, and the remaining 7 do not clearly reflect seasonal characteristics. The remaining seven poems do not clearly reflect the seasonal characteristics. It can be seen that ‘黍’ mainly appears in the spring and autumn seasons.''',
            '''Specifically, there are a number of poems related to spring, such as ‘國風·曹風·下泉’, ‘小雅·北山之什·信南山’, etc. These poems depict the scenes of spring, such as the growth of millet seedlings and the nourishment of the spring rains, which reflect the agricultural activities and natural landscapes in the spring. There are also a number of poems related to autumn, such as ‘國風·王風·黍離’ and ‘國風·豳風·七月’, etc. These verses describe the harvest scenes in autumn, such as the ripening and harvesting of millet and grains, reflecting the agricultural labour and the joy of harvesting in autumn. One poem is related to winter, such as ‘小雅·北山之什·信南山’, in which the poem expresses the coldness of winter and the longing for warmth through the metaphor of millet. Some verses relate to more than one season, such as ‘小雅·北山之什·莆田’, which describes agricultural activities from spring to autumn, showing the farming cycle of the four seasons of the year.<br>  These verses focus on the farming activities of ancient agricultural societies, such as sowing, harvesting, and storage, which are closely related to seasonal changes, reflecting the ancient people's adherence to and use of the laws of nature. The verses not only describe farming activities, but also express thoughts of home and relatives and worries about the fate of the country. Through the description of crops such as millet and grain, these poems show the economic basis of ancient society and the living conditions of the people. '''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.markdown(content, unsafe_allow_html=True)

        st.subheader('2. Emotional associations')
        tabs = st.tabs(
            ["The pain of a fallen country and the mourning of the deceased country", "Hate the Exploitation"])
        contents = [
            '''《诗经·王风·黍离》:“彼黍离离，彼稷之苗”<br>This poem expressed by the poet passing the ruins of the former capital of the 宗周, seeing the past prosperous capital city sorghum, millet grows very lush, causing infinite sadness. The poet expresses the country's former prosperity and present decline of the feelings of sadness of deplorable. This kind of emotion is called “黍离之悲”, which unites the pathos of losing one's homeland and having nothing to do with it.''',
            '''《魏风·硕鼠》, “硕鼠硕鼠，无食我黍！"<br>This verse expresses the laborers' hatred for the insatiable exploiters and their desire for a better life. Millet is compared to the fruit of the laborers' work, denouncing the exploiters for their greediness and cunningness, and for their lack of consideration for other people's lives and deaths. In other chapters of the Book, Millet also symbolizes the fruits of labor, such as “不能蓺稷黍” in 《唐风·鸨羽》, which expresses the helplessness of not being able to go home to cultivate Jigen and Millet due to the endless compulsory labor of the princes' and lords' families.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.markdown(content, unsafe_allow_html=True)

        st.subheader('3. Human qualities')
        st.write('''
                            《小雅·甫田》

                            倬彼甫田，岁取十千。我取其陈，食我农人。自古有年。今适南亩，或耘或耔。黍稷薿薿，攸介攸止，烝我髦士。

                            以我齐明，与我牺羊，以社以方。我田既臧，农夫之庆。琴瑟击鼓，以御田祖。以祈甘雨，以介我稷黍，以穀我士女。

                            曾孙来止，以其妇子。馌彼南亩，田畯至喜。攘其左右，尝其旨否。禾易长亩，终善且有。曾孙不怒，农夫克敏。

                            曾孙之稼，如茨如梁。曾孙之庾，如坻如京。乃求千斯仓，乃求万斯箱。黍稷稻粱，农夫之庆。报以介福，万寿无疆。
                            ''')

        st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/7.PNG', width=300)

        tabs = st.tabs(["Concern for the Nation's Fate", "Diligence and Harvest"])
        contents = [
            '''The terms "millet" and "millet" in "Shuli" are not just crops. The growth status of millet in the poem reflects the poet's deep concern for the rise and fall of the country and his sense of responsibility in personal qualities. When facing the ruins of his homeland, the poet feels deeply worried and helpless. At the same time, the poem "Those who know me, call my heart worried; those who don't know me, call me what I want" expresses the poet's profound understanding of understanding and misunderstanding, as well as the feeling of difficulty in finding a kindred spirit. This reflects the poet's emphasis on understanding and communication in interpersonal relationships, and is also a virtue in personal qualities.''',
            '''"Shuo" in the Book of Songs symbolizes both diligence and harvest, reflecting people's pursuit of hard work, wealth, and a better life. For example, in 《小雅·甫田》, "The crops of great grandchildren are like grains and beams. The crops of great grandchildren are like grains and beams. The jade of great grandchildren are like earth and the capital. They seek a thousand grain granaries and ten thousand grain boxes. The harvest of millet, grains, rice, and beams is a celebration for farmers" describes how great grandchildren obtained abundant crops through diligent farming, reflecting the virtue of hard work and wealth.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.markdown(content, unsafe_allow_html=True)


    elif plant_page == '🍃 Grass':
        st.header('🍃 Grass 蔓草/野草')

        st.subheader('Symbolic Poems Associated with the Plant')
        poems = [
            ("《伯兮》",
             '''- 伯兮朅兮，邦之桀兮。伯也执殳，为王前驱。\n- 自伯之东，首如飞蓬。岂无膏沐？谁适为容！\n- 其雨其雨，杲杲出日。愿言思伯，甘心首疾。\n- 焉得谖草？言树之背。愿言思伯。使我心痗。'''),
            ("《郑风·野有蔓草》",
             '''- “野有蔓草，零露漙兮。有美一人，清扬婉兮。邂逅相遇，适我愿兮。”\n- “野有蔓草，零露瀼瀼。有美一人，婉如清扬。邂逅相遇，与子偕臧。'''),
            ("《国风·卫风·伯兮》",
             '''- “自伯之东，首如飞蓬。岂无膏沐，谁适为容？”\n- “焉得谖草，言树之背。愿言思伯，使我心痗。”'''),
            ("《湛露》",
             '''- 湛湛露斯，匪阳不晞。\n- 厌厌夜饮，不醉无归。\n- 湛湛露斯，在彼丰草。\n- 厌厌夜饮，在宗载考。'''),
            ("《何草不黄》",
             '''- 何草不黄？何日不行？何人不将？经营四方。\n- 何草不玄？何人不矜？哀我征夫，独为匪民。\n- 匪兕匪虎，率彼旷野。哀我征夫，朝夕不暇。\n- 有芃者狐，率彼幽草。有栈之车，行彼周道。'''),
        ]

        # 创建多列
        cols = st.columns(5)  # 根据需要调整列数

        for col, (title, content) in zip(cols, poems):
            with col:
                # 使用更小号的标题字体
                st.markdown(f"<h4 style='text-align: center; font-size:18px;'>{title}</h4>", unsafe_allow_html=True)
                st.write(content)

        st.subheader('1. Seasonal connections ')
        tabs = st.tabs(["Statistical Results", "Nature and Human Activities"])
        contents = [
            '''By screening the poems related to ‘草 (grass)’ in The Book of Songs and the time elements contained in them, the results show that among the 14 occurrences of ‘草’, 5 are in ‘autumn’, 4 in ‘spring’, 1 in ‘summer’, and the remaining 4 do not clearly reflect the seasonal characteristics. The results show that of the 14 occurrences of ‘grass’ in the poem, 5 are in ‘autumn’, 4 in ‘spring’, 1 in ‘summer’, and the remaining 4 do not clearly reflect the seasonal characteristics. It is clear that ‘草’ mainly appears in spring and autumn.''',
            '''Spring features prominently in these poems, such as ‘野有蔓草、零露漙兮’, ‘野有蔓草、零露瀼瀼’ (‘國風·鄭風·野有蔓草’), and ‘喓喓草蟲、趯趯阜螽’ (‘小雅·鹿鳴之什·出車’), etc., depicting the natural scenery and emotional experience of spring, embodying the vitality and vigour of spring. Autumn is also a frequent season, such as ‘湛湛露斯，在彼豐草’ (‘小雅·白華之什·湛露’), etc. Most of these verses express the sullenness of autumn, thoughts of longing, and scenes after a good harvest. There are fewer verses in summer, but for example, ‘小雅·彤弓之什·車攻’ depicts the scene of field hunting in summer, reflecting the warmth and activity of summer.<br>These verses closely connect the natural landscape with the characters' emotions through the imagery of grass, such as the sprawling grass in spring and the joy of encountering a meeting, and the grass and insects in autumn and the thoughts of a gentleman. The imagery of grass in the verses is not only used to express personal emotions, but also reflects the social life of the time, such as farming, hunting and war. The growth and decay of grass symbolise the change of seasons and the passage of time, for example, the yellowing of grass in ‘小雅·都人士之什·何草不黃’ symbolises the coming of autumn. The vitality and decay of grass also provokes thoughts on life, morality and politics, such as the lack of lushness of grass symbolising the decline of the state in ‘大雅·蕩之什·召旻’.<br>To sum up, through the depiction of grass, these verses show the ancient poets' deep understanding and expression of nature, emotion, society and philosophy, reflecting the rich connotation and artistic charm of the Book of Songs as an important part of the treasury of classical Chinese literature.'''

        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.markdown(content, unsafe_allow_html=True)

        st.subheader('2. Emotional associations')
        tabs = st.tabs(["Weakness and Decay", "Longing and Sorrow", "Surprise and Joy", ])
        contents = [
            '''In some verses, grass is depicted as weak and withered. For example, in "《诗经·邶风·谷风》", the phrase "采葑采菲，无以下体" illustrates the image of withered grass, showing a state of weakness and fragility.''',
            '''Grass is also associated with emotions of longing and sorrow. For instance, in The Book of Songs 《卫风·伯兮》, "焉得谖草，言树之背。愿言思伯，使我心痗。", "谖草," also known as the forget-me-not or daylily, symbolizes the desire to forget the sorrow of a husband's long absence. Similarly, 《召南·草虫》, "喓喓草虫，趯趯阜螽。未见君子，忧心忡忡。亦既见止，亦既觏止，我心则降", expresses a woman’s deep longing and anticipation for her husband. The sound of the insects contrasts with her inner turmoil, amplifying the depth of her emotions.''',
            '''《郑风·野有蔓草》, "野有蔓草，零露漙兮。有美一人，清扬婉兮。邂逅相遇，适我愿兮". The lush grass and sparkling dew symbolize unexpected love and happiness, as the poet describes the joy of a serendipitous encounter with a beloved among the flourishing wild grass.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)

        st.subheader('3. Human qualities')
        st.write('''
                            《小雅·何草不黄》

                            何草不黄？何日不行？何人不将？经营四方。


                            《伯兮》

                            伯兮朅兮，邦之桀兮。伯也执殳，为王前驱。

                            自伯之东，首如飞蓬。岂无膏沐？谁适为容！

                            其雨其雨，杲杲出日。愿言思伯，甘心首疾。

                            焉得谖草？言树之背。愿言思伯。使我心痗。
                            ''')

        st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/11.PNG', width=300)

        tabs = st.tabs(["Diligent and Strong Qualities", "Loyalty and Sacrifice"])
        contents = [
            '''In this poem, 《何草不黄》 reflects the qualities of people who are not afraid of difficulties and work hard through the withering of grass and the hustle and bustle of pedestrians. The withered and yellow grass symbolizes the passage of time and the resilience of life, while "何人不将？经营四方。" depicts the image of people rushing around for life and responsibility. The grass here symbolizes resilience and vitality, echoing the indomitable and hardworking spirit of people''',
            '''Grass, this seemingly ordinary yet resilient natural image, is often endowed with rich symbolic meanings in profound cultural connotations. In the narrative depicting Bo's heroic deeds and endless loyalty to the country, grass is not just a green patch on the earth, but also a vivid metaphor, showcasing Bo's heroic posture as a forward, charging forward fearlessly.<br>Bo, the warrior of this country, his figure is like a gust of wind on the grassland, swift and unstoppable. He stood at the forefront of the battle, facing the enemy's swords and shadows, never flinching at all. In his eyes, only the peace of the country and the expectations of the king, personal life and death have long been disregarded. He deeply understands that every charge he makes is the best expression of loyalty to the country; Every time he swings his sword, it is a merciless blow to the enemy, and more importantly, to protect the land and people behind him that have nurtured him.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.markdown(content, unsafe_allow_html=True)


    elif plant_page == '🫘 Beans':
        st.header('🫘 Beans 豆')
        st.write('''
        Beans are not only an important food crop but also a significant element in social interactions and rituals.

        《小雅·采菽》：“采菽采菽，筐之莒之。君子来朝，何锡予之？虽无予之？路车乘马。又何予之？玄衮及黼。”

        This poem describes the scenario where feudal lords visit the emperor, and the emperor presents soybeans as a gift, highlighting the importance of soybeans in society at that time and their value as a gift.

        《豳风·七月》：“七月食瓜，八月断壶，九月叔苴。” 

        Here, "叔苴" (shū jū) likely refers to leguminous plants, reflecting the ancient practice of gathering and consuming beans in different seasons.

        ''')

        st.subheader('Symbolic Poems Associated with the Plant')
        poems = [
            ("《小雅·采菽》",
             '''- 采菽采菽，筐之筥之。\n- 君子来朝，何锡予之？\n- 虽无予之？路车乘马。\n- 又何予之？玄衮及黼'''),
            ("《伐柯》",
             '''- 伐柯如何？匪斧不克。\n- 取妻如何？匪媒不得。\n- 伐柯伐柯，其则不远。\n- 我觏之子，笾豆有践。'''),
            ("《伐木》",
             '''- 伐木于阪，酾酒有衍。笾豆有践，兄弟无远。民之失德，乾餱以愆。\n- 有酒湑我，无酒酤我。坎坎鼓我，蹲蹲舞我。迨我暇矣，饮此湑矣。'''),
            ("《生民》",
             '''- 诞降嘉种，维秬维秠，维穈维芑。恒之秬秠，是获是亩。恒之穈芑，是任是负。以归肇祀。\n- 诞我祀如何？或舂或揄，或簸或蹂。释之叟叟，烝之浮浮。载谋载惟。取萧祭脂，取羝以軷，载燔载烈，以兴嗣岁。\n- 卬盛于豆，于豆于登。其香始升，上帝居歆。胡臭亶时。后稷肇祀。庶无罪悔，以迄于今。'''),
            ("《既醉》",
             '''- 既醉以酒，既饱以德。君子万年，介尔景福。\n- 既醉以酒，尔肴既将。君子万年，介尔昭明\n- 昭明有融，高朗令终，令终有俶。公尸嘉告。\n- 其告维何？笾豆静嘉。朋友攸摄，摄以威仪。''')
        ]

        # 创建多列
        cols = st.columns(5)  # 根据需要调整列数

        for col, (title, content) in zip(cols, poems):
            with col:
                # 使用更小号的标题字体
                st.markdown(f"<h4 style='text-align: center; font-size:18px;'>{title}</h4>", unsafe_allow_html=True)
                st.write(content)

        st.subheader('1. Seasonal connections ')
        tabs = st.tabs(["Statistical Results", "Human Activities"])
        contents = [
            '''Sifting through the poems related to ‘豆’ in The Book of Songs and the temporal elements contained therein, it is found that ‘豆’ occurs 10 times in total, and only one of the poems is related to autumn, while the rest of the poems are not directly related to the seasons or even other temporal elements. However, nine of these ten occurrences are from the Xiaoya (小雅), Daya (大雅), and Ode (頌) sections of The Book of Songs. These sections are closely related to rituals and banquets, and are mainly concerned with recording and describing the contents and rituals of rituals and banquets.''',
            '''The ‘籩豆’ in these verses are mostly related to rituals, such as the sacrificial scenes described in ‘大雅·生民之什·生民’ and ‘頌·魯頌·閟宮’, which reflect the importance of the rituals in ancient times. The ‘籩豆’ in the verses is also closely related to the culture of feasting, such as the banquets for brothers and guests described in ‘小雅·鹿鳴之什·常棣’ and ‘小雅·鹿鳴之什·伐木’ (Xiao Ya - Lu Ming Zhi Shi - False Wood), which reflect the banquets of ancient societies. Through the setting up of ‘籩豆’ and the banqueting activities, the poems demonstrate the social interaction and the pursuit of harmonious relationships in ancient societies. For example, ‘兄弟無遠’ in ‘小雅·北山之什·楚茨’ emphasises the harmony among brothers. In the Song of Songs - Lu Song - égong, the phrase ‘籩豆大房’ is related to the theme of harvest and abundance, reflecting the celebration of and gratitude for a good agricultural harvest.<br>In summary, these verses, through their descriptions of ‘籩豆’, show the social life of ancient times in terms of rituals, banquets, socialising, and agricultural harvests, reflecting the rich cultural connotations and social values of the Classic of Poetry, as an important part of the treasure trove of classical Chinese literature.'''
        ]

        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content, unsafe_allow_html=True)

        st.subheader('2. Emotional associations')
        tabs = st.tabs(["Rituals and Reverence", "Harmony", "Respect"])
        contents = [
            '''In the book of poems,  《诗经·大雅·生民》“卬盛于豆，于豆于登，其香始升。上帝居歆，胡臭亶时。.” It describes a ritual in which food is served in beans (an ancient food container), and as the aroma of the food rises, it expresses reverence for God and prayers for the gods to enjoy it.''',
            '''“我觏之子、笾豆有践。” in 《幽风·伐柯》 describes the harmonious scene of people gathering together and sharing food at a banquet, reflecting the friendly interaction and affection between people.''',
            '''In 《诗经·小雅·宾之初筵》，“宾之初筵、左右秩秩。笾豆有楚、淆核维旅”，The first banquet of the guest was held in an orderly manner, and the guests were seated in accordance with the etiquette, reflecting the respect and courtesy shown to the guests.'''
        ]

        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)

        st.subheader('3. Human qualities')
        st.write('''
                            《幽风·伐柯》

                            伐柯如何、匪斧不克。取妻如何、匪媒不得。

                            伐柯伐柯，其则不远。我覯之子，籩豆有践。

                            《小雅·宾之初筵》

                            賓之初筵、左右秩秩。籩豆有楚、殽核維旅。

                            酒既和旨、飲酒孔偕。鐘鼓既設、舉醻逸逸。
                            ''')

        st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/12.PNG', width=300)

        tabs = st.tabs(["Family Affection", "Order and Harmony"])
        contents = [
            '''This poem represents the arrangement and preparation of food, symbolizing the thoughtfulness of the banquet and respect for guests. "兄弟无远" expresses the idea of strengthening family and friendship, eliminating barriers, and enhancing connections between each other through banquets. Therefore, 'beans' here symbolize the close connection between friendship and family, as well as respect and courtesy towards guests.''',
            '''In these texts, '豆' is mentioned alongside '笾,' depicting the meticulous arrangement of food at a banquet, which mirrors the solemnity and orderliness of the event. Consequently, 'beans' emblemize the structured harmony that characterizes the feast."'''
        ]

        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)


    elif plant_page == '🌲 Pine and Cypress':
        st.header('🌲 Pine and Cypress 松柏')
        st.write('''
                        Unlike the deciduous trees that change color and shed their leaves in the autumn, the needles of pine a remain green all year round, even in the winter. This characteristic adds vitality to the cold season. Their wood, known for its corrosion resistance and strength, is often used in the construction of palaces and boats.

                        《商颂·殷武》：“松桷有梴，旅楹有闲，寝成孔安。”

                        This extract describes: "Pine beams with branches, traveling pillars with leisure, the sleeping temple is very peaceful," indicating that pine wood was used to build sleeping temples, showing its magnificence. 

                        《邶风·柏舟》：“泛彼柏舟，亦泛其流 。”

                        《鄘风·柏舟》：“泛彼柏舟，在彼中河。”

                        《卫风·竹竿 》：“淇水浟浟，桧楫松舟。”

                        Here, the boat made of cypress wood, "柏舟," is used to express a sense of responsibility of "worrying about the monarch while being far from the rivers and lakes," as well as a clean and elegant life that does not follow the world's corruption. The cypress boat is a state of being a person. It also symbolizes a lofty state of living a quiet and nurturing life.
                        ''')

        st.subheader('Symbolic Poems Associated with the Plant')
        poems = [
            ("《小雅·斯干》",
             '''- 秩秩斯干，幽幽南山。如竹苞矣，如松茂矣。兄及弟矣，式相好矣，无相犹矣。\n- 似续妣祖，筑室百堵，西南其户。爰居爰处，爰笑爰语。\n- 约之阁阁，椓之橐橐。风雨攸除，鸟鼠攸去，君子攸芋。\n- 如跂斯翼，如矢斯棘，如鸟斯革，如翚斯飞，君子攸跻。\n- 殖殖其庭，有觉其楹。哙哙其正，哕哕其冥。君子攸宁。'''),
            ("《商颂·殷武》",
             '''- 商邑翼翼，四方之极。赫赫厥声，濯濯厥灵。寿考且宁，以保我后生。\n- 陟彼景山，松柏丸丸。是断是迁，方斫是虔。松桷有梴，旅楹有闲，寝成孔安。'''),
            ("《天保》",
             '''- 吉蠲为饎，是用孝享。禴祠烝尝，于公先王。君曰：卜尔，万寿无疆。\n- 神之吊矣，诒尔多福。民之质矣，日用饮食。群黎百姓，遍为尔德。\n- 如月之恒，如日之升。如南山之寿，不骞不崩。如松柏之茂，无不尔或承。'''),
            ("《頍弁》",
             '''- 有頍者弁，实维伊何？尔酒既旨，尔肴既嘉。岂伊异人？兄弟匪他。\n- 茑与女萝，施于松柏。未见君子，忧心奕奕；既见君子，庶几说怿。\n- 有頍者弁，实维何期？尔酒既旨，尔肴既时。岂伊异人？兄弟具来。\n- 茑与女萝，施于松上。未见君子，忧心怲々；既见君子，庶几有臧。'''),
            ("《皇矣》",
             '''- 帝省其山，柞棫斯拔，松柏斯兑。帝作邦作对，自大伯王季。维此王季，因心则友。则友其兄，则笃其庆，载锡之光。受禄无丧，奄有四方。'''),
        ]

        # 创建多列
        cols = st.columns(5)  # 根据需要调整列数

        for col, (title, content) in zip(cols, poems):
            with col:
                # 使用更小号的标题字体
                st.markdown(f"<h4 style='text-align: center; font-size:18px;'>{title}</h4>", unsafe_allow_html=True)
                st.write(content)

        st.subheader('1. Seasonal connections ')
        tabs = st.tabs(["Statistical Results", "Symbolism"])
        contents = [
            '''By filtering the poems related to ‘松 (Pine)’ and ‘柏 (Cypress)’ in The Book of Songs and the temporal elements contained in them, the results show that ‘松’ and ‘柏’ appear eight times each, and are often mentioned together (four times in total). ''',
            '''However, the relationship between pine and cypress and time is also not very strong, with only one poem (‘颂·鲁颂·閟宫’) reflecting autumn, and none of the other verses reflecting seasons or other temporal elements, which is perhaps also related to the evergreen nature of the pine and cypress, which makes them symbols of longevity and eternity, such as ‘如南山之壽、不騫不崩。如松柏之茂、無不爾或承’ in ‘小雅·鹿鳴之什·天保’, which reflects people's desire and respect for the evergreen nature.'''
        ]

        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)

        st.subheader('2. Emotional associations')
        tabs = st.tabs(
            ["Resilience and Heroism", "Historical Mission and Sense of Concern", "Profound Longing and Inner Sorrow"])
        contents = [
            '''Pine and cypress, because of its evergreen, never withering characteristics, was given the connotation of personality, symbolizing the heroic spirit of steadfastness and indomitable. For example, in 《小雅·斯干》,“如竹苞矣，如松茂矣”, with the pine luxuriant to symbolize the prosperity, tenacity and indomitable spiritual qualities.''',
            '''The imagery of pines and cypresses also reflects a strong sense of historical mission and a sense of concern, such as the 《大雅·皇矣》 in the “帝省其山，柞棫斯拔，松柏斯兑” symbolizes the sense of historical mission.''',
            '''In 《卫风·竹竿》, the poem “淇水滺滺，桧楫松舟”, the woman's deep longing for her home town in the faraway country and her inner sadness are expressed through the imagery of the pine boat. The word “pine” here not only represents the strength and durability of pine wood, but also symbolizes the woman's deep affection for her hometown and her longing for her loved ones. The drifting of the pine boat in the Qi water symbolizes the woman's inner wandering and anxiety.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)

        st.subheader('3. Human qualities')
        st.write('''
                            《小雅·斯干》

                            秩秩斯干，幽幽南山。如竹苞矣，如松茂矣。

                            《大雅·皇矣》

                            帝省其山，柞棫斯拔，松柏斯兑。
                            ''')

        st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/13.PNG', width=300)

        tabs = st.tabs(["Perseverance and Mutual Support", "Resilience in Adversity"])
        contents = [
            '''"如竹苞矣，如松茂矣： expresses the image of pine trees flourishing and standing tall, symbolizing the noble qualities and strong will of human beings. The word 'pine' here not only represents the vitality of nature, but also symbolizes the indomitable and persevering spirit of people in the face of difficulties and challenges. The characteristic of pine trees echoes the virtues of harmonious coexistence and mutual support among brothers, reflecting the emphasis on the value of family and social harmony.''',
            '''The "pine and cypress" in "松柏斯兑" symbolizes steadfast purity and indomitable spirit. Pine and cypress trees were regarded as symbols of nobility and strength in ancient times. They were able to maintain their upright posture even in harsh environments, which corresponds to the firm will and noble character displayed by people in the face of adversity. This unyielding spirit is a precious asset to personal qualities and also a moral standard respected by society.'''
        ]

        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)


    elif plant_page == '🎋 Bamboo':
        st.header('🎋 Bamboo 竹')
        st.write('''
                        In ancient times, Bamboo served as musical instruments, material to make books, and a variety of daily utensils. Various bamboo-made musical instruments were mentioned in the book, such as flutes, pipes, sheng (a reed mouth organ), and yue (a type of ancient Chinese flute). Many bamboo made utensils where also described, including baskets, tubs, winnowing baskets, boxes, fish traps, hats, small bamboo cages, and bamboo containers.

                        《小雅•鹿鸣》：“呦呦鹿鸣，食野之苹。我有嘉宾，鼓瑟吹笙。”

                        This extract was sung at banquets by the ancients. According to Zhu Xi's, it was originally sung by the monarch when entertaining his ministers, and later it gradually spread to the common people and being sung at village banquets. The song begins by depicting a scene on the open plain where a herd of deer leisurely feeds on wild grass. The occasionally emitting a melodious cry 'you you', creating a harmonious and pleasing sound. The poem uses this scene to set a warm and harmonious atmosphere. This highlights the common use of bamboo as a musical instrument, accompanying the sheng music at court banquets.
                        ''')

        st.subheader('Symbolic Poems Associated with the Plant')
        poems = [
            ("《淇奥》",
             '''- 瞻彼淇奥，绿竹猗猗。有匪君子，如切如磋，如琢如磨，瑟兮僴兮，赫兮咺兮。有匪君子，终不可谖兮。\n- 瞻彼淇奥，绿竹青青。有匪君子，充耳琇莹，会弁如星。瑟兮僴兮。赫兮咺兮，有匪君子，终不可谖兮。\n- 瞻彼淇奥，绿竹如箦。有匪君子，如金如锡，如圭如璧。宽兮绰兮，猗重较兮。善戏谑兮，不为虐兮。'''),
            ("《竹竿》",
             '''- 籊籊竹竿，以钓于淇。岂不尔思？远莫致之。\n- 泉源在左，淇水在右。女子有行，远兄弟父母。\n- 淇水在右，泉源在左。巧笑之瑳，佩玉之傩。\n- 淇水滺滺，桧楫松舟。驾言出游，以写我忧。'''),
            ("《诗经·小雅·斯干》",
             '''- 秩秩斯干，幽幽南山。\n- 如竹苞矣，如松茂矣。\n- 兄及弟矣，式相好矣，无相犹矣。'''),
            ("《小戎》",
             '''- 俴驷孔群，厹矛鋈錞。\n- 蒙伐有苑，虎韔镂膺。\n- 交韔二弓，竹闭绲滕。\n- 言念君子，载寝载兴。\n- 厌厌良人，秩秩德音。''')
        ]

        # 创建多列
        cols = st.columns(4)  # 根据需要调整列数

        for col, (title, content) in zip(cols, poems):
            with col:
                # 使用更小号的标题字体
                st.markdown(f"<h4 style='text-align: center; font-size:18px;'>{title}</h4>", unsafe_allow_html=True)
                st.write(content)

        st.subheader('1. Seasonal connections ')
        tabs = st.tabs(["Statistical Results", "Symbolism"])
        contents = [
            '''By filtering the poems related to ‘竹 (Bamboo)’ in The Book of Songs and the time elements they contain, the results show that ‘竹’ appears 6 times, of which 3 times are in ‘spring’, and the remaining 3 times are in unknown seasons. <br>There are a number of poems related to spring, such as ‘瞻彼淇奧、綠竹猗猗’ and ‘瞻彼淇奧、綠竹青青’ in ‘國風·衛風·淇奧’, which depict the scene of lush green bamboo by the Qi water in spring, reflecting the vitality and vigour of spring. ''',
            '''Through the depiction of bamboo, these verses show the ancient poets' profound understanding and expression of nature, emotion, society and craftsmanship, reflecting the rich cultural connotations and social values of The Book of Songs as an important part of the treasury of classical Chinese literature. Through the depiction of bamboo, the poet conveys his admiration for the beauty of nature, his celebration of the virtues of a gentleman, and his yearning for a harmonious society.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content, unsafe_allow_html=True)

        st.subheader('2. Emotional associations')
        tabs = st.tabs(["Praise", "Homeland Sentiment", "Love"])
        contents = [
            '''In The Book of Songs:《国风·淇奥》, the verse“瞻彼淇奥，绿竹猗猗。有匪君子，如切如磋，如琢如磨”uses the lush and vibrant bamboo along the Qi River to extol the lofty virtues of a gentleman. The upright and verdant nature of the bamboo symbolizes the gentleman's integrity and cultivation, while the imagery of “如切如磋，如琢如磨 emphasizes the meticulous refinement of his character.''',
            '''《小雅·斯干》 creates a peaceful and tranquil natural environment by depicting clear streams, deep southern mountains, dense bamboo forests, and pine forests, symbolizing attachment to home and reverence for nature. In the poem, the phrase '兄及弟矣，式相好矣，无相犹矣' expresses the harmony and friendship between brothers, reflects the unity and harmony within the family, and is an important factor in maintaining family stability and prosperity.''',
            '''  In this poem, the emotion of longing is beautifully conveyed through the image of "籊籊竹竿": the poet stands alone by the Qi River, holding the fishing rod, its gentle swaying mirroring the fluctuations of their thoughts. The act of fishing subtly implies the desire to "catch" their beloved. The emotional progression moves from the tangible "籊籊竹竿" to the internal questioning "岂不尔思," and finally to the helpless realization "远莫致之," creating a poignant transition from hope to resignation. This portrays the melancholy of one who carries deep affection yet cannot reach their beloved. The longing expressed here is pure and profound, as steadfast as the bamboo itself-even knowing that reunion is impossible, they still faithfully wait by the water, expressing their endless yearning in this subtle yet sincere manner.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)

        st.subheader('3. Human qualities')
        st.write('''
                            《卫风·淇奥》

                            瞻彼淇奥，绿竹猗猗。有匪君子，如切如磋，如琢如磨。

                            《小雅·斯干》

                            如竹苞矣，如松茂矣。兄及弟矣，式相好矣，无相犹矣。
                            ''')

        st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/14.PNG', width=300)

        tabs = st.tabs(["Integrity and Humility", "Unity and Harmony"])
        contents = [
            '''In this poem, 绿竹猗猗' depicts the lush bamboo forest along the banks of the Qi River, symbolizing the virtues of a gentleman. The upright, verdant, and resilient nature of bamboo symbolizes the noble qualities and strong will of a gentleman. The "bamboo" here represents the integrity, humility, and elegance of a gentleman, reflecting the praise and longing for the moral character of a gentleman.''',
            '''In 《小雅·斯干》, the phrase "如竹苞矣" is taken from the characteristics of lush bamboo clusters, symbolizing brotherhood and harmony. The "bamboo" here symbolizes family harmony and brotherly solidarity, reflecting people's emphasis and admiration for harmonious family relationships. The lush and vibrant bamboo symbolizes harmony and support among family members, reflecting the virtues of unity and mutual assistance.'''
        ]
        for tab, content in zip(tabs, contents):
            with tab:
                st.write(content)

elif page == '😊 Interaction':
    cover_photo_path = "https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/17.PNG"
    st.image(cover_photo_path, use_column_width=True)

    st.title('😊 Interaction')
    # st.write('Here you can find information about our team and our history.')

    st.header('''1. "A Poet's Quest" Interactive Game''')
    st.write('''
    ⭐🌿 Let's Embark on a Journey Through Poetry, Plants, and Time!

    This is an interactive, educational storytelling experience where you embark on a journey as a poet. The game combines visual elements, audio, and interactive features to create a captivating experience.

    ''')

    # 定义要嵌入的网页链接
    url = "https://view.genially.com/673c89a7fffb4fdecd627489/interactive-image-a-poets-quest"
    # 使用HTML的iframe元素嵌入网页
    iframe_html = f"""
        <iframe src="{url}" width="100%" height="400" frameborder="0">
            <p>您的浏览器不支持iframe标签。</p>
        </iframe>
        """
    # 使用st.markdown展示iframe，并设置unsafe_allow_html=True允许HTML代码渲染
    st.markdown(iframe_html, unsafe_allow_html=True)
    # 添加一个链接，点击可以直接跳转到网页
    st.markdown(f"[Click here.]({url})", unsafe_allow_html=True)

    st.subheader("🔍 Navigating the Game")
    categories_content = {
        "🚀 To Start": '''After loading, click through the buttons to uncover details, click "Start" button to begin your quest.''',
        "🎮 Interactive Elements": "Look for clickable icons, buttons, or images throughout the game. These will allow you to:\n  - Uncover interesting facts about the plants\n  - Interact with objects or characters, find the key to advance the storyline\n  - You can revisit previous sections by clicking on the left button on the side of the screen",
        "🧐 Explore Thoroughly": "Click on all interactive elements to uncover hidden clues and secrets.",
        "🎁 Find the treasure!": "Complete the quest to find a hidden surpise!"
    }
    # 创建展开框显示各类别内容
    for category, content in categories_content.items():
        with st.expander(f"{category}"):
            st.write(content)

    st.header('2. “古人看花” Mini-Programme')
    st.write('''
        ✨🌸 Welcome to Our WeChat Mini Program! 

        Discover the wonders of plants like never before! 🌿 Through this mini program, you can explore new plant species 🌼, view plants from the perspective of ancient cultures 📜, and uncover the emotions and historical stories they represent 💕📖. Let's dive into the beauty of nature together! 

        Please scan the QR code below:

        ''')
    st.image('https://github.com/DMGT-0810/CHC5904/blob/8652118f2b19b34c2c20d5432b9e3be203982b72/digital/image/10.PNG', width=300)

    st.subheader("🔍 User Guide")
    categories_content = {
        "📷 Scan the QR Code to Access the Mini Program": "- Use your WeChat app to scan the QR code.\n- Apply for experience permissions if required.",
        "🌿 Upload or Take a Photo of a Plant": "Once inside the Mini Program, you can either upload an existing photo of a plant or take a new one directly using your device's camera.",
        "🤖 Plant Identification with AI": "After uploading the image, the program uses Baidu's image recognition API to identify the plant species for you.",
        "📜 Discover Ancient Plant-Related Poems": "Using OpenAI's GPT-4 model, the program searches the ctext database to find two Chinese ancient poems related to the identified plant.",
        "🌸 View Results in an Easy-to-Read Format": "The program displays:\n- The plant's name.\n- The full text of the two related ancient poems.\n- The imagery and symbolism of the plant in the poems."
    }
    # 创建展开框显示各类别内容
    for category, content in categories_content.items():
        with st.expander(f"{category}"):
            st.write(content)

elif page == '💖 About Us':
    st.title('💖 About Us')
    st.subheader('✨ Team Members')
    st.write('''1.Technological Development:

    SU Zihan (24062583G@connect.polyu.hk)

    CHEN Youyang (24062058G@connect.polyu.hk)

                ''')
    st.write('''2.Humanities Analysis:

    XIAO Qifang (24003563G@connect.polyu.hk)

    DENG Junxuan(24043858G@connect.polyu.hk)

    ZENG Jingwen(24073054G@connect.polyu.hk)

    ZHANG Fengyue (24100774G@connect.polyu.hk)

    TIAN Yuan (24073183G@connect.polyu.hk)
            ''')

    st.subheader('🔍 Methodology')
    st.write('''1.Why we are interested in this research topic on plants, seasons, emotions and locations?

    The Book of Songs and its plant descriptions carry rich cultural connotations, representing the essence of traditional culturje. The botanical descriptions, in thwe Book of Songs contawin abundant cultural information. As carriers of emotion, plants embody the ancient people's sentiments and attitudes toward life. Meanwhile, the geographical features and seasonal climate reflected by these plants are alyso crucial components of their imagery. Analyzing the plants in thme Book of Songs through information visualizationg helps us understand its cultural messages and pass on both the Book of Songs and Chinese. 
                ''')
    st.write('''2.How we selected the plants?

    We used a text analysis tool to count the eight most frequently mentioned plants, which are: mulberry (40 times), millet (26 times), kudzu (21 times), grass (19 times), beans (11 times), pine (11 times), cypress (10 times), and bamboo (7 times).

               ''')
    st.write('''3.How do we present the content?

    We present the georaphical locations of plants through GIS, conduct close reading on seasons, emotional connotations, and human qualities, and we also created an interactive mini-game and a photo-poetry recognition mini-programme to provide users with a diverse experience.
                   ''')

    st.subheader('🎨 Workflow')
    # 滑块
    w = [
        "Occurrences of plants: \nThe Book of Songs contains 305 poems, among which 153 mention plants. Based on this data, we wrote a python program to create a pie chart for this overall distribution.",
        "Frequency of top mentioned plants: \nUsing text analysis tools, we identified the eight most frequently mentioned plants in the Book of Songs, which we then selected as our target species for further study. Subsequently, we created a bar chart to visualize this data.",
        "Emotional themes in selected plants: \nWe analyzed the emotional themes expressed through plants in the Book of Songs and categorized them into major categories and subcategories. This hierarchical structure helps understand the rich emotional palette of the poetry collection.",
        '''Emotional theme network: \nWe created a network visualization to show the relationships between plants and their associated emotional themes in the Book of Songs. The network consists of main emotional categories (like "Love & Longing", "Diligent Life", "National Spirit") connected to specific plant-emotion pairs.''',
        "Seasonal distribution: \nThe seasonal distribution of plants in the Book of Songs was analyzed in two complementary ways - a pie chart showing the overall distribution and a stacked bar chart showing the distribution by plant species. ",
        "Geographical location: \nTo perform GIS, I combined data with conclusions provided by AI to preliminarily determine the geographic locations (latitude and longitude) of the plants.",
    ]
    # 创建一个滑块
    index = st.slider(" ", 1, len(w), format="Step %d")
    st.write(w[index - 1])

    st.subheader('💻 Our Code ')
    codelink = "https://arcg.is/10COOr2"
    st.markdown(f'[<{codelink}>]({codelink})', unsafe_allow_html=True)

    st.subheader('📖 Reference')
    # 定义链接
    url1 = "http://eprints.utar.edu.my/3850/1/fyp_CH_2019_TJM_%2D_1606961.pdf"
    url3 = "https://oversea.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLASN2023&filename=MAZH202305010&uniplatform=OVERSEA&v=ylSE49hEQkLdQ_zny4qeAJlaWElvQap7IxdLk7zWRZlr2SeN0Ynobe8yX_fDtfrE"
    url4 = "https://oversea.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2018&filename=YWJS201804015&uniplatform=OVERSEA&v=K9p3VYC-6rsA3W6KSAWAs0jLCWjP-buyn8UaIir4LH-gX8HxCdHCFtTe_jdqwXqm"
    url5 = "https://oversea.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLAST2024&filename=JGWC202443030&uniplatform=OVERSEA&v=Ey6v7oEDe65heEuSYReYV_-3EdAUGFLx6uykHfNpSLMZtITItdwvDdfG7SIooSA2"
    url6 = "https://oversea.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFD&dbname=CJFDLASN2021&filename=QCSY202114025&uniplatform=OVERSEA&v=_s-ENeE-4H0QCJAmWVPg_1zUTrFs0du_rtqI2DMDzJSeVEeVeKWPGO-vwSWeqB2q"

    # showcase
    st.write(f'[1.《诗经》中“桑”的意向]({url1})')
    st.write(f'[2. 大河印象——《诗经·国风》里的河流书写与情感建构]({url3})')
    st.write(f'[3. 刻骨铭心的爱与怨——《诗经·卫风·氓》情感脉络解析]({url4})')
    st.write(f'[4.《诗经》植物信息可视化应用研究]({url5})')
    st.write(f'[5.《诗经》中的植物及其意象分析——以《诗经·国风》中的植物为例]({url6})')

    st.subheader('💎Original Text')
    url3 = "https://ctext.org/book-of-poetry"
    # 使用HTML的iframe元素嵌入网页
    iframe_html = f"""
            <iframe src="{url3}" width="100%" height="400" frameborder="0">
                <p>您的浏览器不支持iframe标签。</p>
            </iframe>
            """
    # 使用st.markdown展示iframe，并设置unsafe_allow_html=True允许HTML代码渲染
    st.markdown(iframe_html, unsafe_allow_html=True)
    # 添加一个链接，点击可以直接跳转到网页
    st.markdown(f"[Click here.]({url3})", unsafe_allow_html=True)




