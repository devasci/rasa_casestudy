from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_sdk import Action
from rasa_sdk.events import SlotSet
import zomatopy
import json
import smtplib, ssl
import re

email_body_data = ''

class ActionSearchRestaurants(Action):
    cuisines_codes = {25: 'chinese',
                      73: 'mexican',
                      55: 'italian',
                      1: 'american',
                      85: 'south indian',
                      50: 'north indian'}
    
    price_ranges = { 'lessthan_300' : (0,299), 'between_300_to_700': (300, 700), 'morethan_700': (701, 100000)}

    def name(self):
        return 'action_search_restaurants'

    def filterRestaurantsForBot(self, restaurant_details, price_range_id):
        if price_range_id == None:
            print('price range is none')
            price_range_id = 'lessthan_300'

        minPrice, maxPrice = self.price_ranges[price_range_id]
        result_text_format = '{0}. {1} in "{2}" has been rated {3}'
        final_results = []
        results_for_email = []
        cntr = 0
        global email_body_data
        email_body_data = ''
        for e in restaurant_details['restaurants']:
            cost_for_two = int(e['restaurant']['average_cost_for_two'])

            if cost_for_two >= minPrice and cost_for_two <= maxPrice:
                cntr += 1
                final_results.append(
                        result_text_format.format(cntr,e['restaurant']['name'],
                                                  e['restaurant']['location']['address'],
                                                  e['restaurant']['user_rating']['aggregate_rating']
                                                #   e['restaurant']['user_rating']['rating_text'],
                                                ))
                email_body = str(cntr)+'.  '+e['restaurant']['name']+'\n'
                email_body += 'Address: '+e['restaurant']['location']['address']+'\n'
                email_body += 'Average buget for two people: Rs. '+str(e['restaurant']['average_cost_for_two'])+'\n'
                email_body += 'Zomato user rating: '+e['restaurant']['user_rating']['aggregate_rating']+' ('+e['restaurant']['user_rating']['rating_text']+')'+'\n\n'
                email_body_data += email_body

                if len(final_results) >= 10:
                    break
        return final_results

    def run(self, dispatcher, tracker, domain):
        config = {"user_key": "1d4135a3fffd11b1ad7587b5e1471c69"}
        zomato = zomatopy.initialize_app(config)
        
        cuisine = tracker.get_slot('cuisine')
        
        loc = tracker.get_slot('location')
        location_detail = zomato.get_location(loc, 1)
        d1 = json.loads(location_detail)
        lat = d1["location_suggestions"][0]["latitude"]
        lon = d1["location_suggestions"][0]["longitude"]

        price_range_selected = tracker.get_slot('price_range')

        results = zomato.restaurant_search(
            "", lat, lon, str(self.cuisines_codes.get(cuisine.lower())), 10)
        d = json.loads(results)
        response = ""
        if d['results_found'] == 0:
            response = "no results"
        else:
            filtered_results = self.filterRestaurantsForBot(d, price_range_selected)
            
            if len(filtered_results) == 0:
                response = 'There are no restaurants available in the given price range, \nplease choose a different price range.'
                dispatcher.utter_message(response)
                return [SlotSet('change_price_range', 'Yes')]
            elif len(filtered_results) > 0:
                response = 'Showing you top rated restaurants: \n'+'\n'.join(filtered_results[0:5])

        dispatcher.utter_message(response)
        return [SlotSet('change_price_range', 'No')]

class ActionCheckCity(Action):

    operating_cities = ['bengaluru', 'chennai', 'delhi', 'hyderabad', 'kolkata', 'mumbai',
                        'ahmedabad', 'pune', 'agra', 'ajmer', 'aligarh', 'amravati', 'amritsar',
                        'asansol', 'aurangabad', 'bareilly', 'belgaum', 'bhavnagar', 'bhiwandi',
                        'bhopal', 'bhubaneswar', 'bikaner', 'bilaspur', 'bokaro steel city',
                        'chandigarh', 'coimbatore', 'nagpur', 'cuttack', 'dehradun', 'dhanbad', 'bhilai',
                        'durgapur', 'erode', 'faridabad', 'firozabad', 'ghaziabad', 'gorakhpur', 'gulbarga',
                        'guntur', 'gwalior', 'gurgaon', 'guwahati', 'hamirpur', 'hubli–dharwad', 'indore',
                        'jabalpur', 'jaipur', 'jalandhar', 'jammu', 'jamnagar', 'jamshedpur', 'jhansi',
                        'jodhpur', 'kakinada', 'kannur', 'kanpur', 'kochi', 'kolhapur', 'kollam',
                        'kozhikode', 'kurnool', 'ludhiana', 'lucknow', 'madurai', 'malappuram', 'mathura',
                        'goa', 'mangalore', 'meerut', 'moradabad', 'mysore', 'nanded', 'nashik', 'nellore',
                        'noida', 'patna', 'pondicherry', 'purulia prayagraj', 'raipur', 'rajkot', 'rajahmundry',
                        'ranchi', 'rourkela', 'salem', 'sangli', 'shimla', 'siliguri', 'solapur', 'srinagar',
                        'thiruvananthapuram', 'thrissur', 'tiruchirappalli', 'tiruppur', 'ujjain', 'bijapur',
                        'vadodara', 'varanasi', 'vasai-virar city', 'vijayawada', 'vellore', 'warangal', 'surat',
                        'visakhapatnam']

    def name(self):
        return 'action_check_city'

    def run(self, dispatcher, tracker, domain):
        loc = tracker.get_slot('location')

        if loc == None:
            return [SlotSet('is_operated_in_city', False), SlotSet('is_valid_city_name', True)]

        if loc.lower() in self.operating_cities:
            return [SlotSet('is_operated_in_city', True), SlotSet('is_valid_city_name', True)]
        
        config = {"user_key": "1d4135a3fffd11b1ad7587b5e1471c69"}
        zomato = zomatopy.initialize_app(config)

        try:
            city_id = zomato.get_city_ID(loc)
        except Exception as e:
            if e.__str__() == 'InvalidCityId' or e.__str__() == 'invalid_city_name':
                dispatcher.utter_message('Sorry, didn’t find any such location. Can you please tell again?')

            return [SlotSet('is_valid_city_name', False), SlotSet('is_operated_in_city', False)]

        # print(f'city: {loc} is present in operating cities list')
        return [SlotSet('is_operated_in_city', False), SlotSet('is_valid_city_name', True)]

class ActionSendMail(Action):

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "foodie.restaurants.bot@gmail.com"
    password = 'Zxy098#!' 

    def name(self):
        return 'action_send_email'

    def run(self, dispatcher, tracker, domain):
        to_email_id = tracker.get_slot('to_email_id')
        cuisine = tracker.get_slot('cuisine')
        location = tracker.get_slot('location')

        if to_email_id == None:
            dispatcher.utter_message('No email id given.')
            return [SlotSet('is_email_valid', False)]

        email_match = re.search('([\w.-]+)@([\w.-]+)', to_email_id)
        if email_match == None:
            dispatcher.utter_message('mail id is invalid, please enter valid mail id.')
            return [SlotSet('is_email_valid', False)]
        
        SlotSet('is_email_valid', True)

        context = ssl.create_default_context()
        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()  # Can be omitted
            server.starttls(context=context)
            server.ehlo()  # Can be omitted
            server.login(self.sender_email, self.password)
            global email_body_data
            subject = 'Subject: Foodie: {0} restaurants in {1}\n'.format(cuisine, location)
            server.sendmail(self.sender_email, [to_email_id], subject+email_body_data)
        
        return