from mycroft import MycroftSkill, intent_file_handler


class Servowatering(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('servowatering.intent')
    def handle_servowatering(self, message):
        plant = message.data.get('plant')

        self.speak_dialog('servowatering', data={
            'plant': plant
        })


def create_skill():
    return Servowatering()

