import streamlit as st
import pandas as pd

st.set_page_config(page_title="VoyaShort Lounge", page_icon="🏖️", layout="centered")

if "client_database" not in st.session_state:
    st.session_state.client_database = [{"ID": 1, "Channel": "WhatsApp", "Contact": "+79991234567", "From": "Moscow (SVO)", "To": "Moscow (SVO)", "Destination": "Phuket 🇹🇭", "Type": "Вилла / Дом 🏡", "Month": "Декабрь", "Duration": "1 неделя", "Adults": 2, "Children": 0, "Ages": "", "IncludeFlight": "Включить билеты", "PriceType": "За всю компанию"}]
if "agency_listings" not in st.session_state:
    st.session_state.agency_listings = [{"Agency": "Phuket VIP Homes", "Title": "Rawai Sea View Villa", "Dest": "Phuket 🇹🇭", "NetPrice": 350}]

st.markdown("""
    <style>
    [data-testid="stSidebar"], [data-testid="stSidebarCollapsedControl"] { display: none !important; }
    .stApp { background-color: #040811 !important; background-image: radial-gradient(circle at 50% 30%, #0a1324 0%, #02050a 100%) !important; color: #f5f6f8 !important; font-family: 'Georgia', serif !important; }
    h1, h2, h3 { color: #f3e5ab !important; text-align: center !important; }
    .subtitle { text-align: center !important; color: #dfba53 !important; font-size: 1.15rem !important; font-style: italic !important; margin-bottom: 2.5rem !important; }
    .stApp label, .stApp p, .stApp .stMarkdown p { color: #e2e8f0 !important; font-weight: 600 !important; font-size: 0.95rem !important; }
    .stTextInput>div>div>input, .stSelectbox>div>div, .stTextArea>div>div>textarea { background-color: #070d18 !important; color: #ffffff !important; border: 1px solid #b88728 !important; border-radius: 4px !important; }
    div[data-baseweb="select"] span, div[data-baseweb="select"] div[aria-selected="true"] { color: #ffffff !important; }
    .stButton>button { background: linear-gradient(130deg, #101c30 0%, #050910 100%) !important; color: #dfba53 !important; border: 1px solid #b88728 !important; font-weight: 600 !important; width: 100% !important; border-radius: 4px !important; }
    .stButton>button:hover { background: #dfba53 !important; color: #040811 !important; }
    .stTextArea textarea { background-color: #050b14 !important; color: #dfba53 !important; font-family: 'Courier New', monospace !important; border: 2px solid #b88728 !important; }
    hr { border: 0 !important; height: 1px !important; background-image: linear-gradient(to right, rgba(184, 135, 40, 0), rgba(184, 135, 40, 0.6), rgba(184, 135, 40, 0)) !important; margin: 3rem 0 !important; }
    .logo-container { display: flex; justify-content: center; margin-top: 1.5rem; margin-bottom: 0.5rem; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<div class="logo-container"><img src="https://postimg.cc" width="120" style="border-radius: 50%; border: 2px solid #b88728;"></div>', unsafe_allow_html=True)
st.title("VoyaShort")
st.markdown("<div class='subtitle'>Ваш private travel-консультант</div>", unsafe_allow_html=True)
st.write("Укажите ваши критерии. Мы подберем лучшие закрытые варианты проживания и предоставим готовые ссылки на оптимальные авиарейсы.")

col_c1, col_c2 = st.columns(2)
with col_c1: c_channel = st.selectbox("Способ связи", ["WhatsApp", "Telegram", "Viber", "Email", "Phone Call"])
with col_c2: c_contact = st.text_input("Номер / никнейм для связи", value="")

st.markdown("### ✈️ Маршрут перелета")
col_from, col_to = st.columns(2)
with col_from: c_from = st.text_input("Откуда вылетаете?", value="Moscow (SVO)")
with col_to: c_to_option = st.selectbox("Куда возвращаетесь?", ["Туда и обратно", "В одну сторону"])
c_to = st.text_input("Город возвращения", value="") if "сторону" in c_to_option else c_from

st.markdown("### 👥 Количество гостей")
col_g1, col_d_cnt = st.columns(2)
with col_g1: c_adults = st.selectbox("Взрослые", [1, 2, 3, 4, 5, "6+"])
with col_d_cnt: c_children = st.selectbox("Дети", [0, 1, 2, 3, 4, "5+"])
c_children_ages = st.text_input("Возраст детей", value="") if c_children != 0 else ""

st.markdown("### ⚙️ Кастомизация расчета стоимости")
col_opt1, col_opt2 = st.columns(2)
with col_opt1: c_include_flight = st.selectbox("Авиабилеты:", ["Включить билеты в цену за сутки", "Авиабилеты отдельно"])
with col_opt2: c_price_type = st.selectbox("Показ стоимости:", ["За всю компанию", "За 1 человека"])

st.markdown("### 🏡 Куда хотите отправиться?")
col_d1, col_d2 = st.columns(2)
with col_d1:
    c_dest = st.selectbox("Направление", ["Dubai 🇦🇪", "Phuket 🇹🇭", "Bali 🇮🇩"])
    c_type = st.selectbox("Тип жилья", ["Апартаменты 🏙️", "Вилла / Дом 🏡", "Люкс Комплекс 👑"])
with col_d2:
    c_month = st.selectbox("Месяц", ["Ноябрь", "Декабрь", "Январь", "Февраль", "Март", "Апрель"])
    c_duration = st.selectbox("Длительность", ["1 неделя", "2 недели", "3 недели", "1 месяц"])

if st.button("Получить решение"):
    if c_contact in ["admin999", "partner777"]: st.warning("Код активирован. Прокрутите вниз.")
    elif not c_contact: st.error("Пожалуйста, заполните данные.")
    else:
        new_id = len(st.session_state.client_database) + 1
        st.session_state.client_database.append({"ID": new_id, "Channel": c_channel, "Contact": c_contact, "From": c_from, "To": c_to, "Destination": c_dest, "Type": c_type, "Month": c_month, "Duration": c_duration, "Adults": str(c_adults), "Children": str(c_children), "Ages": c_children_ages, "IncludeFlight": "Включить" if "Включить" in c_include_flight else "Отдельно", "PriceType": "За всю компанию" if "компанию" in c_price_type else "За 1 человека"})
        st.success("✨ Ваша заявка принята!")

# --- 2. ПАРТНЬОРСКИ ПАНЕЛ ("partner777") ---
if c_contact == "partner777":
    st.markdown("<hr>### 🤝 B2B Partner Exchange Dashboard", unsafe_allow_html=True)
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        a_name = st.text_input("Agency Name:")
        a_title = st.text_input("Property Title:")
    with col_b2:
        a_dest = st.selectbox("Destination", ["Dubai 🇦🇪", "Phuket 🇹🇭", "Bali 🇮🇩"], key="b2b_dest")
        a_net = st.number_input("Net Price per Night ($):", value=200)
    if st.button("Submit Property"):
        if a_name and a_title: st.session_state.agency_listings.append({"Agency": a_name, "Title": a_title, "Dest": a_dest, "NetPrice": a_net}); st.success("Logged.")
    st.dataframe(pd.DataFrame(st.session_state.client_database).drop(columns=["Contact"], errors='ignore'))

# --- 3. СКРИТ АДМИН ПАНЕЛ ("admin999") ---
if c_contact == "admin999":
    st.markdown("<hr>## 👑 ЦЕНТРАЛЕН АДМИН ПАНЕЛ (HQ Engine)", unsafe_allow_html=True)
    col_ad1, col_ad2 = st.columns(2)
    with col_ad1: revolut_username = st.text_input("Revolut @username:", value="@dmitry_luxe")
    with col_ad2: revolut_link = st.text_input("Revolut Payment Link:", value="https://revolut.me")
    
    if st.session_state.client_database:
        df_all = pd.DataFrame(st.session_state.client_database)
        selected_client = st.selectbox("Избери ID на клиент:", df_all["ID"].unique())
        client_row = df_all[df_all["ID"] == selected_client].iloc
        valid_props = [p for p in st.session_state.agency_listings if p["Dest"] in client_row["Destination"]]
        
        chosen_title, prop_net = "Премиум вилла (Индивидуальный подбор)", 300
        if valid_props:
            options = [f"{p['Title']} ({p['Agency']}) - ${p['NetPrice']}" for p in valid_props]
            sel_prop = st.selectbox("Избери имот от партньорите:", options)
            chosen_title = valid_props[options.index(sel_prop)]["Title"]
            prop_net = valid_props[options.index(sel_prop)]["NetPrice"]

        col_m1, col_m2 = st.columns(2)
        with col_m1:
            my_markup = st.number_input("Твоята такса на нощувка ($):", value=50)
            flight_est_price = st.number_input("ОБЩА цена на самолетните билети ($):", value=450)
        with col_m2: flight_link = st.text_input("Линк за билета:", value="https://skyscanner.net")

        days = 7
        total_people = int(client_row["Adults"] if client_row["Adults"].isdigit() else 2)
        base_price = prop_net + my_markup
        
        if client_row["IncludeFlight"] == "Включить":
            final_price = (base_price / total_people) + (flight_est_price / days / total_people) if client_row["PriceType"] == "За 1 человека" else base_price + (flight_est_price / days)
            price_label = "на 1 человека в сутки" if client_row["PriceType"] == "За 1 человека" else "за всех в сутки"
        else:
            final_price = base_price / total_people if client_row["PriceType"] == "За 1 человека" else base_price
            price_label = "на 1 человека в сутки" if client_row["PriceType"] == "За 1 человека" else "за всех в сутки"

        russian_text = f"Привет! ✨ Подготовил для вас эксклюзивный вариант поездки.\\n\\n🏡 **ОБЩАЯ СПЕЦИФИКАЦИЯ ТУРА:**\\nЛокация: {chosen_title} ({client_row['Type']}).\\nПериод: {client_row['Month']} ({client_row['Duration']}).\\n\\n🏷️ **Стоимость предложения: ${final_price:.2f} ({price_label})**.\\n\\n🔒 **Как оплатить тур (Revolut):**\\n📱 Наш Revolut тег: {revolut_username}\\n🔗 Ссылка для оплаты: {revolut_link}\\n\\nОформляем?"
        st.text_area("Copy and Send:", value=russian_text, height=200)
