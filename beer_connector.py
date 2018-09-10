from connector import Connector
import overpy
import random

class  BeerConnector(Connector):
    def get_text(self):
        api = overpy.Overpass()
        query = "[out:xml];area[name=\"" + params["vacation_location"] + "\"]->.a;node(area.a)[craft=brewery];out;"

        result = ""

        no_brewery_answers = ["Leider gibt es in " + params["vacation_location"] + " kein Bier.", "Nicht mal eine anstaendige Brauerei gibt es in " +params["vacation_location"] + "!"]
        brewery_answers =   [
                                "Hier in " + params["vacation_location"] + " gibt es das beste Bier bei {name}. Es ist {smell}, {temperature} und {taste}!",
                                "Das Bier in " + params["vacation_location"] + " bei {name} riecht sehr {smell}, schmeckt {taste} und ist {temperature}.",
                                "Das {temperature}e Bier bei {name} war {smell} und im Abgang {taste}!"
                            ]

        smell_adjectives = ["duftend", "aphrodisierend", "kaesig", "stechend", "nussig"]
        temperature_adjectives = ["lauwarm", "heiss", "kühl", "gefroren"]
        taste_adjectives = ["rustikal", "lecker", "revolutionaer", "scharf", "geschmacklos", "fatal", "verheerend", "bitter", "fad", "metallisch"]

        print("fetch results....")
        api_output = api.query(query)

        brewerys = api_output.get_nodes()

        if (len(brewerys) == 0):
            result = random.choice(no_brewery_answers)
        else:
            brewery = random.choice(brewerys)

            name = brewery.tags.get("name")
            taste = random.choice(taste_adjectives)
            smell = random.choice(smell_adjectives)
            temperature = random.choice(temperature_adjectives)

            result = random.choice(brewery_answers).format(name=name,taste=taste,smell=smell,temperature=temperature)

        return result



# DEBUG
if __name__ == "__main__":
    params = {"receiver_name": "Elwood Blues",
              "sender_name": "Jake Blues",
              "receiver_gender": "male",
              "sender_gender": "male",
              "lang": "DE",
              "formal": False,
              "vacation_location": "Berlin",
              "vacation_startdate": 1536314400,
              "vacation_enddate": 1536516000
              }

    print(BeerConnector(params).get_text())
