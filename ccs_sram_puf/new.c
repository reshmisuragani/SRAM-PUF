#include <stdint.h>
#include <stdbool.h>
#include "inc/hw_memmap.h"
#include "driverlib/gpio.h"
#include "driverlib/pin_map.h"
#include "driverlib/rom.h"
#include "driverlib/sysctl.h"
#include "driverlib/uart.h"

int main(void)
{

    ROM_FPULazyStackingEnable();
    ROM_SysCtlClockSet(SYSCTL_SYSDIV_4 | SYSCTL_USE_PLL | SYSCTL_XTAL_16MHZ |SYSCTL_OSC_MAIN);   // Set the clocking to run directly from the crystal.
    // Initialize the UART.
    ROM_SysCtlPeripheralEnable(SYSCTL_PERIPH_GPIOA);  // Enable the GPIO Peripheral used by the UART.
    ROM_SysCtlPeripheralEnable(SYSCTL_PERIPH_UART0);  // Enable UART0
    ROM_GPIOPinConfigure(GPIO_PA0_U0RX);
    ROM_GPIOPinConfigure(GPIO_PA1_U0TX);
    ROM_GPIOPinTypeUART(GPIO_PORTA_BASE, GPIO_PIN_0 | GPIO_PIN_1);  // Configure GPIO Pins for UART mode.
    UARTClockSourceSet(UART0_BASE, UART_CLOCK_PIOSC);  // Use the internal 16MHz oscillator as the UART clock source.
    UARTStdioConfig(0, 115200, 16000000);  // Initialize the UART for console I/O.


    uint32_t * ptr=(uint32_t)0x20002500;


    for(ptr=(uint32_t)0x20002500; ptr<(uint32_t)0x20007000; ptr=ptr+(uint32_t)0x4 )
    {
        //UARTprintf("%p:%d:%p\n",(void*)&ptr,(void*)*ptr,start);

        //UARTprintf("%p:%x\n",ptr,*ptr);
        UARTprintf("%x\n",*ptr);

        //SysCtlDelay(SysCtlClockGet() / 10 / 3);
        SysCtlDelay(400000); //10 milliseconds delay

    }

}
