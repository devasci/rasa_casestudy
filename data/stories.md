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
    - action_restart
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
    - action_restart
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
    - action_restart
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
    - action_restart
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
    - action_restart
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
    - action_restart
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
    - action_restart
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
    - action_restart
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
    - action_restart
## interactive_story_1
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "tirupati"}
    - slot{"location": "tirupati"}
    - action_check_city
    - slot{"is_operated_in_city": false}
    - utter_not_operating_city
    - utter_goodbye
    - action_restart
## interactive_story_1
* out_of_context{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_outofcontext
    - action_restart
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
    - action_restart
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
    - action_restart
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
    - action_restart

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
* restaurant_search{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
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
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* restaurant_search{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart
## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* restaurant_search{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
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
* restaurant_search{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai", "price_range": "morethan_700"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - slot{"price_range": "morethan_700"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* restaurant_search{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "agra"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "agra"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* restaurant_search{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "agra"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "agra"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "agra"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "agra"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "agra"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "agra"}
    - utter_not_greeted_u_greet_sure
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "No"}
    - slot{"change_price_range": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "chennai", "price_range": "between_300_to_700"}
    - slot{"cuisine": "italian"}
    - slot{"location": "chennai"}
    - slot{"price_range": "between_300_to_700"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
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
* restaurant_search{"to_email_id": "gmail.com"}
    - slot{"to_email_id": "gmail.com"}
    - action_send_email
    - slot{"is_email_valid": false}
    - utter_ask_emailid
* restaurant_search
    - utter_invalid_mail_id
    - utter_ask_emailid
* restaurant_search{"to_email_id": "devendra4sci@gmail.com"}
    - slot{"to_email_id": "devendra4sci@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "Bengaluru"}
    - slot{"location": "Bengaluru"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
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
* restaurant_search{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "rishikesh"}
    - slot{"location": "rishikesh"}
    - action_check_city
    - slot{"is_operated_in_city": false}
    - utter_not_operating_city
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_2
* restaurant_search{"location": "allahabad"}
    - slot{"location": "allahabad"}
    - action_check_city
    - slot{"is_operated_in_city": false}
    - utter_not_operating_city
* affirm
    - utter_goodbye
    - action_restart

## interactive_story_3
    - utter_greet
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* restaurant_search{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_mail_sent
    - action_restart

## interactive_story_4
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_city
    - slot{"is_operated_in_city": false}
    - utter_not_operating_city
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mubaim"}
    - slot{"location": "mubaim"}
    - action_check_city
    - slot{"is_valid_city_name": false}
    - slot{"is_operated_in_city": false}
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "aurangabad"}
    - slot{"location": "aurangabad"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "American"}
    - slot{"cuisine": "American"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "Yes"}
    - slot{"is_email_requested": "Yes"}
    - utter_ask_emailid
* restaurant_search{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - action_send_email
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "mexican", "location": "rajkot"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "rajkot"}
    - utter_not_greeted_u_greet_sure
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* out_of_context
    - utter_default
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Mexican"}
    - slot{"cuisine": "Mexican"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "Yes"}
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "kochi"}
    - slot{"location": "kochi"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_not_greeted_u_greet_sure
    - utter_ask_location
* restaurant_search
    - utter_ask_location_city_name
* restaurant_search{"location": "coorg"}
    - slot{"location": "coorg"}
    - action_check_city
    - slot{"is_valid_city_name": false}
    - slot{"is_operated_in_city": false}
    - utter_not_operating_city
    - utter_goodbye
    - action_restart

## interactive_story_2
    - utter_greet
* greet
* restaurant_search{"cuisine": "mexican", "to_email_id": "devendra.satram@gmail.com"}
    - slot{"cuisine": "mexican"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - utter_ask_location
* restaurant_search{"location": "mangalore"}
    - slot{"location": "mangalore"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - action_send_email
    - utter_mail_sent
    - action_restart

## interactive_story_3
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "Bengaluru"}
    - slot{"cuisine": "italian"}
    - slot{"location": "Bengaluru"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "morethan_700"}
    - slot{"price_range": "morethan_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_4
    - utter_greet
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "Yes"}
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_5
* greet
    - utter_greet
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "Chinese"}
    - slot{"cuisine": "Chinese"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "No"}
    - slot{"change_price_range": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_6
    - utter_greet
* restaurant_search{"location": "goa"}
    - slot{"location": "goa"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "South Indian"}
    - slot{"cuisine": "South Indian"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "No"}
    - slot{"change_price_range": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "Yes"}
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"location": "coimbatore"}
    - slot{"location": "coimbatore"}
    - action_check_city
    - slot{"is_operated_in_city": false}
    - slot{"is_valid_city_name": true}
    - utter_not_operating_city
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "coimbatore"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "coimbatore"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "No"}
    - slot{"change_price_range": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "No"}
    - utter_ask_restults_on_email
* sendemail{"is_email_requested": "No"}
    - slot{"is_email_requested": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_1
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chandigarh"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chandigarh"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "No"}
    - slot{"change_price_range": "No"}
    - utter_goodbye
    - action_restart

## interactive_story_2
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chennai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chennai"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "Yes"}
    - slot{"change_price_range": "Yes"}
    - utter_ask_emailid
* restaurant_search{"to_email_id": "devendra.satram@gmail.com"}
    - slot{"to_email_id": "devendra.satram@gmail.com"}
    - utter_mail_sent
    - action_restart

## interactive_story_3
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "chennai"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "chennai"}
    - action_check_city
    - slot{"is_operated_in_city": true}
    - slot{"is_valid_city_name": true}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "Yes"}
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "lessthan_300"}
    - slot{"price_range": "lessthan_300"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "Yes"}
    - slot{"change_price_range": "Yes"}
    - utter_ask_pricerange
* restaurant_search{"price_range": "between_300_to_700"}
    - slot{"price_range": "between_300_to_700"}
    - action_search_restaurants
    - slot{"change_price_range": "Yes"}
    - utter_ask_change_pricerange
* restaurant_search{"change_price_range": "No"}
    - slot{"change_price_range": "No"}
    - utter_goodbye
    - action_restart
