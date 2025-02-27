#define MICROPY_HW_BOARD_NAME "Piazote C3"
#define MICROPY_HW_MCU_NAME "ESP32C3"
#define MICROPY_PY_NETWORK_HOSTNAME_DEFAULT "Piazote-C3"

#define MICROPY_HW_ENABLE_SDCARD (0)
#define MICROPY_PY_MACHINE_I2S (0)

// Enable UART REPL for modules that have an external USB-UART and don't use native USB.
#define MICROPY_HW_ENABLE_UART_REPL (1)

#define MICROPY_HW_I2C0_SCL (5)
#define MICROPY_HW_I2C0_SDA (4)
