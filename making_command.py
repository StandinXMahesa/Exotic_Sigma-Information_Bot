import os
import telebot
from dotenv import load_dotenv
from data_txt import *
from PIL import Image

# Load Env
load_dotenv()

# bot
API_KEY = os.getenv('API')
bot = telebot.TeleBot(API_KEY)


# --------------------------------------Callback---------------------------------- 

@bot.callback_query_handler(func=lambda message : True)
def callback(call):
        if(call.data == "menu0"):
            bot.send_message(call.from_user.id, data['help'],parse_mode='HTML')
        elif(call.data == "r_tarantula"):
            pesan = bot.send_message(call.from_user.id, data['saran'][0],parse_mode='HTML')
            bot.register_next_step_handler(pesan,saran_tarantula)
        elif(call.data == "r_fitur"):
            pesan = bot.send_message(call.from_user.id, data['saran'][0],parse_mode='HTML')
            bot.register_next_step_handler(pesan,saran_fitur)
         

        
# --------------------------------------Start Awal----------------------------------

@bot.message_handler(commands=["start"])
def start(message):
    markup = telebot.util.quick_markup({"Menu/Help":{"callback_data":"menu0"}})
    bot.send_message(message.chat.id, data['start'],parse_mode="HTML",reply_markup=markup)
    
# --------------------------------------Rekomendasi----------------------------------
@bot.message_handler(commands=["saran"])
def rekomendasi(message):
    markup = telebot.util.quick_markup({"Tarantula":{"callback_data":"r_tarantula"},"Fitur":{"callback_data":"r_fitur"}})
    bot.send_message(message.chat.id,"======👍🏼<b> Apa yang ingin kalian beri saran / kritik </b>👍🏼======",parse_mode="HTML",reply_markup=markup)

def saran_tarantula(message):
    bot.send_message(message.chat.id,"===<b>😉 Terima kasih sudah memberikan saran Tarantula 😉===</b>",parse_mode='HTML')
    
def saran_fitur(message):
    bot.send_message(message.chat.id,"===<b>😉 Terima kasih sudah memberikan saran Fitur 😉===</b>",parse_mode='HTML')

# --------------------------------------Help / Menu----------------------------------

@bot.message_handler(commands=["help","menu"])
def help(message):
    bot.send_message(message.chat.id, data['help'],parse_mode='HTML')


# --------------------------------------Tarantula----------------------------------

@bot.message_handler(commands=["tarantula"])
def tarantula(message):
    bot.send_message(message.chat.id, data["penjelasan"]["tarantula"],parse_mode="HTML")
    bot.send_message(message.chat.id, data["penjelasan"]["berbahaya"],parse_mode="HTML")
    bot.send_message(message.chat.id, data["penjelasan"]["membedakan"],parse_mode="HTML")
    bot.send_message(message.chat.id, data["penjelasan"]["oldnew"],parse_mode="HTML")
    bot.send_message(message.chat.id, data["penjelasan"]["bau"],parse_mode="HTML")


# --------------------------------------Caresheet----------------------------------

@bot.message_handler(commands=["caresheet"])
def tarantula(message):
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["penjelasan"],parse_mode="HTML")

@bot.message_handler(commands=["sling"])
def sling(message):
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["sling"][0],parse_mode="HTML")
    img = Image.open("src/cup_kecil.jpg")
    bot.send_photo(message.chat.id,img)
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["sling"][1],parse_mode="HTML")
    img1 = Image.open("src/spray_bottle.jpg")
    bot.send_photo(message.chat.id,img1)
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["sling"][2],parse_mode="HTML")
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["sling"][3],parse_mode="HTML")
    img2 = Image.open("src/tarantula_molting.jpg")
    bot.send_photo(message.chat.id,img2)
    
@bot.message_handler(commands=["juve"])
def juve(message):
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["juve"][0],parse_mode="HTML")
    img = Image.open("src/kandang_juve.jpg")
    bot.send_photo(message.chat.id,img)
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["juve"][1],parse_mode="HTML")
    img1 = Image.open("src/water-dish_tarantula.jpg")
    bot.send_photo(message.chat.id,img1)
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["juve"][2],parse_mode="HTML")
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["juve"][3],parse_mode="HTML")
    img2 = Image.open("src/tarantula_molting.jpg")
    bot.send_photo(message.chat.id,img2)
    
@bot.message_handler(commands=["mature"])
def mature(message):
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["mature"][0],parse_mode="HTML")
    img = Image.open("src/kandang_juve.jpg")
    bot.send_photo(message.chat.id,img)
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["mature"][1],parse_mode="HTML")
    img1 = Image.open("src/water-dish_tarantula.jpg")
    bot.send_photo(message.chat.id,img1)
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["mature"][2],parse_mode="HTML")
    bot.send_message(message.chat.id, data["penjelasan"]["caresheet"]["mature"][3],parse_mode="HTML")
    img2 = Image.open("src/tarantula_molting.jpg")
    bot.send_photo(message.chat.id,img2)


