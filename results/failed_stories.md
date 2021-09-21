## happy path 1
* greet: hello there!   <!-- predicted: saludo: hello there! -->
    - utter_greet   <!-- predicted: maquina_saludo -->
* mood_great: amazing   <!-- predicted: negacion: amazing -->
    - utter_happy   <!-- predicted: maquina_despedida -->


## happy path 2
* greet: hello there!   <!-- predicted: saludo: hello there! -->
    - utter_greet   <!-- predicted: maquina_saludo -->
* mood_great: amazing   <!-- predicted: negacion: amazing -->
    - utter_happy   <!-- predicted: maquina_despedida -->
* goodbye: bye-bye!   <!-- predicted: despedida: bye-bye! -->
    - utter_goodbye   <!-- predicted: maquina_despedida -->


## sad path 1
* greet: hello   <!-- predicted: saludo: hello -->
    - utter_greet   <!-- predicted: maquina_saludo -->
* mood_unhappy: not good   <!-- predicted: negacion: not good -->
    - utter_cheer_up   <!-- predicted: maquina_despedida -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* affirm: yes   <!-- predicted: afirmacion: yes -->
    - utter_happy   <!-- predicted: maquina_feliz -->


## sad path 2
* greet: hello   <!-- predicted: saludo: hello -->
    - utter_greet   <!-- predicted: maquina_saludo -->
* mood_unhappy: not good   <!-- predicted: negacion: not good -->
    - utter_cheer_up   <!-- predicted: maquina_despedida -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: not really   <!-- predicted: mood_triste: not really -->
    - utter_goodbye   <!-- predicted: maquina_animacion -->


## sad path 3
* greet: hi   <!-- predicted: saludo: hi -->
    - utter_greet   <!-- predicted: maquina_saludo -->
* mood_unhappy: very terrible   <!-- predicted: mood_triste: very terrible -->
    - utter_cheer_up   <!-- predicted: maquina_animacion -->
    - utter_did_that_help   <!-- predicted: action_listen -->
* deny: no   <!-- predicted: negacion: no -->
    - utter_goodbye   <!-- predicted: maquina_despedida -->


## say goodbye
* goodbye: bye-bye!   <!-- predicted: despedida: bye-bye! -->
    - utter_goodbye   <!-- predicted: maquina_despedida -->


## bot challenge
* bot_challenge: are you a bot?
    - utter_iamabot   <!-- predicted: maquina_soy_bot -->


