from dog import Dog
class JackRussellTerrier(Dog):
    def speak(self, sound="Arf"):
#        return f"{self.name} says {sound}"
         return super().speak("sound")