# --------------------------------------P3 Gigitan----------------------------------

@bot.message_handler(commands=["tergigit"])
def gigitan(message):
    bot.send_message(message.chat.id, data["penjelasan"]["tergigit"],parse_mode="HTML")

# --------------------------------------Keuntungan----------------------------------

@bot.message_handler(commands=["keuntungan"])
def keuntungan(message):
    bot.send_message(message.chat.id, data["penjelasan"]["keuntungan"],parse_mode="HTML")

# --------------------------------------Penyakit--------------------------------------

@bot.message_handler(commands=["penyakit"])
def penyakit(message):
    bot.send_message(message.chat.id, data["penjelasan"]["penyakit"],parse_mode="HTML")
    

# --------------------------------------Sexing-------------------------------------------
@bot.message_handler(commands=["sexing"])
def penyakit(message):
    bot.send_message(message.chat.id, data["penjelasan"]["sexing"][0],parse_mode="HTML")
    img = Image.open("src/anatomi_tarantula.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Google</b>",parse_mode="HTML")
    bot.send_message(message.chat.id, data["penjelasan"]["sexing"][1],parse_mode="HTML")
    img1 = Image.open("src/ventral_sexing.jpeg")
    bot.send_photo(message.chat.id,img1,caption="<b>Cara 1 : Meneliti Epigastric Furrow</b>",parse_mode="HTML")
    img2 = Image.open("src/bawah_abdomen.jpg")
    bot.send_photo(message.chat.id,img2,caption="<b>Cara 2 : Meneliti Jarak antara 2 Booklungs Anterior. Semakin jauh/lebar : Female (kiri), jika sebaliknya : Male (kanan)</b>",parse_mode="HTML")
    bot.send_message(message.chat.id, data["penjelasan"]["sexing"][2],parse_mode="HTML")
    img3 = Image.open("src/emboli-diagram.jpg")
    bot.send_photo(message.chat.id,img3,caption="<b>From https://tomsbigspiders.com. Dengan melakukan perbandingan pada pedipalps-nya</b>",parse_mode="HTML")
    bot.send_message(message.chat.id, data["penjelasan"]["sexing"][3],parse_mode="HTML")

# --------------------------------------Old Word Tarantula----------------------------------

@bot.message_handler(commands=["murinus"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["murinus"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/pterinochilus_murinus.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["ezendami"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["ezendami"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/augacephalus_ezendami.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["borneo"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["borneo"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/borneo_black.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["darlingi"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["darlingi"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/ceratogyrus_darlingi.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["lividus"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["lividus"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/cyriopagopus_lividus.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["hatihati"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["borneo"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/cyriopagopus_sp.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["dorirae"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["dorirae"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/haplopelma_doriae_arachnoboard.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From arachnoboard</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["nigerriumum"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["nigerriumum"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/lampropelma_nigerrimum.png")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["balfouri"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["balfouri"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/monocrentropus_balfouri.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["formosa"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["formosa"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/poecilotheria_formosa.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["metallica"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["metallica"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/poecilotheria_metallica.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["regalis"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["regalis"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/poecilotheria_regalis.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["javanensis"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["oldword"]["javanensis"],parse_mode="HTML")
    img = Image.open("src/tarantula/oldword/javanensis.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")

# --------------------------------------New Word Tarantula----------------------------------
@bot.message_handler(commands=["avimetallica"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["avimetallica"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/avicularia_metallica.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["albiceps"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["albiceps"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/brachypelma_albiceps.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["aratum"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["aratum"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/brachypelma_aratum.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["boehmei"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["boehmei"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/brachypelma_boehmei.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["emelia"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["emelia"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/brachypelma_emelia.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["klassi"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["klassi"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/brachypelma_klassi.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["cyaneo"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["cyaneo"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/chromatopelma_cyaneopubescens.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["pulchripes"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["pulchripes"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/grammostola_pulchripes.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["parahybana"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["parahybana"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/lasiodora_parahybana.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["chromatus"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["chromatus"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/nhandu_chromatus.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["tripedii"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["tripedii"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/nhandu_tripepii.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["blondi"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["blondi"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/theraphosa_blondi.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["albopilosum"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["albopilosum"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/tliltocatl_albopilosum.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["vagans"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["vagans"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/tliltocatl_vagans.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")
    
@bot.message_handler(commands=["verdezi"])
def murinus(message):
    bot.send_message(message.chat.id, data["tarantula"]["newword"]["verdezi"],parse_mode="HTML")
    img = Image.open("src/tarantula/newword/tliltocatl_verdezi.jpg")
    bot.send_photo(message.chat.id,img,caption="<b>From Pinterest</b>",parse_mode="HTML")


# --------------------------------------Salah Fitur---------------------------------- 

@bot.message_handler(content_types=["text","document","audio","sticker","photo"])
def salah(message):
    bot.send_message(message.chat.id,"Pesan yang anda kirim tidak ada")

bot.infinity_polling()