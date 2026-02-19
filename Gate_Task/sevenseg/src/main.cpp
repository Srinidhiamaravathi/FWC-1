#include <Arduino.h>

int a = 2;
int b = 3;
int c = 4;
int d = 5;
int e = 6;
int f = 7;
int g = 8;

int P1 = 9;
int P2 = 10;

void displayDigit(int A, int B, int C, int D, int E, int F, int G) {
  digitalWrite(a, A);
  digitalWrite(b, B);
  digitalWrite(c, C);
  digitalWrite(d, D);
  digitalWrite(e, E);
  digitalWrite(f, F);
  digitalWrite(g, G);
}

void setup() {
  pinMode(a, OUTPUT);
  pinMode(b, OUTPUT);
  pinMode(c, OUTPUT);
  pinMode(d, OUTPUT);
  pinMode(e, OUTPUT);
  pinMode(f, OUTPUT);
  pinMode(g, OUTPUT);

  pinMode(P1, INPUT_PULLUP);
  pinMode(P2, INPUT_PULLUP);
}

void loop() {

  int p1 = digitalRead(P1);
  int p2 = digitalRead(P2);

  if(p1 == HIGH && p2 == HIGH) {
    displayDigit(0,0,0,0,0,0,1);
  }
  else if(p1 == LOW && p2 == HIGH) {
    displayDigit(0,0,1,0,0,1,0);
  }
  else if(p1 == HIGH && p2 == LOW) {
    displayDigit(0,1,0,0,1,0,0);
  }
  else {
    displayDigit(0,1,1,0,0,0,0);
  }
}
