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
* restaurant_search{"price_range": "morethan_700"}
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
* restaurant_search{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - utter_ask_restults_on_email
* restaurant_search{"is_email_requested": "Yes"}
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
* restaurant_search{"price_range": "morethan_700"}
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
* restaurant_search{"price_range": "morethan_700"}
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
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "morethan_700"}
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

## interactive_story_1
* restaurant_search{"location": "india"}
    - slot{"location": "india"}
    - action_restart

## interactive_story_2
    - utter_ask_howcanhelp
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south indian"}
    - slot{"cuisine": "south indian"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* sendemail{"to_email_id": "testmail@gmail.com"}
    - slot{"to_email_id": "testmail@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "tirupati"}
    - slot{"location": "tirupati"}
    - action_check_city
    - slot{"is_operated_in_city": false}
    - utter_not_operating_city
    - utter_goodbye

## interactive_story_1
* out_of_context{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_outofcontext
    - utter_ask_howcanhelp
* restaurant_search

## interactive_story_1
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - utter_not_greeted_u_greet_sure
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* goodbye
    - utter_goodbye

## interactive_story_1
* restaurant_search{"price_range": "lessthan_300", "location": "chennai"}
    - slot{"location": "chennai"}
    - slot{"price_range": "lessthan_300"}
    - utter_not_greeted_u_greet_sure
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
    - action_check_city
    - slot{"is_operated_in_city": true}
* affirm
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye

## interactive_story_1
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_not_greeted_u_greet_sure
    - utter_ask_location
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "visakhapatnam"}
    - slot{"location": "visakhapatnam"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_debug_ok

## interactive_story_1
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_not_greeted_u_greet_sure
    - utter_ask_location
* restaurant_search{"location": "visakhapatnam"}
    - slot{"location": "visakhapatnam"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "Yes"}
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* restaurant_search{"to_email_id": "pannuruteja@gmail.com"}
    - slot{"to_email_id": "pannuruteja@gmail.com"}
    - action_send_email
    - utter_goodbye

## interactive_story_1
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - utter_not_greeted_u_greet_sure
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
