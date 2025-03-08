/* ========================================
 *
 * Copyright YOUR COMPANY, THE YEAR
 * All Rights Reserved
 * UNPUBLISHED, LICENSED SOFTWARE.
 *
 * CONFIDENTIAL AND PROPRIETARY INFORMATION
 * WHICH IS THE PROPERTY OF your company.
 *
 * ========================================
*/
#include "project.h"

int main(void)
{
    CyGlobalIntEnable; /* Enable global interrupts. */

    /* Place your initialization/startup code here (e.g. MyInst_Start()) */
    UART_LOG_Start();
    char buffer[128] = {};
    uint8_t statusReg = UART_LOG_ReadRxStatus();
    sprintf(buffer + strlen(buffer), "%u\r\n", statusReg);
    UART_LOG_PutString(buffer);
    
    for(;;)
    {
        /* Place your application code here. */
       
    }
}

/* [] END OF FILE */
