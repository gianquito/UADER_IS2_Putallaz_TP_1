
// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
}

void parpadeo(int encendido, int apagado, int repetir){
  int n = 1; // cambiar para cada caso
  for(int i=0; i < repetir; i++){
    digitalWrite(LED_BUILTIN, HIGH); 
    delay(encendido * n); 
    digitalWrite(LED_BUILTIN, LOW); 
    delay(apagado * n);
  }
}

// the loop function runs over and over again forever
void loop() {
    parpadeo(400,400,3);
    parpadeo(0,1200,1);
    parpadeo(1200,1200,3);
    parpadeo(0,1200,1);
    parpadeo(400,400,3);
    parpadeo(0,3600,1);
}
