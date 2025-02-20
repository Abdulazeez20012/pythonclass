import unittest
from Dsa_Function.TV import TV

class TestTV(unittest.TestCase):

    def test_the_initial_state_of_the_TV(self):
        self.tv = TV()
        self.assertFalse(self.tv.power_status)
        self.assertEqual(self.tv.volume, 0)
        self.assertEqual(self.tv.channel, 1)

    def test_to_turn_on_tv_when_switched_off(self):
        self.tv = TV()

        self.tv.is_switched_off()
        self.assertTrue(self.tv.power_status)

        self.tv.turn_on()
        self.assertTrue(self.tv.power_status)

    def test_to_switch_off_tv_when_on(self):
        self.tv = TV()

        self.tv.is_switched_off()
        self.assertTrue(self.tv.power_status)

        self.tv.turn_on()
        self.assertTrue(self.tv.power_status)

    def test_to_increase_volume_of_tv_when_low(self):
        self.tv = TV()

        self.tv.turn_on()
        self.assertTrue(self.tv.power_status)

        self.tv.decrease_volume()
        self.assertEqual(self.tv.volume, 0)

        self.tv.increase_volume()
        self.assertEqual(self.tv.volume, 1)

    def test_to_decrease_volume_of_tv_when_high(self):
        self.tv = TV()

        self.tv.is_switched_off()
        self.assertTrue(self.tv.power_status)

        self.tv.turn_on()
        self.assertTrue(self.tv.power_status)

        self.tv.increase_volume()
        self.tv.increase_volume()
        self.assertEqual(self.tv.volume, 2)

        self.tv.decrease_volume()
        self.assertEqual(self.tv.volume, 1)

    def test_to_set_volume_limits_for_increasing(self):
        self.tv = TV()
        self.tv.is_switched_off()
        self.assertTrue(self.tv.power_status)

        self.tv.turn_on()
        self.assertTrue(self.tv.power_status)

        for index in range(100):
            self.tv.increase_volume()
        self.assertNotEqual(self.tv.volume, 1111)

    def test_to_set_volume_limits_for_decreasing(self):
        self.tv = TV()
        for index in range(200):
            self.tv.decrease_volume()
        self.assertEqual(self.tv.volume, 0)


    def test_that_can_change_channel_up_5_6_7_8(self):
        self.tv = TV()
        self.tv.turn_on()
        self.assertTrue(self.tv.power_status)

        self.tv.change_channel(5)
        self.assertEqual(self.tv.channel, 5)

        self.tv.change_channel(6)
        self.assertEqual(self.tv.channel, 6)

        self.tv.change_channel(7)
        self.assertEqual(self.tv.channel, 7)

        self.tv.change_channel(8)
        self.assertEqual(self.tv.channel, 8)

    def test_that_can_change_channel_down_8_7_6_5(self):
        self.tv = TV()

        self.tv.turn_on()
        self.assertTrue(self.tv.power_status)

        self.tv.change_channel(8)
        self.assertNotEqual(self.tv.channel, 7)

        self.tv.change_channel(7)
        self.assertEqual(self.tv.channel, 7)

        self.tv.change_channel(6)
        self.assertEqual(self.tv.channel, 6)

        self.tv.change_channel(5)
        self.assertEqual(self.tv.channel, 5)

    def test_that_cant_display_invalid_channel_eg_minus1(self):
        self.tv = TV()
        self.tv.is_switched_off()
        self.assertTrue(self.tv.power_status)

        self.tv.turn_on()
        self.assertTrue(self.tv.power_status)

        with self.assertRaises(ValueError):
            self.tv.change_channel(-1)

    def test_that_can_mute_tv_when_on(self):
        self.tv = TV()
        self.tv.turn_on()
        self.tv.increase_volume()
        self.assertEqual(self.tv.volume, 1)
        self.tv.mute()
        self.assertEqual(self.tv.volume, 0)

    def test_that_can_unmute_when_mute(self):
        self.tv = TV()
        self.tv.turn_on()
        self.tv.increase_volume()
        self.tv.mute()
        self.assertEqual(self.tv.volume, 0)
        self.tv.unmute()
        self.assertEqual(self.tv.volume, 1)


    def test_that_can_mute_when_tv_is_off(self):
        self.tv = TV()
        self.tv.turn_off()
        self.tv.mute()
        self.assertEqual(self.tv.volume, 0)

    def test_that_volume_remains_in_desame_state_when_tv_is_on_after_off(self):
        self.tv = TV()
        self.tv.is_switched_off()
        self.assertTrue(self.tv.power_status)

        self.tv.turn_on()
        self.assertTrue(self.tv.power_status)

        self.tv.increase_volume()
        self.assertEqual(self.tv.volume, 1)

        self.tv.turn_off()
        self.assertEqual(self.tv.volume, 1)

        self.tv.turn_on()
        self.assertEqual(self.tv.volume, 1)
        self.tv.remain_instate()
        self.assertEqual(self.tv.volume, 1)



if __name__ == "__main__":
    unittest.main()
