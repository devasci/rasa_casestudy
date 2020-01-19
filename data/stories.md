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
* sendemail{"is_email_requested": "yes"}
    - slot{"is_email_requested": "yes"}
    - utter_ask_emailid
* sendemail{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye
