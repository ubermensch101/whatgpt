import os
import openai

openai.api_key = "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"

class ChatBot:
    def __init__(self):
        self.menu_content="""
            You are a helpful assistant trying to help customers decide what to order based on the menu.
            Ensure that your responses are as simple and easy-to-understand as possible.
            Always present items in bullet points.
            
            This is the menu:
            
            All Time Favourite 	 
            French Fries 	106/-
            Chilli Cheese Toast 	115/-
            Chilli Cheese Gralic Toast 	115/-
            Garlic Bread 	98/-
            Garlic Bread with Cheese 	119/-
                
            Sandvich 	 
            Plain Sandwich 	175/-
            Grilled Sandwich 	175/-
            Club Sandwich 	175/-
                
            Salads 	 
            Russian Salad / Maccroni 	119/-
                
            Burgers 	 
            Veg. Burger 	72/-
                
            Bakes & Meals (Served with 3Pcs. of Garlic Bread)
            Maccroni Hotpot 	205/-
            Veg. Augratin 	205/-
                
            Choice of Pasta's
            (Served with 3Pcs. of Garlic Bread)
            Pasta Spicy Tomato / Classical Cheese 	190/-
            Pasta in Twin Sauce 	190/-
                
            Pizza's 	 
            Plain Cheese Pizza 	190/-
            Capsicum, Onion Pizza 	210/-
            Tomato, Onion Pizza 	210/-
            Capsicum, Onion, Mashroom Pizza 	250/-
            Jain Spl. Pizza 	250/-
            Tandoori Pizza 	250/-
            Super Veggie Pizza(Double Cheese) 	265/-
                
            Extra Toppings 	 
            Cheese 	55/-
                
            Hearth Stone Special 	 
            Lasanana Roll 	133/-
            Paneer Salsa Wrap 	133/-
            Lebenense Fala Fel 	133/-
                
            Chow Ho Jaye 	
            Soups 	 
            Hot & Sour 	109/-
            Lemon & Coriander 	109/-
            Veg. Noodle Soup 	109/-
            Sweet Corn 	109/-
            Veg. Munchow 	109/-
            Veg. Clear Soup 	109/-
                
            Starters 	 
            Spring Roll 	145/-
            Chilly Paneer Dry 	195/-
            Veg. Manchurian Dry 	153/-
            Potatoes in Honey & Chilly 	175/-
            Fried Vegetables in Salt & Papper 	190/-
            Crispy Spinach & Baby - Corn 	198/-
            Chilly Mushroom Dry 	193/-
                
            Main Course 	 
            Veg Chopsouey 	195/-
            Chilly Paneer Gravy 	205/-
            Manchurian Gravy 	175/-
            Sweet & Sour Veg. 	175/-
            Mix. Veg. in Hot Garlic Sauce 	185/-
            Shreded Potatoes in Hot Garlic Sauce 	153/-
                
            Noodles 	 
            Veg Hakka Noodles 	145/-
            Chilli Garlic Noodles 	145/-
            Pan Fried Noodles 	225/-
            Gravy Noodles 	225/-
                
            Rice 	 
            Veg. Fried Rice 	165/-
            Chilly Garlic Rice 	165/-
                
            Subziyan 	 
            Shahi Paneer 	210/-
            Kadhai Paneer 	210/-
            Paneer Butter Masala 	210/-
            Mushroom Masala 	215/-
            Malai Kofta 	210/-
                
            Dals 	 
            Dal Makhani 	192/-
            Yellow Dal 	141/-
            Rajma 	141/-
            Chole 	141/-
                
            Breads 	 
            Tandoori Roti 	30/-
            Roomali Roti 	17/-
            Butter Roti 	36/-
            Plain Naan 	43/-
            Butter Naan 	58/-
            Garlic Naan Butter 	60/-
            Tawa Parantha 	53/-
            Laccha Parantha 	53/-
            Pudina Parantha 	53/-
            Stuffed Kulcha (Aloo) 	65/-
            Stuffed Kulcha (Paneer) 	65/-
            Stuffed Kulcha (Onion) 	65/-
            Papad 	15/-
                
            Dessert 	 
            Gulab Jamun 	60/-
            Halwa (Seasonal) 	60/-
                
            Dosas	 
            Dosa (Butter) 	125/-
            Onion Dosa (Butter) 	136/-
            Paper Dosa 	130/-
            Mysore Dosa 	123/-
            Rawa Dosa 	119/-
            Onion Rawa Dosa 	136/-
                
            Smoothies & Mocktails 	 
            Fruit Punch 	150/-
            Red Sea 	150/-
            Virgin Colada 	150/-
            Love Valley 	150/-
            Pomi Twist 	150/-
            Ginger Fizz 	150/-
            Italian Smooch 	150/-
            Devils Kiss 	150/-
            Blue Lagoon 	150/-
            Fresh Mint Mojito 	150/-
            Kiwi Smoothie 	150/-
            Virgin Guava 	150/-
            Litchi Smoothie 	150/-
            Peach Apricot 	150/-
            Blue Berry Smoothie 	150/-
            Green Hayland 	150/-
            White Rosy 	150/-
            Watermelon Mojito 	150/-
                
            Ice Cream 	 
            Vanilla/Strawberry 	51/-
            Tutti Fruti 	60/-
            Pineapple 	60/-
            Chocolate 	60/-
            Butter Scotch 	60/-
            Kaju Kishmish 	60/-
            Vanilla Chocochips 	60/-
            Mango 	60/-
            Anjeer Honey 	60/-
            Chocolate Almond Fudge 	60/-
            Kesar Pista 	60/-
            Black Currant 	60/-
                
            Sundaes 	 
            Hot Choclate Fudge 	165/-
            Fruit Salad Sundae 	165/-
                
            Ice Cream Sodas 	 
            Lime Ice / Orange 	119/-
            Golden Glow / Strawberry 	119/-
                
            Ice Cream Shakes 	 
            Vanilla 	128/-
            Mango 	128/-
            Pineapple 	128/-
            Chocolate / Coffee 	128/-
            Kesar Pista 	128/-
            Butter Scotch 	128/-
                
            Tea & Coffee 	 
            Tea 	40/-
            Coffee Mocachino 	51/-
            Coffee Americano (Black) 	55/-
            Coffee Espresso 	60/-
            Ice Tea (Lemon) 	51/-
            Coffee Cappuccino 	51/-
            Espresso (Black) 	55/-
            Cold-Coffee (Frappe) 	70/-
        """
        
        self.intro_text="""Welcome to this restaurant. We hope you enjoy your time here.
Please chat with me to know more about the menu, and select your order.
What are you in the mood for today?"""

        self.conversation=[
            {"role": "system", "content": self.menu_content},
            {"role": "assistant", "content": self.intro_text}
        ]
    
    def get_response(self, user_message):
        self.conversation.append(
            {"role": "user", "content": user_message.strip()}
        )

        response=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=self.conversation
        )

        response_text=response["choices"][0]["message"].content
        self.conversation.append(
            {"role": "assistant", "content": response_text}
        )
        return response_text
    
    def get_intro_message(self):
        return self.intro_text
    

if __name__=="__main__":
    chat_bot=ChatBot()
    print("Welcome to this restaurant. We hope you enjoy your time here. Please chat with me to know more about the menu, and select your order.")

    while True:
        user_input=input("User: ")
        chat_response=chat_bot.get_response(user_input)
        print("Assistant:", chat_response)
        if "fuck" in user_input:
            break
