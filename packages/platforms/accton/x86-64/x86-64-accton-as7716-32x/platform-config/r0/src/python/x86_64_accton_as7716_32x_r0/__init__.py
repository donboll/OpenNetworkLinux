from onl.platform.base import *
from onl.platform.accton import *

class OnlPlatform_x86_64_accton_as7716_32x_r0(OnlPlatformAccton):

    def model(self):
        return "AS7716-32X"

    def platform(self):
        return "x86-64-accton-as7716-32x-r0"

    def sys_oid_platform(self):
        return ".7716.32"

    def baseconfig(self):
        ########### initialize I2C bus 0 ###########
        self.new_i2c_devices([
                # initialize multiplexer (PCA9548)
                ('pca9548', 0x77, 0),

                # initiate leaf multiplexer (PCA9548)
                ('pca9548', 0x76 1),

                # initiate chassis fan
                ('as7716_32x_fan', 0x66, 9),

                # inititate LM75
                ('lm75', 0x48, 10),
                ('lm75', 0x49, 10),
                ('lm75', 0x4a, 10),

                #initiate CPLD
                ('accton_i2c_cpld', 0x60, 11),
                ('accton_i2c_cpld', 0x62, 12),
                ('accton_i2c_cpld', 0x64, 13),

                # initiate leaf multiplexer (PCA9548)
                ('pca9548', 0x71, 2),

                # initiate PSU-1
                ('as7716_32x_psu1', 0x53, 18),
                ('ym2651', 0x5b, 18),

                # initiate PSU-2
                ('as7716_32x_psu2', 0x50, 17),
                ('ym2651', 0x58, 17),

                # initiate leaf multiplexer (PCA9548)
                ('pca9548', 0x72, 2),
                ('pca9548', 0x73, 2),
                ('pca9548', 0x74, 2),
                ('pca9548', 0x75, 2),

                # initialize QSFP port 1-32
                ('as7716_32x_sfp9',  0x50, 25),
                ('as7716_32x_sfp10', 0x50, 26),
                ('as7716_32x_sfp11', 0x50, 27),
                ('as7716_32x_sfp12', 0x50, 28),
                ('as7716_32x_sfp1',  0x50, 29),
                ('as7716_32x_sfp2',  0x50, 30),
                ('as7716_32x_sfp3',  0x50, 31),
                ('as7716_32x_sfp4',  0x50, 32),
                ('as7716_32x_sfp6',  0x50, 33),
                ('as7716_32x_sfp5',  0x50, 34),
                ('as7716_32x_sfp8',  0x50, 35),
                ('as7716_32x_sfp7',  0x50, 36),
                ('as7716_32x_sfp13', 0x50, 37),
                ('as7716_32x_sfp14', 0x50, 38),
                ('as7716_32x_sfp15', 0x50, 39),
                ('as7716_32x_sfp16', 0x50, 40),
                ('as7716_32x_sfp17', 0x50, 41),
                ('as7716_32x_sfp18', 0x50, 42),
                ('as7716_32x_sfp19', 0x50, 43),
                ('as7716_32x_sfp20', 0x50, 44),
                ('as7716_32x_sfp25', 0x50, 45),
                ('as7716_32x_sfp26', 0x50, 46),
                ('as7716_32x_sfp27', 0x50, 47),
                ('as7716_32x_sfp28', 0x50, 48),
                ('as7716_32x_sfp29', 0x50, 49),
                ('as7716_32x_sfp30', 0x50, 50),
                ('as7716_32x_sfp31', 0x50, 51),
                ('as7716_32x_sfp32', 0x50, 52),
                ('as7716_32x_sfp21', 0x50, 53),
                ('as7716_32x_sfp22', 0x50, 54),
                ('as7716_32x_sfp23', 0x50, 55),
                ('as7716_32x_sfp24', 0x50, 56),
                ('24c02', 0x56, 0),
                ])

        return True),
