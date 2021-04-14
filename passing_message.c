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
#define req_read_ldr 1
#define req_write_led 10
#define req_play_sound 11


//led at pc0 pc1 pc2
void set_led(unsigned led ,unsigned state){
 if(state)
  PORTC |= (1<<led); 
 else 
  PORTC &= ~(1<<led);
}


void play_sound(unsigned state){
 if(state)
  PORTB |= (1<<PB5);
 else 
  PORTB &= ~(1<<PB5);
}


uint16_t read_adc(uint8_t channel)
{
    ADMUX = (0<<REFS1)|(1<<REFS0) // use VCC as reference voltage
          | (0<<ADLAR)            // store result to the right of ADCH/ADCL
          | (channel & 0b1111);   // point MUX to the specified channel
    ADCSRA = (1<<ADEN)            // enable ADC
           | (1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0) // set speed to 1/128 of system clock
           | (1<<ADSC);           // start conversion
    // wait until ADSC bit becomes 0, indicating complete conversion
    while ((ADCSRA & (1<<ADSC)))
       ;   
    return ADCL + ADCH*256;
}


usbMsgLen_t usbFunctionSetup(uint8_t data[8]){
  usbRequest_t *rq = (usbRequest_t*)data;
  static uint8_t switch_state;  
  static uint8_t ldr_state[2];
  switch_state = 0; 
  if(rq->bRequest == req_read_switch1){
   if((PINB & (1<<PB1))==0)
     switch_state -= 1;
   if((PINB & (1<<PB2))==0)
     switch_state -= 2;
   if((PINB & (1<<PB3))==0)
     switch_state -= 4;
   if((PINB & (1<<PB4))==0)
     switch_state -= 8;

   switch_state -= 241;
   usbMsgPtr = (uchar*)&switch_state;
   return sizeof(switch_state);
  }
  else if(rq->bRequest == req_read_ldr){
   /*ldr_state = read_adc(PC3);
   usbMsgPtr = (uint16_t*)ldr_state;
   return sizeof(ldr_state);*/
   int ldr = read_adc(PC3);
   ldr_state[0] = (ldr>>8)&0xff;
   ldr_state[1] = (ldr)&0xff;
   usbMsgPtr = (uint8_t*)ldr_state;
   return 2;
  }  
  else if(rq->bRequest == req_write_led){
   unsigned index = rq->wIndex.word;
   unsigned value = rq->wValue.word;
   set_led(index,value);
   return 0;
  }
  else if(rq->bRequest == req_play_sound){
   play_sound(rq->wValue.word);
   return 0;
  }  
  return 0;
}




void init_port_b(){
   //PC0..PC2 -> output
 DDRC |= (1<<PC0)|(1<<PC1)|(1<<PC2);
 DDRB |= (1<<PB5);
 //PB0,PB1,PB2,PB3,PCB4 -> input
 DDRB &= ~((1<<PB0)|(1<<PB1)|(1<<PB2)|(1<<PB3)|(1<<PB4));
 //DDRC &= ~(1<<PC5);
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

