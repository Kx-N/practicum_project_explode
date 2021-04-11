//#include<iostream>
#define F_CPU 16000000L
#define MCU = "atmega328p"
#include<avr/io.h>
#include<avr/interrupt.h>
#include<util/delay.h>
#include<avr/pgmspace.h>
#include"usbdrv.h"
//#include"init_board.h"



#define req_read_switch1 0
#define req_write_led 10

void set_led(unsigned led ,unsigned state){
 if(state)
  PORTC |= (1<<led);
 else 
  PORTC &= ~(1<<led);
}


usbMsgLen_t usbFunctionSetup(uint8_t data[8]){
  usbRequest_t *rq = (usbRequest_t*)data;
  static uint8_t switch_state;  
  switch_state = 0; 
  if(rq->bRequest == req_read_switch1){
   if((PINB & (1<<PB1))==0)
     switch_state -= 1;
   if((PINB & (1<<PB2))==0)
     switch_state -= 2;
   if((PINB & (1<<PB3))==0)
     switch_state -= 4;
   if((PINB & (1<<PB3))==0)
     switch_state -= 8;

   switch_state -= 241;
   usbMsgPtr = (uchar*)&switch_state;
   return sizeof(switch_state);
  }
  else if(rq->bRequest == req_write_led){
   unsigned index = rq->wIndex.word;
   unsigned value = rq->wValue.word;
   set_led(index,value);
   return 0;
  }
  return 0;
}




void init_port_b(){
   //PC0..PC2 -> output
 DDRC |= (1<<PC0)|(1<<PC1)|(1<<PC2);
 //PB0,PB1,PB2,PB3,PCB4 -> input
 DDRB &= ~((1<<PB0)|(1<<PB1)|(1<<PB2)|(1<<PB3)|(1<<PB4));
 PORTB |= (1<<PB0);
 PORTB |= (1<<PB1);
 PORTB |= (1<<PB2);
 PORTB |= (1<<PB3);
 PORTB |= (1<<PB4);
 PORTC &= 0b000; 
}



int main(){
 init_port_b();

 usbInit();
 usbDeviceDisconnect();
 _delay_ms(300);
 usbDeviceConnect();
 sei();
 for(;;){
  usbPoll();
 }
 return 0;
}

