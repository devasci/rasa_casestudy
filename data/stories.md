## common_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
    - action_listen
    - action_check_city
    - utter_ask_cuisine
    - action_listen
    - utter_ask_pricerange
    - action_listen
    - action_search_restaurants
* affirm
    - utter_goodbye
## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "agra"}
    - slot{"location": "agra"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_pricerange
* sendemail{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"location": "agra"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* sendemail{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_pricerange
* sendemail{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* sendemail{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - utter_not_greeted_u_greet_sure
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_pricerange
* sendemail{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - action_search_restaurants
    - slot{"location": "chennai"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* sendemail{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "tirupati"}
    - slot{"location": "tirupati"}
    - action_check_city
    - slot{"is_operated_in_city": false}
    - utter_not_operating_city
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "Bengaluru", "to_email_id": "devendra.satram@gmail.com"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "Bengaluru"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - utter_not_greeted_u_greet_sure
    - action_check_city
    - slot{"is_operated_in_city": false}
    - utter_not_operating_city
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "american", "location": "Bengaluru", "to_email_id": "devendra.satram@gmail.com"}
    - slot{"cuisine": "american"}
    - slot{"location": "Bengaluru"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - utter_not_greeted_u_greet_sure
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_pricerange
* sendemail{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"location": "Bengaluru"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"cuisine": "south indian", "location": "chennai"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "chennai"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_pricerange
* sendemail{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* sendemail{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* sendemail{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* sendemail{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye
