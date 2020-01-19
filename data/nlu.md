## intent:affirm
- yes
- yep
- yeah
- indeed
- that's right
- ok
- great
- right, thank you
- correct
- great choice
- sounds really good
- thanks
- ok, thankyou

## intent:goodbye
- bye
- goodbye
- good bye
- stop
- end
- farewell
- Bye bye
- have a good one

## intent:greet
- hey
- howdy
- hey there
- hello
- hi
- good morning
- good evening
- dear sir

## intent:restaurant_search
- i'm looking for a place to eat
- I want to grab lunch
- I am searching for a dinner spot
- I am looking for some restaurants in [Delhi](location).
- I am looking for some restaurants in [Bangalore](location)
- I am looking for some restaurants in [bengalore](location)
- I am looking for some restaurants in [Banglore](location)
- I am looking for some restaurants in [bengaluru](location)
- I am looking for some restaurants in [bangaluru](location)
- list restaurants in [benguluru](location)
- show me [chinese](cuisine) restaurants
- show me [chines](cuisine:chinese) restaurants in the [New Delhi](location:Delhi)
- show me a [mexican](cuisine) place in the [centre](location)
- i am looking for an [indian](cuisine) spot called olaolaolaolaolaola
- search for restaurants
- anywhere in the [west](location)
- I am looking for [asian fusion](cuisine) food
- I am looking a restaurant in [294328](location)
- in [Gurgaon](location)
- Oh, sorry, in [Italy](location)
- in [delhi](location)
- I am looking for some restaurants in [Mumbai](location)
- I am looking for [mexican indian fusion](cuisine)
- [central](location) [indian](cuisine) restaurant
- please help me to find restaurants in [pune](location)
- Please find me a restaurantin [bangalore](location)
- [mumbai](location)
- show me restaurants
- please find me [chinese](cuisine) restaurant in [delhi](location)
- can you find me a [chinese](cuisine) restaurant
- [delhi](location)
- [banglore](location)
- please find me a restaurant in [ahmedabad](location)
- please show me a few [italian](cuisine) restaurants in [bangalore](location)
- list restaurants
- find restaurants in [guntur](location)
- [South Indian](cuisine:south indian)
- find restaurant
- [South Indian](cuisine)
- [North Indian](cuisine)
- [American](cuisine)
- [Mexican](cuisine)
- [Italian](cuisine)
- [Chinese](cuisine:chinese)
- [chinese](cuisine)
- [Lithuania](location)
- [guntur](location)
- [Lesser than 300](price_range:lessthan_300)
- [Rs. 300 to 700](price_range:between_300_to_700)
- [More than 700](price_range:morethan_700)
- [between_300_to_700](price_range)
- [morethan_700](price_range)
- [lessthan_300](price_range)
- [banglore](location:Bengaluru)
- [banglore](location:Bengaluru)
- [Chinese](cuisine:chinese)
- [lessthan_300](price_range)

## intent:sendemail
- get me results on email [devendra.satram@gmail.com](to_email_id)
- [send via email](is_email_requested:Yes)
- [No](is_email_requested)
- [Nope](is_email_requested:No)
- mail id is [devendra.satram@gmail.com](to_email_id)
- [Yes](is_email_requested)
- [devendra.satram@gmail.com](to_email_id)
- [foodie.restaurants.bot@gmail.com](to_email_id)

## synonym:4
- four

## synonym:Bengaluru
- banglore
- bangalore
- bangulore
- banguluru
- bangulur
- bengaluru
- bengulur
- bengalore
- benglore

## synonym:Delhi
- New Delhi

## synonym:chinese
- chines
- Chinese
- Chines

## synonym:south indian
- South Indian

## synonym:vegetarian
- veggie
- vegg

## regex:greet
- hey[^\s]*

## regex:pincode
- [0-9]{6}

## lookup:location
data/tire_1_2_cities_list.txt