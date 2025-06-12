
int lecturasFondo[8];
int lecturasLinea[8];
int lecturas[8];
int pines[8] ={A0,A1,A2,A3,A4,A5,A6,A7};
int umbral[8];

//1 -> fondo blanco linea negra
//0 -> fondo negro linea blanca
int linea = 1;

int sumap;
int suma;

int pos;
int posLast;

void setup() {
  Serial.begin(9600);
  LecturaFyL();
  Serial.println("\t Fin de lecturas");
  Umbral();
}
void loop() {
  Lectura();
  RecorrerLecturas();
  ImprimirValores();
  sumaPonderada();  
  Serial.println(pos);
}
void Umbral(){
  for(int i =0; i<8; i++){
    umbral[i] = (lecturasFondo[i]+lecturasLinea[i])/2;
  }
}
void LecturaFyL(){
  delay(2000);
  //FOR PARA ESCRITURA
  Serial.println("\tLectura Fondo");
  for(int i=0; i<8;i++){
    lecturasFondo[i] = analogRead(pines[i]);
    Serial.print(lecturasFondo[i]);
    Serial.print("\t");
  }
  Serial.println(" ");
  delay(4000);
  Serial.println("\tLectura Linea");
   for(int i=0; i<8;i++){
    lecturasLinea[i] = analogRead(pines[i]);
    Serial.print(lecturasLinea[i]);
    Serial.print("\t");
  }
  Serial.println(" ");
  delay(2000);
}
void Lectura(){
  for(int i=0; i<8;i++){
    lecturas[i] = analogRead(pines[i]);
  }
}
void RecorrerLecturas(){
  //FOR DE IMPRESION
    for(int i=0; i<8; i++){
      if(linea==1){
        if(lecturas[i]<=umbral[i]){
          lecturas[i] =0;
        }else {
          lecturas[i]=1;
        }
      }else{
        if(lecturas[i]<=umbral[i]){
          lecturas[i] =1;
        }else {
          lecturas[i]=0;
        }
      }
    }
}
void ImprimirValores(){
  for(int i=0; i<8; i++){      
      Serial.print(lecturas[i]);
      Serial.print("\t");
    }
    Serial.println("   ");
    delay(500);
}
void sumaPonderada(){
    sumap = (700*lecturas[0]+600*lecturas[1]+500*lecturas[2]+400*lecturas[3]+
             300*lecturas[4]+200*lecturas[5]+100*lecturas[6]+0*lecturas[7]);
    suma = (lecturas[0]+lecturas[1]+lecturas[2]+lecturas[3]+lecturas[4]+lecturas[5]
          +lecturas[6]+lecturas[7]);
    pos = (sumap/suma);
}
void ajustarDireccion(){
  
}
