MCU=atmega328p
F_CPU=16000000L
TARGET=passing_massage.hex
OBJS=./usbdrv.o ./usbdrvasm.o
CFLAGS=-Wall -Os -DF_CPU=$(F_CPU) -Iusbdrv -I. -mmcu=$(MCU)

all: $(TARGET)

flash: $(TARGET)
	    avrdude -p $(MCU) -c usbasp -U flash:w:$(TARGET)

%.hex: %.elf
	    avr-objcopy -j .text -j .data -O ihex $< $@

%.elf: %.o $(OBJS)
	    avr-gcc $(CFLAGS) -o $@ $?

%.o: %.c
	    avr-gcc -c $(CFLAGS) -o $@ $<

%.o: %.S
	    avr-gcc $(CFLAGS) -x assembler-with-cpp -c -o $@ $<

clean:
	    rm -f $(OBJS)
			rm -f $(TARGET)
			rm -f *~
