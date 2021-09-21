# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/

from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

# Esta acción permite que se guarden los entimientos para moestrarlos después
#class ActionReturnFeeling(Action):

    def name(self) -> Text:
        return "action_your_sentimiento"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template = "utter_your_sentimiento",
         						 sentimiento=(tracker.get_slot('SentimientoNecesidadSatisfecha')).lower())
        return []

# ESTA ACCION HACE QUE SE GUARDEN LOS SENTIMIENTOS PARA MOSTRARLOS DESPUES
#class ActionReturnFeellingBad(Action):

    def name(self) -> Text:
        return "action_your_sentimiento_bad"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template = "utter_your_sentimiento_bad",
                                 sentimiento_bad=(tracker.get_slot('SentimientoNecesidadNoSatisfecha')).lower())
        return []



# ESTE FORMULARIO RECOGE EL COLOR Y EL ANIMAL PARA MOSTRAR EL RESUMEN DE HABLAR SOBRE SENTIMIENTOS
#class ActionFormInfo(FormAction):
    def name(self) -> Text:
        """Unique identifier of the form"""

        return "form_sentimientos"

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """A list of required slots that the form has to fill"""

        return ["SentimientosColor", "SentimientosAnimal"]

    def submit(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
    ) -> List[Dict]:
        """Define what the form has to do
            after all required slots are filled"""

        # utter submit template
        dispatcher.utter_message(template="utter_resumen_sentimientos", color=tracker.get_slot('SentimientosColor'),
                                 animal=tracker.get_slot('SentimientosAnimal'))
        return []

    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
        """A dictionary to map required slots to
            - an extracted entity
            - intent: value pairs
            - a whole message
            or a list of them, where a first match will be picked"""

        return {
            "color": [self.from_entity(entity="SentimientosColor", intent='Color'),
                     self.from_text()],
            "animal": [self.from_entity(entity="SentimientosAnimal", intent="Animal"),
                        self.from_text()],
        }