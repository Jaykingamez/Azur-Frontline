class DeathSystem():
     def roll_death(self, character):
        """
        Happens when hitting <= 0 hp. unless dead,

        """

        result = self.roll_random_table("1d8", death_table)
        if result == "dead":
            character.at_death()
        else:
            # survives with degraded abilities (1d4 roll)
            abi = self.death_map[result]

            current_abi = getattr(character, abi)
            loss = self.roll("1d4")

            current_abi -= loss

            if current_abi < -10:
                # can't lose more - die
                character.at_death()
            else:
                # refresh health, but get permanent ability loss
                new_hp = self.roll("1d4")
                character.heal(new_hp)
                setattr(character, abi, current_abi)

                character.msg(
                    "~" * 78
                    + "\n|yYou survive your brush with death, "
                    f"but are |r{result.upper()}|y and permanently |rlose {loss} {abi}|y.|n\n"
                    f"|GYou recover |g{new_hp}|G health|.\n"
                    + "~" * 78
                )